"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
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
from scipy.signal import resample_poly, periodogram, welch
from scipy.optimize import curve_fit
from joblib import Parallel, delayed
import matplotlib.pyplot as plt

from CEAMSModules.PSGReader import SignalModel as test

# Import the FOOOF object
from fooof import FOOOF
import yasa
# Import some internal functions
#   These are used here to demonstrate the algorithm
#   You do not need to import these functions for standard usage of the module
from fooof.sim.gen import gen_aperiodic
from fooof.plts.spectra import plot_spectra
from fooof.plts.annotate import plot_annotated_peak_search

# Import a utility to download and load example data
from fooof.utils.download import load_fooof_data

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
        InputPlug('flag',self) # flag to choose between rythmic spectral analysis (True) and FOOOF (False)

        # Output plugs
        OutputPlug('psd',self)
        OutputPlug('slope',self)
        OutputPlug('intercept',self)
        
        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    

    def compute(self, signals, win_len_sec, win_step_sec, window_name,first_freq,last_freq, flag=True):
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
        psd = []
        # get data and split and stack accordingly
        for i, signal_model in enumerate(signals):
            sign2d_split, new_chan, start_time, end_time, new_dur = self.split_and_stack(signal_model, win_len_sec, fs)
            # compute rythmic spectral analysis
            if flag:
                residu, freq_bins = self.rhythmic_FOOOF(sign2d_split, fs, first_freq, last_freq, window_name)
            else:
                #residu, psd_aperiodic, freq_bins  = self.IRASA(sign2d_split, fs,first_freq,last_freq, window_name, window_sec=win_len_sec, new_chan=new_chan)
                residu, res_mean, freq_bins,intercept,beta,freq_raw, psd_raw  = self.rythmic_spectral_analysis(sign2d_split, fs,first_freq,last_freq, window_name)
            # Define output
            data = {}
            data['psd'] = residu
            data['freq_bins'] = freq_bins
            data['win_len'] = win_len_sec
            data['win_step'] = win_step_sec
            data['sample_rate'] = fs[i]
            data['chan_label'] = new_chan[0]
            data['start_time'] = start_time[0]
            data['end_time'] = end_time[-1]
            data['duration'] = sum(new_dur)

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
    
    
    def raw_spectral_analysis(self, signals, fs, window_name, nfft=None):
        """ Compute the raw PSD using scipy.signal.welch with the same parameters
        that yasa.irasa uses internally, so that the raw PSD and the IRASA
        aperiodic/periodic spectra share the exact same frequency grid.

        Parameters
        -----------
        signals        : Array (Nepocs X time)
        fs             : float
            Sampling frequency (Hz)
        window_name    : str
            Window passed to scipy.signal.welch (e.g. 'hamming').
        nfft           : int or None
            FFT length. If None, uses n_samples (no zero-padding).
            To match yasa.irasa, pass ``int(n_samples * hset.max())``.

        Returns
        -----------
        psd_data        : ndarray [Nepocs x n_freqs]
            Power spectrum of the signal (scaling='spectrum', uV^2).
        freq_bins       : ndarray
            The frequency bins array (Hz)

        Usage : psd_data, freq_bins = compute(ts_signal, 100)
        """
        fs = fs[0]

        _, n = signals.shape
        nperseg = n
        if nfft is None:
            nfft = n

        # Mirror yasa.irasa: median-averaged Welch with the same window,
        # nperseg and nfft. When the signal length equals nperseg this is a
        # single windowed FFT (and 'average' is a no-op), which matches what
        # the IRASA wrapper sees when it processes one epoch at a time.
        freq_bins, psd_data = welch(
            signals, fs=fs, window=window_name, nperseg=nperseg, nfft=nfft,
            scaling='spectrum', detrend=False, average='median', axis=1,
        )

        return psd_data, freq_bins


    def resampled_spectral_analysis(self, signals, fs, last_freq, window_name,
                                    hset=None, nfft=None):
        """Compute the IRASA aperiodic PSD estimate using scipy.signal.welch
        on the h / 1/h resamplings, with the same parameters that
        ``yasa.irasa`` uses internally.

        Parameters
        -----------
        signals     : 1D ndarray
            A single epoch of the signal.
        fs          : list or tuple of float
            ``fs[0]`` is the sampling frequency (Hz).
        last_freq   : float
            Upper bound of the frequency range of interest. Kept for API
            compatibility; cropping to the band is done by the caller so that
            the aperiodic fit is computed on the same points yasa.irasa uses.
        window_name : str
            Window passed to scipy.signal.welch (e.g. 'hamming').
        hset        : 1D array_like or None
            Resampling factors. Defaults to ``np.arange(1.05, 1.75, 0.03)``.
        nfft        : int or None
            FFT length. Defaults to ``int(Npoints * hset.max())``. Pass the
            same value used by ``raw_spectral_analysis`` so the raw and
            aperiodic spectra share the exact same frequency grid.

        Returns
        -----------
        psd_aperiodic : 1D ndarray
            Aperiodic (fractal) power spectrum on ``freq_bins``.
        freq_bins     : 1D ndarray
            Frequency grid (Hz), identical to the one produced by
            ``scipy.signal.welch(..., fs=fs, nfft=nfft)``.
        """
        fs = fs[0]
        Npoints = len(signals)
        nperseg = Npoints

        if hset is None:
            hset = np.arange(1.05, 1.75, 0.03)
        # Round to 4 decimals like yasa.irasa to avoid float-precision issues
        # with np.arange and to get clean Fraction(str(h)) ratios (e.g. 21/20).
        hset = np.round(np.asarray(hset, dtype=float), 4)
        nscale = len(hset)

        if nfft is None:
            nfft = int(Npoints * hset.max())

        # Single frequency grid, built the way scipy.signal.welch builds it,
        # so the caller can align psd_raw and psd_aperiodic bin-for-bin.
        freq_full = np.fft.rfftfreq(nfft, d=1.0 / fs)
        Nfrac = freq_full.size

        pow_up = np.full((nscale, Nfrac), np.nan)
        pow_dw = np.full((nscale, Nfrac), np.nan)

        for i, h in enumerate(hset):
            # Exact rational representation from the decimal string, matching
            # yasa.irasa's Fraction(str(h)). For values like 1.05 this gives
            # 21/20 instead of an approximation of the binary float.
            rat = Fraction(str(float(h)))
            up, dw = rat.numerator, rat.denominator

            sig_up = resample_poly(signals, up, dw)
            sig_dw = resample_poly(signals, dw, up)

            _, psd_up = welch(
                sig_up, fs=fs * h, window=window_name, nperseg=nperseg,
                nfft=nfft, scaling='spectrum', detrend=False, average='median',
            )
            _, psd_dw = welch(
                sig_dw, fs=fs / h, window=window_name, nperseg=nperseg,
                nfft=nfft, scaling='spectrum', detrend=False, average='median',
            )

            pow_up[i, :] = psd_up
            pow_dw[i, :] = psd_dw

        # Geometric mean of the up/down pair for each h, then median across h.
        # Algebraically identical to yasa's
        #   psd_aperiodic = median(sqrt(psd_up * psd_dw), axis=0)
        psd_aperiodic = np.nanmedian(np.sqrt(pow_up * pow_dw), axis=0)

        return psd_aperiodic, freq_full


    def _process_single_epoch(self, data, fs, first_freq, last_freq, window_name,
                              hset=None, nfft=None):
        """Process a single epoch for parallel computation.

        Fits the IRASA aperiodic PSD with the same semilog model
        (``log(psd) = a + b*log(f)``) and the same slope bounds
        (``b in [-10, 2]``) as ``yasa.irasa``.
        """
        if np.any(np.isnan(data)):
            return np.nan, np.nan

        try:
            pow_ap, freq = self.resampled_spectral_analysis(
                data, fs, last_freq, window_name, hset=hset, nfft=nfft,
            )
            pow_ap = np.squeeze(pow_ap)
            freq = np.squeeze(freq)

            # Inclusive band mask like yasa.irasa (masked_outside), but also
            # drop the 0 Hz bin. yasa.irasa asserts band[0] > 0 at entry so
            # it can safely be inclusive; here `first_freq` is user input, so
            # we exclude f=0 explicitly to avoid log(0) in the fit and
            # 0**(-beta)=0 when evaluating the aperiodic power law.
            freqr = np.where((freq >= first_freq) & (freq <= last_freq) & (freq > 0))
            freq_subset = freq[freqr]
            pow_subset = pow_ap[freqr]

            if len(freq_subset) == 0 or len(pow_subset) == 0:
                return np.nan, np.nan

            if np.any(np.isnan(freq_subset)) or np.any(np.isnan(pow_subset)) or \
               np.any(freq_subset <= 0) or np.any(pow_subset <= 0):
                return np.nan, np.nan

            # YASA's aperiodic model (see yasa.spectral.irasa):
            #   func(f, a, b) = a + log(f**b) = a + b*log(f)
            # fit against log(psd_aperiodic), with slope bounded to [-10, 2].
            def _aperiodic_model(t, a, b):
                return a + np.log(t ** b)

            popt, _ = curve_fit(
                _aperiodic_model, freq_subset, np.log(pow_subset),
                p0=(2.0, -1.0),
                bounds=((-np.inf, -10.0), (np.inf, 2.0)),
            )
            intercept_val, beta_val = popt[0], popt[1]
            return beta_val, intercept_val

        except Exception:
            return np.nan, np.nan

    def rythmic_spectral_analysis(self, signals, fs, first_freq, last_freq, window_name):
        """IRASA-style rhythmic spectrum, aligned with ``yasa.irasa``.

        Uses scipy.signal.welch with the same window, nperseg, nfft, averaging
        and detrending as ``yasa.irasa``; exact Fraction(str(h)) resampling
        ratios; an inclusive [first_freq, last_freq] band; and a bounded
        semilog fit of the aperiodic component. The residu is the raw PSD
        divided by the aperiodic power-law fit.
        """
        Nepocs, Npoints = signals.shape

        # Single nfft shared by the raw PSD and every resampled PSD, so all
        # spectra live on the exact same frequency grid (same rule as
        # yasa.irasa when kwargs_welch=dict(nfft=...)).
        hset = np.round(np.arange(1.05, 1.75, 0.03), 4)
        fixed_nfft = int(Npoints * hset.max())

        psd_raw, freq_raw = self.raw_spectral_analysis(
            signals, fs, window_name, nfft=fixed_nfft,
        )
        psd_raw_mean = np.nanmean(psd_raw, axis=0)

        results = Parallel(n_jobs=-1, backend='threading')(
            delayed(self._process_single_epoch)(
                signals[i, :], fs, first_freq, last_freq, window_name,
                hset=hset, nfft=fixed_nfft,
            )
            for i in range(Nepocs)
        )

        beta = np.array([r[0] for r in results]).reshape(-1, 1)
        intercept = np.array([r[1] for r in results]).reshape(-1, 1)

        # Inclusive band mask like yasa.irasa (masked_outside), but also
        # drop the 0 Hz bin so that (freq_raw[0])**(-beta) == 0**positive
        # doesn't force the DC column of `residu` to exactly 0 for every
        # epoch when `first_freq == 0`. yasa.irasa avoids this via its
        # ``assert band[0] > 0``; we enforce the same invariant here.
        freqr = np.where(
            (freq_raw >= first_freq) & (freq_raw <= last_freq) & (freq_raw > 0)
        )
        freqr = np.squeeze(freqr)

        # aperiodic_fit(f) = exp(intercept) * f**beta   (beta<0 for 1/f)
        # residu = psd_raw / aperiodic_fit
        residu = np.exp(-intercept) * (freq_raw[freqr]) ** (-beta) * (psd_raw[:, freqr])
        residu_mean = np.nanmean(residu, axis=0)

        return residu, residu_mean, freq_raw[freqr], beta, intercept, freq_raw, psd_raw_mean
    
    def rhythmic_FOOOF(self, signals, fs, first_freq, last_freq, window_name):
        
        psd_raw, freq_raw = self.raw_spectral_analysis(signals, fs, window_name)
        # FOOOF excludes 0 Hz, so we need to skip it in our arrays too
        # Initialize array for rhythmic spectra (excluding 0 Hz)
        Sf = (len(freq_raw) - 1) / freq_raw[-1]  # Sampling frequency for FOOOF (based on max frequency)
        num_freq_sample = (int(Sf * last_freq))
        spectrum_array = np.zeros((psd_raw.shape[0], num_freq_sample))
        
        # Fit each epoch separately to extract rhythmic component
        for i in range(psd_raw.shape[0]):
            if np.isnan(psd_raw[i, :]).any():
                spectrum_array[i, :] = np.full(num_freq_sample, np.nan)
            else:
                # Initialize FOOOF with appropriate settings
                fm = FOOOF(peak_width_limits=[1, 8], max_n_peaks=6, min_peak_height=0.15)
                # Fit the model - FOOOF works in log-log space internally
                # FOOOF will skip 0 Hz internally
                fm.fit(freq_raw, psd_raw[i, :], [first_freq, last_freq])
                # Generate aperiodic fit in LINEAR space using fitted parameters
                # fm.freqs excludes 0 Hz, so ap_fit has length len(freq_raw) - 1
                ap_fit = gen_aperiodic(fm.freqs, fm._robust_ap_fit(fm.freqs, np.log(psd_raw[i, :num_freq_sample])))
                # Rhythmic component: Subtract aperiodic fit from original spectrum
                rhythmic_spectrum = np.log(psd_raw[i, :num_freq_sample]) - ap_fit
                spectrum_array[i, :] = rhythmic_spectrum
        # Return frequencies excluding 0 Hz to match spectrum_array dimensions
        return spectrum_array, fm.freqs

    def IRASA(self, signals, fs, first_freq, last_freq, window_name, window_sec, new_chan):
        # Apply the IRASA technique
        fs = fs[0]  # Use the first sampling rate (assuming all are the same)
        n_epochs = signals.shape[0]
        n_samples = signals.shape[1]  # Number of samples per epoch
        # define scale
        scale = np.arange(1.05, 1.75, 0.03)
        # Use fixed nfft for all scales to ensure consistent frequency grids
        fixed_nfft = int(n_samples * scale[-1])
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
                band=(first_freq, last_freq), hset=scale, win_sec=window_sec, return_fit=True,
                kwargs_welch=dict(average="median", window=window_name, nfft=fixed_nfft, scaling='spectrum', detrend=False)
            )
            freqs_i = np.asarray(irasa_result[0])
            aperiodic_i = np.asarray(irasa_result[1])
            periodic_i = np.asarray(irasa_result[2])
            residu_i = np.exp((-irasa_result[3]['Intercept'][0])) * (freqs_i)**((-irasa_result[3]['Slope'][0])) * (aperiodic_i + periodic_i)
            
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
            if r_i.shape[1] > 0:
                residu_array[i, :r_i.shape[1]] = r_i

        # Compute ratio-style residu to match rhythmic_spectral_analysis output
        # residu = (aperiodic + periodic) / aperiodic = 1 + (periodic / aperiodic)
        with np.errstate(divide='ignore', invalid='ignore'):
            residu = (aperiodic_array + periodic_array) / aperiodic_array
            residu[~np.isfinite(residu)] = np.nan  # Handle division by zero or invalid values
        
        return residu_array, aperiodic_array, freqs