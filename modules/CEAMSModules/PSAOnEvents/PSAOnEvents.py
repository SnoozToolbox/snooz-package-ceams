"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    PSAOnEvents
    Compile the PSA run on selected events.  The compilation is for a cohort.
"""

import numpy as np
import os
import pandas as pd

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

from CEAMSModules.EventReader import manage_events
from CEAMSModules.PSACompilation import commons as PSA
from CEAMSModules.PSAOnEvents.PSAOnEventsDoc import write_doc_file, _get_doc
from CEAMSModules.SleepReport import SleepReport

DEBUG = False

class PSAOnEvents(SciNode):
    """
    Compile the PSA run on selected events.  The compilation is for a cohort.

    Inputs:

        "subject_info": dict
            filename : Recording filename without path and extension.
            id1 : Identification 1
            id2 : Identification 2
            first_name : first name of the subject recorded
            last_name : last name of the subject recorded
            ...
        "PSD":  list of dicts
            psd : power (µV^2)
            freq_bins : frequency bins (Hz)
            win_len : windows length (s)
            win_step : windows step (s)
            sample_rate : sampling rate of the original signal (Hz)
            chan_label : channel label
        "events": Pandas Dataframe ['group','name','start_sec','duration_sec','channels']
            List of events.
        "PSA_event_group": String of dict
            A key for each filname and the value is the events group, each group is separated by a comma.
            Event group label to run the PSA on, each group is separated by a comma. 
        "PSA_event_name": String of dict
            A key for each filname and the value is the events name, each name is separated by a comma.
            Event name label to run the PSA on, each name is separated by a comma.
        "mini_bandwidth" : float
            The bandwidth of eah mini band division (Hz)
        "first_freq" : float
            The minimum (first) frequency analyzed.
        "last_freq" : float
            The maximum (last) frequency analysed.
            ! Warning : the last frequency is limited to fs/2
        "dist_total" : bool
            True to write the total spectral activity.
        "dist_hour" : bool
            True to write the spectral activity per clock hour.
        "dist_cycle" : bool
            True to write the spectral activity per sleep cycle.
        "parameters_cycle" : String (dict converted into a string)
            Sleep cycle definition parameters.
        "artifact_group": String
            Event group to ignore, each group is separated by a comma. 
        "artefact_name": String
            Event name to ignore, each name is separated by a comma.
        "cycle_labelled" : pandas DataFrame
            List of NREM and REM periods
            (columns=['group','name','start_sec','duration_sec','channels']).
        "report_constants": dict
            Constants used in the report (N_HOURS, N_CYCLES).
        "PSA_out_filename": string
            Path and filename to write the output.
        "match_event_channels": bool
            If True, compile each event only on its annotated channel. If
            False, use the event intervals for every analyzed PSD channel.

    Outputs: None, a file is saved.
        
    """
    def __init__(self, **kwargs):
        """ Initialize module PSAOnEvents """
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')

        # Input plugs
        InputPlug('subject_info',self)
        InputPlug('PSD',self)
        InputPlug('events',self)
        InputPlug('PSA_event_group',self)
        InputPlug('PSA_event_name',self)
        InputPlug('mini_bandwidth',self)
        InputPlug('first_freq',self)
        InputPlug('last_freq',self)
        InputPlug('dist_total',self)
        InputPlug('dist_hour',self)
        InputPlug('dist_cycle',self)
        InputPlug('parameters_cycle',self)
        InputPlug('artifact_group',self)
        InputPlug('artifact_name',self)
        InputPlug('cycle_labelled',self)
        InputPlug('report_constants',self)
        InputPlug('PSA_out_filename',self)
        InputPlug('match_event_channels',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 

        # Dict to accumulate the act per event, hour and cycle.
        self.PSD_act_param = {}
        self.PSD_avg_per_event ={}
        self.N_HOURS = 0
        self.N_CYCLES = 0
    
    def compute(self, subject_info,PSD,events,PSA_event_group,PSA_event_name,mini_bandwidth,\
        first_freq,last_freq,dist_total,dist_hour,dist_cycle,parameters_cycle,artifact_group,\
        artifact_name,cycle_labelled,report_constants,PSA_out_filename,match_event_channels=True):
        """
        Compile the PSA run on selected events.  The compilation is for a cohort.

        Inputs:
            "subject_info": dict           
                filename : Recording filename without path and extension.
                id1 : Identification 1
                id2 : Identification 2
                first_name : first name of the subject recorded
                last_name : last name of the subject recorded
                ...
            "PSD":  list of dicts
                psd : power (µV^2)
                freq_bins : frequency bins (Hz)
                win_len : windows length (s)
                win_step : windows step (s)
                sample_rate : sampling rate of the original signal (Hz)
                chan_label : channel label
            "events": Pandas Dataframe ['group','name','start_sec','duration_sec','channels']
                List of events.
            "PSA_event_group": String of dict
                A key for each filname and the value is the events group, each group is separated by a comma.
                Event group label to run the PSA on, each group is separated by a comma. 
            "PSA_event_name": String of dict
                A key for each filname and the value is the events name, each name is separated by a comma.
                Event name label to run the PSA on, each name is separated by a comma.
            "mini_bandwidth" : float
                The bandwidth of eah mini band division (Hz)
            "first_freq" : float
                The minimum (first) frequency analyzed.
            "last_freq" : float
                The maximum (last) frequency analysed.
                ! Warning : the last frequency is limited to fs/2
            "dist_total" : bool
                True to write the total spectral activity.
            "dist_hour" : bool
                True to write the spectral activity per clock hour.
            "dist_cycle" : bool
                True to write the spectral activity per sleep cycle.
            "parameters_cycle" : String (dict converted into a string)
                Sleep cycle definition parameters.
            "artifact_group": String
                Event group to ignore, each group is separated by a comma. 
            "artefact_name": String
                Event name to ignore, each name is separated by a comma.
            "cycle_labelled" : pandas DataFrame
                List of NREM and REM periods
                (columns=['group','name','start_sec','duration_sec','channels']).
            "report_constants": dict
                Constants used in the report (N_HOURS, N_CYCLES).
            "PSA_out_filename": string
                Path and filename to write the output.
            "match_event_channels": bool
                If True, compile each event only on its annotated channel. If
                False, use the event intervals for every analyzed PSD channel.

        Outputs: None, a file is saved.
            
        """
        # Input Type verification
        if isinstance(subject_info, str) and subject_info != '':
            subject_info = eval(subject_info)
        if (not isinstance(subject_info,dict)):
            raise NodeInputException(self.identifier, "subject_info", \
                f"PSAOnEvents input of wrong type. Expected: <dict> received: {type(subject_info)}") 

        if not isinstance(PSD,list):
            raise NodeInputException(self.identifier, "PSD", \
                f"PSAOnEvents input of wrong type. Expected: <class 'list'> received: {type(PSD)}")   
        if match_event_channels in ("", None):
            match_event_channels = True
        elif isinstance(match_event_channels, str):
            if match_event_channels.lower() == "true":
                match_event_channels = True
            elif match_event_channels.lower() == "false":
                match_event_channels = False
        if type(match_event_channels) != bool:
            raise NodeInputException(
                self.identifier,
                "match_event_channels",
                "PSAOnEvents match_event_channels parameter must be a boolean"
            )
        try:
            mini_bandwidth = float(mini_bandwidth)
        except ValueError:
            raise NodeInputException(self.identifier, "mini_bandwidth", \
                f"PSAOnEvents input of wrong type or empty. Expected: str of float") 
        try:
            first_freq = float(first_freq)
        except ValueError:
            raise NodeInputException(self.identifier, "first_freq", \
                f"PSAOnEvents input of wrong type or empty. Expected: str of float") 
        try:
            last_freq = float(last_freq)
        except ValueError:
            raise NodeInputException(self.identifier, "last_freq", \
                f"PSAOnEvents input of wrong type or empty. Expected: str of float") 

        dist_total = self._parse_bool_flag(dist_total, "dist_total", default=True)
        dist_hour = self._parse_bool_flag(dist_hour, "dist_hour", default=False)
        dist_cycle = self._parse_bool_flag(dist_cycle, "dist_cycle", default=False)

        if isinstance(parameters_cycle, str):
            if parameters_cycle == '':
                parameters_cycle = {}
            else:
                try:
                    parameters_cycle = eval(parameters_cycle)
                except Exception:
                    raise NodeInputException(self.identifier, "parameters_cycle", \
                        f"PSAOnEvents input of wrong type. Expected: <class 'dict'> received: {type(parameters_cycle)}")
        if type(parameters_cycle) != dict:
            raise NodeInputException(self.identifier, "parameters_cycle", \
                f"PSAOnEvents input of wrong type. Expected: <class 'dict'> received: {type(parameters_cycle)}")

        if isinstance(cycle_labelled, str) and cycle_labelled == '':
            cycle_labelled = pd.DataFrame(
                columns=['group', 'name', 'start_sec', 'duration_sec', 'channels']
            )
        if (dist_hour or dist_cycle) and \
            ((not isinstance(cycle_labelled, pd.DataFrame)) or len(cycle_labelled)==0):
            raise NodeInputException(self.identifier, "cycle_labelled", \
                f"PSAOnEvents input of wrong type or empty. Expected: <class 'pd.DataFrame'> received: {type(cycle_labelled)}")
        elif not isinstance(cycle_labelled, pd.DataFrame):
            raise NodeInputException(self.identifier, "cycle_labelled", \
                f"PSAOnEvents input of wrong type. Expected: <class 'pd.DataFrame'> received: {type(cycle_labelled)}")

        if isinstance(report_constants, str) and report_constants == '':
            report_constants = {'N_HOURS': 0, 'N_CYCLES': 0}
        elif isinstance(report_constants, str):
            try:
                report_constants = eval(report_constants)
            except Exception:
                raise NodeInputException(self.identifier, "report_constants", \
                    "PSAOnEvents report_constants parameter must be set.")
        if isinstance(report_constants, dict) == False:
            raise NodeInputException(self.identifier, "report_constants",\
                "PSAOnEvents report_constants expected type is dict and received type is " + str(type(report_constants)))
        self.N_HOURS = int(float(report_constants.get('N_HOURS', 0)))
        self.N_CYCLES = int(float(report_constants.get('N_CYCLES', 0)))

        if not (dist_total or dist_hour or dist_cycle):
            raise NodeInputException(self.identifier, "dist_total", \
                "PSAOnEvents requires at least one of dist_total, dist_hour or dist_cycle to be enabled.")

        if isinstance(PSA_event_group, str):
            if PSA_event_group=='':
                raise NodeInputException(self.identifier, "PSA_event_group", \
                    f"PSAOnEvents not connected are empty") 
            else:
                try:
                    PSA_event_group = eval(PSA_event_group)
                except ValueError:
                    raise NodeInputException(self.identifier, "PSA_event_group", \
                        f"PSAOnEvents input of wrong type. Expected: str of dict")        

        if isinstance(PSA_event_name, str):
            if PSA_event_name=='':
                raise NodeInputException(self.identifier, "PSA_event_name", \
                    f"PSAOnEvents not connected are empty") 
            else:
                try:
                    PSA_event_name = eval(PSA_event_name)
                except ValueError:
                    raise NodeInputException(self.identifier, "PSA_event_name", \
                        f"PSAOnEvents input of wrong type. Expected: str of dict")                 

        # Extract subject info
        subject_info_params = {"filename": subject_info['filename']}
        if (subject_info['id1'] is not None) and len(subject_info['id1'].strip())>0:
            subject_info_params['id1'] = subject_info['id1']
        elif (subject_info['id2'] is not None) and len(subject_info['id2'].strip())>0:
            subject_info_params['id1'] = subject_info['id2']
        else:
            subject_info_params['id1'] = subject_info['id1']

        cycle_info_param = {}
        if parameters_cycle and (dist_hour or dist_cycle):
            cycle_info_param = SleepReport.get_sleep_cycle_parameters(self, parameters_cycle)

        # Manage the artefacts, clean list of channels and select the artefact from events
        artifact_info_param, artifact_selected = \
            self.get_event_info(artifact_group, artifact_name, events.copy(), 'artifact')

        # Manage the events on which the PSA is run, clean list of channels and select the PSA events
        # Find wich key in PSA_event_group_sel contains the subject_info['filename']
        file_found = False
        for key in PSA_event_group.keys():
            if (subject_info['filename'] in key) and (not file_found):
                PSA_event_group_sel = PSA_event_group[key]
                PSA_event_name_sel = PSA_event_name[key]
                file_found=True
        if not file_found:
            raise NodeRuntimeException(self.identifier, PSA_event_group, \
                f"PSAOnEvents - The filename {subject_info['filename']} was not found in the PSA_event_group.")
                
        PSA_evt_info_param, PSA_evt_selected = \
            self.get_event_info(PSA_event_group_sel, PSA_event_name_sel, events.copy(), 'PSA_event')

        # Extract duration_sec
        event_dur_s = PSA_evt_selected['duration_sec'].values
        if any(event_dur_s < PSD[0]['win_len']):
            # Log message for the Logs tab
            if all(event_dur_s < PSD[0]['win_len']):
                self._log_manager.log(self.identifier, \
                    f"All the PSA events in the file {subject_info['filename']} are shorter than the fft window length of {PSD[0]['win_len']}s.")        
                raise NodeRuntimeException(self.identifier, PSA_event_group, \
                    f"PSAOnEvents - All the PSA events in the group {PSA_event_group_sel} and name {PSA_event_name_sel} "\
                        +f"are shoter than the fft window length of {PSD[0]['win_len']}s.")   
            else:
                self._log_manager.log(self.identifier, \
                    f"The file {subject_info['filename']} has PSA events shorter than the fft window length of {PSD[0]['win_len']}s.")
            

        # Extract the unique channel list
        channels_list = np.unique(PSA.get_attribute(PSD, 'chan_label'))

        # Create the list of events from all the files to create a valid file (the number of columns has to be known for the cohort)
        unique_event_name = []
        for val_names in PSA_event_name.values():
            name_list = val_names.split(',')
            unique_event_name.append(name_list)
        # Flat the list
        unique_event_name = [item for sublist in unique_event_name for item in sublist]
        # Make it unique and stable for cohort column order
        unique_event_name = sorted(set(unique_event_name))

        # The channels are grouped in the PSA cohort file
        report_df = []
        for channel in channels_list:
            # Reset accumulation for the current channel
            self.PSD_act_param = {}
            self.PSD_avg_per_event = {}

            # Extract the sampling rate of the current channel
            channel_info_param, fs_chan = PSA.get_channel_info(PSD, channel)

            # Compute the number of artefacts for the current channel and selected sleep stage
            channel_info_param['channel_artefact_count'] = \
                self.get_n_artefact_sel(
                    artifact_selected,
                    channel,
                    PSA_evt_selected,
                    match_event_channels
                )

            # Extract the fft length and step
            PSD_info_params = PSA.get_PSD_info(self.identifier, PSD, channel)

            # Extract the PSD property for the current channel
            #   freq_bin_chan is an [1 x n_freq_bins] (because it is unique across the recording)
            #   psd_start_time is an [1 x sleep_stages] (a start time for each epoch processed)
            #   psd_end_time is an [1 x sleep_stages] (a start time for each epoch processed)
            freq_bin_chan, psd_start_time, psd_end_time = PSA.get_PSD_attribute_chan(self.identifier, PSD, channel)
            psd_start_time = np.asarray(psd_start_time, dtype=float)

            # Extract PSA Events for the current channel if any
            PSA_evt_channel = self.select_events_for_channel(
                PSA_evt_selected,
                channel,
                match_event_channels
            ).reset_index(drop=True)

            labels_computed = []

            # --------------------------------------------------------------------------
            # Total / hour / cycle compilation
            # --------------------------------------------------------------------------
            if dist_total:
                self.compute_fft_win_event(
                    unique_event_name, PSD, PSA_evt_channel, psd_start_time, channel, 'total'
                )
                labels_computed.append('total')

            if dist_hour:
                for cur_div in range(self.N_HOURS):
                    label = f'clock_h{cur_div+1}'
                    if len(cycle_labelled) > 0 and isinstance(cycle_labelled.iloc[0]['start_sec'], float):
                        start_hour = cycle_labelled.iloc[0]['start_sec'] + cur_div * 3600
                        end_hour = start_hour + 3600
                        evt_div, psd_starts_div = self._filter_events_by_time(
                            PSA_evt_channel, psd_start_time, start_hour, end_hour
                        )
                    else:
                        evt_div = PSA_evt_channel.iloc[0:0].copy()
                        psd_starts_div = np.array([])
                    self.compute_fft_win_event(
                        unique_event_name, PSD, evt_div, psd_starts_div, channel, label
                    )
                    labels_computed.append(label)

            if dist_cycle:
                for cur_div in range(self.N_CYCLES):
                    label = f'cyc{cur_div+1}'
                    if len(cycle_labelled) > 0 and isinstance(cycle_labelled.iloc[0]['start_sec'], float):
                        if (cur_div * 2) < len(cycle_labelled):
                            start_cycle = cycle_labelled.iloc[cur_div * 2]['start_sec']
                        else:
                            start_cycle = (
                                cycle_labelled.iloc[-1]['start_sec']
                                + cycle_labelled.iloc[-1]['duration_sec']
                            )
                        if (cur_div * 2 + 1) < len(cycle_labelled):
                            end_cycle = (
                                cycle_labelled.iloc[cur_div * 2 + 1]['start_sec']
                                + cycle_labelled.iloc[cur_div * 2 + 1]['duration_sec']
                            )
                        else:
                            end_cycle = (
                                cycle_labelled.iloc[-1]['start_sec']
                                + cycle_labelled.iloc[-1]['duration_sec']
                            )
                        self.PSD_act_param[f'{label}_length_min'] = (end_cycle - start_cycle) / 60
                        evt_div, psd_starts_div = self._filter_events_by_time(
                            PSA_evt_channel, psd_start_time, start_cycle, end_cycle
                        )
                    else:
                        self.PSD_act_param[f'{label}_length_min'] = np.NaN
                        evt_div = PSA_evt_channel.iloc[0:0].copy()
                        psd_starts_div = np.array([])
                    self.compute_fft_win_event(
                        unique_event_name, PSD, evt_div, psd_starts_div, channel, label
                    )
                    labels_computed.append(label)
                
            # --------------------------------------------------------------------------
            # Average activity for each mini band
            # --------------------------------------------------------------------------
            # Define the spectral band
            # Compute the freq bins indexes to average for each mini band
            # the upper limit is included as [min, max[

            # To avoid too many decimal in the frequency bins
            freq_bin_space = np.average(np.diff(freq_bin_chan))
            # This works only for frequency bins < 1
            if freq_bin_space<1:
                precision_space = int(abs(np.log10(freq_bin_space)))+2
                freq_bin_chan = np.round(freq_bin_chan,precision_space)
            else:
                precision_space = 1
                freq_bin_chan = np.round(freq_bin_chan,precision_space)

            # Compute the freq bins indexes for each mini band
            miniband_indices = PSA.get_miniband_index(self.identifier, freq_bin_chan, mini_bandwidth, first_freq, last_freq, fs_chan)
            # For each mini band use the n_fft_win and n_fft_win_valid computed above (fixed accross all mini bands)
            for miniband_index in miniband_indices:

                # The frequency band defined as [min, max[ (i.e. 0-3.8 Hz) are written in the report as 0-4 Hz
                self.PSD_act_param['freq_low_Hz'] = freq_bin_chan[miniband_index[0]]
                self.PSD_act_param['freq_high_Hz'] = freq_bin_chan[miniband_index[1]+1]

                for label in labels_computed:
                    # Gate on valid windows: all-artefacted windows yield nanmean=NaN,
                    # and np.nansum(NaN)=0.0 which would falsely look like zero power.
                    _, tot_valid_key, act_key = self._stat_keys(label)
                    if self.PSD_act_param.get(tot_valid_key, 0) > 0:
                        self.PSD_act_param[act_key] = np.nansum(
                            self.PSD_avg_per_event[act_key][miniband_index[0]:miniband_index[1]+1]
                        )
                    else:
                        self.PSD_act_param[act_key] = np.NaN

                    for cur_event_name in unique_event_name:
                        _, evt_valid_key, evt_act_key = self._stat_keys(label, cur_event_name)
                        if self.PSD_act_param.get(evt_valid_key, 0) > 0:
                            self.PSD_act_param[evt_act_key] = np.nansum(
                                self.PSD_avg_per_event[evt_act_key][miniband_index[0]:miniband_index[1]+1]
                            )
                        else:
                            self.PSD_act_param[evt_act_key] = np.NaN

                # --------------------------------------------------------------------------
                # Organize data to Write the file
                # --------------------------------------------------------------------------
                # Construction of the pandas dataframe that will be used to create the CSV file
                # There is a new line for each channel and mini band
                output = (
                    subject_info_params
                    | cycle_info_param
                    | artifact_info_param
                    | channel_info_param
                    | PSD_info_params
                    | self.PSD_act_param
                )
                cur_row_report_df = pd.DataFrame.from_records([output])
                if len(report_df):
                    report_df = pd.concat([report_df, cur_row_report_df])
                else:
                    report_df = cur_row_report_df

        # Order columns as the doc file (same approach as PSACompilation)
        n_hours_doc = self.N_HOURS if dist_hour else 0
        n_cycles_doc = self.N_CYCLES if dist_cycle else 0
        out_columns = list(_get_doc(
            n_hours_doc,
            n_cycles_doc,
            unique_event_name,
            include_total=dist_total
        ).keys())
        # Keep only columns that exist, then append any unexpected extras at the end
        ordered_columns = [col for col in out_columns if col in report_df.columns]
        extra_columns = [col for col in report_df.columns if col not in ordered_columns]
        report_df = report_df[ordered_columns + extra_columns]

        # Write the current report for the current subject into the tsv file
        write_header = not os.path.exists(PSA_out_filename)
        try : 
            report_df.to_csv(path_or_buf=PSA_out_filename, sep='\t', \
                index=False, mode='a', header=write_header, encoding="utf_8")
        except : 
            error_message = f"Snooz can not write in the file {PSA_out_filename}."+\
                f" Check if the drive is accessible and ensure the file is not already open."
            raise NodeRuntimeException(self.identifier, "PSAOnEvents", error_message)           

        # To write the info text file to describe the variable names
        if write_header:
            # Write the documentation file
            file_name, file_extension = os.path.splitext(PSA_out_filename)
            doc_filepath = file_name+"_info"+file_extension
            if not os.path.exists(doc_filepath):
                write_doc_file(
                    doc_filepath,
                    n_hours_doc,
                    n_cycles_doc,
                    unique_event_name,
                    include_total=dist_total
                )
                # Log message for the Logs tab
                self._log_manager.log(self.identifier, f"The file {doc_filepath} has been created.")

        return {
        }      


    # To select the artefact events according to artefact groups and names.
    # Generate the artefact info dict to write. 
    def get_event_info(self, event_group, event_name, events, print_label):
        # Select the group and name
        art_selected = manage_events.create_event_dataframe(None)
        if isinstance(event_group,str) and len(event_group)>0:
            art_group_lst = event_group.split(',')
        else:
            art_group_lst = []
        if isinstance(event_name,str) and len(event_name)>0:
            art_name_lst = event_name.split(',')
        else:
            art_name_lst = []
        if len(art_group_lst)==len(art_name_lst):
            for i, group_cur in enumerate(art_group_lst):
                cur_selection = events[(events['group']==group_cur) & (events['name']==art_name_lst[i])]
                art_selected = pd.concat([art_selected,cur_selection])
        elif len(art_group_lst)>0 and len(art_name_lst)==0:
            for group_cur in art_group_lst:
                group_selected = events[(events['group']==group_cur)]
                art_selected = pd.concat([art_selected,group_selected])
        elif len(art_name_lst)>0 and len(art_group_lst)==0:
            for name_cur in art_name_lst:
                name_selected = events[(events['name']==name_cur)]
                art_selected = pd.concat([art_selected,name_selected])
        else:
            raise NodeInputException(self.identifier, print_label, \
                f"PSACompilation input of wrong size. If both group and name are defined they need to be the same length, group length:\
                     {len(art_group_lst)} and name length: {len(art_name_lst)}") 
        artefact_info_param = {}
        artefact_info_param[print_label+'_group_name_list']=''
        for i_art, group in enumerate(art_group_lst):
            temp = '('+str(i_art)+')'+"group:"+group+" name:"+art_name_lst[i_art]+' '
            artefact_info_param[print_label+'_group_name_list']=artefact_info_param[print_label+'_group_name_list']+temp

        # Reset index
        art_selected.reset_index(inplace=True, drop=True)
        # Sort events based on the start_sec
        art_selected.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')   

        return artefact_info_param, art_selected


    # Compute the number of artefact for the current channel and selected events
    def _parse_bool_flag(self, value, plug_name, default=False):
        if value in ("", None):
            return default
        if isinstance(value, bool):
            return value
        if isinstance(value, (int, float)):
            return bool(int(value))
        if isinstance(value, str):
            lowered = value.strip().lower()
            if lowered in ("true", "1"):
                return True
            if lowered in ("false", "0"):
                return False
            try:
                return bool(int(float(lowered)))
            except ValueError:
                pass
        raise NodeInputException(
            self.identifier,
            plug_name,
            f"PSAOnEvents {plug_name} parameter must be a boolean"
        )


    def select_events_for_channel(self, events, channel, match_event_channels):
        if not match_event_channels:
            return events
        return events[
            (events['channels'] == channel) |
            (events['channels'] == "")
        ]


    def _stat_keys(self, label, event_name=None):
        """
        Return (fft_win_count_key, fft_win_valid_count_key, act_key).

        Total keeps the historical annotation-report column names.
        Hour/cycle use PSACompilation-like prefixes.
        """
        if label == 'total':
            if event_name is None:
                return 'fft_win_count', 'fft_win_valid_count', 'act_total'
            return (
                f'fft_win_{event_name}_count',
                f'fft_win_valid_{event_name}_count',
                f'act_{event_name}'
            )
        if event_name is None:
            return (
                f'{label}_fft_win_count',
                f'{label}_fft_win_valid_count',
                f'{label}_act'
            )
        return (
            f'{label}_{event_name}_fft_win_count',
            f'{label}_{event_name}_fft_win_valid_count',
            f'{label}_{event_name}_act'
        )


    def _filter_events_by_time(self, events, psd_start_time, start_sec, end_sec):
        """
        Keep events whose start falls in [start_sec, end_sec).

        When events and psd_start_time are 1:1 aligned, filter both with the
        same mask so FFT matching stays consistent.
        """
        if events is None or len(events) == 0:
            empty = events.iloc[0:0].copy() if isinstance(events, pd.DataFrame) else \
                pd.DataFrame(columns=['group', 'name', 'start_sec', 'duration_sec', 'channels'])
            return empty, np.array([])

        evt_starts = events['start_sec'].to_numpy(dtype=float)
        time_mask = (evt_starts >= start_sec) & (evt_starts < end_sec)
        evt_div = events.loc[time_mask].reset_index(drop=True)

        psd_start_time = np.asarray(psd_start_time, dtype=float)
        if len(psd_start_time) == len(events):
            psd_starts_div = psd_start_time[time_mask]
        else:
            psd_starts_div = evt_div['start_sec'].to_numpy(dtype=float)
        return evt_div, psd_starts_div


    def get_n_artefact_sel(self, art_selected, channel, PSA_evt_selected, match_event_channels):
        # Extract PSA Events for the current channel if any
        PSA_evt_channel = self.select_events_for_channel(
            PSA_evt_selected,
            channel,
            match_event_channels
        )
        # Extract PSA Events info
        PSA_evt_start_all = PSA_evt_channel['start_sec'].to_numpy()
        PSA_evt_start_all = np.around(PSA_evt_start_all)
        PSA_evt_end_all = PSA_evt_start_all+PSA_evt_channel['duration_sec'].to_numpy()
        PSA_evt_end_all = np.around(PSA_evt_end_all)
        # Extract artefact for the current channel
        art_channel_arr = art_selected['channels'].to_numpy()
        art_start_arr = art_selected['start_sec'].to_numpy()
        art_start_arr = np.around(art_start_arr)
        art_dur_arr = art_selected['duration_sec'].to_numpy()
        art_dur_arr = np.around(art_dur_arr)
        n_arts = 0
        for start, dur, chan in zip(art_start_arr, art_dur_arr, art_channel_arr):
            if channel == chan:
                if any( (PSA_evt_start_all<=(start+dur)) & (PSA_evt_end_all>=start) ):
                    n_arts += 1
        # Compute the number of artefacts for the selected sleep stages
        return n_arts


    # --------------------------------------------------------------------------
    # Compute the total and the valid number of fft windows and
    # average the activity across windows through the recording
    # for each selected annotation event.
    # --------------------------------------------------------------------------
    # Parameters :
    #   event_name_unique : list of string
    #       List pf event label to compute the PSA on
    #   PSD : list of dict for the current channel
    #       psds of signals
    #   PSA_evt_selected : pandas DataFrame
    #       events to run the PSA on
    #   psd_start_time : array
    #       Start time value in seconds of the PSD
    #   label_stat_div : str
    #       Prefix for the stats (total, clock_h1, cyc1, ...)
    # Compute :
        # self.PSD_act_param : dict
            #     fft_win_count : total number of fft windows
            #     fft_win_valid_count : total number of valid fft windows
            #     for each PSA event
            #         i.e. n_fft_win_MEVE, n_fft_win_valid_MOR, ...
        # self.PSD_avg_per_event : dict
        #   psd data average through the recording for each event
        #     act : narray [1 x n_freq_bins]
        #     for each event
        #         i.e. act_MEVE, total_act_MOR ...
    def compute_fft_win_event(self, event_name_unique, PSD, PSA_evt_selected, psd_start_time, channel, label_stat_div='total'):
        psd_data_tot = np.empty([0,0])
        psd_start_time = np.asarray(psd_start_time, dtype=float)
        tot_fft_key, tot_valid_key, tot_act_key = self._stat_keys(label_stat_div)

        # Loop for each different event name (i.e. M-EVE, MOR, clean_bsl, ...)
        if PSA_evt_selected is None or len(PSA_evt_selected) == 0:
            for cur_event_name in event_name_unique:
                evt_fft_key, evt_valid_key, evt_act_key = self._stat_keys(label_stat_div, cur_event_name)
                self.PSD_act_param[evt_fft_key] = 0
                self.PSD_act_param[evt_valid_key] = 0
                self.PSD_avg_per_event[evt_act_key] = np.NaN
            self.PSD_act_param[tot_fft_key] = 0
            self.PSD_act_param[tot_valid_key] = 0
            self.PSD_avg_per_event[tot_act_key] = np.NaN
            return

        for cur_event_name in event_name_unique:
            evt_fft_key, evt_valid_key, evt_act_key = self._stat_keys(label_stat_div, cur_event_name)

            # Compute the number of fft win total and valid
            psd_data_cur_event = np.empty([0,0])
            # Channel filtering is already applied by the caller via
            # select_events_for_channel(match_event_channels=...).
            # Keep only the current event name here.
            name_mask = (PSA_evt_selected['name'] == cur_event_name).to_numpy()
            if len(name_mask) == len(psd_start_time):
                psd_starts_cur = psd_start_time[name_mask]
            else:
                psd_starts_cur = PSA_evt_selected.loc[
                    PSA_evt_selected['name'] == cur_event_name, 'start_sec'
                ].to_numpy(dtype=float)

            # For each event of the group
            for psd_start_cur in psd_starts_cur:
                # Extract the psd data for the current channel and start_time
                matched = [item_list.get('psd') for item_list in PSD \
                    if (item_list.get('chan_label')==channel) and (item_list.get('start_time')==psd_start_cur)]
                if len(matched) == 0:
                    continue
                psd_data_cur_start = np.vstack(matched)
                # Accumulate the psd data for all the start of the current event name
                if psd_data_cur_event.size>0:
                    psd_data_cur_event = np.vstack((psd_data_cur_event,psd_data_cur_start))
                else:
                    psd_data_cur_event = psd_data_cur_start

            if len(psd_data_cur_event)>0:
                # Compute the number of valid fft windows (find out if there is a nan for each window) for each event group
                n_nan_fft_win = np.sum(np.isnan(np.sum(psd_data_cur_event, axis=1)))
                event_n_fft_win = len(psd_data_cur_event)
                event_n_fft_win_valid = event_n_fft_win-n_nan_fft_win
                self.PSD_act_param[evt_fft_key] = event_n_fft_win
                self.PSD_act_param[evt_valid_key] = event_n_fft_win_valid
                # Average the activity through the recording (keeping all the frequency bins)
                self.PSD_avg_per_event[evt_act_key]= np.nanmean(psd_data_cur_event,axis=0)

                # Accumulate act and n fft for the total
                if psd_data_tot.size:
                    psd_data_tot = np.vstack((psd_data_tot,psd_data_cur_event))
                else:
                    psd_data_tot = psd_data_cur_event
            else:
                self.PSD_act_param[evt_fft_key] = 0
                self.PSD_act_param[evt_valid_key] = 0
                self.PSD_avg_per_event[evt_act_key]= np.NaN
        if psd_data_tot.size>0:
            # Compute the total number of valid fft windows (find out if there is a nan for each window)
            n_nan_fft_win = np.sum(np.isnan(np.sum(psd_data_tot, axis=1)))
            tot_n_fft_win = len(psd_data_tot)
            tot_n_fft_win_valid = tot_n_fft_win-n_nan_fft_win
            self.PSD_act_param[tot_fft_key] = tot_n_fft_win
            self.PSD_act_param[tot_valid_key] = tot_n_fft_win_valid
            # Average the activity through the recording (keeping all the frequency bins)
            self.PSD_avg_per_event[tot_act_key]= np.nanmean(psd_data_tot,axis=0)
        else:
            self.PSD_act_param[tot_fft_key] = 0
            self.PSD_act_param[tot_valid_key] = 0
            self.PSD_avg_per_event[tot_act_key]= np.NaN

