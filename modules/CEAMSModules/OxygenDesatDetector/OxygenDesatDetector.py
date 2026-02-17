"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    OxygenDesatDetector
    A Class to analyze the oxygen channel, detect oxygen desaturations and export oxygen saturation report.
"""
#from time import time
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
        self.stage_stats_labels =   ['N1',   'N2',   'N3',   'R',    'W',    'NREM',             'N2N3',         'SLEEP']
        self.stage_stats_list =     [['N1'], ['N2'], ['N3'], ['R'], ['W'],   ['N1', 'N2', 'N3'], ['N2', 'N3'], ['N1', 'N2', 'N3', 'R', 'W']]
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

        #------------------------------------------------------------------------------
        # Header parameters
        # subject info, sleep cycle parameters, desaturation parameters
        #------------------------------------------------------------------------------
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

        # Keep stages from the first sleep stage (1-5) to the last sleep stage (1-5) to define the sleep period
        sleep_stage_df.loc[:, 'name'] = sleep_stage_df['name'].apply(int)
        index_sleep = sleep_stage_df[(sleep_stage_df['name']>=1) & (sleep_stage_df['name']<=5)].index
        stage_sleep_period_df = sleep_stage_df.loc[index_sleep[0]:index_sleep[-1]]
        stage_sleep_period_df.reset_index(inplace=True, drop=True)

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

        # Extract samples for the sleep period
        data_stats, data_starts = self.extract_signal_data_for_sleep_period(stage_sleep_period_df, signals)

        # Detect artifact 
        #   data_clean is the raw signal with short artifacts interpolated and long artifact forced to NaN
        artifact_events = []
        data_clean, artifact_det_lst = self.detect_artifact_SpO2(data_stats, data_starts, fs_chan)
        artifact_events += [('SpO2', 'art_SpO2', start_sec, duration_sec, '') # Add back channel
                         for start_sec, duration_sec in artifact_det_lst]
        # Convert artifact_events to dataframe
        artifact_events_df = manage_events.create_event_dataframe(data=artifact_events)
        # Add artifact events to invalid events
        invalid_events = pd.concat([invalid_events, artifact_events_df], ignore_index=True)

        # Compute stats for the sleep period
        #----------------------------------------------------------------------
        total_stats = self.compute_total_stats_saturation(\
            stage_sleep_period_df, data_clean, data_starts, \
                subject_info, fs_chan, picture_dir, invalid_events)

        # Compute stats for thirds
        #----------------------------------------------------------------------
        n_divisions = 3
        section_label = 'third'
        third_stats = self.compute_division_stats_saturation(\
            n_divisions, section_label, stage_sleep_period_df, data_clean, data_starts, fs_chan)

        # Compute stats for halves
        #----------------------------------------------------------------------
        n_divisions = 2
        section_label = 'half'
        half_stats = self.compute_division_stats_saturation(\
            n_divisions, section_label, stage_sleep_period_df, data_clean, data_starts, fs_chan)

        # Compute stats for stages
        #----------------------------------------------------------------------       
        stage_stats = self.compute_stages_stats_saturation(\
            stage_sleep_period_df, data_clean, data_starts, fs_chan)

        # Compute stats for cycles
        #----------------------------------------------------------------------       
        cycle_stats = self.compute_cycles_stats_saturation(\
            sleep_cycles_df,  data_clean, data_starts, fs_chan)

        # Detect desaturation 
        #----------------------------------------------------------------------
        # time the processing time for detection desaturation
        #start_time = time.time()
            # "parameters_oxy": dict
            # 'desaturation_drop_percent' : 'Drop level (%) for the oxygen desaturation "3 or 4"',
            # 'max_slope_drop_sec' : 'The maximum duration (s) during which the oxygen level is dropping "180 or 20"',
            # 'min_hold_drop_sec' : 'Minimum duration (s) during which the oxygen level drop is maintained "10 or 5"',
        desat_df, plateau_df, data_lpf_list, data_hpf_list, data_dev_list, lmax_indices_list, lmin_indices_list = \
            self.detect_desaturation_ABOSA(data_starts, data_clean, fs_chan, channel, parameters_oxy)
        #end_time = time.time()
        # Log message for the Logs tab
        #self._log_manager.log(self.identifier, f"{len(desat_df)} desaturation events in {end_time - start_time:.2f} seconds.")
        
        # Save the list of desaturation events detected and their characteristics
        #----------------------------------------------------------------------
        # filename including path to save the dataframe 
        picture_dir_channel = os.path.join(picture_dir, subject_info['filename'])
        # Save the oxygen saturation events with characteristics
        if len(picture_dir)>0:
            file_events_name = os.path.join(picture_dir, f"{subject_info['filename']}_oxygen_saturation_events.tsv")
            pd.DataFrame.to_csv(desat_df, path_or_buf=file_events_name, sep='\t', index=False, encoding="utf_8")
            
        # Compute desaturation stats
        #----------------------------------------------------------------------
        desat_stats = self.compute_desat_stats(desat_df, total_stats, stage_sleep_period_df)

        # Remove desaturation features not included in the Snooz annotations
        #----------------------------------------------------------------------
        # Keep ['group', 'name', 'start_sec', 'duration_sec', 'channels']
        desat_df = desat_df[['group', 'name', 'start_sec', 'duration_sec', 'channels']]

        # Add invalid sections to desaturation events
        desat_df = pd.concat([desat_df, invalid_events], ignore_index=True)

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
                signal_dev = signals[index_longuest].clone(clone_samples=False)
                signal_raw.samples = data_stats[index_longuest]
                signal_raw.start_time = data_starts[index_longuest]
                signal_lpf.samples = data_lpf_list[index_longuest]
                signal_lpf.start_time = data_starts[index_longuest]
                signal_lpf.channel = signal_raw.channel+'_lpf'
                signal_dev.samples = data_dev_list[index_longuest]
                signal_dev.start_time = data_starts[index_longuest]
                signal_dev.channel = signal_raw.channel+'_dev'
                signal_hpf.samples = data_hpf_list[index_longuest]
                signal_hpf.start_time = data_starts[index_longuest]
                signal_hpf.channel = signal_raw.channel+'_hpf'
                cache['signal_raw'] = signal_raw
                cache['signal_lpf'] = signal_lpf
                cache['signal_hpf'] = signal_dev
                #cache['signal_dev'] = signal_dev
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

    def compute_division_stats_saturation(self, n_divisions, section_label, stage_sleep_period_df, data_clean, data_starts, fs):
        """""
            Compute the statistics (mean, std, max and min) of the oxygen saturation for the requested division.
            n_divisions can be 3 or 2.

            Parameters
            -----------
                n_divisions                 : int
                    Number of divisions.
                section_label               : string
                    Label of the division.
                stage_sleep_period_df                : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])  
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
        n_epochs = len(stage_sleep_period_df)
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
            start = stage_sleep_period_df.iloc[index_start]['start_sec']
            end = stage_sleep_period_df.iloc[index_stop-1]['start_sec']+ stage_sleep_period_df.iloc[index_stop-1]['duration_sec']
            dur = end - start
            signals_third = []
            for samples, data_start in zip(data_clean, data_starts):
                # Because of the discontinuity
                # we have to verify if the signal includes at least partially the events
                # Look for the Right windows time
                if (data_start<(start+dur)) and ((data_start+len(samples)/fs)>start): 
                    # Extract samples for the current division
                    channel_cur_samples = self.extract_samples_from_array(samples, data_start, start, dur, fs)
                    signals_third.append(channel_cur_samples)

            # Flat signals into an array
            data_array = np.empty(0)
            for i_bout, samples in enumerate(signals_third):
                if len(data_array)==0:
                    data_array = samples
                else:
                    data_array = np.concatenate((data_array, samples), axis=0)

            # Clean-up invalid values
            #data_array = np.round(data_array,0) # to copy Gaetan
            data_array[data_array>100]=np.nan
            data_array[data_array<=0]=np.nan
            stats_dict[f"{section_label}{section_val}_saturation_avg"] = np.nanmean(data_array)
            stats_dict[f"{section_label}{section_val}_saturation_std"] = np.nanstd(data_array)
            # stats_dict[f"{section_label}{section_val}_saturation_min"] = np.round(np.nanmin(data_array),0)
            # stats_dict[f"{section_label}{section_val}_saturation_max"] = np.round(np.nanmax(data_array),0)     
            stats_dict[f"{section_label}{section_val}_saturation_min"] = np.nanmin(data_array)
            stats_dict[f"{section_label}{section_val}_saturation_max"] = np.nanmax(data_array)     
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
    

    def extract_signal_data_for_sleep_period(self, stage_sleep_period_df, signals):
        """
        Extract signal data and start times for the sleep period, handling discontinuities.

        Parameters :
            stage_sleep_period_df : pandas DataFrame
                Sleep stages from lights off to lights on.
            signals : list of SignalModel
                List of SignalModel objects from the whole recording.

        Return : 
            data_stats : list of numpy array
                Oxygen saturation values (cleaned: >100 or <=0 set to NaN) for each continuous section.
            data_starts : list of float
                Start time in sec of each continuous section (more than one when there are discontinuities).
        """
        start = stage_sleep_period_df['start_sec'].values[0]
        end = stage_sleep_period_df['start_sec'].values[-1] + stage_sleep_period_df['duration_sec'].values[-1]
        dur = end - start
        data_stats = []
        data_starts = []
        for signal in signals:
            # Because of the discontinuity
            # we have to verify if the signal includes at least partially the events
            # Look for the Right windows time
            if (signal.start_time < (start + dur)) and ((signal.start_time + signal.duration) > start):
                cur_start = signal.start_time if start <= signal.start_time else start
                cur_end = end if end <= signal.end_time else signal.end_time
                # Extract and define the new extracted channel_cur
                channel_cur = self.extract_samples_from_events(signal, cur_start, cur_end - cur_start)
                # Clean-up invalid values
                # channel_cur[channel_cur > 100] = np.nan
                # channel_cur[channel_cur <= 0] = np.nan
                data_starts.append(cur_start)
                data_stats.append(channel_cur)
        return data_stats, data_starts


    def extract_samples_from_array(self, samples, data_start, start, dur, fs):
        """
        Extract samples from a numpy array for a given time window.

        Parameters :
            samples : numpy array
                Signal samples.
            data_start : float
                Start time in sec of the signal array.
            start : float
                Start time in sec of the window to extract.
            dur : float
                Duration in sec of the window to extract.
            fs : float
                Sampling rate in Hz.

        Return : 
            extracted_samples : numpy array
                Samples within the specified time window.
        """
        signal_start_samples = int(data_start * fs)
        end_time = start + dur
        first_sample = int(start * fs)
        last_sample = int(end_time * fs)
        # Add verification to avoid negative indexing
        if first_sample - signal_start_samples < 0:
            first_sample = signal_start_samples
        # Add verification to avoid exceeding array length
        if last_sample - signal_start_samples > len(samples):
            last_sample = len(samples) + signal_start_samples
        extracted_samples = samples[first_sample - signal_start_samples:last_sample - signal_start_samples]
        return extracted_samples


    def compute_total_stats_saturation(self, stage_sleep_period_df, data_clean, data_starts, subject_info, fs_chan, picture_dir, invalid_events):
        """
        Parameters :
            stage_sleep_period_df : pandas DataFrame
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
        # Compute duration of sleep period for stats
        sleep_period_start_sec = stage_sleep_period_df['start_sec'].values[0]
        sleep_period_end_sec = stage_sleep_period_df['start_sec'].values[-1] + stage_sleep_period_df['duration_sec'].values[-1]
        sleep_period_dur_sec = sleep_period_end_sec - sleep_period_start_sec

        # Generate and save the oxygen saturation graph
        if len(picture_dir)>0:
            for i_bout, samples in enumerate(data_clean):
                fig_name = os.path.join(picture_dir, f"{subject_info['filename']}_oxygen_saturation{i_bout}.pdf")
                self._plot_oxygen_saturation(samples, fs_chan, fig_name, data_starts[i_bout], invalid_events)

        # Flat signals into an array (discontinuity handling)
        data_array = np.empty(0)
        for i_bout, samples in enumerate(data_clean):
            if data_array.size == 0:
                data_array = samples
            else:
                data_array = np.concatenate((data_array, samples), axis=0)

        total_stats = {}
        total_stats["sleep_period_min"] = sleep_period_dur_sec/60
        total_stats["total_valid_min"] = (len(data_array)-np.isnan(data_array).sum())/fs_chan/60
        total_stats["total_invalid_min"]  = np.isnan(data_array).sum()/fs_chan/60
        total_stats["total_saturation_avg"] = np.nanmean(data_array)
        total_stats["total_saturation_std"] = np.nanstd(data_array)
        total_stats["total_saturation_min"] = np.nanmin(data_array)
        total_stats["total_saturation_max"] = np.nanmax(data_array)
        for val in self.values_below:
            total_stats[f"total_below_{val}_percent"] = ((data_array<val).sum()/fs_chan)/(total_stats["total_valid_min"]*60)*100
        return total_stats


    def compute_stages_stats_saturation(self, stage_sleep_period_df, data_clean, data_starts, fs_chan):
        """
        Parameters :
            stage_sleep_period_df : pandas DataFrame
                Sleep stages from lights off to lights on.
            data_clean : list of numpy arrays   
                signal with channel, samples, sample_rate...
            data_starts : list
                start in sec of each continuous section (more than one when there are discontinuities)
            fs_chan : float
                sampling rate of the channel
        Return : 
            stage_dict : dict
                statistics fot the stages.
                Saturation_avg, std, min and max for each stage.
                Duration in min for saturation under different thresholds.
        """    
        stage_start_times = stage_sleep_period_df['start_sec'].to_numpy().astype(float)
        stage_duration_times = stage_sleep_period_df['duration_sec'].to_numpy().astype(float)
        stage_name = stage_sleep_period_df['name'].apply(str).to_numpy()

        stage_dict = {}
        for stage_label, stage_list in zip(self.stage_stats_labels, self.stage_stats_list):
            stage_mask = np.zeros(stage_name.shape, dtype=bool)
            for i in range(len(stage_list)):
                stage_mask = stage_mask | (stage_name == commons.sleep_stages_name[stage_list[i]])
            start_masked = stage_start_times[stage_mask]
            dur_masked = stage_duration_times[stage_mask]
            if any(stage_mask):
                signals_from_stages = []
                for start, dur in zip(start_masked, dur_masked):
                    for samples, start_signal in zip(data_clean, data_starts):
                        cur_samples = self.extract_samples_from_array(samples, start_signal, start, dur, fs_chan)
                        # When the last epoch is not completed
                        if (len(cur_samples)/fs_chan) < dur:
                            n_miss_samples = int(round((dur-len(cur_samples)/fs_chan)*fs_chan,0))
                            cur_samples = np.pad(cur_samples, (0, n_miss_samples), constant_values=(0,np.nan))
                        signals_from_stages.append(cur_samples)

                # Flat signals into an array
                signals_cur_stage = np.empty(0)
                for i_bout, samples in enumerate(signals_from_stages):
                    if signals_cur_stage.size == 0:
                        signals_cur_stage = samples
                    else:
                        signals_cur_stage = np.concatenate((signals_cur_stage, samples), axis=0)

                # Clean-up invalid values
                # signals_cur_stage[signals_cur_stage>100]=np.nan # handled in the artifact detection
                # signals_cur_stage[signals_cur_stage<=0]=np.nan  # handled in the artifact detection
                stage_dict[f'{stage_label}_saturation_avg'] = np.nanmean(signals_cur_stage)
                stage_dict[f'{stage_label}_saturation_std'] = np.nanstd(signals_cur_stage)
                stage_dict[f'{stage_label}_saturation_min'] = np.nanmin(signals_cur_stage)
                stage_dict[f'{stage_label}_saturation_max'] = np.nanmax(signals_cur_stage)
                for val in self.values_below:
                    signals_flat = signals_cur_stage.flatten()
                    n_valid = np.sum(~np.isnan(signals_flat)) # To excluded artifact from the total number of samples
                    stage_dict[f"{stage_label}_below_{val}_percent"] = (signals_flat<val).sum()/n_valid*100 if n_valid > 0 else np.nan
            else:
                stage_dict[f'{stage_label}_saturation_avg'] = np.nan
                stage_dict[f'{stage_label}_saturation_std'] = np.nan
                stage_dict[f'{stage_label}_saturation_min'] = np.nan
                stage_dict[f'{stage_label}_saturation_max'] = np.nan
                for val in self.values_below:
                    stage_dict[f"{stage_label}_below_{val}_percent"] = np.nan                           
        return stage_dict


    def compute_cycles_stats_saturation(self, sleep_cycles_df, data_clean, data_starts, fs_chan):
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
                for samples, data_start in zip(data_clean, data_starts):
                    # Because of the discontinuity
                    # we have to verify if the signal includes at least partially the events
                    # Look for the Right windows time
                    if (data_start<(start+dur)) and ((data_start+len(samples)/fs_chan)>start): 
                        # Extract and define the new extracted channel_cur
                        channel_cur = self.extract_samples_from_array(samples, data_start, start, dur, fs_chan)
                        signals_cyc.append(channel_cur)
                
                # Flat signals into an array
                data_stats = np.empty(0)
                for i_bout, samples in enumerate(signals_cyc):
                    if data_stats.size == 0:
                        data_stats = samples
                    else:
                        data_stats = np.concatenate((data_stats, samples), axis=0)

                #data_stats = np.round(data_stats,0) # to copy Gaétan   
                # Clean-up invalid values
                # data_stats[data_stats>100]=np.nan
                # data_stats[data_stats<=0]=np.nan        
                cyc_dict[f'cyc{i_cyc+1}_saturation_avg'] = np.nanmean(data_stats)
                cyc_dict[f'cyc{i_cyc+1}_saturation_std'] = np.nanstd(data_stats)
                cyc_dict[f'cyc{i_cyc+1}_saturation_min'] = np.nanmin(data_stats)
                cyc_dict[f'cyc{i_cyc+1}_saturation_max'] = np.nanmax(data_stats)
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

    def compute_desaturation_area(self, signal, data_start, start_sec, duration_sec, fs_chan):
        """
        Compute the area of a desaturation event.
        
        The area is calculated as the integral of the drop below the baseline (starting SpO2 value)
        over the duration of the event. The result is in %-seconds.
        
        Parameters:
            signal : numpy array
                SpO2 signal samples.
            data_start : float
                Start time in seconds of the signal array.
            start_sec : float
                Start time in seconds of the desaturation event.
            duration_sec : float
                Duration in seconds of the desaturation event.
            fs_chan : float
                Sampling frequency in Hz.
        
        Returns:
            area : float
                Area of the desaturation event in %-seconds.
        """
        # Extract samples for the desaturation event
        event_samples = self.extract_samples_from_array(signal, data_start, start_sec, duration_sec, fs_chan)
        
        if len(event_samples) == 0 or np.all(np.isnan(event_samples)):
            return np.nan
        
        # Baseline is the first valid sample (start of desaturation = max SpO2 before drop)
        baseline = event_samples[0] if not np.isnan(event_samples[0]) else np.nanmax(event_samples)
        
        # Compute the drop below baseline for each sample
        drop_below_baseline = baseline - event_samples
        drop_below_baseline = np.clip(drop_below_baseline, 0, None)  # Only count positive drops
        
        # Compute the area using trapezoidal integration
        # Each sample represents 1/fs_chan seconds
        dt = 1.0 / fs_chan
        area = np.nansum(drop_below_baseline) * dt
        
        return area


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
            current_start, current_dur, current_rate, current_drop = sorted_events[i]
            current_end = current_start + current_dur
            
            # Find all overlapping events
            overlapping = [(i, current_start, current_dur, current_rate, current_drop)]
            j = i + 1
            while j < len(sorted_events):
                next_start, next_dur, next_rate, next_drop = sorted_events[j]
                next_end = next_start + next_dur
                
                # Check for overlap: events overlap if next starts before current ends
                if next_start < current_end:
                    overlapping.append((j, next_start, next_dur, next_rate, next_drop))
                    # Update current_end to include the new event's range
                    current_end = max(current_end, next_end)
                    j += 1
                else:
                    break
            
            # Select the event with the steepest fall rate (most negative, closest to -4)
            best_event = min(overlapping, key=lambda x: x[3])  # x[3] is fall_rate
            resolved_events.append((best_event[1], best_event[2], best_event[3], best_event[4]))
            
            if DEBUG and len(overlapping) > 1:
                print(f"Resolved {len(overlapping)} overlapping desaturations:")
                for idx, start, dur, rate, drop in overlapping:
                    marker = " <-- KEPT" if (start, dur, rate, drop) == (best_event[1], best_event[2], best_event[3], best_event[4]) else ""
                    print(f"  start={start:.2f}s, duration={dur:.2f}s, fall_rate={rate:.3f}%/s{marker}, drop={drop:.3f}%")
            
            # Move to the next non-overlapping event
            i = overlapping[-1][0] + 1
        
        return resolved_events

    def detect_desaturation_ABOSA(self, data_starts, data_stats, fs_chan, channel, parameters_oxy):
        """
        Detect desaturation as described in ABOSA [1].

        Parameters :
            data_stats : list of numpy array
                oxygen saturation integer values from 1 to 100% (cleaned)
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
        data_dev_list = []
        all_desat_events = []
        plateau_lst = []
        lmin_indices_list = []
        lmax_indices_list = []        

        #---------------------
        # ABOSA parameters
        #---------------------♣
        # Avg fall rate limits to consider for desaturation events
        avg_fall_rate_lower_limit = -4.0  # % per second, the deepest
        # The least steep (-0.05 in the paper) -0.08 for better performance
        avg_fall_rate_upper_limit = -0.05  # % per second

        # peak detection parameters
        min_peak_distance_sec = 5 # ABOSA = 5 sec
        min_peak_prominence = 1 # ABOSA = 1; 0.5 for better performance
        # Filter order for lowpass (finding peaks) and highpass (fall rate) filtering
        order = 4 # ABOSA paper= 2; ABOSA email=4; 8 for better performance
        low_frequency_cutoff = 0.1 #same as the paper
        # To shift right the maximum to the point where the fall starts
        high_frequency_cutoff = 0.1 # Filter to enhance the variation for fall rate detection
        # Accepted slope to shift Lmax right (more negative is steeper and will reject the shift, the fall starts before)
        fall_rate_threshold = -0.05 # % 
        # Adjust Lmax and all Lmin candidates for plateau on the filtered signal
        min_plateau_duration_sec = 10 # ABOSA=30 sec paper, but ABOSA email=5 sec; 15 sec has better performance
        derivative_threshold = 0.08 # % per second; slope threshold to define a plateau. ABOSA not mentionned; 
        derivative_mean_threshold = 0.05 # % per second; mean slope threshold to define a plateau. ABOSA not mentionned; works well 0.1% < mean slope < 0.15%
        #plateau_std_threshold = 0.05 # ABOSA not mentionned; works well 0.1% < std < 0.15%
        # Minimum drop on filtered signal between adjusted Lmax and Lmin
        min_drop_on_filtered_signal = 1 # % Not in ABOSA; 1 work well until 1.5 %


        if DEBUG:
            print("\n--- Detect desaturation events ---")
            print(f"Minimum plateau duration: {min_plateau_duration_sec}s, threshold: {derivative_threshold}%")

        for i, signal in enumerate(data_stats):
            valid_mask = ~np.isnan(signal)
            if not np.any(valid_mask):
                continue

            # Low pass filter the signal to get the trend in order to detect local min and max
            signal_lpf = self.filter_nan_filtfilt(signal, order, fs_chan, low_frequency_cutoff, 'low')

            # High-pass filter the signal at 0.1 Hz (which is already low-pass filtered to 0.1 Hz)
            signal_hpf = self.filter_nan_filtfilt(signal_lpf, order, fs_chan, high_frequency_cutoff , 'high')

            # derivative signal for plateau detection
            signal_derivative = np.gradient(signal_lpf) * fs_chan

            # Step 1: Locate potential endpoints (Lmin)
            min_peak_distance_samples = int(min_peak_distance_sec * fs_chan)
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
                for lmin_idx, lmin_time, lmin_val, drop in lmin_list:

                    # Adjust Lmax for fall rate
                    # The Lmax is shifted forward to a point where the fall starts using the low pass filtered signal.
                    # The high pass filtered signal is used to verify abrupt transition
                    adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, signal_squared = \
                        self.adjust_lmax_for_fall_rate(signal_lpf, signal_hpf, lmax_idx, lmin_idx, \
                                                       data_starts[i], fs_chan, fall_rate_threshold)
                    
                    # Adjust Lmax and all Lmin candidates for derivative plateau
                    adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, \
                        adjusted_lmin_idx, adjusted_lmin_time, adjusted_lmin_val, plateau = \
                        self.adjust_for_derivative_plateau(
                            signal_lpf, signal_derivative, \
                            adjusted_lmax_idx, adjusted_lmax_val, 
                            lmin_idx, lmin_time, lmin_val,
                            data_starts[i], fs_chan, 
                            min_plateau_duration_sec, derivative_threshold, derivative_mean_threshold
                        )

                    if len(plateau) > 0:
                        plateau_lst.extend(plateau)

                    if adjusted_lmax_time >= adjusted_lmin_time:
                        if DEBUG:
                            print(f"Lmax at {adjusted_lmax_time:.2f}s is after Lmin at {adjusted_lmin_time:.2f}s after plateau adjustment")
                        break

                    # # Verify on the low pass filtered signal that a miminum drop is respected
                    # # It means that too few samples really drop between adjusted Lmax and Lmin
                    # # or too few samples are in the max peak before Lmin
                    # current_lmax_val = np.nanmax(signal_lpf[adjusted_lmax_idx:adjusted_lmin_idx+1])
                    # current_lmin_val = np.nanmin(signal_lpf[adjusted_lmax_idx:adjusted_lmin_idx+1])
                    # if (current_lmax_val - current_lmin_val) <= min_drop_on_filtered_signal: # 1.5 default
                    #     if DEBUG:
                    #         print(f"  Drop too small ({current_lmax_val - current_lmin_val:.1f}%) between adjusted Lmax at {adjusted_lmax_time:.2f}s and Lmin at {adjusted_lmin_time:.2f}s on low pass filtered signal")
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
                        (avg_fall_rate_lower_limit <= avg_fall_rate <= avg_fall_rate_upper_limit)):
                        # Valid desaturation event with the avg_fall_rate to filter overlapping later
                        all_desat_events.append((adjusted_lmax_time, duration, avg_fall_rate, drop))
                    else:
                        if DEBUG:
                            print(f"  Invalid desaturation: start={adjusted_lmax_time:.2f}s, "
                                  f"duration={duration:.2f}s, drop={drop:.1f}%, "
                                  f"fall_rate={avg_fall_rate:.3f}%/s")

            # Debug output for the result view
            if DEBUG: 
                data_lpf_list.append(signal_lpf)
                data_hpf_list.append(signal_squared)
                data_dev_list.append(signal_derivative)

        # Resolve overlapping desaturations by keeping events with steepest fall rate
        all_desat_events = self.resolve_overlapping_desaturations(all_desat_events)

        # Compute the area under the desaturation events for further analysis
        desat_areas = []
        for start_sec, duration_sec, slope, depth in all_desat_events:
            # Find which signal segment contains this event
            area = np.nan
            for samples, data_start in zip(data_stats, data_starts):
                signal_end = data_start + len(samples) / fs_chan
                # Check if the event is within this signal segment
                if start_sec >= data_start and start_sec < signal_end:
                    area = self.compute_desaturation_area(samples, data_start, start_sec, duration_sec, fs_chan)
                    break
            desat_areas.append(area)

        # Create output dataframe
        # desat_events = [('SpO2', 'desat_SpO2', start_sec, duration_sec, channel) 
        #                 for start_sec, duration_sec in all_desat_events]
        desat_events = [('SpO2', 'desat_SpO2', start_sec, duration_sec, '', slope, depth)
                        for start_sec, duration_sec, slope, depth in all_desat_events]

        # plateau_events = [('SpO2', 'plateau_SpO2', start_sec, duration_sec, channel) 
        #                   for start_sec, duration_sec in plateau_lst]
        plateau_events = [('SpO2', 'plateau_SpO2', start_sec, duration_sec, '') 
                          for start_sec, duration_sec in plateau_lst]
        if DEBUG:
            print(f"\n{len(desat_events)} desat events\n")
            print(f"\n{len(plateau_events)} plateau events\n")
            for i in range(len(data_stats)):
                print(f"{len(lmax_indices_list[i])} possible max\n")
                print(f"{len(lmin_indices_list[i])} possible min\n")

        desat_df = pd.DataFrame(data=desat_events, columns=['group', 'name', 'start_sec', 'duration_sec', 'channels', 'slope', 'depth'])
        # Add the desaturation features to compute stats
        desat_df['area_percent_sec'] = desat_areas
        plateau_df = manage_events.create_event_dataframe(data=plateau_events)
  
        return desat_df, plateau_df, data_lpf_list, data_hpf_list, data_dev_list, lmax_indices_list, lmin_indices_list


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


    def detect_artifact_SpO2(self, sraw, data_starts, fs_chan):
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
        
        data_cleaned = []
        for samples, data_start in zip(sraw, data_starts):
            # 1. Identify artifact points directly from raw signal first
            # This avoids filter edge effects
            artifact_mask = np.zeros(len(samples), dtype=bool)
            artifact_mask |= (samples < lower_bound)
            artifact_mask |= (samples > upper_bound)
            artifact_mask |= np.isnan(samples)
            
            # 2. Apply 4th order Butterworth high-pass filter (1 Hz cutoff) on valid samples only
            filtered_signal = self.filter_nan_filtfilt(samples, filter_order, fs_chan, cutoff_freq, 'high')
            
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
            extended_mask = np.zeros(len(samples), dtype=bool)
            
            for start, end in zip(starts, ends):
                # Apply symmetric buffer: 1s before start and 1s after the last artifact sample
                extended_start = max(0, start - extension_samples)
                extended_end = min(len(samples), end + extension_samples)
                extended_mask[extended_start:extended_end] = True
            
            # Re-identify artifact regions after extension
            diff = np.diff(np.concatenate([[0], extended_mask.astype(int), [0]]))
            starts = np.where(diff == 1)[0]
            ends = np.where(diff == -1)[0]
            
            # 6. Interpolate artifacts with duration ≤ 5 seconds
            cleaned_signal = samples.copy()
            threshold_samples = int(fs_chan * linear_art_sec)
            artifact_events = []
            
            for start, end in zip(starts, ends):
                # start is first artifact sample, end is first non-artifact sample
                duration = end - start
                
                if duration <= threshold_samples:
                    # Linear interpolation for short artifacts
                    if start > 0 and end < len(samples):
                        x = [start - 1, end]
                        y = [samples[start - 1], samples[end]]
                        interpolator = interp1d(x, y, kind='linear')
                        cleaned_signal[start:end] = interpolator(np.arange(start, end))
                    
                    # Mark as non-artifact after interpolation
                    extended_mask[start:end] = False
                else:
                    # Keep artifacts longer than 5s
                    start_sec = (start / fs_chan) + data_start
                    duration_sec = duration / fs_chan
                    artifact_events.append((start_sec, duration_sec))
                    # Mark these samples as NaN in cleaned signal
                    cleaned_signal[start:end] = np.nan

            data_cleaned.append(cleaned_signal)
        
        return data_cleaned, artifact_events


    def correct_peak_indices_in_window(self, signal, peak_indices, window_s, fs_chan, find_max=True):
        """
        Correct peak locations by finding actual extrema in the original signal within a time window.
        Vectorized implementation for better performance.
        
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
        peak_indices = np.asarray(peak_indices)
        if len(peak_indices) == 0:
            return np.array([], dtype=int)
        
        half_window_samples = int((window_s / 2) * fs_chan)
        signal_len = len(signal)
        
        # Vectorized window bounds calculation
        window_starts = np.maximum(0, peak_indices - half_window_samples)
        window_ends = np.minimum(signal_len, peak_indices + half_window_samples)
        
        corrected_indices = np.empty(len(peak_indices), dtype=int)
        valid_mask = np.ones(len(peak_indices), dtype=bool)
        
        for i, (ws, we) in enumerate(zip(window_starts, window_ends)):
            window_signal = signal[ws:we]
            if len(window_signal) > 0 and not np.all(np.isnan(window_signal)):
                if find_max:
                    corrected_indices[i] = ws + np.nanargmax(window_signal)
                else:
                    corrected_indices[i] = ws + np.nanargmin(window_signal)
            else:
                valid_mask[i] = False
        
        return corrected_indices[valid_mask]


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
        
        # Convert to numpy array for efficient operations (searchsorted, indexing)
        filtered_lmax_indices = np.array(filtered_lmax_indices, dtype=int)
        
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
            # Use searchsorted for O(log n) lookup instead of np.where O(n)
            current_pos = np.searchsorted(lmax_indices, lmax_idx)
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
        Shift Lmax forward to the next variation peak using the high-pass filtered signal 
        to identify the onset of the fall, accepting the shift only if the slope between 
        consecutive peaks is positive or not steeper than the negative fall-rate threshold.
        
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
                Fall rate threshold in %/s (deepest fall rate to accept a shift).
        
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

        # Square the high-pass filtered signal to enhance peaks (in both directions)
        signal_squared = signal_hpf ** 2
        
        # Detect peaks in the Squared signal - we are looking for the biggest drops
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
                
                duration_sec = (lmax_shifted - lmax_corrected) / fs_chan
                drop = signal[lmax_shifted] - signal[lmax_corrected]

                # Evaluate fall rate to ensure it's a valid shift
                fall_rate = drop / duration_sec if duration_sec > 0 else 0
                # For any positive fall rate or slow fall rate, we accept the shift
                if fall_rate >= fall_rate_threshold:
                    adjusted_lmax_idx = lmax_shifted
                # If fall rate is too steep, keep current position and stop
                else:
                    break
        
        adjusted_lmax_time = data_start + adjusted_lmax_idx / fs_chan
        adjusted_lmax_val = signal[adjusted_lmax_idx]
        return adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, signal_squared


    def adjust_for_plateau(self, signal, adjusted_lmax_idx, adjusted_lmax_val, lmin_idx, lmin_time, lmin_val, 
                           data_start, fs_chan, min_plateau_duration_sec=30, plateau_std_threshold=0.2):
        """
        Adjust Lmax or Lmin if a flat plateau exists within the event.
        The plateau length is dynamically determined (minimum 30s, can be longer).
        Iteratively detects plateaus until no more are found or the remaining duration is < 30s.
        
        Uses rolling standard deviation for O(n) complexity instead of O(n * window_size).
        
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
            plateau_std_threshold : float
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
            
            # Use rolling std for O(n) complexity instead of O(n * window_size)
            # Compute rolling mean and variance using cumulative sums
            n = len(event_signal)
            window = min_plateau_samples
            
            # Handle NaN values by replacing with interpolated values temporarily
            event_clean = event_signal.copy()
            nan_mask = np.isnan(event_clean)
            if np.any(nan_mask) and not np.all(nan_mask):
                # Linear interpolation for NaN values
                valid_indices = np.where(~nan_mask)[0]
                event_clean[nan_mask] = np.interp(
                    np.where(nan_mask)[0], valid_indices, event_clean[valid_indices]
                )
            elif np.all(nan_mask):
                break
            
            # Compute rolling std using cumulative sums (Welford's online algorithm approach)
            cumsum = np.cumsum(event_clean)
            cumsum_sq = np.cumsum(event_clean ** 2)
            
            # Rolling sum and sum of squares
            rolling_sum = cumsum[window-1:] - np.concatenate([[0], cumsum[:-window]])
            rolling_sum_sq = cumsum_sq[window-1:] - np.concatenate([[0], cumsum_sq[:-window]])
            
            # Rolling variance: E[X^2] - E[X]^2
            rolling_mean = rolling_sum / window
            rolling_var = rolling_sum_sq / window - rolling_mean ** 2
            rolling_var = np.maximum(rolling_var, 0)  # Numerical stability
            rolling_std = np.sqrt(rolling_var)
            
            # Find first position where std is below threshold
            flat_positions = np.where(rolling_std <= plateau_std_threshold)[0]
            
            if len(flat_positions) == 0:
                break
            
            best_plateau_start = flat_positions[0]
            best_plateau_end = best_plateau_start + window
            
            # Extend plateau as long as it remains flat
            # Use incremental std calculation for extension
            current_sum = rolling_sum[best_plateau_start]
            current_sum_sq = rolling_sum_sq[best_plateau_start]
            current_n = window
            
            while best_plateau_end < n:
                # Add new sample
                new_val = event_clean[best_plateau_end]
                current_sum += new_val
                current_sum_sq += new_val ** 2
                current_n += 1
                
                # Calculate new std
                mean = current_sum / current_n
                var = current_sum_sq / current_n - mean ** 2
                std = np.sqrt(max(var, 0))
                
                if std <= plateau_std_threshold:
                    best_plateau_end += 1
                else:
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
            
                # Make sure the current max on the low pass filtered signal is the maximum value until the Lmin candidate
                real_lmax_val = np.nanmax(signal[adjusted_lmax_idx:lmin_idx+1])
                if real_lmax_val > adjusted_lmax_val:
                    # Update adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val to the real maximum on the low pass filtered signal
                    adjusted_lmax_idx = np.nanargmax(signal[adjusted_lmax_idx:lmin_idx+1]) + adjusted_lmax_idx
                    adjusted_lmax_time = data_start + adjusted_lmax_idx / fs_chan
                    adjusted_lmax_val = signal[adjusted_lmax_idx]

        return adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, lmin_idx, lmin_time, lmin_val, plateau_list
    

    def adjust_for_derivative_plateau(self, signal, signal_derivative, adjusted_lmax_idx, adjusted_lmax_val, lmin_idx, lmin_time, lmin_val, 
                           data_start, fs_chan, min_plateau_duration_sec=10, derivative_threshold=0.1, 
                           derivative_mean_threshold=0.01):
        """
        Adjust Lmax or Lmin if a flat plateau exists within the event.
        Plateau detection is based on the derivative of the signal:
        - Each sample must have |derivative| < derivative_threshold (rejects steep spikes)
        - The mean derivative over the plateau must have |mean| < derivative_mean_threshold (rejects constant slopes)
        
        This allows detection of plateaus with small oscillations around a mean value,
        while rejecting both steep transitions and constant drifts.
        
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
                Minimum plateau duration in seconds (default 10s).
            derivative_threshold : float
                Maximum absolute derivative (%/sec) at each sample to be considered flat (default 0.01).
            derivative_mean_threshold : float
                Maximum absolute mean derivative (%/sec) over the plateau to reject constant slopes (default 0.01).
        
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
            derivative = signal_derivative[adjusted_lmax_idx:lmin_idx + 1]
    
            # Stop if remaining duration is less than minimum plateau duration
            if len(event_signal) < min_plateau_samples:
                break
            
            # # Handle NaN values by replacing with interpolated values temporarily
            # event_clean = event_signal.copy()
            # nan_mask = np.isnan(event_clean)
            # if np.any(nan_mask) and not np.all(nan_mask):
            #     # Linear interpolation for NaN values
            #     valid_indices = np.where(~nan_mask)[0]
            #     event_clean[nan_mask] = np.interp(
            #         np.where(nan_mask)[0], valid_indices, event_clean[valid_indices]
            #     )
            # elif np.all(nan_mask):
            #     break
            
            # # Compute derivative (slope) in %/sec using gradient
            # derivative = np.gradient(event_clean) * fs_chan  # %/sec
            
            # Step 1: Identify samples where individual derivative is below threshold
            # This rejects steep spikes (both positive and negative)
            flat_mask = np.abs(derivative) < derivative_threshold
            
            # Find contiguous flat regions based on individual derivative threshold
            diff = np.diff(np.concatenate([[0], flat_mask.astype(int), [0]]))
            starts = np.where(diff == 1)[0]
            ends = np.where(diff == -1)[0]
            
            # Step 2: For each candidate region, check if mean derivative is also low
            # This rejects constant slopes (e.g., steady decline)
            plateau_found = False
            best_plateau_start = 0
            best_plateau_end = 0
            for start, end in zip(starts, ends):
                if (end - start) >= min_plateau_samples:
                    # Compute mean derivative over this candidate region
                    mean_derivative = np.mean(derivative[start:end])
                    # Accept only if mean derivative is also low (rejects constant slopes)
                    if np.abs(mean_derivative) < derivative_mean_threshold:
                        best_plateau_start = start
                        best_plateau_end = end
                        plateau_found = True
                        break
            
            if not plateau_found:
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
            
                # Make sure the current max on the low pass filtered signal is the maximum value until the Lmin candidate
                if lmin_idx - adjusted_lmax_idx > 1:
                    real_lmax_val = np.nanmax(signal[adjusted_lmax_idx:lmin_idx+1])
                    if real_lmax_val > adjusted_lmax_val:
                        # Update adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val to the real maximum on the low pass filtered signal
                        adjusted_lmax_idx = np.nanargmax(signal[adjusted_lmax_idx:lmin_idx+1]) + adjusted_lmax_idx
                        adjusted_lmax_time = data_start + adjusted_lmax_idx / fs_chan
                        adjusted_lmax_val = signal[adjusted_lmax_idx]

        return adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, lmin_idx, lmin_time, lmin_val, plateau_list
    

    def compute_desat_stats(self, desat_df, total_stats, stage_sleep_period_df):
        desat_stats = {}
        # The number of oxygen desaturation in the sleep period.
        desat_stats['desat_count'] = len(desat_df)
        # The average duration in sec of the oxygen desaturation events in the sleep period.
        desat_stats['desat_avg_sec'] = desat_df['duration_sec'].mean()
        # The variance value of the duration in sec of the oxygen desaturation events in the sleep period.
        desat_stats['desat_var_sec'] = desat_df['duration_sec'].var()
        # The median value of the duration in sec of the oxygen desaturation events in the sleep period.
        desat_stats['desat_med_sec'] = desat_df['duration_sec'].median()
        # The percentage of time spent in desaturation during the sleep period.
        desat_stats['desat_SP_percent'] = desat_df['duration_sec'].sum()/(total_stats['total_valid_min']*60)*100
        # The Oxygen Desaturation Index (ODI) : number of desaturation per sleep hour.
        desat_stats['desat_ODI'] = len(desat_df)/((total_stats['total_valid_min'])/60)
        # The average area under the desaturation events in percent*sec.
        desat_stats['desat_area_avg'] = desat_df['area_percent_sec'].mean()
        # The average slope of the desaturation events in percent/sec.
        desat_stats['desat_slope_avg'] = desat_df['slope'].mean()
        # The average depth of the desaturation events in percent.
        desat_stats['desat_depth_avg'] = desat_df['depth'].mean()
        # Desaturation severity : The sum of areas under the desaturation events in percent*sec over the sleep period (sec).
        desat_stats['desat_severity'] = desat_df['area_percent_sec'].sum()/(total_stats['total_valid_min']*60)



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