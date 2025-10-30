"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    PSAPicsGenerator
    Class to generate pictures of PSA (Power Spectral Analysis) data from PSA report files.
"""
import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Qtagg')  # Use non-GUI backend
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = True

class PSAPicsGenerator(SciNode):
    """
    Class to generate pictures of PSA (Power Spectral Analysis) data from PSA report files.

    This module processes PSA data files and generates various types of plots including:
    - Subject-level plots (individual subjects, single or all channels)
    - Cohort-level plots (group averages with standard deviation bands)
    - Support for multiple sleep stages, frequency ranges, and log/linear scales
    - Automatic color expansion for scenarios with many recordings

    Input Parameters
    ----------------
    filenames : dict
        Keys are filenames. Each file contains a TSV file with PSA data.
    file_group : dict
        Keys are filenames. Values are the group label for cohort analysis.
    ROIs_def : dict
        Keys are ROI names and values are [channels_list, blank_flag].
        blank_flag=True requires all channels to be present.
    chans_ROIs_sel : dict
        Keys are channel labels or ROI names. Values are boolean selection flags.
    pics_param : dict
        Plotting parameters with keys:
        - 'cohort_avg', 'cohort_sel', 'subject_avg', 'subject_sel': bool flags for plot types
        - 'display': str, display mode ('all', 'mean', 'mean_std')
        - 'force_axis': bool or [xmin, xmax, ymin, ymax]
        - 'output_folder': str, path to save figures
        - 'freq_range': [float, float], frequency range to display
        - 'log_scale': bool, use log scale for y-axis
        - 'sleep_stage_selection': list of str, sleep stages to include
        - 'activity_var': str, variable for activity ('total', 'clock_h', 'stage_h', 'cyc')
        - 'hour': int, hour for 'clock_h' and 'stage_h' variables
        - 'cycle': int, cycle for 'cyc' variable
        
    colors_param : dict
        Color palettes for different plot types with keys:
        - 'subject_avg', 'subject_sel', 'cohort': list of color strings

    Returns
    -------
    dict
        Empty dictionary (no outputs - figures are saved to files)
    """
    def __init__(self, **kwargs):
        """ Initialize module PSAPicsGenerator """
        super().__init__(**kwargs)
        if DEBUG: print('PSAPicsGenerator.__init__')

        # Input plugs
        InputPlug('filenames',self)
        InputPlug('file_group',self)
        InputPlug('ROIs_def',self)
        InputPlug('chans_ROIs_sel',self)
        InputPlug('pics_param',self)
        InputPlug('colors_param',self)

        # Output plugs
        
        # Properties of the module
        # To display the pictures
        self.figsize = (8, 6) # in inches
        # Default frequency range for PSA plots (typical for sleep EEG)
        self.default_freq_range = [0.5, 30]
        # Default frequency resolution
        self.freq_resolution = 0.5

        # Associate a linestyle to each PSA categories
        self.linestyles = ['-', '--', '-.', ':','dotted'] # 5 different linestyles for distinguishing stages when colors are the same

        self._is_master = False 
    
    def compute(self, filenames, file_group, ROIs_def, chans_ROIs_sel, pics_param, colors_param):
        """
        Load PSA data from PSA report files, process ROIs and groups, and generate PSA pictures.

        Parameters
        ----------
        filenames : dict
            Keys are filenames. Each file contains a TSV file with PSA data.
        file_group : dict
            Keys are filenames. Values are the group label for cohort analysis.
        ROIs_def : dict
            Keys are ROI names and values are [channels_list, blank_flag].
        chans_ROIs_sel : dict
            Keys are channel labels or ROI names. Values are boolean selection flags.
        pics_param : dict
            Plotting parameters (see class docstring for details).
        colors_param : dict
            Color palettes for different plot types (see class docstring for details).

        Returns
        -------
        dict
            Empty dictionary (figures are saved to files specified in pics_param['output_folder']).

        Raises
        ------
        NodeInputException
            If any input parameters have invalid types or missing required keys.
        NodeRuntimeException
            If file operations fail or data validation errors occur.
        """

        # Input validation
        if isinstance(filenames, str) and not filenames=='':
            filenames = eval(filenames)
        if not isinstance(filenames, dict):
            raise NodeInputException(self.identifier, "filenames", \
                f"PSAPicsGenerator : dict is expected for filenames and it is {type(filenames)}")

        if isinstance(ROIs_def, str) and not ROIs_def=='':
            ROIs_def = eval(ROIs_def)
        if not isinstance(ROIs_def, dict):
            raise NodeInputException(self.identifier, "ROIs_def", \
                f"PSAPicsGenerator : dict is expected for ROIs_def and it is {type(ROIs_def)}")

        if isinstance(chans_ROIs_sel, str) and not chans_ROIs_sel=='':
            chans_ROIs_sel = eval(chans_ROIs_sel)
        if not isinstance(chans_ROIs_sel, dict):
            raise NodeInputException(self.identifier, "chans_ROIs_sel", \
                f"PSAPicsGenerator : dict is expected for chans_ROIs_sel and it is {type(chans_ROIs_sel)}")

        if isinstance(pics_param, str) and not pics_param=='':
            pics_param = eval(pics_param)
        if not isinstance(pics_param, dict):
            raise NodeInputException(self.identifier, "pics_param", \
                f"PSAPicsGenerator : dict is expected for pics_param and it is {type(pics_param)}")

        if isinstance(file_group, str) and not file_group=='':
            file_group = eval(file_group)
        if not isinstance(file_group, dict):
            raise NodeInputException(self.identifier, "file_group", \
                f"PSAPicsGenerator : dict is expected for file_group and it is {type(file_group)}")

        if isinstance(colors_param, str) and not colors_param=='':
            colors_param = eval(colors_param)
        if not isinstance(colors_param, dict):
            raise NodeInputException(self.identifier, "colors_param", \
                f"PSAPicsGenerator : dict is expected for colors_param and it is {type(colors_param)}")

        # Dict to keep the PSA data per channel
        psa_data_per_chan = {} # the key is the channel label and the value is the PSA data
        # the key is the group label and the value is the PSA data
        psa_data_cohort = {}
        n_cats = 1

        for file_name in filenames.keys():
            file_group_name = file_group[file_name]
            
            # Check if the file exists
            if(not os.path.isfile(file_name)):
                raise NodeRuntimeException(self.identifier, "filenames", \
                    f"PSAPicsGenerator file not found:{file_name}")
            
            # Load PSA data from TSV file
            try:
                psa_data_subject = pd.read_csv(file_name, sep='\t', \
                    header=0, engine='python', encoding = 'utf_8')
            except Exception as e:
                raise NodeRuntimeException(self.identifier, "filenames", \
                    f"PSAPicsGenerator could not read file {file_name}: {str(e)}")

            # Validate required columns for Snooz PSA format
            required_columns = ['filename', 'channel_label', 'freq_low_Hz', 'freq_high_Hz']
            missing_columns = [col for col in required_columns if col not in psa_data_subject.columns]
            if missing_columns:
                raise NodeRuntimeException(self.identifier, "filenames", \
                    f"PSAPicsGenerator missing required columns in {file_name}: {missing_columns}")
            
            # Check for at least one power column (stage-specific activity)
            power_columns = [col for col in psa_data_subject.columns if '_act' in col]
            if not power_columns:
                raise NodeRuntimeException(self.identifier, "filenames", \
                    f"PSAPicsGenerator no power columns found in {file_name}. Expected columns with '_act' suffix.")

            # Process each selected channel/ROI
            psa_data_all_chan = []
            chan_label_all_chan = []
            
            # For each channel in chans_ROIs_sel dict
            for ch in chans_ROIs_sel.keys():
                # if the channel is selected
                if chans_ROIs_sel[ch]:
                    if DEBUG:
                        print(f"Processing selected channel/ROI: {ch}")
                    # Extract PSA data for the current channel or ROI
                    psa_data_ch_sel = self.extract_psa_data_ch(psa_data_subject, ch, ROIs_def)
                    if psa_data_ch_sel is not None and len(psa_data_ch_sel) > 0:
                        if DEBUG:
                            print(f"Successfully extracted data for {ch}, shape: {psa_data_ch_sel.shape}")
                        # Generate the pictures
                        if "roi" in ch.lower():
                            # Use the full ROI label to distinguish between different ROIs
                            chan_label = ch
                        else:
                            chan_label = ch
                        chan_label_all_chan.append(chan_label)
                        if DEBUG:
                            print(f"Added {chan_label} to chan_label_all_chan. Current list: {chan_label_all_chan}")
                    else:
                        if DEBUG:
                            print(f"No data extracted for {ch}")

                    # **********************************************
                    # One figure for the current subject : one picture per channel or ROI
                    # **********************************************
                    if pics_param['subject_sel'] | pics_param['cohort_sel']:
                        # Save figure for a subject and a channel.
                        if pics_param['subject_sel']:
                            fig_save = 'subject_sel'
                        else:
                            fig_save = False
                        
                        psa_avg_per_chan_cat, max_cats = \
                            self._save_subject_chan_fig_psa(psa_data_ch_sel, \
                                pics_param, file_name, chan_label, fig_save, colors_param['subject_sel'])
                        
                        if chan_label in psa_data_per_chan.keys():
                            psa_data_per_chan[chan_label].append(\
                                [psa_avg_per_chan_cat, file_group_name])
                        else:
                            psa_data_per_chan[chan_label] = \
                                [[psa_avg_per_chan_cat, file_group_name]]
                        
                        if fig_save:
                            self._log_manager.log(self.identifier, \
                                f"Images are generated for the file {file_name} and channel/ROI {ch}.")

                        n_cats = max(n_cats, max_cats)

                    if pics_param['subject_avg'] | pics_param['cohort_avg']:
                        if psa_data_ch_sel is not None and len(psa_data_ch_sel) > 0:
                            psa_data_all_chan.append(psa_data_ch_sel)

            # **********************************************
            # One figure for the current subject : one picture for all channels
            # **********************************************
            if pics_param['subject_avg'] | pics_param['cohort_avg']:
                if pics_param['subject_avg']:
                    fig_save = 'subject_avg'
                else:
                    fig_save = False
                if len(chan_label_all_chan)>1:
                    colors = colors_param['subject_avg']
                else:
                    # If there is only one channel, differentiate the categories by color.
                    colors = colors_param['subject_sel']
                if (len(psa_data_all_chan)>0):
                    # psa_avg_per_cat : numpy array
                    #     Average PSA for each category for the current subject
                    # max_cat : int
                    #     The number of categories for the current subject
                    psa_avg_per_cat, max_cats = \
                        self._save_subject_chan_fig_psa(psa_data_all_chan, \
                            pics_param, file_name, chan_label_all_chan, fig_save, colors)

                    if fig_save:
                        self._log_manager.log(self.identifier, \
                            f"The image is generated for the file {file_name} for all channels.")

                    n_cats = max(n_cats, max_cats)
                else:
                    n_cats = 1
                    psa_avg_per_cat = np.empty(0)

            # Accumulate data for cohort analysis (independent of subject_avg plotting)
            if pics_param['cohort_avg']:
                # For cohort_avg, store all channel data (not averaged) to compute proper std across subjects
                # Each subject contributes their list of channel DataFrames
                if len(psa_data_all_chan) > 0:
                    if file_group_name in psa_data_cohort.keys():
                        psa_data_cohort[file_group_name].append(psa_data_all_chan)
                    else:
                        psa_data_cohort[file_group_name] = [psa_data_all_chan]

        # -> all subjects are processed

        # **********************************************
        # One figure for the cohort : one picture per channel
        # **********************************************
        if pics_param['cohort_sel']:
            # For each channel in chans_ROIs_sel dict
            for ch, psa_data_grp in psa_data_per_chan.items():
                # For each subject accumulate data
                psa_data = {}
                for psa_data_cur_sjt, group_cur_sjt in psa_data_grp:
                    if not (group_cur_sjt in psa_data.keys()):
                        if len(psa_data_cur_sjt)>0:
                            psa_data[group_cur_sjt] = [psa_data_cur_sjt]
                    else:
                        if len(psa_data_cur_sjt)>0:
                            psa_data[group_cur_sjt].append(psa_data_cur_sjt)
            
                # psa_data : for the current channel -> one PSA per subject,
                #  they need to be aligned together
                self._save_cohort_chan_fig_psa(psa_data, \
                    pics_param, ch, n_cats, colors_param['cohort'])

        # **********************************************
        # One figure for the cohort : one picture for all channels
        # **********************************************
        if pics_param['cohort_avg']:
            self._save_cohort_chan_fig_psa(psa_data_cohort, \
                pics_param, '', n_cats, colors_param['cohort'])

        return {
        }

    def extract_psa_data_ch(self, psa_data_subject, ch, ROIs_def):
        """
        Extract the PSA data for the current channel or ROI from Snooz format.
        If the ROI has the blank option and at least one channel is missing None will be returned

        Parameters
        -----------
            psa_data_subject : pandas dataframe
                PSA data for the current subject in Snooz format
            ch : string
                Label of the selected channel or ROI
            ROIs_def : dict
                Definition of the ROIs (keys are ROI label and values are the channels list and the blank flag)
        Returns
        -----------  
            psa_data_ch_sel : pandas dataframe
                PSA data for the current channel or ROI
        """
        # Verify if it is an ROI
        if "roi" in ch.lower():
            # Check if ROI definition exists
            if ch not in ROIs_def:
                if DEBUG:
                    print(f"Warning: ROI {ch} not found in ROIs_def. Available ROIs: {list(ROIs_def.keys())}")
                return None
                
            # Select the PSA data for all the channels included in the ROI
            chan_lst = ROIs_def[ch][0]
            blank_flag = ROIs_def[ch][1]
            
            # When the blank flag is set, all the channels must be present in the file
            missing_channels = []
            if blank_flag:
                for roi_ch in chan_lst:
                    # Check if channel exists in the data
                    channel_exists = False
                    for existing_ch in psa_data_subject['channel_label'].unique():
                        if roi_ch.lower() in existing_ch.lower():
                            channel_exists = True
                            break
                    if not channel_exists:
                        missing_channels.append(roi_ch)
            
            # If blank flag is set and channels are missing, return None
            if blank_flag and missing_channels:
                if DEBUG:
                    print(f"Warning: ROI {ch} requires all channels but missing: {missing_channels}")
                return None
            
            # Average PSA data across channels in ROI
            roi_data_list = []
            found_channels = []
            for roi_ch in chan_lst:
                # Find matching channel in the data
                channel_found = False
                for existing_ch in psa_data_subject['channel_label'].unique():
                    if roi_ch.lower() in existing_ch.lower():
                        # Extract data for this channel
                        ch_data = psa_data_subject[psa_data_subject['channel_label'] == existing_ch]
                        roi_data_list.append(ch_data)
                        found_channels.append(existing_ch)
                        channel_found = True
                        break
                
                if not channel_found and not blank_flag:
                    # If blank flag is not set, we can proceed with available channels
                    if DEBUG:
                        print(f"Warning: Channel {roi_ch} not found for ROI {ch}, but blank flag is False, continuing...")
            
            if roi_data_list:
                # Combine and average data across channels in ROI
                combined_data = pd.concat(roi_data_list, ignore_index=True)
                # Group by frequency bands and average power values
                power_columns = [col for col in combined_data.columns if '_act' in col]
                if power_columns:
                    # Average power values for each frequency band
                    averaged_data = combined_data.groupby(['freq_low_Hz', 'freq_high_Hz'])[power_columns].mean().reset_index()
                    psa_data_ch_sel = averaged_data
                    if DEBUG:
                        print(f"ROI {ch} processed with {len(found_channels)} channels: {found_channels}")
                else:
                    if DEBUG:
                        print(f"Warning: No power columns found for ROI {ch}")
                    psa_data_ch_sel = None
            else:
                if DEBUG:
                    print(f"Warning: No data found for ROI {ch}")
                psa_data_ch_sel = None
        else:
            # Single channel - find matching channel in the data
            channel_found = False
            for existing_ch in psa_data_subject['channel_label'].unique():
                if ch.lower() == existing_ch.lower():
                    psa_data_ch_sel = psa_data_subject[psa_data_subject['channel_label'] == existing_ch].copy()
                    channel_found = True
                    break
            
            if not channel_found:
                if DEBUG:
                    print(f"Warning: Channel {ch} not found in data")
                psa_data_ch_sel = None
                
        return psa_data_ch_sel

    def _save_subject_chan_fig_psa(self, psa_data_all_chan, pics_param, base_name, chan_label, fig_save, colors):
        """
        Function to save figure for a subject.
        This function display PSA data for the selected channels/ROIs.

        Parameters
        -----------
            psa_data_all_chan : list of pandas dataframe or list of list of pandas dataframe
                List of PSA data for the selected channels/ROIs
            pics_param: dict
                Each key is a parameter to generate pictures.
            base_name : str
                Base name for the figure file
            chan_label : str or list of str
                List of labels for the current channel/ROI
            fig_save : str or bool
                The type (label) of figure to save. If false, the figure is not saved.
            colors : list of str
                List of colors.
        Returns 
        -------
            psa_avg_per_cat : numpy array or pandas DataFrame
                Average PSA for each category for the current subject, or DataFrame with averaged data for cohort accumulation
            max_cat : int
                The number of categories for the current subject
        """
        if fig_save:
            if 'subject' in fig_save:
                # Initialize the figure and canvas for plotting
                fig = Figure()
                fig.set_size_inches(self.figsize)
                fig.clear() # reset the hold on
                ax = fig.add_subplot()

        if isinstance(chan_label, str):
            psa_data_all_chan = [psa_data_all_chan]
            chan_label = [chan_label]

        n_channels = len(psa_data_all_chan)
        max_cat = 1
        legend_labels = {}
        
        if DEBUG:
            print(f"_save_subject_chan_fig_psa: Processing {n_channels} channels/ROIs")
            print(f"Channel labels: {chan_label}")
            print(f"Colors available: {len(colors)} colors")

        # Initialize variables for cohort averaging
        all_freq_data = []
        all_power_data = []

        # Get frequency range from parameters
        freq_range = pics_param.get('freq_range', self.default_freq_range)
        log_scale = pics_param.get('log_scale', False)
        sleep_stage_selection = pics_param.get('sleep_stage_selection', ['All'])

        # For each channel display the PSA data
        for i_chan in range(n_channels):
            if DEBUG:
                print(f"Processing channel {i_chan}: {chan_label[i_chan] if i_chan < len(chan_label) else 'Unknown'}")
            # Extract the PSA data for the current channel
            psa_data_cur_chan = psa_data_all_chan[i_chan]
            
            if psa_data_cur_chan is not None and len(psa_data_cur_chan) > 0:
                # Check if there are multiple filenames in the data
                unique_filenames = []
                if 'filename' in psa_data_cur_chan.columns:
                    unique_filenames = psa_data_cur_chan['filename'].unique()
                    if DEBUG and len(unique_filenames) > 1:
                        print(f"Found {len(unique_filenames)} unique filenames in channel {chan_label[i_chan]}: {unique_filenames}")
                
                # If there are multiple filenames, process each separately
                if len(unique_filenames) > 1:
                    # Determine total number of items to plot (filenames * channels)
                    total_items = len(unique_filenames) * n_channels
                    # Expand colors if needed
                    expanded_colors = self._expand_colors(colors, total_items)
                    for filename_idx, filename_val in enumerate(unique_filenames):
                        # Filter data for this specific filename
                        psa_data_for_file = psa_data_cur_chan[psa_data_cur_chan['filename'] == filename_val]
                        
                        # Get frequency bands and power data from Snooz format
                        freq_low = psa_data_for_file['freq_low_Hz'].values
                        freq_high = psa_data_for_file['freq_high_Hz'].values
                        freq_center = (freq_low + freq_high) / 2  # Use center frequency for plotting
                        
                        # Filter frequency range
                        freq_mask = (freq_center >= freq_range[0]) & (freq_center <= freq_range[1])
                        freq_filtered = freq_center[freq_mask]
                        
                        # Get power columns (stage-specific activity) based on stage selection
                        power_columns = []
                        for stage in sleep_stage_selection:
                            if stage == 'All' and pics_param['activity_var'] == 'total':
                                stage_col = f"{pics_param['activity_var']}_act"
                            elif stage == 'All' and (pics_param['activity_var'] == 'clock_h' or pics_param['activity_var'] == 'stage_h'):
                                stage_col = f"{pics_param['activity_var']}{pics_param['hour']}_act"
                            elif stage == 'All' and pics_param['activity_var'] == 'cyc':
                                stage_col = f"{pics_param['activity_var']}{pics_param['cycle']}_act"
                            elif stage != 'All' and pics_param['activity_var'] == 'total':
                                stage_col = f"{pics_param['activity_var']}_{stage}_act"
                            elif stage != 'All' and (pics_param['activity_var'] == 'clock_h' or pics_param['activity_var'] == 'stage_h'):
                                stage_col = f"{pics_param['activity_var']}{pics_param['hour']}_{stage}_act"
                            elif stage != 'All' and pics_param['activity_var'] == 'cyc':
                                stage_col = f"{pics_param['activity_var']}{pics_param['cycle']}_{stage}_act"

                            if stage_col in psa_data_for_file.columns:
                                power_columns.append(stage_col)
                        
                        if power_columns:
                            # Plot each stage-specific power with different linestyles
                            for stage_idx, stage_col in enumerate(power_columns):
                                # Use different colors for different filenames
                                # Calculate unique index for this filename+channel combination
                                color_idx = (i_chan * len(unique_filenames) + filename_idx) % len(expanded_colors)
                                linestyle_idx = stage_idx % len(self.linestyles)
                                power_data = psa_data_for_file[stage_col].values
                                power_filtered = power_data[freq_mask]
                                
                                # Accumulate data for cohort averaging if enabled
                                if pics_param.get('cohort_avg', False):
                                    all_freq_data.append(freq_filtered)
                                    all_power_data.append(power_filtered)
                                
                                if fig_save:
                                    # Create label with filename
                                    stage_name = stage_col.replace('_act', '')
                                    filename_short = os.path.basename(filename_val).split('.')[0] if isinstance(filename_val, str) else f"file_{filename_idx}"
                                    if n_channels > 1:
                                        label_name = f'{chan_label[i_chan]}_{filename_short}_{stage_name}'
                                    else:
                                        label_name = f'{filename_short}_{stage_name}'
                                    
                                    if label_name not in legend_labels:
                                        ax.plot(freq_filtered, power_filtered, color=expanded_colors[color_idx], 
                                               label=label_name, linewidth=2, linestyle=self.linestyles[linestyle_idx])
                                        legend_labels[label_name] = True
                                    else:
                                        ax.plot(freq_filtered, power_filtered, color=expanded_colors[color_idx], 
                                               linewidth=2, linestyle=self.linestyles[linestyle_idx])
                else:
                    # Single filename or no filename column - process as before
                    # Get frequency bands and power data from Snooz format
                    freq_low = psa_data_cur_chan['freq_low_Hz'].values
                    freq_high = psa_data_cur_chan['freq_high_Hz'].values
                    freq_center = (freq_low + freq_high) / 2  # Use center frequency for plotting
                    
                    # Filter frequency range
                    freq_mask = (freq_center >= freq_range[0]) & (freq_center <= freq_range[1])
                    freq_filtered = freq_center[freq_mask]
                    
                    # Get power columns (stage-specific activity) based on stage selection
                    power_columns = []
                    for stage in sleep_stage_selection:
                        if stage == 'All' and pics_param['activity_var'] == 'total':
                            stage_col = f"{pics_param['activity_var']}_act"
                        elif stage == 'All' and (pics_param['activity_var'] == 'clock_h' or pics_param['activity_var'] == 'stage_h'):
                            stage_col = f"{pics_param['activity_var']}{pics_param['hour']}_act"
                        elif stage == 'All' and pics_param['activity_var'] == 'cyc':
                            stage_col = f"{pics_param['activity_var']}{pics_param['cycle']}_act"
                        elif stage != 'All' and pics_param['activity_var'] == 'total':
                            stage_col = f"{pics_param['activity_var']}_{stage}_act"
                        elif stage != 'All' and (pics_param['activity_var'] == 'clock_h' or pics_param['activity_var'] == 'stage_h'):
                            stage_col = f"{pics_param['activity_var']}{pics_param['hour']}_{stage}_act"
                        elif stage != 'All' and pics_param['activity_var'] == 'cyc':
                            stage_col = f"{pics_param['activity_var']}{pics_param['cycle']}_{stage}_act"

                        if stage_col in psa_data_cur_chan.columns:
                            power_columns.append(stage_col)
                    
                    if power_columns:
                        # Plot each stage-specific power with different linestyles when colors are the same
                        for stage_idx, stage_col in enumerate(power_columns):
                            # Cycle through all available linestyles
                            linestyle_idx = stage_idx % len(self.linestyles)
                            power_data = psa_data_cur_chan[stage_col].values
                            power_filtered = power_data[freq_mask]
                            
                            # Accumulate data for cohort averaging if enabled
                            if pics_param.get('cohort_avg', False):
                                all_freq_data.append(freq_filtered)
                                all_power_data.append(power_filtered)
                            
                            if fig_save:
                                # Check if the label has already been added to the legend
                                stage_name = stage_col.replace('_act', '')
                                label_name = f'{chan_label[i_chan]}_{stage_name}'
                                if label_name not in legend_labels:
                                    # Plot the PSA with a specific color and linestyle
                                    ax.plot(freq_filtered, power_filtered, color=colors[i_chan], 
                                           label=label_name, linewidth=2, linestyle=self.linestyles[linestyle_idx])
                                    # Add the label to the legend
                                    legend_labels[label_name] = True
                                else:
                                    ax.plot(freq_filtered, power_filtered, color=colors[i_chan], 
                                           linewidth=2, linestyle=self.linestyles[linestyle_idx])
                    else:
                        # Fallback: try to find any numeric columns that might be power
                        numeric_cols = psa_data_cur_chan.select_dtypes(include=[np.number]).columns
                        power_cols = [col for col in numeric_cols if col not in ['freq_low_Hz', 'freq_high_Hz']]
                        
                        if power_cols:
                            # Use the first power column found
                            power_data = psa_data_cur_chan[power_cols[0]].values
                            power_filtered = power_data[freq_mask]
                            
                            # Accumulate data for cohort averaging if enabled
                            if pics_param.get('cohort_avg', False):
                                all_freq_data.append(freq_filtered)
                                all_power_data.append(power_filtered)
                            
                            if fig_save:
                                # Check if the label has already been added to the legend
                                if f'{chan_label[i_chan]}' not in legend_labels:
                                    # Plot the PSA with a specific color
                                    ax.plot(freq_filtered, power_filtered, color=colors[i_chan], 
                                           label=f'{chan_label[i_chan]}', linewidth=2)
                                    # Add the label to the legend
                                    legend_labels[f'{chan_label[i_chan]}'] = True
                                else:
                                    ax.plot(freq_filtered, power_filtered, color=colors[i_chan], linewidth=2)

        # If the function is used to generate pictures
        if fig_save:
            if pics_param['subject_avg'] | pics_param['subject_sel']:
                fig_name = pics_param['output_folder']+'/'+os.path.basename(base_name)
                if pics_param['subject_sel']:
                    fig_name = fig_name + '_' + chan_label[0]
                fig_name = fig_name + '_psa'
                fig_name = fig_name + '.pdf'

                if pics_param['subject_sel']:
                    fig_title = os.path.basename(base_name)+ '_' + chan_label[0]
                if pics_param['subject_avg']:
                    fig_title = os.path.basename(base_name)

                if pics_param['force_axis']:
                    ax.set_xlim(pics_param['force_axis'][0], pics_param['force_axis'][1])
                    ax.set_ylim(pics_param['force_axis'][2], pics_param['force_axis'][3])
                else:
                    ax.set_xlim(freq_range[0], freq_range[1])

                if log_scale:
                    ax.set_yscale('log')

                ax.set_xlabel('Frequency (Hz)')
                ax.set_ylabel('Power (μV²/Hz)')
                ax.grid(which='both', axis='both')
                ax.set_title(fig_title)
                
                # Add legend after all plotting
                if n_channels > 1 or len(legend_labels) > 1:
                    ax.legend(loc='upper right')
                
                try:
                    fig.savefig(fig_name)
                except:
                    raise NodeRuntimeException(self.identifier, "filenames", f"Error while saving figure {fig_name}, make sure it is not open")
                if DEBUG:
                    print(f"{fig_name} is saved")
                fig.clf()

        # Compute average PSA data for cohort accumulation if enabled
        if pics_param.get('cohort_avg', False) and all_power_data:
            # For cohort analysis, we need to keep the raw channel data (not pre-averaged)
            # so that we can compute proper std across subjects later
            # Store all channel data as a list of DataFrames
            
            # Use the first channel's DataFrame as template for structure
            if psa_data_all_chan and len(psa_data_all_chan) > 0:
                # Just return the first channel's data as representative
                # The cohort analysis will handle averaging across all subjects' channels
                psa_avg_per_cat = psa_data_all_chan[0].copy()
            else:
                psa_avg_per_cat = pd.DataFrame()
        else:
            # Return dummy values for compatibility when cohort_avg is not enabled
            psa_avg_per_cat = np.empty(0)
        
        return psa_avg_per_cat, max_cat

    def _save_cohort_chan_fig_psa(self, psa_data, pics_param, chan_label, n_cats, colors):
        """
        Save the cohort figure for the current channel or ROI

        Parameters
        -----------
            psa_data : dict of list of numpy array
                keys are the subject group and values are the PSA data for the current channel or ROI
            pics_param : dict
                keys are the parameter to generate pictures
            chan_label : string
                Label of the selected channel or ROI (can be empty)
            n_cats : int
                Number of PSA categories
            colors : list of str
                List of colors for different groups
        Returns
        -----------  
            None
        """
        # Define the figure name
        if chan_label=='':
            if pics_param['activity_var']=='total':
                fig_name = pics_param['output_folder']+'/cohort_psa_'+ pics_param['display']+ '_' + pics_param['activity_var']+'.pdf'
                fig_title = 'Cohort PSA_total'
            elif pics_param['activity_var']=='clock_h' or pics_param['activity_var']=='stage_h':
                fig_name = pics_param['output_folder']+'/cohort_psa_'+ pics_param['display']+ '_' + pics_param['activity_var']+str(pics_param['hour'])+'.pdf'
                fig_title = 'Cohort PSA_'+pics_param['activity_var']+str(pics_param['hour'])
            elif pics_param['activity_var']=='cyc':
                fig_name = pics_param['output_folder']+'/cohort_psa_'+ pics_param['display']+ '_' + pics_param['activity_var']+str(pics_param['cycle'])+'.pdf'
                fig_title = 'Cohort PSA_'+pics_param['activity_var']+str(pics_param['cycle'])
        else:
            if pics_param['activity_var']=='total':
                fig_name = pics_param['output_folder']+'/cohort_psa_'+ pics_param['display']+ '_' + pics_param['activity_var'] +chan_label+'.pdf'
                fig_title = 'Cohort PSA_total_'+chan_label
            elif pics_param['activity_var']=='clock_h' or pics_param['activity_var']=='stage_h':
                fig_name = pics_param['output_folder']+'/cohort_psa_'+ pics_param['display']+ '_' + pics_param['activity_var']+str(pics_param['hour'])+'_'+chan_label+'.pdf'
                fig_title = 'Cohort PSA_'+pics_param['activity_var']+str(pics_param['hour'])+'_'+chan_label
            elif pics_param['activity_var']=='cyc':
                fig_name = pics_param['output_folder']+'/cohort_psa_'+ pics_param['display']+ '_' + pics_param['activity_var']+str(pics_param['cycle'])+'_'+chan_label+'.pdf'
                fig_title = 'Cohort PSA_'+pics_param['activity_var']+str(pics_param['cycle'])+'_'+chan_label

        # Create the figure
        fig = Figure()
        fig.set_size_inches(self.figsize)
        fig.clear() # reset the hold on
        ax = fig.add_subplot()
        legend_labels = {}

        # Get frequency range from parameters
        freq_range = pics_param.get('freq_range', self.default_freq_range)
        log_scale = pics_param.get('log_scale', False)
        sleep_stage_selection = pics_param.get('sleep_stage_selection', ['All'])

        # Create the unique list of keys of psa_data
        group_list = list(set(psa_data.keys()))

        # signal_to_plot_grp : dict of list of numpy array
        #         keys are the subject group and values are the average signal for the current channel or ROI
        #         values are a list of number of sleep stages
        signal_to_plot_grp = {} 

        # For each group of the cohort
        for i_grp, cohort_group in enumerate(group_list):
            # For each subject
            n_subjects = len(psa_data[cohort_group])
            for i_sjt in range(n_subjects):
                subject_data = psa_data[cohort_group][i_sjt]
                
                # Check if this is cohort_avg mode (list of channel DataFrames) or cohort_sel mode (single DataFrame)
                if isinstance(subject_data, list):
                    # cohort_avg: subject_data is a list of channel DataFrames
                    # Process each sleep stage separately
                    for stage_idx, stage in enumerate(sleep_stage_selection):
                        stage_freq_data = []
                        stage_power_data = []
                        
                        # Collect data from all channels for this stage
                        for chan_df in subject_data:
                            if chan_df is not None and len(chan_df) > 0:
                                freq_low = chan_df['freq_low_Hz'].values
                                freq_high = chan_df['freq_high_Hz'].values
                                freq_center = (freq_low + freq_high) / 2
                                
                                freq_mask = (freq_center >= freq_range[0]) & (freq_center <= freq_range[1])
                                freq_filtered = freq_center[freq_mask]
                                
                                if stage == 'All' and pics_param['activity_var'] == 'total':
                                    stage_col = f"{pics_param['activity_var']}_act"
                                elif stage == 'All' and (pics_param['activity_var'] == 'clock_h' or pics_param['activity_var'] == 'stage_h'):
                                    stage_col = f"{pics_param['activity_var']}{pics_param['hour']}_act"
                                elif stage == 'All' and pics_param['activity_var'] == 'cyc':
                                    stage_col = f"{pics_param['activity_var']}{pics_param['cycle']}_act"
                                elif stage != 'All' and pics_param['activity_var'] == 'total':
                                    stage_col = f"{pics_param['activity_var']}_{stage}_act"
                                elif stage != 'All' and (pics_param['activity_var'] == 'clock_h' or pics_param['activity_var'] == 'stage_h'):
                                    stage_col = f"{pics_param['activity_var']}{pics_param['hour']}_{stage}_act"
                                elif stage != 'All' and pics_param['activity_var'] == 'cyc':
                                    stage_col = f"{pics_param['activity_var']}{pics_param['cycle']}_{stage}_act"
                                
                                if stage_col in chan_df.columns:
                                    power_data = chan_df[stage_col].values
                                    power_filtered = power_data[freq_mask]
                                    
                                    stage_freq_data.append(freq_filtered)
                                    stage_power_data.append(power_filtered)
                        
                        # Process this stage's data
                        if stage_power_data and len(stage_power_data) > 0:
                            # Average across channels for this stage
                            if len(stage_power_data) == 1:
                                freq_to_plot = stage_freq_data[0]
                                power_to_plot = stage_power_data[0]
                            else:
                                # Interpolate to common frequency grid
                                min_freq = max([freq.min() for freq in stage_freq_data if len(freq) > 0])
                                max_freq = min([freq.max() for freq in stage_freq_data if len(freq) > 0])
                                common_freq = np.linspace(min_freq, max_freq, 100)
                                
                                interpolated_power = []
                                for i, power_data in enumerate(stage_power_data):
                                    freq_data = stage_freq_data[i]
                                    if len(power_data) > 0 and len(freq_data) > 0:
                                        interp_power = np.interp(common_freq, freq_data, power_data)
                                        interpolated_power.append(interp_power)
                                
                                if interpolated_power:
                                    freq_to_plot = common_freq
                                    # Don't average here - keep individual channel data for proper std calculation
                                    power_to_plot = interpolated_power  # Keep as list of arrays
                                else:
                                    continue
                            
                            # Store data for mean calculation or plot
                            stage_name = stage
                            if 'mean' in pics_param['display']:
                                # Store all interpolated power data (not averaged) for proper std calculation
                                if cohort_group in signal_to_plot_grp.keys():
                                    if f'stage_{stage_name}' in signal_to_plot_grp[cohort_group].keys():
                                        # Concatenate all channel data for this subject
                                        for channel_data in power_to_plot:
                                            signal_to_plot_grp[cohort_group][f'stage_{stage_name}'] = np.concatenate((signal_to_plot_grp[cohort_group][f'stage_{stage_name}'], channel_data.reshape(-1,1)), axis=1)
                                    else:
                                        # Initialize with first channel data
                                        signal_to_plot_grp[cohort_group][f'stage_{stage_name}'] = power_to_plot[0].reshape(-1,1)
                                        # Add remaining channel data
                                        for channel_data in power_to_plot[1:]:
                                            signal_to_plot_grp[cohort_group][f'stage_{stage_name}'] = np.concatenate((signal_to_plot_grp[cohort_group][f'stage_{stage_name}'], channel_data.reshape(-1,1)), axis=1)
                                else:
                                    signal_to_plot_grp[cohort_group] = {}
                                    # Initialize with first channel data
                                    signal_to_plot_grp[cohort_group][f'stage_{stage_name}'] = power_to_plot[0].reshape(-1,1)
                                    # Add remaining channel data
                                    for channel_data in power_to_plot[1:]:
                                        signal_to_plot_grp[cohort_group][f'stage_{stage_name}'] = np.concatenate((signal_to_plot_grp[cohort_group][f'stage_{stage_name}'], channel_data.reshape(-1,1)), axis=1)
                            else:
                                # For individual traces, average across channels for plotting
                                power_to_plot_avg = np.mean(power_to_plot, axis=0)
                                # Display all individual PSA traces
                                # Check if the label has already been added to the legend
                                if f'stage_{stage_name}-{cohort_group}' not in legend_labels:
                                    # Add the label to the legend
                                    legend_labels[f'stage_{stage_name}-{cohort_group}'] = True
                                    # Plot the PSA with a specific color and linestyle
                                    if len(sleep_stage_selection) > 1:
                                        ax.plot(freq_to_plot, power_to_plot_avg, color=colors[i_grp], 
                                               linestyle=self.linestyles[stage_idx % len(self.linestyles)], 
                                               label=f'{stage_name}-{cohort_group}', alpha=0.7, linewidth=1)
                                    else:
                                        ax.plot(freq_to_plot, power_to_plot_avg, color=colors[i_grp], 
                                               label=f'{cohort_group}', alpha=0.7, linewidth=1)
                                else:
                                    # Plot the PSA with a specific color and linestyle
                                    if len(sleep_stage_selection) > 1:
                                        ax.plot(freq_to_plot, power_to_plot_avg, color=colors[i_grp], 
                                               linestyle=self.linestyles[stage_idx % len(self.linestyles)], alpha=0.7, linewidth=1)
                                    else:
                                        ax.plot(freq_to_plot, power_to_plot_avg, color=colors[i_grp], alpha=0.7, linewidth=1)
                else:
                    # cohort_sel: subject_data is a single DataFrame
                    psa_data_subject = subject_data
                    if psa_data_subject is not None and len(psa_data_subject) > 0:
                        # Get frequency bands and power data from Snooz format
                        freq_low = psa_data_subject['freq_low_Hz'].values
                        freq_high = psa_data_subject['freq_high_Hz'].values
                        freq_center = (freq_low + freq_high) / 2  # Use center frequency for plotting
                        
                        # Filter frequency range
                        freq_mask = (freq_center >= freq_range[0]) & (freq_center <= freq_range[1])
                        freq_filtered = freq_center[freq_mask]
                        
                        # Get power columns for each sleep stage
                        for stage_idx, stage in enumerate(sleep_stage_selection):
                            if stage == 'All' and pics_param['activity_var'] == 'total':
                                stage_col = f"{pics_param['activity_var']}_act"
                            elif stage == 'All' and (pics_param['activity_var'] == 'clock_h' or pics_param['activity_var'] == 'stage_h'):
                                stage_col = f"{pics_param['activity_var']}{pics_param['hour']}_act"
                            elif stage == 'All' and pics_param['activity_var'] == 'cyc':
                                stage_col = f"{pics_param['activity_var']}{pics_param['cycle']}_act"
                            elif stage != 'All' and pics_param['activity_var'] == 'total':
                                stage_col = f"{pics_param['activity_var']}_{stage}_act"
                            elif stage != 'All' and (pics_param['activity_var'] == 'clock_h' or pics_param['activity_var'] == 'stage_h'):
                                stage_col = f"{pics_param['activity_var']}{pics_param['hour']}_{stage}_act"
                            elif stage != 'All' and pics_param['activity_var'] == 'cyc':
                                stage_col = f"{pics_param['activity_var']}{pics_param['cycle']}_{stage}_act"
                            
                            if stage_col in psa_data_subject.columns:
                                power_data = psa_data_subject[stage_col].values
                                power_filtered = power_data[freq_mask]
                                
                                # Store data for mean calculation
                                if 'mean' in pics_param['display']:
                                    # concatenate the current signal to all signals
                                    if cohort_group in signal_to_plot_grp.keys():
                                        if f'stage_{stage}' in signal_to_plot_grp[cohort_group].keys():
                                            signal_to_plot_grp[cohort_group][f'stage_{stage}'] = np.concatenate((signal_to_plot_grp[cohort_group][f'stage_{stage}'], power_filtered.reshape(-1,1)), axis=1)
                                        else:
                                            signal_to_plot_grp[cohort_group][f'stage_{stage}'] = power_filtered.reshape(-1,1)
                                    else:
                                        signal_to_plot_grp[cohort_group] = {}
                                        signal_to_plot_grp[cohort_group][f'stage_{stage}'] = power_filtered.reshape(-1,1)
                                else:
                                    # Display all individual PSA traces
                                    # Check if the label has already been added to the legend
                                    if f'stage_{stage}-{cohort_group}' not in legend_labels:
                                        # Add the label to the legend
                                        legend_labels[f'stage_{stage}-{cohort_group}'] = True
                                        # Plot the PSA with a specific color and linestyle
                                        if len(sleep_stage_selection) > 1:
                                            ax.plot(freq_filtered, power_filtered, color=colors[i_grp], 
                                                   linestyle=self.linestyles[stage_idx % len(self.linestyles)], 
                                                   label=f'{stage}-{cohort_group}', alpha=0.7, linewidth=1)
                                        else:
                                            ax.plot(freq_filtered, power_filtered, color=colors[i_grp], 
                                                   label=f'{cohort_group}', alpha=0.7, linewidth=1)
                                    else:
                                        # Plot the PSA with a specific color and linestyle
                                        if len(sleep_stage_selection) > 1:
                                            ax.plot(freq_filtered, power_filtered, color=colors[i_grp], 
                                                   linestyle=self.linestyles[stage_idx % len(self.linestyles)], alpha=0.7, linewidth=1)
                                        else:
                                            ax.plot(freq_filtered, power_filtered, color=colors[i_grp], alpha=0.7, linewidth=1)

        # For mean display, compute and plot averages for each stage
        if 'mean' in pics_param['display']:
            for i_grp, cohort_group in enumerate(group_list):
                for stage_idx, stage in enumerate(sleep_stage_selection):
                    if cohort_group in signal_to_plot_grp and f'stage_{stage}' in signal_to_plot_grp[cohort_group]:
                        # Average the signals to get the mean signal
                        signal_to_plot_mean = np.nanmean(signal_to_plot_grp[cohort_group][f'stage_{stage}'], axis=1)
                        # Compute the standard deviation
                        signal_to_plot_std = np.nanstd(signal_to_plot_grp[cohort_group][f'stage_{stage}'], axis=1)
                        
                        # Create frequency array (assuming all subjects have same frequency grid)
                        # We need to get the frequency array from the data
                        freq_array = np.linspace(freq_range[0], freq_range[1], len(signal_to_plot_mean))
                        
                        # Plot the channels with a specific linestyle and the stages with a specific color
                        if len(sleep_stage_selection) > 1:
                            ax.plot(freq_array, signal_to_plot_mean, color=colors[i_grp],
                                 linestyle=self.linestyles[stage_idx % len(self.linestyles)], label=f'{stage}-{cohort_group}')
                            if 'std' in pics_param['display']:
                                # Plot standard deviation as shaded area
                                if log_scale:
                                    # For log scale, use multiplicative std (more appropriate for log-transformed data)
                                    # Convert to log space, add/subtract std, then convert back
                                    log_mean = np.log10(signal_to_plot_mean + 1e-10)  # Add small epsilon to avoid log(0)
                                    log_std = signal_to_plot_std / (signal_to_plot_mean + 1e-10) / np.log(10)
                                    lower_bound = 10 ** (log_mean - log_std)
                                    upper_bound = 10 ** (log_mean + log_std)
                                    ax.fill_between(freq_array, lower_bound, upper_bound, 
                                                  color=colors[i_grp], alpha=0.3,
                                                  edgecolor=colors[i_grp], linestyle=self.linestyles[stage_idx % len(self.linestyles)],
                                                  linewidth=1.5)
                                else:
                                    # For linear scale, use additive std
                                    ax.fill_between(freq_array, signal_to_plot_mean - signal_to_plot_std, 
                                                  signal_to_plot_mean + signal_to_plot_std, color=colors[i_grp], 
                                                  alpha=0.3, edgecolor=colors[i_grp],
                                                  linestyle=self.linestyles[stage_idx % len(self.linestyles)], linewidth=1.5)
                        else:
                            ax.plot(freq_array, signal_to_plot_mean, color=colors[i_grp], label=f'{cohort_group}')
                            if 'std' in pics_param['display']:
                                # Plot standard deviation as shaded area
                                if log_scale:
                                    # For log scale, use multiplicative std (more appropriate for log-transformed data)
                                    # Convert to log space, add/subtract std, then convert back
                                    log_mean = np.log10(signal_to_plot_mean + 1e-10)  # Add small epsilon to avoid log(0)
                                    log_std = signal_to_plot_std / (signal_to_plot_mean + 1e-10) / np.log(10)
                                    lower_bound = 10 ** (log_mean - log_std)
                                    upper_bound = 10 ** (log_mean + log_std)
                                    ax.fill_between(freq_array, lower_bound, upper_bound, 
                                                  color=colors[i_grp], alpha=0.3,
                                                  edgecolor=colors[i_grp], linestyle='-', linewidth=1.5)
                                else:
                                    # For linear scale, use additive std
                                    ax.fill_between(freq_array, signal_to_plot_mean - signal_to_plot_std, 
                                                  signal_to_plot_mean + signal_to_plot_std, color=colors[i_grp], 
                                                  alpha=0.3, edgecolor=colors[i_grp], linestyle='-', linewidth=1.5)

        # Set the limits of the axes
        if pics_param['force_axis']:
            ax.set_xlim(pics_param['force_axis'][0], pics_param['force_axis'][1])
            ax.set_ylim(pics_param['force_axis'][2], pics_param['force_axis'][3])
        else:
            ax.set_xlim(freq_range[0], freq_range[1])

        if log_scale:
            ax.set_yscale('log')

        ax.grid(which='both', axis='both')
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('Power (μV²/Hz)')
        # set the legend to the upper right
        ax.legend(loc="upper right")
        ax.set_title(fig_title)
        if pics_param['cohort_avg'] | pics_param['cohort_sel']:
            try:
                fig.savefig(fig_name)
            except:
                raise NodeRuntimeException(self.identifier, "filenames", f"Error while saving figure {fig_name}, make sure it is not open")
            if DEBUG:
                print(f"{fig_name} is saved...")
            fig.clf()

    def _expand_colors(self, base_colors, n_needed):
        """
        Expand the color palette when more than 10 colors are needed.
        Uses maximally distinct colors in HSV space for better visual separation.
        
        Parameters
        ----------
        base_colors : list
            Base color palette (typically 10 colors)
        n_needed : int
            Number of colors needed
            
        Returns
        -------
        list
            Extended color list with well-separated colors
        """
        if n_needed <= 10:
            # Use base colors as-is
            return base_colors
        
        # Need to generate more distinct colors
        import matplotlib.colors as mcolors
        import colorsys
        
        extended_colors = []
        
        # Strategy: Distribute colors evenly in HSV space for maximum distinction
        # Use golden ratio for better color distribution
        golden_ratio = 0.618033988749895
        
        # Start with base colors converted to HSV to understand their distribution
        base_hues = []
        for base_color in base_colors:
            rgb = mcolors.to_rgb(base_color)
            hsv = colorsys.rgb_to_hsv(*rgb)
            base_hues.append(hsv[0])
        
        # Generate new colors by:
        # 1. Distributing hues evenly across the color wheel
        # 2. Varying saturation and value to create distinctions
        hue_start = 0.0
        for i in range(n_needed):
            # Use golden ratio to get maximally distinct hues
            hue = (hue_start + i * golden_ratio) % 1.0
            
            # Vary saturation and value to create more distinction
            # Use different saturation levels (high/medium) and value levels (bright/medium)
            sat_level = i % 3  # 3 saturation levels
            val_level = (i // 3) % 2  # 2 value levels
            
            if sat_level == 0:
                saturation = 0.9  # High saturation
            elif sat_level == 1:
                saturation = 0.65  # Medium saturation
            else:
                saturation = 0.45  # Lower saturation
            
            if val_level == 0:
                value = 0.95  # Bright
            else:
                value = 0.7  # Medium brightness
            
            # Convert HSV to RGB
            rgb = colorsys.hsv_to_rgb(hue, saturation, value)
            extended_colors.append(rgb)
        
        return extended_colors[:n_needed] 