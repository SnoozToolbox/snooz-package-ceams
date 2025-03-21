"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    YasaSleepStaging
    This class performs automatic sleep scoring using the YasaSleepStaging package.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import os
import mne
import yasa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import resample
from sklearn.metrics import classification_report, confusion_matrix

DEBUG = False

class YasaSleepStaging(SciNode):
    """
    This class performs automatic sleep scoring using the YasaSleepStaging package.

    Parameters
    ----------
        filename: TODO TYPE
            TODO DESCRIPTION
        signals: TODO TYPE
            TODO DESCRIPTION
        sleep_stages: TODO TYPE
            TODO DESCRIPTION
        events: TODO TYPE
            TODO DESCRIPTION
        

    Returns
    -------
        results: TODO TYPE
            TODO DESCRIPTION
        write: TODO TYPE
            TODO DESCRIPTION
        
    """
    def __init__(self, **kwargs):
        """ Initialize module YasaSleepStaging """
        super().__init__(**kwargs)
        if DEBUG: print('YasaSleepStaging.__init__')

        # Input plugs
        InputPlug('filename', self)
        InputPlug('signals_EEG', self)
        InputPlug('signals_EOG', self)
        InputPlug('signals_EMG', self)
        InputPlug('sleep_stages', self)
        InputPlug('events', self)
        InputPlug('Checkbox', self)

        # Output plugs
        OutputPlug('results', self)
        OutputPlug('info', self)
        OutputPlug('new_events', self)

        self.is_done = False
        self._is_master = False
    
    def compute(self, filename,signals_EEG, signals_EOG, signals_EMG ,sleep_stages,events, Checkbox):
        """
        TODO DESCRIPTION

        Parameters
        ----------
            filename: TODO TYPE
                TODO DESCRIPTION
            signals: TODO TYPE
                TODO DESCRIPTION
            sleep_stages: TODO TYPE
                TODO DESCRIPTION
            events: TODO TYPE
                TODO DESCRIPTION
            

        Returns
        -------
            results: TODO TYPE
                TODO DESCRIPTION
            write: TODO TYPE
                TODO DESCRIPTION
            

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        # Split the data into EEG, EOG, and EMG signals
        signals = self.SplitData(signals_EEG, signals_EOG, signals_EMG)
        y_pred_list = []
        confidence_list = []
        for signal in signals:
            # Prepare raw data for sleep staging
            signal = self.prepare_raw_data(signal)
            # Apply sleep staging
            sls = self.apply_sleep_staging(signal)
            # Check the features
            #features = sls.get_features()
            # Predict sleep stages
            y_pred = sls.predict()
            y_pred_list.append(y_pred)
            # Get the probability of each stage
            proba = sls.predict_proba()        
            # Get the confidence
            confidence = proba.max(axis=1)
            confidence_list.append(confidence)
        # Perform majority vote for each element across all lists in y_pred_list
        y_pred_majority_vote = []
        Decided_Confidence = []
        for i in range(len(y_pred_list[0])):
            max_confidence_index = np.argmax([confidence[i] for confidence in confidence_list])
            Decided_Confidence.append(confidence_list[max_confidence_index][i])
            y_pred_majority_vote.append(y_pred_list[max_confidence_index][i])
        '''for i in range(len(y_pred_list[0])):
            votes = [y_pred[i] for y_pred in y_pred_list]
            majority_vote = max(set(votes), key=votes.count)
            y_pred_majority_vote.append(majority_vote)'''
        Avg_Confidence = 100 * np.mean(Decided_Confidence)
        y_pred = y_pred_majority_vote
        y_pred = yasa.Hypnogram(y_pred, freq="30s")

        # If Checkbox is True, we are in validation mode, else we are in prediction mode
        if Checkbox:
                
                    # Mapping of sleep stages
            stage_mapping = {
                '0': 'WAKE',
                '1': 'N1',
                '2': 'N2',
                '3': 'N3',
                '4': 'N3',
                '5': 'REM',
                '9': 'UNS'
            }
            # Map stages to be compatible with Snooz staging
            labels = sleep_stages['name'].values
            labels = [stage_mapping.get(stage, 'UNKNOWN') for stage in labels]
            labels = yasa.Hypnogram(labels, freq="30s")
            # Mask unwanted stages
            #labels_new, first_wake, last_wake = self.mask_list(list(labels.hypno), mask_value='UNS', flag=True)
            #y_pred_new, _, _ = self.mask_list(list(y_pred.hypno), mask_value='UNS', first_wake=first_wake, last_wake=last_wake, flag=False)

            labels_new = list(labels.hypno)
            y_pred_new = list(y_pred.hypno)
            
            #NOTE Create a new events dataframe
            new_events = self.event_writer(y_pred_new, events) #NOTE: Uncomment it if you want to write the events to a new file
            # Filter out "UNS" stages
            labels_new, y_pred_new = self.filter_uns(labels_new, y_pred_new)

            # Calculate Accuracy
            Accuracy = 100 * (pd.Series(labels_new) == pd.Series(y_pred_new)).mean()
            report_dict = classification_report(labels_new, y_pred_new, output_dict=True)

            # Calculate F1 scores for each stage
            F1_scores = {stage: report_dict[stage]['f1-score']*100 if stage in report_dict else None for stage in ['WAKE', 'N1', 'N2', 'N3', 'REM']}

            print(f"The overall agreement is {Accuracy:.2f}%")

            # Convert lists back to Hypnogram objects
            labels_new = yasa.Hypnogram(labels_new, freq="30s")
            y_pred_new = yasa.Hypnogram(y_pred_new, freq="30s")

            # Cache the results
            file_name = filename[:-4] # Extract the file name from the path
            self.cache_signal(labels_new, y_pred_new, Accuracy, sls, Avg_Confidence, file_name)

            # Log the results
            self._log_manager.log(self.identifier, "Hypnogram computed.")
            self._log_manager.log(self.identifier, f"The overall agreement is {Accuracy:.2f}%")
            filenamewe = os.path.basename(file_name)
            name_without_extension = os.path.splitext(filenamewe)[0]
            # Create a DataFrame for the classification report
            df_Classification_report = pd.DataFrame({'Subject Name': [name_without_extension], 'Accuracy': [Accuracy], 'Average Confidence':[Avg_Confidence], **{f'F1-{stage}': [F1_scores[stage]] for stage in F1_scores}})
        else:
            y_pred_new = list(y_pred.hypno)
            #NOTE Create a new events dataframe
            new_events = self.event_writer_perd(y_pred_new, events) #NOTE: Uncomment it if you want to write the events to a new file
            df_Classification_report = pd.DataFrame()
            labels_new = None
            file_name = None
            
        return {
            'results': df_Classification_report,
            'info': [labels_new, y_pred_new, file_name],
            'new_events': new_events
        }

    def SplitData(self, raw_EEG, raw_EOG, raw_EMG):
        """
        Split the data into EEG, EOG, and EMG signals based on available inputs.
        EEG is mandatory, while EOG and EMG are optional.

        Parameters
        ----------
        raw_EEG : list
            List of EEG signal objects (mandatory)
        raw_EOG : list or None
            List of EOG signal objects (optional)
        raw_EMG : list or None
            List of EMG signal objects (optional)

        Returns
        -------
        list
            List of signal combinations for each EEG signal. Each combination will include
            available EOG and EMG signals.

        Raises
        ------
        NodeInputException
            If raw_EEG is empty or None
        """
        # Validate that EEG is present (mandatory)
        if not raw_EEG:
            raise NodeInputException(self.identifier, "raw_EEG", "EEG signal is mandatory but was not provided")

        rawlist = []
        
        # Get optional EOG and EMG signals if available
        eog = next(iter(raw_EOG), None) if raw_EOG else None
        emg = next(iter(raw_EMG), None) if raw_EMG else None
        
        # Create combinations based on available signals
        for eeg in raw_EEG:
            if eog and emg:  # All signals available
                rawlist.append([eeg, eog, emg])
            elif eog:  # Only EEG and EOG
                rawlist.append([eeg, eog])
            elif emg:  # Only EEG and EMG
                rawlist.append([eeg, emg])
            else:  # Only EEG
                rawlist.append([eeg])
        
        return rawlist
        '''eog = next(s for s in raw_EOG)
        emg = next(s for s in raw_EMG)
        rawlist = [[i, eog, emg] for i in raw_EEG]'''

    def prepare_raw_data(self, raw):
        """
        Prepare raw data for sleep staging.

        Parameters
        ----------
        raw: list
            List of raw signal objects.

        Returns
        -------
        RawArray
            Prepared raw data.
        """
        # Check the number of channels as input
        if len(raw) == 3:
            raw = self.sort_and_resample(raw, ['EEG', 'EOG', 'EMG'])
            ch_names = [raw[0].channel, raw[1].channel, raw[2].channel]
            ch_type = ['eeg', 'eog', 'emg']
        elif len(raw) == 2:
            raw = self.sort_and_resample(raw, ['EEG', 'EOG', 'EMG'])
            ch_names = [raw[0].channel, raw[1].channel]
            ch_type = ['eeg', 'emg' if 'EMG' in raw[1].channel else 'eog']
        elif len(raw) == 1:
            ch_names = [raw[0].channel]
            ch_type = ['eeg']
        else:
            raise NodeInputException(self.identifier, "raw", "The number of channels is not supported.")

        # Create MNE RawArray object
        sfreq = raw[0].sample_rate
        data = np.array([r.samples*1e-6 for r in raw])
        
        info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_type)
        return mne.io.RawArray(data, info)

    def sort_and_resample(self, raw, channel_order):
        """
        Sort and resample raw data.

        Parameters
        ----------
        raw: list
            List of raw signal objects.
        channel_order: list
            List of channel types in order.

        Returns
        -------
        list
            Sorted and resampled raw data.
        """
        # Order the channels from EEG, EOG, EMG
        channel_order = {ch: i for i, ch in enumerate(channel_order)}
        raw = sorted(raw, key=lambda x: channel_order.get(x.alias.upper(), len(channel_order)))
        # Resample the signals if the sampling frequency is different
        sfreq = raw[0].sample_rate
        for r in raw[1:]:
            if r.sample_rate != sfreq:
                num_samples = int(len(r.samples) * sfreq / r.sample_rate)
                r.samples = resample(r.samples, num_samples)
                r.sample_rate = sfreq
        return raw

    def apply_sleep_staging(self, raw):
        """
        Apply sleep staging using Yasa.

        Parameters
        ----------
        raw: RawArray
            Prepared raw data.

        Returns
        -------
        SleepStaging
            Yasa SleepStaging object.
        """
        ch_names = raw.ch_names
        ch_types = raw.get_channel_types()
        if len(ch_names) == 3:
            return yasa.SleepStaging(raw, eeg_name=ch_names[0], eog_name=ch_names[1], emg_name=ch_names[2])
        else:
            return yasa.SleepStaging(raw, eeg_name=ch_names[0], eog_name=ch_names[1] if 'eog' in ch_types else None, emg_name=ch_names[1] if 'emg' in ch_types else None)

    def cache_signal(self, labels_new, y_pred_new, Accuracy, sls, Avg_Confidence, file_name):
        """
        Cache the hypnogram.

        Parameters
        ----------
        labels_new : Hypnogram
            The new labels hypnogram.
        y_pred_new : Hypnogram
            The predicted labels hypnogram.
        Accuracy : float
            The Accuracy of the prediction.
        sls : SleepStaging
            The Yasa SleepStaging object.
        first_wake : int
            Index of the first wake.
        last_wake : int
            Index of the last wake.
        """
        cache = {
            'labels_new': labels_new,
            'y_pred_new': y_pred_new,
            'Accuracy': Accuracy,
            'sls': sls,
            'Avg_Confidence': Avg_Confidence,
            'file_name': file_name
        }
        self._cache_manager.write_mem_cache(self.identifier, cache)

    def mask_list(self, lst, mask_value=None, first_wake=None, last_wake=None, flag=False):
        """
        Mask elements outside the range of first and last "WAKE".

        Parameters
        ----------
        lst : list
            List to be masked.
        mask_value : any
            Value to mask with.
        first_wake : int
            Index of the first wake.
        last_wake : int
            Index of the last wake.
        flag : bool
            Flag to indicate if first and last wake should be found.

        Returns
        -------
        tuple
            Masked list, first wake index, last wake index.
        """
        try:
            if flag:
                first_wake = lst.index("WAKE")
                last_wake = len(lst) - 1 - lst[::-1].index("WAKE")
            masked_list = [mask_value if i < first_wake or i > last_wake else lst[i] for i in range(len(lst))]
            return masked_list, first_wake, last_wake
        except ValueError:
            return [mask_value] * len(lst), None, None

    def filter_uns(self, labels, preds):
        """
        Filter out "UNS" labels and corresponding predictions.

        Parameters
        ----------
        labels : list
            List of labels.
        preds : list
            List of predictions.

        Returns
        -------
        tuple
            Filtered labels and predictions.
        """
        filtered_labels = []
        filtered_preds = []
        for label, pred in zip(labels, preds):
            if label != "UNS":
                filtered_labels.append(label)
                filtered_preds.append(pred)
        return filtered_labels, filtered_preds

    def event_writer(self, y_pred_new, events):
        """
        Write events to a new file.

        Parameters
        ----------
        y_pred_new : list
            List of predicted labels.
        events : dataframe
            List of events.

        Returns
        -------
        list
            New list of events.
        """
        #NOTE creating the new dataframe for the predicted labels
        # decode the lables names to the numerical values
                # Mapping of numerical stages to string labels
        stage_mapping = {
            'WAKE': '0',
            'N1': '1',
            'N2': '2',
            'N3': '3',
            'REM': '5',
            'UNS': '9'
        }
        y_pred_decod = [stage_mapping.get(stage, '9') for stage in y_pred_new]
        # Update the 'stage' column values in the dictionary
        j = -1
        for i, stage in enumerate(events['group']):
            if stage == 'stage':
                j += 1
                events['name'][i] = y_pred_decod[j]  # Change 'new_value' to the desired value
        new_events = events
        return new_events
    
    def event_writer_perd(self, y_pred_new, events):
        """
        Write events to a new file.

        Parameters
        ----------
        y_pred_new : list
            List of predicted labels.
        events : dataframe
            List of events.

        Returns
        -------
        list
            New list of events.
        """
        #NOTE creating the new dataframe for the predicted labels
        # decode the lables names to the numerical values
                # Mapping of numerical stages to string labels
        stage_mapping = {
            'WAKE': '0',
            'N1': '1',
            'N2': '2',
            'N3': '3',
            'REM': '5',
            'UNS': '9'
        }
        y_pred_decod = [stage_mapping.get(stage, '9') for stage in y_pred_new]
        # Update the 'stage' column values in the dictionary
        
        for i in range(len(y_pred_decod)):
            if events['group'][i] == 'stage':
                events['name'][i] = y_pred_decod[i]  # Change 'new_value' to the desired value
        new_events = events
        return new_events
    
