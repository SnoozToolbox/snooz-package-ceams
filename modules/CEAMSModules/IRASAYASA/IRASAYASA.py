"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    IRASAYASA
    TODO CLASS DESCRIPTION
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

import numpy as np
import math
from fractions import Fraction
from scipy.signal import resample_poly, periodogram, welch
from scipy.optimize import curve_fit
from joblib import Parallel, delayed
import matplotlib.pyplot as plt
from scipy import fft as sp_fft
from CEAMSModules.PSGReader import SignalModel as test
import yasa

DEBUG = False

class IRASAYASA(SciNode):
    """
    TODO CLASS DESCRIPTION

    Parameters
    ----------
        signals: TODO TYPE
            TODO DESCRIPTION
        win_len_sec: TODO TYPE
            TODO DESCRIPTION
        win_step_sec: TODO TYPE
            TODO DESCRIPTION
        window_name: TODO TYPE
            TODO DESCRIPTION
        first_freq: TODO TYPE
            TODO DESCRIPTION
        last_freq: TODO TYPE
            TODO DESCRIPTION
        flag: TODO TYPE
            TODO DESCRIPTION
        

    Returns
    -------
        rhythmic_psd: TODO TYPE
            TODO DESCRIPTION
        arhythmic_psd: TODO TYPE
            TODO DESCRIPTION
        
    """
    def __init__(self, **kwargs):
        """ Initialize module IRASAYASA """
        super().__init__(**kwargs)
        if DEBUG: print('IRASAYASA.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('win_len_sec',self)
        InputPlug('win_step_sec',self)
        InputPlug('window_name',self)
        InputPlug('first_freq',self)
        InputPlug('last_freq',self)
        InputPlug('flag',self)
        

        # Output plugs
        OutputPlug('rhythmic_psd',self)
        OutputPlug('arhythmic_psd',self)
        
        self._is_master = False 
    
    def compute(self, signals,win_len_sec,win_step_sec,window_name,first_freq,last_freq,flag=False):
        """
        Compute the rhytmic spectrum for each epoch of a 2D array (NepocsXNsamples)

        Parameters
        -----------
            signals    : a list of SignalModel
                        signal.samples : The actual signal data as numpy list
                        signal.sample_rate : sampling rate of the signal (used to STFT)
                        signal.channel : current channel label
            win_len_sec     : float
                window length in sec (how much data is taken for each fft)
            win_step_sec    : float 
                window step in sec (each time the fft is applied)
            window_name     : string, optional
                Window's name to scale the extracted time series before applying the fft
            

        Outputs:
            "psd": list of dicts (length of signals)
                key of each dict:
                    psd : power (µV^2) narray [Nepocs x Nsamples]
                    freq_bins : frequency bins (Hz)
                    win_len : windows length (s)
                    win_step : windows step (s)
                    sample_rate : sampling rate of the original signal (Hz)
                    chan_label : channel label
                    start_time : start (s) of the signal (item of signals) on which the ffts are performed
                    end_time : end (s) of the signal (item of signals) on which the ffts are performed
                    duration : duraiton (s) of the signal (item of signals) on which the ffts are performed            
                    
            "slope": list
                beta : slope characterizing the arhytmic spectrum for each epoch  
            "intercept": list
                intercept : intercept characterizing the arhytmic spectrum  for each epoch 
            

        """

        # Code examples

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"RandB input of wrong type. Expected: <class 'list'> received: {type(signals)}")
        cache = {}

        win_len_sec = float(win_len_sec)
        win_step_sec = float(win_step_sec)
        first_freq = float(first_freq)
        last_freq = float(last_freq)
        if isinstance(flag, str):
            flag = flag.strip().lower() == 'true'
        # get data

        #sign2d = test.SignalModel.get_attribute(signals,'samples' , None)       
        fs = test.SignalModel.get_attribute(signals,'sample_rate' , None)
        allsignals = test.SignalModel.get_attribute(signals,'samples' , None)
        channel = test.SignalModel.get_attribute(signals,'channel' , None)
        rhythmic_psd = []
        arhythmic_psd = []
        # get data and split and stack accordingly
        for i, signal_model in enumerate(signals):
            sign2d_split, new_chan, start_time, end_time, new_dur = self.split_and_stack(signal_model, win_len_sec, fs)
            # compute rythmic spectral analysis
            if flag:
                continue
            else:
                residu, psd_aperiodic, freq_bins  = self.IRASA(sign2d_split, fs,first_freq,last_freq, window_name, window_sec=win_len_sec, new_chan=new_chan, return_fit=False)
            # Define output
            data_rhythmic = {}
            data_rhythmic['psd'] = residu
            data_rhythmic['freq_bins'] = freq_bins
            data_rhythmic['win_len'] = win_len_sec
            data_rhythmic['win_step'] = win_step_sec
            data_rhythmic['sample_rate'] = fs[i]
            data_rhythmic['chan_label'] = new_chan[0]
            data_rhythmic['start_time'] = start_time[0]
            data_rhythmic['end_time'] = end_time[-1]
            data_rhythmic['duration'] = sum(new_dur)
            data_rhythmic['flag'] = "rhythmic"

            data_arhythmic = {}
            data_arhythmic['psd'] = psd_aperiodic
            data_arhythmic['freq_bins'] = freq_bins
            data_arhythmic['win_len'] = win_len_sec
            data_arhythmic['win_step'] = win_step_sec
            data_arhythmic['sample_rate'] = fs[i]
            data_arhythmic['chan_label'] = new_chan[0]
            data_arhythmic['start_time'] = start_time[0]
            data_arhythmic['end_time'] = end_time[-1]
            data_arhythmic['duration'] = sum(new_dur)
            data_arhythmic['flag'] = "arhythmic"
            '''cache['psd'] = res_mean
            cache['freq_bins'] = data['freq_bins']
            cache['channel'] = signals[i].channel
            cache['sample_rate'] = signals[i].sample_rate
            cache['win_step_sec'] = win_step_sec
            cache['win_len'] = win_len_sec
            cache['psd_raw'] = psd_raw
            cache['freq_raw'] = freq_raw
            cache['first_freq'] = first_freq
            cache['last_freq'] = last_freq
            self._cache_manager.write_mem_cache(self.identifier, cache)'''
            rhythmic_psd.append(data_rhythmic.copy())
            arhythmic_psd.append(data_arhythmic.copy())
        return {
            'rhythmic_psd': rhythmic_psd,
            'arhythmic_psd': arhythmic_psd
        }
    
    def split_and_stack(self, signals, win_len_sec, fs):
        # split data according to time and then stack it 

        nsample = int(win_len_sec*fs[0])
        sign = np.asarray(signals.samples)
        remainder = sign.shape[0] % nsample
        ####################
        if remainder > 0:
            if sign.shape[0]/2 > nsample:
                col_keep = (sign.shape[0]//nsample) * nsample
                cols_to_cut = sign.shape[0]-col_keep
                sign = sign[:-cols_to_cut]
            else:
                col_keep = nsample
                cols_to_cut = sign.shape[0]-col_keep
                sign = sign[:-cols_to_cut]
        if remainder ==  0:
            col_keep = sign.shape[0]
        ####################

        cols_per_div = sign.shape[0] // nsample
        segments = np.split(sign, cols_per_div, axis= 0)
        new_arr = np.vstack(segments)
        new_chan = np.repeat(np.asarray(signals.channel), cols_per_div)
        new_dur =  np.repeat(np.asarray(win_len_sec), cols_per_div)

        startTime = signals.start_time
        time_array = np.empty((cols_per_div, 2))
        for j in range(cols_per_div):
            endTime = startTime + (win_len_sec)
            time_array[j,0] = startTime
            time_array[j,1] =endTime
            startTime = startTime + win_len_sec
        start_time = time_array[:,0]
        end_time = time_array[:,1]

        return new_arr, new_chan, start_time, end_time, new_dur

    def IRASA(self, signals, fs, first_freq, last_freq, window_name, window_sec, new_chan, return_fit=False):
        # Apply the IRASA technique
        fs = fs[0]  # Use the first sampling rate (assuming all are the same)
        n_epochs = signals.shape[0]
        n_samples = signals.shape[1]  # Number of samples per epoch
        # Use fixed nfft for all scales to ensure consistent frequency grids based on the original paper's recommendation
        #fixed_nfft = 2 * (int(2 ** np.ceil(np.log2(n_samples)))) # The one suggested by the original paper
        fixed_nfft = sp_fft.next_fast_len(n_samples, real=True) # The one used in the Stft module
        # First pass: run analysis and determine target column count.
        periodic_rows = []
        aperiodic_rows = []
        freqs_rows = []
        residu_rows = []
        target_cols = 0

        for i in range(n_epochs):
            if np.isnan(signals[i, :]).any():
                periodic_rows.append(None)
                aperiodic_rows.append(None)
                freqs_rows.append(None)
                residu_rows.append(None)
                continue

            irasa_result = yasa.irasa(
                signals[i, :], fs, ch_names=new_chan[i],
                band=(first_freq, last_freq), win_sec=window_sec, return_fit=return_fit,
                kwargs_welch=dict(average="median", window=window_name, nfft=fixed_nfft, scaling='spectrum', detrend=False)
            )

            freqs_i = np.asarray(irasa_result[0])
            aperiodic_i = np.asarray(irasa_result[1])
            periodic_i = np.asarray(irasa_result[2])

            residu_i = None
            if return_fit and len(irasa_result) > 3:
                fit_params = irasa_result[3]
                residu_i = np.exp((-fit_params['Intercept'][0])) * (freqs_i)**((-fit_params['Slope'][0])) * (aperiodic_i + periodic_i)
            
            periodic_rows.append(periodic_i)
            aperiodic_rows.append(aperiodic_i)
            freqs_rows.append(freqs_i)
            residu_rows.append(residu_i)
            target_cols = max(target_cols, periodic_i.shape[0], aperiodic_i.shape[0], freqs_i.shape[0])

        # Second pass: allocate fixed 2D arrays and fill available values.
        periodic_array = np.zeros((n_epochs, target_cols))
        aperiodic_array = np.zeros((n_epochs, target_cols))
        freqs = np.zeros(target_cols)
        residu_array = np.zeros((n_epochs, target_cols))

        for row_freqs in freqs_rows:
            if row_freqs is not None and row_freqs.shape[0] > 0:
                freqs[:row_freqs.shape[0]] = row_freqs
                break

        for i in range(n_epochs):
            p_i = periodic_rows[i]
            a_i = aperiodic_rows[i]
            r_i = residu_rows[i]
            if p_i is None or a_i is None:
                periodic_array[i, :] = np.nan
                aperiodic_array[i, :] = np.nan
                residu_array[i, :] = np.nan
                continue
            if p_i.shape[1] > 0:
                periodic_array[i, :p_i.shape[1]] = p_i
            if a_i.shape[1] > 0:
                aperiodic_array[i, :a_i.shape[1]] = a_i
            if return_fit and r_i is not None and r_i.shape[1] > 0:
                residu_array[i, :r_i.shape[1]] = r_i

        if return_fit:
            return residu_array, aperiodic_array, freqs

        # Compute ratio-style residu to match rhythmic_spectral_analysis output
        # residu = (aperiodic + periodic) / aperiodic = 1 + (periodic / aperiodic)
        with np.errstate(divide='ignore', invalid='ignore'):
            residu = (aperiodic_array + periodic_array) / aperiodic_array
            residu[~np.isfinite(residu)] = np.nan  # Handle division by zero or invalid values

        return residu, aperiodic_array, freqs