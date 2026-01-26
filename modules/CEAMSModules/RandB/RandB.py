"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    RandB
    TODO CLASS DESCRIPTION
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException

import numpy as np
import math
from fractions import Fraction
from scipy.signal import resample_poly, periodogram

from CEAMSModules.PSGReader import SignalModel as test

DEBUG = False

class RandB(SciNode):
    """
    TODO CLASS DESCRIPTION

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
        "psd": TODO TYPE
            TODO DESCRIPTION
        "slope": TODO TYPE
            TODO DESCRIPTION
        "intercept": TODO TYPE
            TODO DESCRIPTION
        
    """
    def __init__(self, **kwargs):
        """ Initialize module RandB """
        super().__init__(**kwargs)
        if DEBUG: print('RandB.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('win_len_sec',self)
        InputPlug('win_step_sec',self)
        InputPlug('window_name',self)
        InputPlug('first_freq',self)
        InputPlug('last_freq',self)

        # Output plugs
        OutputPlug('psd',self)
        OutputPlug('slope',self)
        OutputPlug('intercept',self)
        

        # Init module variables
        self.this_is_an_example_you_can_delete_it = 0

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    

    def compute(self, signals, win_len_sec, win_step_sec, window_name,first_freq,last_freq):
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
        # get data

        #sign2d = test.SignalModel.get_attribute(signals,'samples' , None)       
        fs = test.SignalModel.get_attribute(signals,'sample_rate' , None)
        stacked_signal = []
        stacked_channel = []
        stacked_start_time = []
        stacked_end_time = []
        stacked_dur = []

        # get data and split and stack accordingly
        for i, signal_model in enumerate(signals):
            sign2d_split, new_chan, start_time, end_time, new_dur = self.split_and_stack(signal_model, win_len_sec, fs)
            stacked_signal.append(sign2d_split)
            stacked_channel.append(new_chan)
            stacked_start_time.append(start_time)
            stacked_end_time.append(end_time)
            stacked_dur.append(new_dur)
            
        stacked_signal = np.concatenate(stacked_signal)
        stacked_channel = np.concatenate(stacked_channel)
        stacked_start_time = np.concatenate(stacked_start_time)
        stacked_end_time = np.concatenate(stacked_end_time)
        stacked_dur = np.concatenate(stacked_dur)
   
        # compute rythmic spectral analysis
        residu, res_mean, freq_bins,intercept,beta,freq_raw, psd_raw  = self.rythmic_spectral_analysis(stacked_signal, fs,first_freq,last_freq)

        # Define output
        psd = []
        data = {}
        data['psd'] = residu
        data['freq_bins'] = freq_bins
        data['win_len'] = win_len_sec
        data['win_step'] = win_step_sec
        data['sample_rate'] = fs[0]
        data['chan_label'] = stacked_channel[0]
        data['start_time'] = stacked_start_time[0]
        data['end_time'] = stacked_end_time[-1]
        data['duration'] = sum(stacked_dur)

        cache['psd'] = res_mean
        cache['freq_bins'] = data['freq_bins']
        cache['channel'] = signals[0].channel
        cache['sample_rate'] = signals[0].sample_rate
        cache['win_step_sec'] = win_step_sec
        cache['win_len'] = win_len_sec
        cache['psd_raw'] = psd_raw
        cache['freq_raw'] = freq_raw
        cache['first_freq'] = first_freq
        cache['last_freq'] = last_freq
        self._cache_manager.write_mem_cache(self.identifier, cache)
        psd.append(data.copy())

        # Write to the cache to use the data in the resultTab
           
        return {
            'psd': psd
            #'slope': list(str(beta)),
            #'intercept': list(str(intercept))
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
                sign = sign[:, :-cols_to_cut]
            else:
                col_keep = nsample
                cols_to_cut = sign.shape[0]-col_keep
                sign = sign[:, :-cols_to_cut]
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
    
    
    def raw_spectral_analysis(self, signals, fs):
        """ Compute the spectral analysis of the signals using scipy.signal.periodogram

        Parameters
        -----------
        signals        : Array (Nepocs X time)
        fs             : float
            Sampling frequency (Hz)
        win_len_sec     : float
            window length in sec (how much data is taken for each fft)            
        Returns
        -----------
        psd_data        : ndarray [fft_win_count x 0-fs/2 Hz]
            Power spectral density data as an array.
            A value of the power for each frequency bin for each extracted window.
        freq_bins       : ndarray
            The frequency bins array (Hz)

        Usage : psd_data, freq_bins = compute(ts_signal, 100)

        """    
        # valid fs
        fs = fs[0]

        # select segment using next power of 2
        _, n = signals.shape
        # compute spectral analysis using scipy periodogram
        # scaling='density' gives power spectral density in V^2/Hz
        # we'll use 'spectrum' to get power spectrum directly
        freq_bins, psd_data = periodogram(signals, fs=fs, window='boxcar', 
                                          nfft=n, scaling='spectrum', 
                                          detrend=False, axis=1)

        return psd_data, freq_bins


    def resampled_spectral_analysis(self, signals, fs):
        """Compute resampled spectral analysis using scipy periodogram"""
        fs = fs[0]
        Npoints = len(signals)
        
        # define scale
        scale = np.arange(1.05, 1.75, 0.03)
        nscale = len(scale)
        
        # Use the full signal
        sign = signals
        
        # Get maximum frequency bins needed
        max_nfft = int(Npoints * scale[-1])
        Nfrac = max_nfft // 2 + 1
        
        # initialize array for power resampling
        pow1 = np.full((nscale, Nfrac), np.nan)
        pow2 = np.full((nscale, Nfrac), np.nan)

        for i in range(nscale):
            a = scale[i]
            fraction = Fraction(a).limit_denominator()
            num = fraction.numerator
            dem = fraction.denominator
            
            # compute power scaling UP
            sign_rescaled = resample_poly(sign, num, dem)
            Nsign_rescaled = len(sign_rescaled)
            freq_up, psd_up = periodogram(sign_rescaled, fs=fs, window='boxcar',
                                         nfft=Nsign_rescaled, scaling='spectrum',
                                         detrend=False)
            nfill = min([Nfrac, len(psd_up)])
            pow1[i, 0:int(nfill)] = psd_up[0:int(nfill)]
            
            # compute power scaling DOWN
            sign_rescaled = resample_poly(sign, dem, num)
            Nsign_rescaled = len(sign_rescaled)
            freq_down, psd_down = periodogram(sign_rescaled, fs=fs, window='boxcar',
                                             nfft=Nsign_rescaled, scaling='spectrum',
                                             detrend=False)
            nfill = min([Nfrac, len(psd_down)])
            pow2[i, 0:int(nfill)] = psd_down[0:int(nfill)]

        # Compute geometric mean of resampled spectra
        P1P2 = np.exp(np.nanmean(0.5 * np.log(np.multiply(pow1, pow2)), axis=0))
        
        # Remove NaN values and get corresponding frequencies
        YesNaN = np.argwhere(~np.isnan(P1P2))
        psd_data = P1P2[YesNaN]
        
        # Create frequency array matching the PSD length
        freq = fs / 2 * np.linspace(0, 1, Nfrac)
        freq_bins = freq[YesNaN]

        return psd_data, freq_bins


    def rythmic_spectral_analysis(self, signals, fs, first_freq, last_freq):

        psd_raw, freq_raw = self.raw_spectral_analysis(signals, fs)
        psd_raw_mean = np.nanmean(psd_raw,axis = 0)

        Nepocs, Npoints = signals.shape

        FW_all = []
        beta = np.zeros((Nepocs)) 
        intercept = np.zeros((Nepocs))
        for i in range(Nepocs):
            data = signals[i,:]
            pow , freq = self.resampled_spectral_analysis(data, fs)
            # flatten array
            pow = np.squeeze(pow); freq = np.squeeze(freq)
            # exclude lower boundary in case first_freq  = 0
            freqr = np.where((freq > first_freq) & (freq <= last_freq))
            beta[i], intercept[i] = np.polyfit(np.log(freq[freqr]), np.log(pow[freqr]), 1)
        
        beta = beta.reshape((len(beta), 1))
        intercept = intercept.reshape((len(intercept), 1))
        freqr = np.squeeze(freqr)

        # compute rythmic spectrum
        residu = np.exp((-intercept))*(freq_raw[freqr])**((-beta))*(psd_raw[:,freqr])
        residu_mean = np.mean(residu, axis = 0)
        return residu, residu_mean,  freq_raw[freqr], beta, intercept, freq_raw, psd_raw_mean
