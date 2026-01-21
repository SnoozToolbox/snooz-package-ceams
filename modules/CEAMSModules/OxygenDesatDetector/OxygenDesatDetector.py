"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    OxygenDesatDetector
    A Class to analyze the oxygen channel, detect oxygen desaturations and export oxygen saturation report.
"""
import matplotlib.pyplot as plt
plt.switch_backend('agg')  # turn off gui
import numpy as np
import os.path
import pandas as pd
import scipy.signal as scipysignal
from scipy.interpolate import interp1d

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

from CEAMSModules.EventTemporalLink import EventTemporalLink
from CEAMSModules.EventReader import manage_events
from CEAMSModules.PSACompilation import PSACompilation
from CEAMSModules.PSGReader.SignalModel import SignalModel
from CEAMSModules.PSGReader import commons
from CEAMSModules.SleepReport import SleepReport

from CEAMSModules.OxygenDesatDetector.OxygenDesatDetector_doc import write_doc_file
from CEAMSModules.OxygenDesatDetector.OxygenDesatDetector_doc import _get_doc

DEBUG = False

class OxygenDesatDetector(SciNode):
    """
    A Class to analyze the oxygen channel, detect oxygen desaturations and export oxygen saturation report.
    To copy the previous software, the oxygen saturation channel is downsampled to 1 Hz.

    Inputs:
        "artifact_group": String
            The group label of the invalid section annotation for the oxy chan analysis.
        "artifact_name": String
            The name label of the invalid section annotation for the oxy chan analysis.
        "arousal_group": String
            The group label of the arousal annotations for temporal link analysis.
            (Obsolete, the feature was removed 2024-01-30, not robust)
        "arousal_name": String
            The name label of the arousal annotations for temporal link analysis.
            (Obsolete, the feature was removed 2024-01-30, not robust)
        "signals": a list of SignalModel
            Each item of the list is a SignalModel object as described below:
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the sampling rate of the signal
                signal.channel : current channel label
                signal.start_time : The start time of the signal in sec
                signal.end_time : The end time of the signal in sec
                (for more info : look into common/SignalModel)
        "events": pandas DataFrame
            df of events with field
            'group': Group of events this event is part of (String)
            'name': Name of the event (String)
            'start_sec': Starting time of the event in sec (Float)
            'duration_sec': Duration of the event in sec (Float)
            'channels' : Channel where the event occures (String)
            (within Snooz channels is a string of a single channel or [] for all channels)
        "stages_cycles": Pandas Dataframe ['group','name','start_sec','duration_sec','channels']
            Events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
            The sleep stage group has to be commons.sleep_stage_group "stage" and 
            the sleep cycle group has to be commons.sleep_cycle_group "cycle".            
        "subject_info": dict
            filename : Recording filename without path and extension.
            id1 : Identification 1
            id2 : Identification 2
            first_name : first name of the subject recorded
            last_name : last name of the subject recorded
            sex :
            ...
        "parameters_oxy": dict
            'desaturation_drop_percent' : 'Drop level (%) for the oxygen desaturation "3 or 4"',
            'max_slope_drop_sec' : 'The maximum duration (s) during which the oxygen level is dropping "120 or 20"',
            'min_hold_drop_sec' : 'Minimum duration (s) during which the oxygen level drop is maintained "10 or 5"',

        "parameters_cycle": Dict
            Options used to define the cycles
            "{
                'defined_option':'Minimum Criteria'
                'Include_SOREMP' : '1'
                'Include_last_incompl' : '1'
                'Include_all_incompl: : '1'
                'dur_ends_REMP' = '15'
                'NREM_min_len_first':'0'
                'NREM_min_len_mid_last':'15'
                'NREM_min_len_val_last':'0'
                'REM_min_len_first':'0'
                'REM_min_len_mid':'0'
                'REM_min_len_last':'0'
                'mv_end_REMP':'0'
                'sleep_stages':'N1, N2, N3, N4, R'
                'details': '<p>Adjust options based on minimum criteria.</p>
            }"
        "report_constants": dict
            Constants used in the report (N_HOURS, N_CYCLES)  
        "cohort_filename": String
            Path and filename to save the oxygen saturation report for the cohort. 
        "picture_dir" : String
            Directory path to save the oxygen saturation graph picture.
            One graph per recording (1 picture per discontinuity).

    Outputs:
        desat_events : pandas DataFrame
            df of events with field
            'group': Group of events this event is part of (String)
            'name': Name of the event (String)
            'start_sec': Starting time of the event in sec (Float)
            'duration_sec': Duration of the event in sec (Float)
            'channels' : Channel where the event occures (String)
            (within Snooz channels is a string of a single channel or [] for all channels)
        
    """
    def __init__(self, **kwargs):
        """ Initialize module OxygenDesatDetector """
        super().__init__(**kwargs)
        if DEBUG: print('OxygenDesatDetector.__init__')

        # Input plugs
        InputPlug('artifact_group',self)
        InputPlug('artifact_name',self)
        InputPlug('arousal_group',self)
        InputPlug('arousal_name',self)
        InputPlug('signals',self)
        InputPlug('events',self)
        InputPlug('stages_cycles',self)
        InputPlug('subject_info',self)
        InputPlug('parameters_oxy',self)
        InputPlug('parameters_cycle',self)
        InputPlug('report_constants',self)
        InputPlug('cohort_filename',self)
        InputPlug('picture_dir',self)
        
        # Output plugs
        OutputPlug('desat_events',self)

        # A master module allows the process to be reexcuted multiple time.
        self._is_master = False 

        # Init module variables
        self.stage_stats_labels = ['N1', 'N2', 'N3', 'R', 'W']
        self.N_CYCLES = 9
        self.values_below = [96, 94, 92, 90, 85, 80, 75, 70, 60]
    

    def compute(self, artifact_group, artifact_name, arousal_group, arousal_name, \
        signals, events, stages_cycles, subject_info, parameters_oxy, parameters_cycle,\
             report_constants, cohort_filename, picture_dir):
        """
        To analyze the oxygen channel, detect oxygen desaturations and export oxygen saturation report.

        Inputs:
            "artifact_group": String
                The group label of the invalid section annotation for the oxy chan analysis.
            "artifact_name": String
                The name label of the invalid section annotation for the oxy chan analysis.
            "arousal_group": String
                The group label of the arousal annotations for temporal link analysis.
            "arousal_name": String
                The name label of the arousal annotations for temporal link analysis.
            "signals": a list of SignalModel
                Each item of the list is a SignalModel object as described below:
                    signal.samples : The actual signal data as numpy list
                    signal.sample_rate : the sampling rate of the signal
                    signal.channel : current channel label
                    signal.start_time : The start time of the signal in sec
                    signal.end_time : The end time of the signal in sec
                    (for more info : look into common/SignalModel)
            "events": pandas DataFrame
                df of events with field
                'group': Group of events this event is part of (String)
                'name': Name of the event (String)
                'start_sec': Starting time of the event in sec (Float)
                'duration_sec': Duration of the event in sec (Float)
                'channels' : Channel where the event occures (String)
                (within Snooz channels is a string of a single channel or [] for all channels)
            "stages_cycles": Pandas Dataframe ['group','name','start_sec','duration_sec','channels']
                Events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
                The sleep stage group has to be commons.sleep_stage_group "stage" and 
                the sleep cycle group has to be commons.sleep_cycle_group "cycle".            
            "subject_info": dict
                filename : Recording filename without path and extension.
                id1 : Identification 1
                id2 : Identification 2
                first_name : first name of the subject recorded
                last_name : last name of the subject recorded
                sex :
                ...
            "parameters_oxy": dict
                'desaturation_drop_percent' : 'Drop level (%) for the oxygen desaturation "3 or 4"',
                'max_slope_drop_sec' : 'The maximum duration (s) during which the oxygen level is dropping "120 or 20"',
                'min_hold_drop_sec' : 'Minimum duration (s) during which the oxygen level drop is maintained "10 or 5"',
                'window_link_sec' : 'The window length (s) to compute the temporal link between desaturations and arousals',
                'arousal_min_sec' : 'The minimum length (s) of the arousal events kept',
                'arousal_max_sec' : 'The maximum length (s) of the arousal events kept',

            "parameters_cycle": Dict
                Options used to define the cycles
                "{
                    'defined_option':'Minimum Criteria'
                    'Include_SOREMP' : '1'
                    'Include_last_incompl' : '1'
                    'Include_all_incompl: : '1'
                    'dur_ends_REMP' = '15'
                    'NREM_min_len_first':'0'
                    'NREM_min_len_mid_last':'15'
                    'NREM_min_len_val_last':'0'
                    'REM_min_len_first':'0'
                    'REM_min_len_mid':'0'
                    'REM_min_len_last':'0'
                    'mv_end_REMP':'0'
                    'sleep_stages':'N1, N2, N3, N4, R'
                    'details': '<p>Adjust options based on minimum criteria.</p>
                }"
            "report_constants": dict
                Constants used in the report (N_HOURS, N_CYCLES)  
            "cohort_filename": String
                Path and filename to save the oxygen saturation report for the cohort. 
            "picture_dir" : String
                Directory path to save the oxygen saturation graph picture.
                One graph per recording (1 picture per discontinuity).
        Outputs:

        """
        self.clear_cache()

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if subject_info=='':
            raise NodeInputException(self.identifier, "subject_info", \
                f"OxygenDesatDetector this input is empty, it needs to identify the subject recorded.")
        if cohort_filename=='':
            raise NodeInputException(self.identifier, "cohort_filename", \
                f"OxygenDesatDetector has nothing to generate, 'cohort_filename' is empty")    
        if isinstance(signals, str) and signals=='':
            raise NodeInputException(self.identifier, "signals", \
                f"OxygenDesatDetector this input is empty, no signals no Oxygen Saturation Report.")         
        if isinstance(stages_cycles, str) and stages_cycles=='':
            raise NodeInputException(self.identifier, "stages_cycles", \
                f"OxygenDesatDetector this input is empty")    
        if isinstance(parameters_cycle, str) and parameters_cycle=='':
            raise NodeInputException(self.identifier, "parameters_cycle", \
                f"OxygenDesatDetector this input is empty")  
        if isinstance(parameters_oxy, str) and parameters_oxy=='':
            raise NodeInputException(self.identifier, "parameters_oxy", \
                f"OxygenDesatDetector this input is empty")  
        if isinstance(events, str) and events=='':
            raise NodeInputException(self.identifier, "events", \
                f"OxygenDesatDetector this input is empty, events is not connected.")    

        # Convert string into dicts
        if isinstance(parameters_cycle, str):
            parameters_cycle = eval(parameters_cycle)
        if isinstance(parameters_oxy, str):
            parameters_oxy = eval(parameters_oxy)

        if isinstance(report_constants,str) and report_constants == '':
            raise NodeInputException(self.identifier, "report_constants", \
                "OxygenDesatDetector report_constants parameter must be set.")
        elif isinstance(report_constants,str):
            report_constants = eval(report_constants)
        if isinstance(report_constants,dict) == False:
            raise NodeInputException(self.identifier, "report_constants",\
                "OxygenDesatDetector report_constants expected type is dict and received type is " \
                    + str(type(report_constants)))   
        self.N_CYCLES = int(float(report_constants['N_CYCLES']))

        #----------------------------------------------------------------------
        # Header parameters
        # subject info, sleep cycle parameters, desaturation parameters
        #----------------------------------------------------------------------
        subject_info_params = \
        {
            "filename":subject_info['filename'],
            "id1": subject_info['id1']
            }
        cycle_info_param = SleepReport.get_sleep_cycle_parameters(self,parameters_cycle)

        # Extract cycle
        sleep_cycles_df = stages_cycles[stages_cycles['group']==commons.sleep_cycle_group]
        sleep_cycles_df.reset_index(inplace=True, drop=True)
        sleep_cycle_count = {}
        sleep_cycle_count['sleep_cycle_count']=len(sleep_cycles_df) # 'Number of sleep cycles.',

        desaturation_param = parameters_oxy
        # Select the invalid sections events (self is required for the self.identifier)
        invalid_section_param, invalid_events = \
            PSACompilation.get_artefact_info(self, artifact_group, artifact_name, events.copy())
        invalid_section_param['invalid_events'] = invalid_section_param.pop('artefact_group_name_list')

        # Extract sleep stages
        sleep_stage_df = stages_cycles[stages_cycles['group']==commons.sleep_stages_group]
        sleep_stage_df.reset_index(inplace=True, drop=True)

        # Keep stage from the first awake or sleep until the last awake or sleep
        sleep_stage_df.loc[:, 'name'] = sleep_stage_df['name'].apply(int)
        index_valid = sleep_stage_df[sleep_stage_df['name']<8].index
        stage_rec_df = sleep_stage_df.loc[index_valid[0]:index_valid[-1]]
        stage_rec_df.reset_index(inplace=True, drop=True)

        channels_list = np.unique(SignalModel.get_attribute(signals, 'channel', 'channel'))
        if len(channels_list)>1:
            raise NodeRuntimeException(self.identifier, "signals", \
                f"OxygenDesatDetector more than one channels were selected for {subject_info['filename']}.")
        
        #----------------------------------------------------------------------
        # Define the channel info
        #----------------------------------------------------------------------
        channel = channels_list[0]
        fs_chan = SignalModel.get_attribute(signals, 'sample_rate', 'channel', channel)[0][0] 
        channel_info_param = {}
        channel_info_param['chan_label']=channel
        channel_info_param['chan_fs']=fs_chan

        #----------------------------------------------------------------------
        # Oxygen channel saturation variables
        # Minimum, maximum and average oxygen saturation per thirds, halves, sleep cycles and sleep stages.
        #----------------------------------------------------------------------

        # Compute stats for the whole recording from lights off to lights on
        #----------------------------------------------------------------------
        total_stats, data_stats, data_starts = self.compute_total_stats_saturation(\
            stage_rec_df, signals, subject_info, fs_chan, picture_dir, invalid_events)

        # Compute stats for thirds
        #----------------------------------------------------------------------
        n_divisions = 3
        section_label = 'third'
        third_stats = self.compute_division_stats_saturation(n_divisions, section_label, stage_rec_df, signals)

        # Compute stats for halves
        #----------------------------------------------------------------------
        n_divisions = 2
        section_label = 'half'
        half_stats = self.compute_division_stats_saturation(n_divisions, section_label, stage_rec_df, signals)

        # Compute stats for stages
        #----------------------------------------------------------------------       
        stage_stats = self.compute_stages_stats_saturation(stage_rec_df, signals, fs_chan)

        # Compute stats for cycles
        #----------------------------------------------------------------------       
        cycle_stats = self.compute_cycles_stats_saturation(sleep_cycles_df, signals)

        # Detect desaturation 
        #----------------------------------------------------------------------
            # "parameters_oxy": dict
            # 'desaturation_drop_percent' : 'Drop level (%) for the oxygen desaturation "3 or 4"',
            # 'max_slope_drop_sec' : 'The maximum duration (s) during which the oxygen level is dropping "180 or 20"',
            # 'min_hold_drop_sec' : 'Minimum duration (s) during which the oxygen level drop is maintained "10 or 5"',
        desat_df, plateau_df, data_lpf_list, data_hpf_list, lmax_indices_list, lmin_indices_list = \
            self.detect_desaturation_ABOSA(data_starts, data_stats, fs_chan, channel, parameters_oxy)
        
        # Keep desaturation events (desat_df) that start in asleep stages only
        asleep_stages_df = stage_rec_df[((stage_rec_df['name']>0) & (stage_rec_df['name']<6))]
        
        # Filter desaturation events to keep only those starting during asleep stages
        # Only process desat_SpO2 events, exclude art_SpO2 events
        desat_only_df = desat_df[desat_df['name'] == 'desat_SpO2']
        artifact_df = desat_df[desat_df['name'] == 'art_SpO2']
        
        start_time = asleep_stages_df['start_sec'].values
        end_time = start_time + asleep_stages_df['duration_sec'].values
        desat_tab = desat_only_df[['start_sec','duration_sec']].to_numpy()
        desat_kept = []
        for desat_start, desat_dur in desat_tab:
            if any((start_time <= desat_start) & (end_time >= desat_start)):
                desat_kept.append([desat_start, desat_dur])
        
        # Update desat_df to contain only filtered desaturation events plus all artifact events
        if len(desat_kept) > 0:
            desat_events = [('SpO2', 'desat_SpO2', start_sec, duration_sec, '') 
                          for start_sec, duration_sec in desat_kept]
            filtered_desat_df = manage_events.create_event_dataframe(data=desat_events)
        else:
            filtered_desat_df = pd.DataFrame(columns=['group', 'name', 'start_sec', 'duration_sec', 'channels'])

        if DEBUG:
            print(f"\n{len(filtered_desat_df)} desat events after filtering out desat not starting in asleep\n")

        # Compute desaturation stats
        #----------------------------------------------------------------------
        desat_stats = self.compute_desat_stats(filtered_desat_df, asleep_stages_df)

        # Combine filtered desaturations with artifacts
        desat_df = pd.concat([filtered_desat_df, artifact_df], ignore_index=True)

        if DEBUG:
            cache = {}
            if len(data_lpf_list)>1:
                # Find the longuest signal
                len_data = [len(data) for data in data_lpf_list]
                index_longuest = np.argmax(len_data)
                data_lpf_list = [data_lpf_list[index_longuest]]
            else:
                index_longuest = 0
            if len(data_lpf_list)>0:
                # Create a SignalModel for the raw data and the filtered data
                signal_raw = signals[index_longuest].clone(clone_samples=False)
                signal_lpf = signals[index_longuest].clone(clone_samples=False)
                signal_hpf = signals[index_longuest].clone(clone_samples=False)
                signal_raw.samples = data_stats[index_longuest]
                signal_raw.start_time = data_starts[index_longuest]
                signal_lpf.samples = data_lpf_list[index_longuest]
                signal_lpf.start_time = data_starts[index_longuest]
                signal_lpf.channel = signal_raw.channel+'_lpf'
                signal_hpf.samples = data_hpf_list[index_longuest]
                signal_hpf.start_time = data_starts[index_longuest]
                signal_hpf.channel = signal_raw.channel+'_hpf'
                cache['signal_raw'] = signal_raw
                cache['signal_lpf'] = signal_lpf
                cache['signal_hpf'] = signal_hpf
                cache['desat_df'] = desat_df
                cache['plateau_df'] = plateau_df
                cache['lmax_sec'] = lmax_indices_list[index_longuest]/fs_chan + data_starts[index_longuest]
                cache['lmin_sec'] = lmin_indices_list[index_longuest]/fs_chan + data_starts[index_longuest]
                self._cache_manager.write_mem_cache(self.identifier, cache)

        # Temporal links between desaturation and arousal
        # Removed 2024-01-30
        #   - Does not look robust
        #   - We dont know who asked for it
        #----------------------------------------------------------------------        
        # # Select arousals
        # arousal_section_param, arousal_events = \
        #     PSACompilation.get_artefact_info(self, arousal_group, arousal_name, events.copy())
        # # Select arousals between min and max duration
        # arousals_selected = arousal_events[arousal_events['duration_sec']>=parameters_oxy['arousal_min_sec']]
        # arousals_selected = arousals_selected[arousals_selected['duration_sec']<=parameters_oxy['arousal_max_sec']]

        # # Compute temporal links
        # temporal_stats, link_event_df = self.compute_temporal_link_stats(\
        #     desat_df, arousals_selected, parameters_oxy['window_link_sec'], channel)

        # --------------------------------------------------------------------------
        # Organize data to Write the file
        # --------------------------------------------------------------------------
        # Construction of the pandas dataframe that will be used to create the CSV file
        # There is a new line for each channel and mini band
        output = subject_info_params | cycle_info_param | desaturation_param | invalid_section_param | \
            channel_info_param | sleep_cycle_count | total_stats | third_stats | half_stats | \
                stage_stats | cycle_stats | desat_stats #| temporal_stats
        report_df = pd.DataFrame.from_records([output])

        # Write the current report for the current subject into the cohort tsv file
        write_header = not os.path.exists(cohort_filename)
        # Order columns as the doc file
        out_columns = list(_get_doc(self.N_CYCLES, self.stage_stats_labels, self.values_below).keys())
        # Re order the columns and make sure they all exist
        report_df = report_df[out_columns]
        try : 
            report_df.to_csv(path_or_buf=cohort_filename, sep='\t', \
                index=False, index_label='False', mode='a', header=write_header, encoding="utf_8")
        except :
            error_message = f"Snooz can not write in the file {cohort_filename}."+\
                f" Check if the drive is accessible and ensure the file is not already open."
            raise NodeRuntimeException(self.identifier, "OxygenDesatDetector", error_message)      

        # To write the info text file to describe the variable names
        if write_header:
            # Write the documentation file
            file_name, file_extension = os.path.splitext(cohort_filename)
            doc_filepath = file_name+"_info"+file_extension
            if not os.path.exists(doc_filepath):
                write_doc_file(doc_filepath, self.N_CYCLES, self.stage_stats_labels, self.values_below)
                # Log message for the Logs tab
                self._log_manager.log(self.identifier, f"The file {doc_filepath} has been created.")

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, f"{subject_info['filename']} has been append to {cohort_filename}")
        
        return {
            'desat_events' : desat_df
        }


    def _plot_oxygen_saturation(self, data_to_plot, fs_chan, fig_name, data_starts, invalid_events):

        figure, ax = plt.subplots()
        figure.set_size_inches(25, 5)
        ax.clear()
        ymin = np.nanmin(data_to_plot)
        new_fs = fs_chan
        data_2_plot_end = len(data_to_plot)/new_fs+data_starts
        time = np.arange(data_starts, data_2_plot_end, 1/new_fs)
        ax.plot(time, data_to_plot,'-k', linewidth=1)
        
        # Add invalid section
        invalid_start_time = invalid_events['start_sec'].to_numpy()
        invalid_duration = invalid_events['duration_sec'].to_numpy()
        invalid_end = invalid_start_time + invalid_duration
        for inval_start, inval_end in zip(invalid_start_time, invalid_end):
            # If the invalid section starts during the data_to_plot
            if (inval_start >= data_starts) and (inval_start < data_2_plot_end):
                cur_invalid_start = inval_start
            # If the invalid section starts before the data_to_plot
            elif inval_start < data_starts:
                cur_invalid_start = data_starts
            else:
                cur_invalid_start = None
            # If the invalid section ends during the data_2_plot
            if (inval_end > data_starts) and (inval_end <= data_2_plot_end):
                cur_invalid_end = inval_end
            elif inval_end > data_2_plot_end:
                cur_invalid_end = data_2_plot_end
            else:
                cur_invalid_end = None
            if (cur_invalid_start is not None) and (cur_invalid_end is not None):
                ax.broken_barh([(cur_invalid_start, cur_invalid_end-cur_invalid_start)], (ymin, 100-ymin), facecolors='tab:red')

        ax.set_xlim(data_starts,len(data_to_plot)/new_fs-data_starts)
        ax.set_ylim(ymin,100)
        xticks_hour = np.arange(int(np.floor(min(time)/3600)),int(np.ceil(max(time)/3600)), 0.5)
        ax.set_xticks(xticks_hour*3600)
        ax.set_xticklabels(xticks_hour)
        ax.set_xlabel("Time (h)")
        ax.set_ylabel("Saturation (%)")
        ax.set_title("Oxygen Saturation")
        ax.grid(visible=True, which='both', axis='both')

        if not '.' in fig_name:
            fig_name = fig_name + '.pdf'
        try: 
            figure.savefig(fig_name)
        except :
            raise NodeRuntimeException(self.identifier, "OxygenDesatDetector", \
                f"ERROR : Snooz can not save the picture {fig_name}. "+\
                f"Check if the drive is accessible and ensure the file is not already open.")                           

    
    def compute_division_stats_saturation(self, n_divisions, section_label, stage_rec_df, signals):
        """""
            Compute the statistics (mean, std, max and min) of the oxygen saturation for the requested division.
            n_divisions can be 3 or 2.

            Parameters
            -----------
                n_divisions                 : int
                    Number of divisions.
                section_label               : string
                    Label of the division.
                stage_rec_df                : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])  
                    List of sleep stages from lights off to lights on.
                signals                     : list of SignalModel
                    The list of SignalModel from the whole recording, will be truncated in this fonction.
            Returns
            -----------  
                stats_dict                  : dict
                    Keys are adapted to the division such as
                    stats_dict["third1_saturation_avg"]
                    stats_dict["half2_saturation_min"]

        """""
        # For dividing a number into (almost) equal whole numbers
        # Remainers are added in the first division first
            # 15 epochs divided by 3 => [5, 5, 5]
            # 14 epochs divided by 3 => [5, 5, 4]
            # 13 epochs divided by 3 => [5, 4, 4]
            # 12 epochs divided by 3 => [4, 4, 4]
        n_epochs = len(stage_rec_df)
        n_epoch_div = [n_epochs // n_divisions + (1 if x < n_epochs % n_divisions else 0)  for x in range (n_divisions)]
        # Create a list of indexes to select the epochs in each division
        # Select the portion of the recording, row integer (NOT label), the end point is excluded with the .iloc
        index_div = []
        index_tmp = 0
        for div in range(n_divisions):
            cur_start = index_tmp
            cur_stop = cur_start+n_epoch_div[div]
            index_div.append([cur_start,cur_stop]) # integer index then last is exclusive
            index_tmp = cur_stop
        stats_dict = {}
        section_val = 1
        for index_start, index_stop in index_div:
            start = stage_rec_df.iloc[index_start]['start_sec']
            end = stage_rec_df.iloc[index_stop-1]['start_sec']+ stage_rec_df.iloc[index_stop-1]['duration_sec']
            dur = end - start
            signals_third = []
            for signal in signals:
                # Because of the discontinuity
                # we have to verify if the signal includes at least partially the events
                # Look for the Right windows time
                if (signal.start_time<(start+dur)) and ((signal.start_time+signal.duration)>start): 
                    # Extract and define the new extracted channel_cur
                    channel_cur = self.extract_samples_from_events(signal, start, dur)
                    signals_third.append(channel_cur)

            # Flat signals into an array
            data_array = np.empty(0)
            for i_bout, samples in enumerate(signals_third):
                data_array = np.concatenate((data_array, samples), axis=0)

            # Clean-up invalid values
            #data_array = np.round(data_array,0) # to copy Gaetan
            data_array[data_array>100]=np.nan
            data_array[data_array<=0]=np.nan
            stats_dict[f"{section_label}{section_val}_saturation_avg"] = np.nanmean(data_array)
            stats_dict[f"{section_label}{section_val}_saturation_std"] = np.nanstd(data_array)
            stats_dict[f"{section_label}{section_val}_saturation_min"] = np.round(np.nanmin(data_array),0)
            stats_dict[f"{section_label}{section_val}_saturation_max"] = np.round(np.nanmax(data_array),0)            
            section_val = section_val + 1
        return stats_dict


    def extract_samples_from_events(self, signal, start, dur):
        """
        Parameters :
            signal : SignalModel object
                signal with channel, samples, sample_rate...
            start : float
                start time in sec of the signal
            dur : float
                duration in sec of the signal
        Return : 
            samples :numpy array
                all samples linked to the event specified by start and dur

        """
        channel_cur = signal.clone(clone_samples=False)
        # Because of the discontinuity, the signal can start with an offset (second section)
        signal_start_samples = int(signal.start_time * channel_cur.sample_rate)
        channel_cur.start_time = start
        channel_cur.duration = dur
        channel_cur.end_time = start + dur
        first_sample = int(start * channel_cur.sample_rate)
        last_sample = int(channel_cur.end_time * channel_cur.sample_rate)
        channel_cur_samples = signal.samples[first_sample-signal_start_samples:last_sample-signal_start_samples]
        return channel_cur_samples


    def compute_total_stats_saturation(self, stage_rec_df, signals, subject_info, fs_chan, picture_dir, invalid_events):
        """
        Parameters :
            stage_rec_df : pandas DataFrame
                Sleep stages from lights off to lights on.
            signal : SignalModel object
                signal with channel, samples, sample_rate...
            subject_info : dict
                filename : Recording filename without path and extension.
                id1 : Identification 1
                ...
            fs_chan : float
                sampling rate of the channel
            picture_dir : string
                path of the folder to save the saturation picture (can be empty)
            invalid_events : pandas DataFrame
                Events of the invalid section of the oxygen saturation.
        Return : 
            total_stats : dict
                statistics fot the total recording.
                saturation_avg, std, min and max.
            data_stats : numpy array
                oxygen saturation integer values from 1 to 100% 
            data_starts : list
                start in sec of each continuous section (more than one when there are discontinuities)
        """    
        # Extract samples from lights off to lights on. 
        start = stage_rec_df['start_sec'].values[0]
        end = stage_rec_df['start_sec'].values[-1]+stage_rec_df['duration_sec'].values[-1]
        dur = end - start
        data_stats = []
        data_starts = []
        for signal in signals:
            # Because of the discontinuity
            # we have to verify if the signal includes at least partially the events
            # Look for the Right windows time
            if (signal.start_time<(start+dur)) and ((signal.start_time+signal.duration)>start): 
                cur_start = signal.start_time if start<=signal.start_time else start
                cur_end = end if end<=signal.end_time else signal.end_time
                # if start<=signal.start_time:
                #     cur_start = signal.start_time
                # else:
                #     cur_start = start
                # if end<=signal.end_time:
                #     cur_end = end
                # else:
                #     cur_end = signal.end_time
                #cur_dur = cur_end-cur_start
                # Extract and define the new extracted channel_cur
                channel_cur = self.extract_samples_from_events(signal, cur_start, cur_end-cur_start)
                # Clean-up invalid values
                #channel_cur = np.round(channel_cur,0) # to copy Gaétan
                channel_cur[channel_cur>100]=np.nan
                channel_cur[channel_cur<=0]=np.nan
                data_starts.append(cur_start)      
                data_stats.append(channel_cur)

        # Generate and save the oxygen saturation graph
        if len(picture_dir)>0:
            for i_bout, samples in enumerate(data_stats):
                fig_name = os.path.join(picture_dir, f"{subject_info['filename']}_oxygen_saturation{i_bout}.pdf")
                self._plot_oxygen_saturation(samples, fs_chan, fig_name, data_starts[i_bout], invalid_events)

        # Flat signals into an array
        data_array = np.empty(0)
        for i_bout, samples in enumerate(data_stats):
            data_array = np.concatenate((data_array, samples), axis=0)

        total_stats = {}
        total_stats["total_valid_min"] = (len(data_array)-np.isnan(data_array).sum())/fs_chan/60
        total_stats["total_invalid_min"]  = np.isnan(data_array).sum()/fs_chan/60
        total_stats["total_saturation_avg"] = np.nanmean(data_array)
        total_stats["total_saturation_std"] = np.nanstd(data_array)
        total_stats["total_saturation_min"] = np.round(np.nanmin(data_array),0)
        total_stats["total_saturation_max"] = np.round(np.nanmax(data_array),0)
        for val in self.values_below:
            total_stats[f"total_below_{val}_min"] = (data_array<val).sum()/fs_chan/60
        return total_stats, data_stats, data_starts


    def compute_stages_stats_saturation(self, stage_rec_df, signals, fs_chan):
        """
        Parameters :
            stage_rec_df : pandas DataFrame
                Sleep stages from lights off to lights on.
            signal : SignalModel object
                signal with channel, samples, sample_rate...
            fs_chan : float
                sampling rate of the channel
        Return : 
            stage_dict : dict
                statistics fot the stages.
                Saturation_avg, std, min and max for each stage.
                Duration in min for saturation under different thresholds.
        """    
        stage_start_times = stage_rec_df['start_sec'].to_numpy().astype(float)
        stage_duration_times = stage_rec_df['duration_sec'].to_numpy().astype(float)
        stage_name = stage_rec_df['name'].apply(str).to_numpy()

        stage_dict = {}
        for stage_label in self.stage_stats_labels:
            stage_mask = (stage_name==commons.sleep_stages_name[stage_label])
            start_masked = stage_start_times[stage_mask]
            dur_masked = stage_duration_times[stage_mask]
            if any(stage_mask):
                signals_from_stages = []
                for start, dur in zip(start_masked, dur_masked):
                    end = start + dur
                    for j, signal in enumerate(signals):
                        if (signal.start_time<(start+dur)) and ((signal.start_time+signal.duration)>start): 
                            # Extract and define the new extracted channel_cur
                            cur_start = signal.start_time if start<=signal.start_time else start
                            cur_end = end if end<=signal.end_time else signal.end_time
                            cur_samples = self.extract_samples_from_events(signal, cur_start, cur_end-cur_start)
                            # When the last epoch is not completed
                            if (len(cur_samples)/fs_chan) < dur:
                                n_miss_samples = int(round((dur-len(cur_samples)/fs_chan)*fs_chan,0))
                                cur_samples = np.pad(cur_samples, (0, n_miss_samples), constant_values=(0,np.nan))
                            signals_from_stages.append(cur_samples)

                # Flat signals into an array
                signals_cur_stage = np.empty(0)
                for i_bout, samples in enumerate(signals_from_stages):
                    signals_cur_stage = np.concatenate((signals_cur_stage, samples), axis=0)

                # Clean-up invalid values
                signals_cur_stage[signals_cur_stage>100]=np.nan
                signals_cur_stage[signals_cur_stage<=0]=np.nan
                stage_dict[f'{stage_label}_saturation_avg'] = np.nanmean(signals_cur_stage)
                stage_dict[f'{stage_label}_saturation_std'] = np.nanstd(signals_cur_stage)
                stage_dict[f'{stage_label}_saturation_min'] = np.round(np.nanmin(signals_cur_stage),0)
                stage_dict[f'{stage_label}_saturation_max'] = np.round(np.nanmax(signals_cur_stage),0)
                for val in self.values_below:
                    signals_flat = signals_cur_stage.flatten()
                    stage_dict[f"{stage_label}_below_{val}_min"] = (signals_flat<val).sum()/fs_chan/60
            else:
                stage_dict[f'{stage_label}_saturation_avg'] = np.nan
                stage_dict[f'{stage_label}_saturation_std'] = np.nan
                stage_dict[f'{stage_label}_saturation_min'] = np.nan
                stage_dict[f'{stage_label}_saturation_max'] = np.nan
                for val in self.values_below:
                    stage_dict[f"{stage_label}_below_{val}_min"] = np.nan                           
        return stage_dict


    def compute_cycles_stats_saturation(self, sleep_cycles_df, signals):
        """
        Parameters :
            sleep_cycles_df : pandas DataFrame
                Sleep cycles 
            signal : SignalModel object
                signal with channel, samples, sample_rate...
        Return : 
            cyc_dict : dict
                statistics fot the cycles.
                Saturation_avg, std, min and max for each stage.
        """    
        cyc_dict = {}
        for i_cyc in range(self.N_CYCLES):
            # Extract samples for each cycle
            if len(sleep_cycles_df)>i_cyc:
                start = sleep_cycles_df.iloc[i_cyc]['start_sec']
                end = sleep_cycles_df.iloc[i_cyc]['start_sec']+sleep_cycles_df.iloc[i_cyc]['duration_sec']
                dur = end - start
                signals_cyc = []
                for signal in signals:
                    # Because of the discontinuity
                    # we have to verify if the signal includes at least partially the events
                    # Look for the Right windows time
                    if (signal.start_time<(start+dur)) and ((signal.start_time+signal.duration)>start): 
                        # Extract and define the new extracted channel_cur
                        channel_cur = self.extract_samples_from_events(signal, start, dur)
                        signals_cyc.append(channel_cur)
                
                # Flat signals into an array
                data_stats = np.empty(0)
                for i_bout, samples in enumerate(signals_cyc):
                    data_stats = np.concatenate((data_stats, samples), axis=0)

                #data_stats = np.round(data_stats,0) # to copy Gaétan   
                # Clean-up invalid values
                data_stats[data_stats>100]=np.nan
                data_stats[data_stats<=0]=np.nan        
                cyc_dict[f'cyc{i_cyc+1}_saturation_avg'] = np.nanmean(data_stats)
                cyc_dict[f'cyc{i_cyc+1}_saturation_std'] = np.nanstd(data_stats)
                cyc_dict[f'cyc{i_cyc+1}_saturation_min'] = np.round(np.nanmin(data_stats),0)
                cyc_dict[f'cyc{i_cyc+1}_saturation_max'] = np.round(np.nanmax(data_stats),0)
            else:
                cyc_dict[f'cyc{i_cyc+1}_saturation_avg'] = np.nan
                cyc_dict[f'cyc{i_cyc+1}_saturation_std'] = np.nan
                cyc_dict[f'cyc{i_cyc+1}_saturation_min'] = np.nan
                cyc_dict[f'cyc{i_cyc+1}_saturation_max'] = np.nan
        return cyc_dict


    def convert_sec_to_HHMMSS(self, time_sec):
        HH = (np.floor(time_sec/3600)).astype(int)
        MM = ( np.floor( (time_sec-HH*3600) / 60 )).astype(int)
        SS = np.around( (time_sec-HH*3600 - MM*60).astype(np.double),decimals=2,out=None)
        # return the time as HH:MM:SS
        return f"{HH}:{MM}:{SS}"

    def resolve_overlapping_desaturations(self, desat_events):
        """
        Resolve overlapping desaturation events by keeping the one with the steepest fall rate.
        
        Parameters:
            desat_events : list of tuples
                List of (start_sec, duration_sec, fall_rate) tuples.
        
        Returns:
            resolved_events : list of tuples
                List of non-overlapping (start_sec, duration_sec, fall_rate) tuples.
        """
        if len(desat_events) == 0:
            return desat_events
        
        # Sort events by start time
        sorted_events = sorted(desat_events, key=lambda x: x[0])
        
        resolved_events = []
        i = 0
        while i < len(sorted_events):
            current_start, current_dur, current_rate = sorted_events[i]
            current_end = current_start + current_dur
            
            # Find all overlapping events
            overlapping = [(i, current_start, current_dur, current_rate)]
            j = i + 1
            while j < len(sorted_events):
                next_start, next_dur, next_rate = sorted_events[j]
                next_end = next_start + next_dur
                
                # Check for overlap: events overlap if next starts before current ends
                if next_start < current_end:
                    overlapping.append((j, next_start, next_dur, next_rate))
                    # Update current_end to include the new event's range
                    current_end = max(current_end, next_end)
                    j += 1
                else:
                    break
            
            # Select the event with the steepest fall rate (most negative, closest to -4)
            best_event = min(overlapping, key=lambda x: x[3])  # x[3] is fall_rate
            resolved_events.append((best_event[1], best_event[2], best_event[3]))
            
            if DEBUG and len(overlapping) > 1:
                print(f"Resolved {len(overlapping)} overlapping desaturations:")
                for idx, start, dur, rate in overlapping:
                    marker = " <-- KEPT" if (start, dur, rate) == (best_event[1], best_event[2], best_event[3]) else ""
                    print(f"  start={start:.2f}s, duration={dur:.2f}s, fall_rate={rate:.3f}%/s{marker}")
            
            # Move to the next non-overlapping event
            i = overlapping[-1][0] + 1
        
        return resolved_events

    def detect_desaturation_ABOSA(self, data_starts, data_stats, fs_chan, channel, parameters_oxy):
        """
        Detect desaturation as described in ABOSA [1].

        Parameters :
            data_stats : list of numpy array
                oxygen saturation integer values from 1 to 100% 
            data_starts : list
                start in sec of each continuous section (more than one when there are discontinuities)
            fs_chan     : float
                Sampling frequency (Hz).
            channel     : string
                Channel label.
            parameters_oxy: dict
                'desaturation_drop_percent' : 'Drop level (%) for the oxygen desaturation "3 or 4"',
                'max_slope_drop_sec' : 'The maximum duration (s) during which the oxygen level is dropping "120 or 20"',
                'min_hold_drop_sec' : 'Minimum duration (s) during which the oxygen level drop is maintained "10 or 5"',
            asleep_stages_df : pandas DataFrame
                Asleep stages from lights off to lights on.

        Return : 
            desat_df : pandas DataFrame
                df of events with field
                'group': Group of events this event is part of (String)
                'name': Name of the event (String)
                'start_sec': Starting time of the event in sec (Float)
                'duration_sec': Duration of the event in sec (Float)
                'channels' : Channel where the event occures (String)
            signal_lpf_list : list of numpy array
                low pass filtered oxygen saturation signals (the trend) for debug purpose.
            

        Reference : 
            [1] Karhu, T., Leppänen, T., Töyräs, J., Oksenberg, A., Myllymaa, S., & Nikkonen, S. (2022).
            ABOSA - Freely available automatic blood oxygen saturation signal analysis software: 
            Structure and validation. Computer Methods and Programs in Biomedicine, 226, 107120. 
            https://doi.org/10.1016/j.cmpb.2022.107120
        """   
        data_lpf_list = []
        data_hpf_list = []
        all_desat_events = []
        plateau_lst = []
        lmin_indices_list = []
        lmax_indices_list = []        

        # ABOSA parameters
        min_peak_distance_sec = 5
        min_peak_prominence = 0.5
        order = 8
        # !!!!!!!!!!! try !!!
        low_frequency_cutoff = 0.1
        high_frequency_cutoff = 0.1
        # !!!!!!!!!!! try !!!
        min_peak_distance_samples = int(min_peak_distance_sec * fs_chan)

        if DEBUG:
            print("\n--- Detect desaturation events ---")
            print(f" detection parameters: min_peak_distance_sec={min_peak_distance_sec}, min_peak_prominence={min_peak_prominence}, order={order}, low_frequency_cutoff={low_frequency_cutoff}, high_frequency_cutoff={high_frequency_cutoff}")

        for i, signal in enumerate(data_stats):
            valid_mask = ~np.isnan(signal)
            if not np.any(valid_mask):
                continue
        
            # Detect artifact 
            # signal_clean is the raw signal with short artifacts interpolated and long artifact forced to NaN
            signal_clean, artifact_list = self.detect_artifact_SpO2(signal, data_starts[i], fs_chan)

            # Low pass filter the signal to get the trend in order to detect local min and max
            signal_lpf = self.filter_nan_filtfilt(signal_clean, order, fs_chan, low_frequency_cutoff, 'low')

            # High-pass filter the signal at 0.1 Hz (which is already low-pass filtered to 0.1 Hz)
            signal_hpf = self.filter_nan_filtfilt(signal_lpf, order, fs_chan, high_frequency_cutoff , 'high')
            
            # Step 1: Locate potential endpoints (Lmin)
            lmin_indices = self.detect_local_min(
                signal, signal_lpf, fs_chan, 
                min_peak_distance_samples, min_peak_prominence, 
                data_starts[i]
            )
            lmin_indices_list.append(lmin_indices)

            # Step 2: Locate potential starting points (Lmax)
            # lmax_indices (numpy array) : Indices of local maximums filtered for too low maximums.
            # lmax_indices_org (numpy array) : Indices of local maximums in the original signal.
            lmax_indices, lmax_indices_org = self.detect_local_max(
                signal, signal_lpf, fs_chan, 
                min_peak_distance_samples, min_peak_prominence, 
                data_starts[i]
            )
            lmax_indices_list.append(lmax_indices_org)

            # Step 3: Validate and match Lmax-Lmin pairs
            validated_events = []
            
            for lmax_idx in lmax_indices:
                lmax_time = data_starts[i] + lmax_idx / fs_chan
                lmax_val = signal[lmax_idx]
                
                # discard lmax without lmin
                #   The maximum duration of a desaturation event is limited to 180 s.
                #   The potential Lmax-Lmin pair cannot go through another Lmax.
                lmin_list = self.discard_lmax_without_lmin(
                    signal, lmin_indices, lmax_indices, lmax_idx, lmax_time, lmax_val,
                    data_starts[i], fs_chan, 
                    parameters_oxy['max_slope_drop_sec'], 
                    parameters_oxy['desaturation_drop_percent']
                )
                if lmin_list is None:
                    continue
                if DEBUG and len(lmin_list) > 1:
                    print(f"{len(lmin_list)} Lmins for current Lmax at {lmax_time:.2f}s")
                
                # Process all Lmin candidates through adjustments and validation
                validated_candidates = []
                for lmin_idx, lmin_time, lmin_val, drop in lmin_list:

                    # Adjust Lmax for fall rate
                    # The Lmax is shifted forward to a point where the fall starts using the low pass filtered signal.
                    adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, signal_squared = \
                        self.adjust_lmax_for_fall_rate(signal_lpf, signal_hpf, \
                                                       lmax_idx, lmin_idx, data_starts[i], fs_chan)
                    
                    # Adjust Lman and all Lmin candidates for plateau
                    min_plateau_duration_sec = 20
                    plateau_threshold = 0.1 # std threshold on filtered signal (more robust than max-min)
                    adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, \
                        adjusted_lmin_idx, adjusted_lmin_time, adjusted_lmin_val, plateau = \
                        self.adjust_for_plateau(
                            signal_lpf, adjusted_lmax_idx, adjusted_lmax_val, 
                            lmin_idx, lmin_time, lmin_val,
                            data_starts[i], fs_chan, 
                            min_plateau_duration_sec, plateau_threshold
                        )

                    if len(plateau) > 0:
                        plateau_lst.extend(plateau)

                    if adjusted_lmax_time >= adjusted_lmin_time:
                        if DEBUG:
                            print(f"Lmax at {adjusted_lmax_time:.2f}s is after Lmin at {adjusted_lmin_time:.2f}s after plateau adjustment")
                        break
                    
                    # # Make sure the lmax is the maximum value of the low-pass filtered signal until the lmin
                    # # The goal is to avoid an artificially long desaturation, when a second max occurs before the lmin
                    # possible_desat_signal = signal_lpf[adjusted_lmax_idx:adjusted_lmin_idx+1]
                    # print(f"adjusted_lmax_idx = {adjusted_lmax_idx}\n")
                    # if signal_lpf[adjusted_lmax_idx] < np.nanmax(possible_desat_signal):
                    #     if DEBUG:
                    #         print(f"  Lmax at {adjusted_lmax_time:.2f}s is not the maximum before Lmin at {adjusted_lmin_time:.2f}s")
                    #     continue

                    # Correct Lmax locations by finding actual maximum within 5s window on raw signal
                    adjusted_lmax_idx = self.correct_peak_indices_in_window(
                        signal, [adjusted_lmax_idx], window_s=5, fs_chan=fs_chan)
                    adjusted_lmax_idx = adjusted_lmax_idx[0]
                    adjusted_lmax_time = data_starts[i] + adjusted_lmax_idx / fs_chan
                    adjusted_lmax_val = signal[adjusted_lmax_idx]

                    # Correct Lmin locations by finding actual maximum within 5s window on raw signal
                    adjusted_lmin_idx = self.correct_peak_indices_in_window(
                        signal, [adjusted_lmin_idx], window_s=5, fs_chan=fs_chan, find_max=False)
                    adjusted_lmin_idx = adjusted_lmin_idx[0]
                    adjusted_lmin_time = data_starts[i] + adjusted_lmin_idx / fs_chan
                    adjusted_lmin_val = signal[adjusted_lmin_idx]

                    # Recalculate drop after adjustments
                    drop = adjusted_lmax_val - adjusted_lmin_val
                    duration = adjusted_lmin_time - adjusted_lmax_time
                    
                    # Calculate average fall rate (%/s)
                    avg_fall_rate = -drop / duration if duration > 0 else 0
                    
                    # Validate drop threshold, duration and fall rate limits
                    if ((drop >= parameters_oxy['desaturation_drop_percent']) and 
                        (duration >= parameters_oxy['min_hold_drop_sec']) and
                        (-4.0 <= avg_fall_rate <= -0.05)):
                        all_desat_events.append((adjusted_lmax_time, duration, avg_fall_rate))
                    else:
                        if DEBUG:
                            print(f"  Invalid desaturation: start={adjusted_lmax_time:.2f}s, "
                                  f"duration={duration:.2f}s, drop={drop:.1f}%, "
                                  f"fall_rate={avg_fall_rate:.3f}%/s")
                        # continue
                
                # # Select the first validated Lmin candidate
                # if len(validated_candidates) == 0:
                #     # if DEBUG:
                #     #     print(f"No validated Lmin candidates for Lmax at {lmax_time:.2f}s")
                #     continue


            # Debug output for the result view
            if DEBUG: 
                data_lpf_list.append(signal_lpf)
                data_hpf_list.append(signal_squared)

        # Resolve overlapping desaturations by keeping events with steepest fall rate
        all_desat_events = self.resolve_overlapping_desaturations(all_desat_events)

        # Create output dataframe
        # desat_events = [('SpO2', 'desat_SpO2', start_sec, duration_sec, channel) 
        #                 for start_sec, duration_sec in all_desat_events]
        desat_events = [('SpO2', 'desat_SpO2', start_sec, duration_sec, '') # Add back channel
                        for start_sec, duration_sec, _ in all_desat_events]
        # Add artifact events as invalid sections in desat_events
        desat_events += [('SpO2', 'art_SpO2', start_sec, duration_sec, '') # Add back channel
                         for start_sec, duration_sec in artifact_list]
        # plateau_events = [('SpO2', 'plateau_SpO2', start_sec, duration_sec, channel) 
        #                   for start_sec, duration_sec in plateau_lst]
        plateau_events = [('SpO2', 'plateau_SpO2', start_sec, duration_sec, '') 
                          for start_sec, duration_sec in plateau_lst]
        if DEBUG:
            print(f"\n{len(desat_events)} desat events before filtering out desat not starting in asleep\n")
            print(f"\n{len(plateau_events)} plateau events\n")
            for i in range(len(data_stats)):
                print(f"{len(lmax_indices_list[i])} possible max\n")
                print(f"{len(lmin_indices_list[i])} possible min\n")

        desat_df = manage_events.create_event_dataframe(data=desat_events)
        plateau_df = manage_events.create_event_dataframe(data=plateau_events)
  
        return desat_df, plateau_df, data_lpf_list, data_hpf_list, lmax_indices_list, lmin_indices_list


    def filter_nan_filtfilt(self, signal, order, fs_chan, cutoff_freq, type='low'):
        # We expect to have NaN values in chunk (if any)
        #   so we filter the signal (without nan values) even if it could have border effects
        #   and we reconstruct the filtered signal with the original NaN values.
        non_nan_indices = np.where(~np.isnan(signal))[0]
        if len(non_nan_indices) > 0:
            # reshape the i_nan_samples (x,1) to (x,)
            non_nan_indices = np.squeeze(non_nan_indices)
            samples_without_nan = signal[non_nan_indices]
            order_filtfilt = int(order)/2
            sos = scipysignal.butter(int(order_filtfilt), cutoff_freq,\
                btype=type, output='sos', fs=fs_chan)
            samples_filtered = scipysignal.sosfiltfilt(\
                sos, samples_without_nan).copy() # .copy() is a hack to make 
                                        # recording the EDF with pyedflib much
                                        # much much faster
            filtered_signal = np.empty_like(signal) 
            filtered_signal.fill(np.nan)
            filtered_signal[non_nan_indices] = samples_filtered
        else: # The whole signal is NaN - no filter applied
            filtered_signal = np.empty_like(signal)
            filtered_signal.fill(np.nan)
        return filtered_signal


    def detect_artifact_SpO2(self, sraw, data_start, fs_chan):
        """
        Detect major artifacts from oxygen saturation signal.
        
        First, major artifacts are detected from the signal (SRaw) by filtering 
        the SRaw signal with 4th order Butterworth high-pass filter with a 1 Hz cutoff. 
        Next, the filtered signal is squared. Values >30 in the squared signal, 
        and values <50% and >100% in the SRaw signal are counted as artifacts. 
        Adjacent artifact points are grouped into a single artifact, and artifacts 
        are extended by one second in both directions to add a safety margin. 
        However, artifacts with a duration of ≤5 s are linearly interpolated.
        
        Parameters:
        - sraw: Raw signal array (may contain NaNs)
        - data_start: Start time of the signal in seconds
        - fs_chan: Sampling rate in Hz
        
        Returns:
        - cleaned_signal: Signal with short artifacts interpolated
        - artifact_events: List of (start_sec, duration_sec) tuples for artifacts >5s
        """
        # List of constants
        filter_order = 4
        cutoff_freq = 1.0
        threshold_squared = 30
        lower_bound = 50
        upper_bound = 100
        art_buffer_sec = 1.0 # Extend each artifact by 1 second in both directions
        linear_art_sec = 5.0 # Interpolate artifacts with duration ≤ 5 seconds
        
        # 1. Identify artifact points directly from raw signal first
        # This avoids filter edge effects
        artifact_mask = np.zeros(len(sraw), dtype=bool)
        artifact_mask |= (sraw < lower_bound)
        artifact_mask |= (sraw > upper_bound)
        artifact_mask |= np.isnan(sraw)
        
        # 2. Apply 4th order Butterworth high-pass filter (1 Hz cutoff) on valid samples only
        filtered_signal = self.filter_nan_filtfilt(sraw, filter_order, fs_chan, cutoff_freq, 'high')
        
        # 3. Square the filtered signal
        squared_signal = filtered_signal ** 2
        
        # 4. Add high-frequency artifacts (rapid changes)
        artifact_mask |= (squared_signal > threshold_squared)
        
        # 5. Group adjacent artifacts and extend by 1 second
        diff = np.diff(np.concatenate([[0], artifact_mask.astype(int), [0]]))
        starts = np.where(diff == 1)[0]
        ends = np.where(diff == -1)[0]
        
        # Extend each artifact by 1 second in both directions
        # Note: 'start' is the first artifact sample, 'end' is one past the last artifact sample
        extension_samples = int(fs_chan * art_buffer_sec)
        extended_mask = np.zeros(len(sraw), dtype=bool)
        
        for start, end in zip(starts, ends):
            # Apply symmetric buffer: 1s before start and 1s after the last artifact sample
            extended_start = max(0, start - extension_samples)
            extended_end = min(len(sraw), end + extension_samples)
            extended_mask[extended_start:extended_end] = True
        
        # Re-identify artifact regions after extension
        diff = np.diff(np.concatenate([[0], extended_mask.astype(int), [0]]))
        starts = np.where(diff == 1)[0]
        ends = np.where(diff == -1)[0]
        
        # 6. Interpolate artifacts with duration ≤ 5 seconds
        cleaned_signal = sraw.copy()
        threshold_samples = int(fs_chan * linear_art_sec)
        artifact_events = []
        
        for start, end in zip(starts, ends):
            # start is first artifact sample, end is first non-artifact sample
            duration = end - start
            
            if duration <= threshold_samples:
                # Linear interpolation for short artifacts
                if start > 0 and end < len(sraw):
                    x = [start - 1, end]
                    y = [sraw[start - 1], sraw[end]]
                    interpolator = interp1d(x, y, kind='linear')
                    cleaned_signal[start:end] = interpolator(np.arange(start, end))
                
                # Mark as non-artifact after interpolation
                extended_mask[start:end] = False
            else:
                # Keep artifacts longer than 5s
                start_sec = (start / fs_chan) + data_start
                duration_sec = duration / fs_chan
                artifact_events.append((start_sec, duration_sec))
        
        return cleaned_signal, artifact_events


    def correct_peak_indices_in_window(self, signal, peak_indices, window_s, fs_chan, find_max=True):
        """
        Correct peak locations by finding actual extrema in the original signal within a time window.
        
        Parameters:
            signal : numpy array
                Original SpO2 signal.
            peak_indices : numpy array or list
                Indices of peaks to correct.
            window_s : float
                Window duration in seconds (centered on each peak).
            fs_chan : float
                Sampling frequency (Hz).
            find_max : bool
                If True, find maximum within window; if False, find minimum.
        
        Returns:
            corrected_indices : numpy array
                Corrected indices of peaks in the original signal.
        """
        half_window_samples = int((window_s / 2) * fs_chan)
        corrected_indices = []
        
        for peak_idx in peak_indices:
            # Define window boundaries
            window_start = max(0, peak_idx - half_window_samples)
            window_end = min(len(signal), peak_idx + half_window_samples)
            
            # Find actual extremum within window
            window_signal = signal[window_start:window_end]
            if len(window_signal) > 0 and not np.all(np.isnan(window_signal)):
                if find_max:
                    local_extremum_idx = np.nanargmax(window_signal)
                else:
                    local_extremum_idx = np.nanargmin(window_signal)
                corrected_idx = window_start + local_extremum_idx
                corrected_indices.append(corrected_idx)
        
        return np.array(corrected_indices)


    def detect_local_min(self, signal, signal_lpf, fs_chan, min_peak_distance_samples, min_peak_prominence, data_start):
        """
        Detect local minimums from the low-pass filtered signal and correct their location
        by finding the actual minimum in the original signal within a 10s window.
        
        Parameters:
            signal : numpy array
                Original SpO2 signal.
            signal_lpf : numpy array
                Low-pass filtered SpO2 signal for trend detection.
            fs_chan : float
                Sampling frequency (Hz).
            min_peak_distance_samples : int
                Minimum distance between peaks in samples.
            min_peak_prominence : float
                Minimum prominence for peak detection.
            data_start : float
                Start time in seconds of this signal section.
        
        Returns:
            lmin_indices_corrected : numpy array
                Corrected indices of local minimums in the original signal.
        """
        window_s = 10  # seconds window to identify the real minimum
        half_window_samples = int((window_s / 2) * fs_chan)
        
        # Invert the signal to find minimums using find_peaks
        inverted_signal = -signal_lpf
        
        # Find local minimums (peaks in inverted signal)
        lmin_indices, lmin_properties = scipysignal.find_peaks(
            inverted_signal,
            distance=min_peak_distance_samples,
            prominence=min_peak_prominence
        )
        
        # Correct Lmin locations by finding actual minimum within 10s window
        lmin_indices_corrected = self.correct_peak_indices_in_window(
            signal, lmin_indices, window_s, fs_chan, find_max=False
        )
        
        if DEBUG:
            lmin_times_sec = data_start + lmin_indices_corrected / fs_chan
            lmin_values = signal[lmin_indices_corrected] if len(lmin_indices_corrected) > 0 else []
            print(f"Found {len(lmin_indices_corrected)} local minimums (corrected within {window_s}s window)\n")
            # for idx, (t, v) in enumerate(zip(lmin_times_sec, lmin_values)):
            #     print(f"  Lmin {idx}: time={t:.2f}s, value={v:.1f}%")
        
        return lmin_indices_corrected


    def detect_local_max(self, signal, signal_lpf, fs_chan, min_peak_distance_samples, min_peak_prominence, data_start):
        """
        Detect local maximums from the low-pass filtered signal and correct their location
        by finding the actual maximum in the original signal within a 5s window (to validate).

        If the difference is <3 percentage points between 2 consecutive Lmax, the first Lmax is removed.
        
        Parameters:
            signal : numpy array
                Original SpO2 signal.
            signal_lpf : numpy array
                Low-pass filtered SpO2 signal for trend detection.
            fs_chan : float
                Sampling frequency (Hz).
            min_peak_distance_samples : int
                Minimum distance between peaks in samples.
            min_peak_prominence : float
                Minimum prominence for peak detection.
            data_start : float
                Start time in seconds of this signal section.
        
        Returns:
            filtered_lmax_indices : numpy array
                Indices of local maximums filtered for too low maximums.
            lmax_indices_org : numpy array
                Indices of local maximums in the original signal.
        """
        window_s = 10  # seconds window to identify the real maximum
        min_drop_2_consecutive_max = 3  # minimum drop in SRaw values between two consecutive Lmaxs to consider both Lmaxs
        
        # Find local maximums using find_peaks on the filtered signal
        lmax_indices, lmax_properties = scipysignal.find_peaks(
            signal_lpf,
            distance=min_peak_distance_samples,
            prominence=min_peak_prominence
        )

        # Correct Lmax locations by finding actual maximum within 10s window
        lmax_indices_org = self.correct_peak_indices_in_window(
            signal, lmax_indices, window_s, fs_chan, find_max=True
        )

        # Lmaxvalues that are too low to potentially result in proper desaturation events are removed. 
        # This is done by checking the maximum difference in SRaw values between two adjacent Lmaxs: 
        # if the difference is <3 percentage points, the first Lmax is removed
        filtered_lmax_indices = []
        for i in range(len(lmax_indices_org)-1):
            current_lmax_idx = lmax_indices_org[i]
            next_lmax_idx = lmax_indices_org[i+1]
            signal_vals = signal[current_lmax_idx:next_lmax_idx]
            if len(signal_vals) > 1:
                current_lmax_val = np.nanmax(signal_vals)
                current_lmin_val = np.nanmin(signal_vals)
                if (current_lmax_val - current_lmin_val) >= min_drop_2_consecutive_max:
                    filtered_lmax_indices.append(current_lmax_idx)
            else:
                continue
        
        if DEBUG:
            lmax_times_sec = data_start + filtered_lmax_indices / fs_chan
            lmax_values = signal[filtered_lmax_indices] if len(filtered_lmax_indices) > 0 else []
            print(f"Found {len(filtered_lmax_indices)} local maximums (corrected within {window_s}s window)\n")
            # for idx, (t, v) in enumerate(zip(lmax_times_sec, lmax_values)):
            #     print(f"  Lmax {idx}: time={t:.2f}s, value={v:.1f}%")
        
        return filtered_lmax_indices, lmax_indices_org

    def discard_lmax_without_lmin(self, signal, lmin_indices, lmax_indices, lmax_idx, lmax_time, lmax_val, 
                                  data_start, fs_chan, max_slope_drop_sec, desaturation_drop_percent):
        """
        Find the best Lmin candidate for a given Lmax (lmax_idx).

        The maximum duration of a desaturation event is limited to 180 s.
        The potential Lmax-Lmin pair cannot go through another Lmax.
        
        Parameters:
            signal : numpy array
                Original SpO2 signal.
            lmin_indices : numpy array
                Indices of local minimums.
            lmax_indices : numpy array
                Indices of local maximums.
            lmax_idx : int
                Index of the current Lmax.
            lmax_time : float
                Time in seconds of the current Lmax.
            lmax_val : float
                Value of the current Lmax.
            data_start : float
                Start time in seconds of this signal section.
            fs_chan : float
                Sampling frequency (Hz).
            max_slope_drop_sec : float
                Maximum duration for the desaturation drop.
            desaturation_drop_percent : float
                Minimum drop percentage to be considered a desaturation.
        
        Returns:
            best_lmin : tuple or None
                (lmin_idx, lmin_time, lmin_val, drop) or None if no valid candidate.
        """
        max_end_time = lmax_time + max_slope_drop_sec
        candidate_lmins = []
        
        for lmin_idx in lmin_indices:
            lmin_time = data_start + lmin_idx / fs_chan
            
            # Lmin must be after Lmax and within max duration
            if lmin_time <= lmax_time or lmin_time > max_end_time:
                continue
            
            # Check if there's another Lmax between current Lmax and this Lmin
            current_pos = np.where(lmax_indices == lmax_idx)[0][0]
            if current_pos + 1 < len(lmax_indices):
                next_lmax_time = data_start + lmax_indices[current_pos + 1] / fs_chan
                if next_lmax_time < lmin_time:
                    continue
            
            lmin_val = signal[lmin_idx]
            drop = lmax_val - lmin_val
            
            # Reject if drop is less than minimum threshold
            if drop < desaturation_drop_percent:
                continue
            
            candidate_lmins.append((lmin_idx, lmin_time, lmin_val, drop))
        
        if not candidate_lmins:
            return None
        
        return candidate_lmins


    def adjust_lmax_for_fall_rate(self, signal, signal_hpf, lmax_idx, lmin_idx, data_start, fs_chan, fall_rate_threshold=-0.05):
        """
        Shift Lmax forward to the next variation peak.
        The signal (already low-pass filtered) is high-pass filtered at 0.2 Hz,
        squared, and peaks are detected. Lmax is shifted to the next peak.
        
        Parameters:
            signal : numpy array
                Original SpO2 signal (already low-pass filtered).
            lmax_idx : int
                Index of the current Lmax.
            lmin_idx : int
                Index of the matched Lmin.
            data_start : float
                Start time in seconds of this signal section.
            fs_chan : float
                Sampling frequency (Hz).
            fall_rate_threshold : float
                Fall rate threshold in %/s (not used in new implementation).
        
        Returns:
            adjusted_lmax_idx : int
                Adjusted index of Lmax.
            adjusted_lmax_time : float
                Adjusted time of Lmax.
            adjusted_lmax_val : float
                Adjusted value of Lmax.
        """
        # Find maximum parameter
        min_peak_distance_sec = 1
        #min_peak_prominence = 0.01

        # Invert the variation because we want to identify maximum drops
        signal_squared = signal_hpf ** 2
        
        # Detect peaks in the inverted signal - we are looking for the biggest drops
        min_peak_distance_samples = int(min_peak_distance_sec * fs_chan)  
        peaks, _ = scipysignal.find_peaks(
            signal_squared,
            distance=min_peak_distance_samples,
            #prominence=min_peak_prominence
        )
        
        # Find the next peak after lmax_idx
        adjusted_lmax_idx = lmax_idx
        next_peaks = peaks[peaks > lmax_idx]
        possible_peaks = next_peaks[next_peaks < lmin_idx]

        if len(possible_peaks) > 0:
            # Loop through all peaks before lmin_idx and keep shifting to better maxima
            for peak_idx in possible_peaks:
                    
                # Correct peak locations within 1s window
                lmax_corrected = self.correct_peak_indices_in_window(signal, [adjusted_lmax_idx], window_s=1, fs_chan=fs_chan)
                lmax_corrected = lmax_corrected[0]
                lmax_shifted = self.correct_peak_indices_in_window(signal, [peak_idx], window_s=1, fs_chan=fs_chan)
                lmax_shifted = lmax_shifted[0]
                
                # Check if the shifted peak is higher (better maximum)
                if signal[lmax_shifted] > signal[lmax_corrected]:
                    adjusted_lmax_idx = lmax_shifted
                else:
                    # Evaluate fall rate to ensure it's a valid shift
                    duration_sec = (lmax_shifted - lmax_corrected) / fs_chan
                    drop = signal[lmax_shifted] - signal[lmax_corrected]
                    fall_rate = drop / duration_sec if duration_sec > 0 else 0
                    if fall_rate >= fall_rate_threshold:
                        adjusted_lmax_idx = lmax_shifted
                    # If fall rate is too steep, keep current position and stop
                    else:
                        break
        
        adjusted_lmax_time = data_start + adjusted_lmax_idx / fs_chan
        adjusted_lmax_val = signal[adjusted_lmax_idx]
        return adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, signal_squared


    def adjust_for_plateau(self, signal, adjusted_lmax_idx, adjusted_lmax_val, lmin_idx, lmin_time, lmin_val, 
                           data_start, fs_chan, min_plateau_duration_sec=30, plateau_threshold=0.2):
        """
        Adjust Lmax or Lmin if a flat plateau exists within the event.
        The plateau length is dynamically determined (minimum 30s, can be longer).
        Iteratively detects plateaus until no more are found or the remaining duration is < 30s.
        
        Parameters:
            signal : numpy array
                Low-pass filtered SpO2 signal.
            adjusted_lmax_idx : int
                Current adjusted Lmax index.
            adjusted_lmax_val : float
                Current adjusted Lmax value.
            lmin_idx : int
                Current Lmin index.
            lmin_time : float
                Current Lmin time.
            lmin_val : float
                Current Lmin value.
            data_start : float
                Start time in seconds of this signal section.
            fs_chan : float
                Sampling frequency (Hz).
            min_plateau_duration_sec : float
                Minimum plateau duration in seconds (default 30s).
            plateau_threshold : float
                Maximum standard deviation to be considered flat (default 0.2%).
        
        Returns:
            adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, lmin_idx, lmin_time, lmin_val, plateau_list : tuple
                Adjusted values after plateau handling and list of all detected plateaus.
        """
        min_plateau_samples = int(min_plateau_duration_sec * fs_chan)
        plateau_list = []
        
        # Iterate to detect multiple plateaus
        while True:
            event_signal = signal[adjusted_lmax_idx:lmin_idx + 1]
            adjusted_lmax_time = data_start + adjusted_lmax_idx / fs_chan
            
            # Stop if remaining duration is less than minimum plateau duration
            if len(event_signal) < min_plateau_samples:
                break
            
            # Look for plateau start (minimum 30s)
            best_plateau_start = None
            best_plateau_end = None
            
            for p_start in range(len(event_signal) - min_plateau_samples):
                p_end = p_start + min_plateau_samples
                plateau_segment = event_signal[p_start:p_end]
                
                # Check if this 30s window is flat enough using standard deviation
                if np.nanstd(plateau_segment) <= plateau_threshold:
                    best_plateau_start = p_start
                    best_plateau_end = p_end
                    
                    # Extend plateau as long as it remains flat
                    while best_plateau_end < len(event_signal):
                        # Check if adding the next sample keeps the plateau flat
                        extended_segment = event_signal[best_plateau_start:best_plateau_end + 1]
                        if np.nanstd(extended_segment) <= plateau_threshold:
                            best_plateau_end += 1
                        else:
                            break
                    
                    break
            
            # If no plateau found, stop iterating
            if best_plateau_start is None:
                break
            
            # Store plateau information
            plateau_start_time = data_start + (adjusted_lmax_idx + best_plateau_start) / fs_chan
            plateau_duration = (best_plateau_end - best_plateau_start) / fs_chan
            plateau_list.append([plateau_start_time, plateau_duration])
            
            # Adjust Lmax or Lmin to maximize depth
            plateau_val = np.nanmean(event_signal[best_plateau_start:best_plateau_end])
            drop_before_plateau = adjusted_lmax_val - plateau_val
            drop_after_plateau = plateau_val - lmin_val
            
            if drop_before_plateau > drop_after_plateau:
                # Shift Lmin to start of plateau
                lmin_idx = adjusted_lmax_idx + best_plateau_start
                lmin_time = data_start + lmin_idx / fs_chan
                lmin_val = signal[lmin_idx]
            else:
                # Shift Lmax to end of plateau
                adjusted_lmax_idx = adjusted_lmax_idx + best_plateau_end
                adjusted_lmax_time = data_start + adjusted_lmax_idx / fs_chan
                adjusted_lmax_val = signal[adjusted_lmax_idx]

        return adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, lmin_idx, lmin_time, lmin_val, plateau_list

    def compute_desat_stats(self, desat_df, asleep_stages_df):
        desat_stats = {}
        # The number of oxygen desaturation from lights off to lights on in asleep stages only.
        desat_stats['desat_count'] = len(desat_df)
        # The average duration in sec of the oxygen desaturation events occuring in asleep stages.
        desat_stats['desat_avg_sec'] = desat_df['duration_sec'].mean()
        # The std value of the duration in sec of the oxygen desaturation events occuring in asleep stages.
        desat_stats['desat_std_sec'] = desat_df['duration_sec'].std()
        # The median value of the duration in sec of the oxygen desaturation events occuring in asleep stages.
        desat_stats['desat_med_sec'] = desat_df['duration_sec'].median()
        # The percentage of time spent in desaturation during the asleep stages.
        desat_stats['desat_sleep_percent'] = desat_df['duration_sec'].sum()/asleep_stages_df['duration_sec'].sum()*100
        # The Oxygen Desaturation Index (ODI) : number of desaturation per sleep hour.
        desat_stats['desat_ODI'] = len(desat_df)/(asleep_stages_df['duration_sec'].sum()/3600)
        return desat_stats

    
    def compute_temporal_link_stats(self, desat_df, arousals_selected, window_link_sec, channel):
        """
        Parameters :
            desat_df : pandas DataFrame
                desaturation events
                'group': Group of events this event is part of (String)
                'name': Name of the event (String)
                'start_sec': Starting time of the event in sec (Float)
                'duration_sec': Duration of the event in sec (Float)
                'channels' : Channel where the event occures (String)
            arousals_selected : pandas DataFrame
                arousals events in asleep stages and duration limits applied
            window_link_sec     : float
                The window length (s) to compute the temporal link between desaturations and arousals.
            channel     : string
                Channel label.
        Return : 
            temporal_stats : dict
                Dictionary of statistics
                'desat_start_before_count' : 'The number of desaturations that start before the beginning of the arousal.',
                'desat_start_before_delay_sec' : 'Arousal starts before desaturation- The average delay between arousal and the beginning of the desaturation in sec.',
                'desat_end_before_count' : 'The number of desaturations that end before the beginning of the arousal.',
                'desat_end_before_delay_sec' : 'Desaturation ends before arousal - The average delay between desaturations and the beginning of the arousal in sec.', 
                'arousal_start_before_count' : 'The number of arousals that start before the beginning of the desaturation.',
                'arousal_start_before_delay_sec' : 'Arousal starts before desaturation- The average delay between arousal and the beginning of the desaturation in sec.',
                'arousal_end_before_count' : 'The number of arousals that end before the beginning of the desaturation.',
                'arousal_end_before_delay_sec' : 'Arousal ends before desaturation- The average delay between arousal and the beginning of the desaturation in sec.'                
            link_event_df : pandas DataFrame
                Temporal link events.
        """           
        temporal_stats = {}
        
        # Desaturation first - start
        #---------------------------
        flat_list_delay, i_evt1_linked, i_evt2_unique = \
            EventTemporalLink.compute_delay_start(self, desat_df, arousals_selected, window_link_sec)
        # The number of desaturations that start before the beginning of the arousal.
        temporal_stats['desat_start_before_count'] = len(flat_list_delay)
        if len(flat_list_delay)>0:
            # Desaturation starts before arousal- The average delay between desaturation and the beginning of the arousal in sec.
            temporal_stats['desat_start_before_delay_sec'] = np.mean(flat_list_delay)
            link_start = []
            for i_link in range(len(i_evt1_linked)):
                start_sec = desat_df.loc[i_evt1_linked[i_link]]['start_sec']
                duration_sec = arousals_selected.loc[i_evt2_unique[i_link]]['start_sec']-start_sec
                link_start.append(['SpO2','SpO2_desat_start_link', start_sec, duration_sec, channel])
            link_desat_start_df = manage_events.create_event_dataframe(link_start)
        else:
            temporal_stats['desat_start_before_delay_sec'] = np.nan
            link_desat_start_df = manage_events.create_event_dataframe(None)

        # Desaturation first - end
        #---------------------------
        flat_list_delay, i_evt1_linked, i_evt2_unique = \
            EventTemporalLink.compute_delay_end(self, desat_df, arousals_selected, window_link_sec)
        # The number of desaturations that end before the beginning of the arousal.
        temporal_stats['desat_end_before_count'] = len(flat_list_delay)
        if len(flat_list_delay)>0:
            # Desaturation ends before arousal - The average delay between desaturations and the beginning of the arousal in sec.
            temporal_stats['desat_end_before_delay_sec'] = np.mean(flat_list_delay)
            link_start = []
            for i_link in range(len(i_evt1_linked)):
                start_sec = desat_df.loc[i_evt1_linked[i_link]]['start_sec']+desat_df.loc[i_evt1_linked[i_link]]['duration_sec']
                duration_sec = arousals_selected.loc[i_evt2_unique[i_link]]['start_sec']-start_sec
                link_start.append(['SpO2','SpO2_desat_end_link', start_sec, duration_sec, channel])
            link_desat_end_df = manage_events.create_event_dataframe(link_start)
        else:
            temporal_stats['desat_end_before_delay_sec'] = np.nan
            link_desat_end_df = manage_events.create_event_dataframe(None)

        # Arousal first - start
        #---------------------------
        flat_list_delay, i_evt1_linked, i_evt2_unique = \
            EventTemporalLink.compute_delay_start(self, arousals_selected, desat_df, window_link_sec)
        # The number of arousal that start before the beginning of the desaturation.
        temporal_stats['arousal_start_before_count'] = len(flat_list_delay)
        if len(flat_list_delay)>0:
            # Arousal starts before desaturation- The average delay between arousal and the beginning of the desaturation in sec.
            temporal_stats['arousal_start_before_delay_sec'] = np.mean(flat_list_delay)
            link_start = []
            for i_link in range(len(i_evt1_linked)):
                start_sec = arousals_selected.loc[i_evt1_linked[i_link]]['start_sec']
                duration_sec = desat_df.loc[i_evt2_unique[i_link]]['start_sec']-start_sec
                link_start.append(['SpO2','SpO2_arousal_start_link', start_sec, duration_sec, channel])
            link_arousal_start_df = manage_events.create_event_dataframe(link_start)
        else:
            temporal_stats['arousal_start_before_delay_sec'] = np.nan
            link_arousal_start_df = manage_events.create_event_dataframe(None)

        # Arousal first - end
        #---------------------------
        flat_list_delay, i_evt1_linked, i_evt2_unique = \
            EventTemporalLink.compute_delay_end(self, arousals_selected, desat_df, window_link_sec)
        # The number of arousal that end before the beginning of the desaturation.
        temporal_stats['arousal_end_before_count'] = len(flat_list_delay)
        if len(flat_list_delay)>0:
            # arousal ends before arousal - The average delay between arousal and the beginning of the desaturation in sec.
            temporal_stats['arousal_end_before_delay_sec'] = np.mean(flat_list_delay)        
            link_start = []
            for i_link in range(len(i_evt1_linked)):
                start_sec = arousals_selected.loc[i_evt1_linked[i_link]]['start_sec']+arousals_selected.loc[i_evt1_linked[i_link]]['duration_sec']
                duration_sec = desat_df.loc[i_evt2_unique[i_link]]['start_sec']-start_sec
                link_start.append(['SpO2','SpO2_arousal_end_link', start_sec, duration_sec, channel])
            link_arousal_end_df = manage_events.create_event_dataframe(link_start)