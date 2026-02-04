"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    RnB
    Rhythmic and Background separation using wavelet decomposition
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from CEAMSModules.Stft.Stft import Stft

import numpy as np
from scipy.stats import median_abs_deviation
from scipy.special import zeta
import math
import scipy

from CEAMSModules.PSGReader import SignalModel as test

DEBUG = False

class RnB(SciNode):
    """
    RnBWavelet module for rhythmic and background signal separation
    
    Parameters
    -----------
        signals    : a list of SignalModel
                    signal.samples : The actual signal data as numpy list
                    signal.sample_rate : sampling rate of the signal
                    signal.channel : current channel label
        win_len_sec     : float
            window length in sec (how much data is taken for each analysis)
        win_step_sec    : float 
            window step in sec (each time the analysis is applied)
        alpha_param     : float
            Alpha parameter for spline wavelet regularity (default: 4)
        decomp_level    : int
            Number of wavelet decomposition levels (default: 8)
        
    Outputs:
        rhythmic_signal: list of dicts
            Rhythmic component of the signal
        background_signal: list of dicts
            Background (arrhythmic) component of the signal
        slope: list
            Beta values characterizing the arrhythmic spectrum for each epoch
    """
    def __init__(self, **kwargs):
        """ Initialize module RnB """
        super().__init__(**kwargs)
        if DEBUG: print('RnB.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('win_len_sec',self)
        InputPlug('win_step_sec',self)
        InputPlug('alpha_param',self)
        InputPlug('decomp_level',self)
        

        # Output plugs
        OutputPlug('rhythmic_signal',self)
        OutputPlug('background_signal',self)
        OutputPlug('slope',self)

        self._is_master = False 
    
    def compute(self, signals, win_len_sec=5, win_step_sec=5, alpha_param=4, decomp_level=8):
        """
        Compute the rhythmic and background separation for each epoch
        
        Parameters
        -----------
            signals    : a list of SignalModel
            win_len_sec     : float
                window length in sec
            win_step_sec    : float 
                window step in sec
            alpha_param     : float
                Alpha parameter for wavelet (default: 4)
            decomp_level    : int
                Decomposition levels (default: 8)
                
        Returns
        -----------
            rhythmic_signal : list of dicts
            background_signal : list of dicts
            slope : list of beta values
        """
        
        # Validate inputs
        if not isinstance(signals, list):
            raise NodeInputException(self.identifier, "signals", 
                f"RnBWavelet input of wrong type. Expected: <class 'list'> received: {type(signals)}")
        
        cache = {}
        
        win_len_sec = float(win_len_sec)
        win_step_sec = float(win_step_sec)
        alpha_param = float(alpha_param)
        decomp_level = int(decomp_level)
        
        # Get data
        fs = test.SignalModel.get_attribute(signals, 'sample_rate', None)
        # Define outputs
        rhythmic_output = []
        background_output = []
        # Split and stack signals
        for i, signal_model in enumerate(signals):
            sign2d_split, new_chan, start_time, end_time, new_dur = self.split_and_stack(signal_model, win_len_sec, fs)

            # Compute rhythmic and background separation
            result = self.extract_RnB_signals(sign2d_split, alpha_param, decomp_level)
            rhythmic_signals = result["rhythmic signal"]
            betas = result["slope (beta)"]
        
            # Compute background signal (original - rhythmic)
            background_signals = sign2d_split - rhythmic_signals

            # Recreate an array of (n, 1) for the input signals
            rhythmic_signals = rhythmic_signals.reshape(-1, 1)

            # Removing Nan values from rhythmic and background signals
            #rhythmic_signals = rhythmic_signals[~np.isnan(rhythmic_signals)]
            # Extract psd and freq bins of the rhythmic signal with the weltch method
            #freq_bins, psd_rhythmic = scipy.signal.welch(rhythmic_signals, fs=fs[i], nperseg=128, axis=-1)
            psd_rhythmic, freq_bins = Stft.fft_norm(self,
                                rhythmic_signals,
                                fs[i],
                                win_len_sec,
                                win_step_sec,
                                False,
                                'hann',
                                True,
                                'integrate')   
            # Extract psd and freq bins of the background signal with the weltch method
            #freq_bins, psd_background = scipy.signal.welch(background_signals, fs=fs[i], nperseg=128, axis=-1)
        
            rhythmic_data = {
                'psd': psd_rhythmic,
                'freq_bins' : freq_bins,
                'sample_rate': fs[i],
                'chan_label': new_chan[0],
                'start_time': start_time[0],
                'end_time': end_time[-1],
                'duration': sum(new_dur),
                'win_len': win_len_sec,
                'win_step': win_step_sec
            }
        
            '''background_data = {
                'psd': psd_background,
                'freq_bins' : freq_bins,
                'sample_rate': fs[i],
                'chan_label': new_chan[0],
                'start_time': start_time[0],
                'end_time': end_time[-1],
                'duration': sum(new_dur),
                'win_len': win_len_sec,
                'win_step': win_step_sec
            }'''

            '''# Write to cache
            cache['rhythmic_signal'] = rhythmic_signals
            cache['background_signal'] = background_signals
            cache['slope'] = betas
            cache['channel'] = signals[0].channel
            cache['sample_rate'] = signals[0].sample_rate
            self._cache_manager.write_mem_cache(self.identifier, cache)'''
        
            rhythmic_output.append(rhythmic_data.copy()) 
            #background_output.append(background_data.copy())
            
        return {
            'rhythmic_signal': rhythmic_output,
            'background_signal': background_output,
            'slope': betas.tolist()
        }

    def split_and_stack(self, signals, win_len_sec, fs):
        """Split data according to time and then stack it"""
        nsample = int(win_len_sec * fs[0])
        sign = np.asarray(signals.samples)
        remainder = sign.shape[0] % nsample
        
        if remainder > 0:
            if sign.shape[0] / 2 > nsample:
                col_keep = (sign.shape[0] // nsample) * nsample
                cols_to_cut = sign.shape[0] - col_keep
                sign = sign[:-cols_to_cut]
            else:
                col_keep = nsample
                cols_to_cut = sign.shape[0] - col_keep
                sign = sign[:-cols_to_cut]
        if remainder == 0:
            col_keep = sign.shape[0]

        cols_per_div = sign.shape[0] // nsample
        segments = np.split(sign, cols_per_div, axis=0)
        new_arr = np.vstack(segments)
        new_chan = np.repeat(np.asarray(signals.channel), cols_per_div)
        new_dur = np.repeat(np.asarray(win_len_sec), cols_per_div)

        startTime = signals.start_time
        time_array = np.empty((cols_per_div, 2))
        for j in range(cols_per_div):
            endTime = startTime + win_len_sec
            time_array[j, 0] = startTime
            time_array[j, 1] = endTime
            startTime = startTime + win_len_sec
        start_time = time_array[:, 0]
        end_time = time_array[:, 1]

        return new_arr, new_chan, start_time, end_time, new_dur


    def fractsplineautocorr(self,alpha, nu):

        N = 100
        if alpha <= -0.5:
            raise ValueError('The autocorrelation of the fractional splines exists only for degrees strictly larger than -0.5!')

        S = np.zeros_like(nu)

        err = []
        err0 = []
        for n in range(-N, N+1):
            S = S + np.abs(np.sinc(nu+n))**(2*alpha+2)


            U = 2/(2*alpha+1)/N**(2*alpha+1)
            U = U - 1/N**(2*alpha+2)
            U = U + (alpha+1)*(1/3+2*nu**2)/N**(2*alpha+3)
            U = U - (alpha+1)*(2*alpha+3)*nu**2/N**(2*alpha+4)
            U = U*np.abs(np.sin(np.pi*nu)/np.pi)**(2*alpha+2)

            A = S + U
            A = A.astype(float)

        return A


    def FFTfractsplinefilters(self,M, alpha, tau, typ):

        u = (alpha/2 - tau)
        v = (alpha/2 + tau)
        if alpha <= -0.5:
            raise ValueError('The autocorrelation of the fractional splines exists only for degrees strictly larger than -0.5!')
        
        # Adjust M to nearest power of 2 if needed
        if M != 2**np.round(np.log2(M)):
            M = int(2**np.ceil(np.log2(M)))

        nu = np.arange(0, 1, 1/M)
        A = self.fractsplineautocorr(alpha, nu)

        A2 = np.concatenate((A, A))
        A2 =A2[::2]  # A2(z) = A(z^2)

        if typ[0] == 'o' or typ[0] == 'O':
            # orthonormal spline filters
            lowa = np.sqrt(2) * ((1 + np.exp(2j * np.pi * nu)) / 2) ** (u + 0.5) * ((1 + np.exp(-2j * np.pi * nu)) / 2) ** (v + 0.5) * np.sqrt(A / A2)

            higha = np.exp(2j * np.pi * nu) * lowa
            higha = np.concatenate((np.conj(higha[M//2:M]), np.conj(higha[0:M//2])))

            lows = lowa
            highs = higha


            FFTanalysisfilters = np.vstack((lowa, higha))
            FFTsynthesisfilters = np.vstack((lows, highs))

            return FFTanalysisfilters,FFTsynthesisfilters
        else:
            # semi-orthonormal spline filters
            lowa = np.sqrt(2) * ((1 + np.exp(2j * np.pi * nu)) / 2) ** (u + 0.5) * ((1 + np.exp(-2j * np.pi * nu)) / 2) ** (v + 0.5)

            higha = np.exp(2j * np.pi * nu) * lowa * A
            higha = np.concatenate((higha[M // 2:], higha[:M // 2][::-1].conjugate()))

            lows = lowa * A / A2
            highs = higha / (A2 * np.concatenate((A[M // 2:], A[:M // 2])))

            if typ[0] == 'd' or typ[0] == 'D':
                # dual spline wavelets
                FFTanalysisfilters = np.vstack((lowa, higha))
                FFTsynthesisfilters = np.vstack((lows, highs))
            else:
                # B-spline wavelets
                if typ[0] == 'b' or typ[0] == 'B':
                    FFTsynthesisfilters = np.vstack((lowa, higha))
                    FFTanalysisfilters = np.vstack((lows, highs))
                else:
                    raise ValueError(f"'{typ}' is an unknown filter type!")


    def FFTwaveletsynthesis1D(self,w, FFTsynthesisfilters, J):
        M = len(w)

        if FFTsynthesisfilters.ndim == 1:
            num_cols = len(FFTsynthesisfilters)
        elif FFTsynthesisfilters.ndim == 2:
            num_rows, num_cols = FFTsynthesisfilters.shape

        # Adjust M to power of 2 if needed
        if M != 2**round(np.log2(M)):
            M_new = int(2**np.ceil(np.log2(M)))
            if M < M_new:
                w = np.pad(w, (0, M_new - M), mode='constant')
            else:
                w = w[:M_new]
            M = M_new

        # Adjust to match filter size if needed
        if num_cols != M:
            if M < num_cols:
                w = np.pad(w, (0, num_cols - M), mode='constant')
            else:
                w = w[:num_cols]
            M = num_cols

        # Reconstruction of the signal from its bandpass components
        G = np.conj(FFTsynthesisfilters[0,:])
        H = np.conj(FFTsynthesisfilters[1,:])

        M = int(M/2**J)
        y = w[-M:]
        w = w[:-M]
        Y = np.fft.fft(y,M)

        for j in range(J,0,-1):
            z = w[-M:]
            w = w[:-M]
            Z = np.fft.fft(z,M)
            M = 2*M

            H1 = H[::2**(j-1)]
            G1 = G[::2**(j-1)]

            Y0 = G1[:M//2]*Y + H1[:M//2]*Z
            Y1 = G1[M//2:]*Y + H1[M//2:]*Z
            Y = np.concatenate((Y0,Y1))

        x = np.real(np.fft.ifft(Y,M))

        return x        


    def FFTwaveletanalysis1D(self,x,FFTanalysisfilters,J):

        if FFTanalysisfilters.ndim == 1:
            num_cols = len(FFTanalysisfilters)
        elif FFTanalysisfilters.ndim == 2:
            num_rows, num_cols = FFTanalysisfilters.shape

        M = len(x)

        # Adjust M to power of 2 if needed
        if M != 2**round(np.log2(M)):
            M_new = int(2**np.ceil(np.log2(M)))
            if M < M_new:
                x = np.pad(x, (0, M_new - M), mode='constant')
            else:
                x = x[:M_new]
            M = M_new

        # Adjust to match filter size if needed
        if num_cols != M:
            if M < num_cols:
                x = np.pad(x, (0, num_cols - M), mode='constant')
            else:
                x = x[:num_cols]
            M = num_cols

        X = np.fft.fft(x,M)
        G=FFTanalysisfilters[0,:]
        H=FFTanalysisfilters[1,:]

        w = np.array([])  # Initialize w as an empty array
        for i in range(J):
        # Compute outputs Y and Z
            Y = G * X
            Z = H * X

        # Average corresponding parts of the signal
            half_M = int(M) // 2
            Y = 0.5 * (Y[:half_M] + Y[half_M:half_M * 2])
            Z = 0.5 * (Z[:half_M] + Z[half_M:half_M * 2])

        # Inverse FFT of Z and append to w
            z = np.fft.ifft(Z, half_M)
            w = np.concatenate((w, z)) if len(w) > 0 else z

        # Update variables for the next iteration
            M = half_M
            X = Y
            G = G[::2]
            H = H[::2]

    # Final concatenation of w and the real part of the inverse FFT of X
        u = np.fft.ifft(X, M)
        d = np.concatenate((np.real(w), np.real(u)))

        return d


    def soft_schrinkage(self,w, J):
        """
        Apply soft shrinkage on wavelets.

        Parameters:
            w: ndarray
                Wavelet coefficients.
            J: int
                Number of wavelet decomposition scales in w.

        Returns:
            wt: ndarray
                Shrinked wavelet coefficients.
            r: float
                Percentage of coefficients equal to zero.
        """
        def soft(x, l):
            return np.maximum(np.abs(x) - l, 0) * np.sign(x)
        
        jnoise = 1
        N = len(w)
        wt = []
        o = 0  # Start from 0 for Python indexing

        indices = []
        values = []
        levels = []

        for j in range(1, J + 1):
            N //= 2
            a = np.arange(o, o + N)
            o += N

            indices.extend(a)
            values.extend(w[a])
            levels.extend([j] * N)
        
        indices = np.array(indices)
        values = np.array(values)
        levels = np.array(levels)

        # Threshold for shrinkage:
        sigma = median_abs_deviation((values[levels == jnoise]))
        lambda_ = sigma * np.sqrt(2 * np.log(len(w)))

        # Shrinkage:
        nWt = soft(values, lambda_)
        r = 100 * np.sum(nWt == 0) / len(nWt)
        
        w[indices] = nWt  
        wt = w
        return wt, r


    def FracSplineAnal(self,s0,j12,alpha):

        if not alpha:
            alpha = 3

        tau   = 0
        typ  = 'ortho'
        M1    = len(s0)

        J = int(math.log2(M1))-1
        M2 = 2**int(J+1)
        FFTan,_ = self.FFTfractsplinefilters(int(M2),alpha,tau,typ)

        w  = self.FFTwaveletanalysis1D(s0,FFTan,J)
        w = np.array(w)
        beta = self.beta_estimator(w,J,[])
        return beta


    def beta_estimator(self,w,J,j12):

        N = int(len(w))
        o = int(0) 
        N0 = int(N)

        etatj = np.zeros(J)
        nj = np.zeros(J)
        Sj = np.zeros(J)
        jSj = np.zeros(J)
        j2Sj = np.zeros(J)
        eSj = np.zeros(J)
        jeSj = np.zeros(J)

        for i in range(J):
            N= int(N/2)
            a = np.arange(o, o+N)
            o=o+N
            nj[i] = np.size(a)
            etatj[i] = np.log2(np.sum(np.abs(w[a])**2)/nj[i])
            Sj[i] = N0*np.log(2)*np.log(2)/2/2**(i+1)
            jSj[i] = (i+1)*Sj[i]
            j2Sj[i] = (i+1)*jSj[i]
            eSj[i] = etatj[i]*Sj[i]
            jeSj[i] = (i+1)*eSj[i]


            #double check len
        if len(j12) == 0:
            j1 = 1
            j2 = J-2
        else:
            j1 = 1
            j2 = 4

        beta = (np.sum(Sj[j1:j2])*sum(jeSj[j1:j2]) - sum(jSj[j1:j2])*sum(eSj[j1:j2]))/(sum(Sj[j1:j2])*sum(j2Sj[j1:j2]) - sum(jSj[j1:j2])*sum(jSj[j1:j2]))
        
        return beta
    

    def wavelet_indices(self, N, J, alpha0, tau, typ):

    # Filtre de synthese de l'ondelette de reconstruction
        _, FFTsynthesisfilters = self.FFTfractsplinefilters(N, alpha0, tau, typ)
    # debut (a) et fin (b) des segments d'echelle dans la repersentation en
    # ondelette
        a = np.zeros(J+1, dtype=int)
        nj = np.zeros(J+1, dtype=int)
        b = np.zeros(J+1, dtype=int)

        # Initialize the first elements
        a[0] = 0  # Starts at 0 for Python
        nj[0] = N / 2
        b[0] = a[0] + nj[0] - 1

        # Loop through indices from 1 to J (inclusive)
        for i in range(1, J + 1):
            a[i] = a[i - 1] + nj[i - 1]
            nj[i] = nj[i - 1] / 2
            b[i] = a[i] + nj[i] - 1

        return a, b


    def K(self,b, a):
    
        kappa = (4 * math.pi) ** b
        u = 2 ** (a + 1) - 1
        v = 2 ** (a + b + 1) - 1
        w = zeta(a + 1) / zeta(a + b + 1)
        kappa = kappa * u / v * w
        
        return kappa


    def extract_RnB_signals(self, s, alpha0=4, J=8):
        """Extract rhythmic and background signals using wavelet decomposition"""
        
        if s.ndim == 1:
            s = s[np.newaxis, :]  # Convert to 2D with shape (1, N)
        Nepo, N = s.shape 
        
        # Store original signal length for truncation after reconstruction
        N_original = N
        
        # Other wavelet parameters
        tau = 0
        typ = 'ortho'
        
        # Synthesis filter for reconstruction wavelet (may pad N to power of 2)
        _, FFTsynthesisfilters = self.FFTfractsplinefilters(N, alpha0, tau, typ)
        
        # Get the actual size used (after potential padding)
        N_padded = FFTsynthesisfilters.shape[1]

        a, b = self.wavelet_indices(N_padded, J, alpha0, tau, typ)

        betas = np.zeros(Nepo)  # Array to store beta values for each signal
        sR = np.zeros((Nepo, N_original))  # Use original size
        
        for isignal in range(Nepo):
            # Signal output
            se = np.array([s[isignal]])
            # Normalization
            nh = np.sqrt(np.dot(se, se.T))  
            sh = se / nh 
            # Beta estimation (wavelet estimator)
            se = np.ravel(se)
            sh = np.ravel(sh)

            BETA = self.FracSplineAnal(se, [], alpha0)

            # Alpha parameter for the epoch
            alpha = BETA / 2
            # Analysis filters
            FFTanalysisfilters, _ = self.FFTfractsplinefilters(N_padded, alpha0 + alpha, tau, typ)

            # Analysis
            w = self.FFTwaveletanalysis1D(sh, FFTanalysisfilters, J)

            # Denoising (soft shrinkage): keeps only 'strong' coefficients (associated with rhythms)
            w = self.soft_schrinkage(w, J)
            w = w[0]

            # Reconstruction (exclude scaling part; keep only wavelet coefficients)
            wr = np.zeros_like(w)

            # Filtering
            for i in range(J):
                aWj = w[int(a[i]):int(b[i]+1)]  # Python 0-based indexing with exclusive end
                aWp = self.K(alpha, alpha0) * 2 ** (-i * alpha) * aWj
                wr[int(a[i]):int(b[i]+1)] = aWp

            # Reconstruct signal (may be padded size)
            reconstructed = self.FFTwaveletsynthesis1D(wr, FFTsynthesisfilters, J)
            
            # Truncate to original size and denormalize
            sR[isignal] = reconstructed[:N_original] * nh

            betas[isignal] = BETA

        return {
            "rhythmic signal": sR,
            "slope (beta)": betas
        }
