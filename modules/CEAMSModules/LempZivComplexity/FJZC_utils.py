"""
FJZC_utils.py
=============
Normalized Fourier-surrogate Lempel-Ziv complexity for EEG (Snooz).

Scientific provenance
---------------------
* Lempel-Ziv complexity (phrase count):
    Lempel & Ziv (1976); Kaspar & Schuster, Phys. Rev. A, 1987.
* Joint / multidimensional LZC (mode='joint'):
    Zozor, Ravier & Buttelli, Physica A 345:285-302, 2005.
* Concatenated multivariate LZC (mode='concat'):
    Schartner et al., PLoS One, 2015.
* EEG preprocessing + FT-surrogate normalization used here:
    Toker et al., PNAS 2022
    ("Consciousness is supported by near-critical slow cortical electrodynamics").
  Modes matching Toker:
    - 'univariate': LZC per channel (array); median across channels is
      also reported as Toker's univariate summary
    - 'joint': Zozor joint LZC (all channels together)
    - 'concat': Schartner concatenation into one string
* Surrogate generators (FT and others):
    Lancaster, Iatsenko et al., Physics Reports, 2018
    (see license header on surrogate()).

Why C via ctypes?
---------------------------------------------
The LZ scan is ~O(nt^2). Pure Python is too slow for sleep / hd-EEG.
That loop is already compiled C (calculate_complexity.c), shipped in files/
for each supported platform:
    Windows x86_64       calculate_complexity_64.dll
    Linux x86_64         calculate_complexity_64.so
    macOS Intel x86_64   calculate_complexity_x86_64.dylib
    macOS Apple Silicon  calculate_complexity_arm64.dylib
_load_lib() picks the one matching the running Python process. 
Window-level speedup uses joblib.(same pattern as AECConnectivity / DpliConnectivity).

Joint packing / automatic grouping
----------------------------------
Zozor packing encodes binary channels as one integer per time point.
IEEE-754 doubles only represent integers uniquely up to 2^53, so we pack
at most MAX_CH_PER_GROUP (=50) channels per group and require all groups
to match (see complexity_joint in the C file). 

IMPORTANT (hd-EEG / joint mode)
-------------------------------
True joint LZC saturates when the joint alphabet is huge relative to the
epoch length: with many channels, almost every time point is a new joint
state, so LZC(data) ≈ LZC(surrogate) ≈ n_times and the normalized ratio
→ ~1. This is expected mathematics, not a grouping bug. Prefer
mode='univariate' (or joint on a smaller channel subset) for dense EEG.
"""

import numpy as np
from scipy.signal import detrend
from scipy.signal import hilbert
from scipy.fft import fft
from scipy.fft import ifft
from scipy.signal import find_peaks
from joblib import Parallel, delayed
from commons.parallel_utils import normalize_n_jobs, select_joblib_backend
import ctypes
import os
import platform
import struct


    
# Must match MAX_CH_PER_GROUP in calculate_complexity.c
MAX_CH_PER_GROUP = 50

# Compiled calculate_complexity.c for each (operating system, CPU architecture)
# pair, as named by the build workflow of the lzc_complexity repository.
_LIB_NAMES = {
    ('Windows', 'x86_64'): 'calculate_complexity_64.dll',
    ('Linux', 'x86_64'): 'calculate_complexity_64.so',
    ('Darwin', 'x86_64'): 'calculate_complexity_x86_64.dylib',
    ('Darwin', 'arm64'): 'calculate_complexity_arm64.dylib',
}

# platform.machine() spelling differs between operating systems.
_MACHINE_ALIASES = {
    'amd64': 'x86_64',
    'x86_64': 'x86_64',
    'x64': 'x86_64',
    'arm64': 'arm64',
    'aarch64': 'arm64',
}

# Cached ctypes handle to the complexity library
_LIB = None


def _files_dir():
    """Directory that holds calculate_complexity.c and its compiled libraries."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')


def _lib_filename():
    """
    Return the name of the compiled library matching the running Python.

    The architecture of the Python process is used, not the one of the
    computer : an Intel Python running through Rosetta on Apple Silicon must
    load the x86_64 library.
    """
    system = platform.system()
    machine = platform.machine().lower()
    machine = _MACHINE_ALIASES.get(machine, machine)
    if struct.calcsize('P') != 8:
        raise OSError(
            'The complexity library requires a 64-bit Python; '
            f'running a {struct.calcsize("P") * 8}-bit Python on {system}.'
        )
    lib_name = _LIB_NAMES.get((system, machine))
    if lib_name is None:
        supported = ', '.join(f'{s} {m}' for s, m in _LIB_NAMES)
        raise OSError(
            f'No compiled complexity library for {system} {machine}. '
            f'Supported platforms: {supported}.'
        )
    return lib_name


def _load_lib():
    """
    Load the complexity library of the current platform once and cache it.

    Path is based on __file__ so it works from Snooz packages, not only
    when the process CWD is the pipeline root (unlike './files/...').
    """
    global _LIB
    if _LIB is not None:
        return _LIB

    lib_path = os.path.abspath(os.path.join(_files_dir(), _lib_filename()))
    if not os.path.isfile(lib_path):
        raise FileNotFoundError(
            f'Complexity library not found: {lib_path}. '
            'Build calculate_complexity.c for this platform with the '
            'lzc_complexity workflow and copy it into the files folder.'
        )
    try:
        # Absolute path is required: ctypes looks next to the Python
        # executable when a relative path is given.
        _LIB = ctypes.CDLL(lib_path)
    except OSError as e:
        hint = ''
        if platform.system() == 'Darwin':
            # Files downloaded through a browser are quarantined by Gatekeeper.
            hint = f' On macOS, try: xattr -d com.apple.quarantine "{lib_path}"'
        raise OSError(
            f'Complexity library could not be loaded: {lib_path} ({e}).{hint}'
        )
    return _LIB


def bsxfun_minus(matrix):
    """
    Subtract each channel's mean (MATLAB-style bsxfun demean).

    Used after detrend, before Hilbert, following Toker / fJLZC.m.
    """
    B = np.zeros((matrix.shape))
    for row in range(matrix.shape[0]):
        B[row, :] = matrix[row, :] - np.mean(matrix[row, :])
    return B


def bsxfun_greater(A):
    """
    Binarize each channel by thresholding at that channel's mean.

    Toker: threshold = mean of instantaneous Hilbert amplitude.
    Output is 0/1 (int), later cast to float64 for the C API.
    """
    B = (A > A.mean(axis=1, keepdims=True)).astype(np.int32)
    return B


def JoinDisc(M, alpha=2):
    """
    Zozor joint discretization in pure Python (reference / fallback).

    Same math as C multi_uni: at each time, sum binary_ch * alpha^ch.
    Production FJZC uses the C path instead of this function.
    """
    Nc, Ns = M.shape
    Xjd = []
    for itime in range(Ns):
        r = 0
        for ch in range(Nc):
            Xv = M[ch, itime]
            if Xv == 1:
                r += (alpha ** ch)
        Xjd.append(r)
    return Xjd, Nc


# Authors: Dmytro Iatsenko & Gemma Lancaster
# This software accompanies the article "Surrogate data for hypothesis
# testing in physical systems", G. Lancaster, D. Iatsenko, A. Pidde,
# V. Ticcinelli and A. Stefanovska. Physics Reports, 2018.
#
# Bug reports, suggestions and comments are welcome. Please email them to
# physics-biomed@lancaster.ac.uk
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# surrogate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# See <http://www.gnu.org/licenses/>.
def surrogate(sig, N, method, fs):
    """
    Generate N surrogate copies of a 1D signal.

    FJZC only needs method='FT' (phase-randomized Fourier transform):
    keep the amplitude spectrum, randomize phases, inverse FFT.
    That destroys temporal structure while preserving the power spectrum,
    which is Toker's null for normalizing LZC (following Brito et al.).

    Other methods (RP, AAFT, tshift, CSS) are kept from Lancaster et al.
    for completeness but are not used by FJZC().
    """
    L = np.max(sig.shape)
    L2 = int(np.ceil(L / 2))

    if method == 'RP':
        # Random permutation of samples (destroys all temporal structure).
        surr = np.zeros((N, np.max(sig.shape)))
        for k in range(N):
            surr[k, :] = sig[np.random.permutation(np.arange(L))]

    elif method == 'FT':
        # Phase-randomized FT surrogate (used by Toker / FJZC).
        a = 0
        b = 2 * np.pi
        eta = (b - a) * np.random.rand(N, L2 - 1).astype(np.float64)
        ftsig = fft(sig)
        ftrp = np.zeros((N, np.max(ftsig.shape))).astype(np.complex128)
        ftrp[:, 0] = ftsig[0]
        F = ftsig[1:L2]
        if len(F.shape) == 1:
            F = np.expand_dims(F, 0)
        F = F[np.zeros(N).astype(np.int32), :]
        ftrp[:, 1:L2] = F * (np.exp(1j * eta))
        # Hermitian symmetry so the inverse FFT is real-valued.
        ftrp[:, 1 + L - L2:] = np.conj(np.fliplr(ftrp[:, 1:L2]))
        surr = np.real(ifft(ftrp, axis=1))

    elif method == 'AAFT':
        # Amplitude-adjusted FT surrogate.
        a = 0
        b = 2 * np.pi
        eta = (b - a) * np.random.rand(N, L2 - 1)
        val = np.sort(sig)
        ind = np.argsort(sig)
        rankind = np.zeros_like(ind)
        rankind[ind] = np.arange(L)

        gn = np.sort(np.random.randn(N, np.max(sig.shape)))
        for j in range(N):
            gn[j, :] = gn[j, rankind]

        ftgn = fft(gn)
        F = ftgn[:, 1:L2]

        surr = np.zeros((N, np.max(sig.shape))).astype(np.complex128)
        surr[:, 0] = gn[:, 0]
        surr[:, 1:L2] = F * (np.exp(1j * eta))
        surr[:, 1 + L - L2:] = np.conj(np.fliplr(surr[:, 1:L2]))
        surr = np.real(ifft(surr, axis=1)).astype(np.float32)

        ind2 = np.argsort(surr)
        rrank = np.zeros((L))
        for k in range(N):
            rrank[ind2[k, :]] = np.arange(L)
            surr[k, :] = val[rrank.astype(np.int32)]

    elif method == 'tshift':
        # Circular time shift.
        surr = np.zeros((N, np.max(sig.shape)))
        for sn in range(N):
            startp = np.random.randint(1, high=L - 1)
            surr[sn, :] = np.concatenate((sig[startp:], sig[:startp]))

    elif method == 'CSS':
        # Cycle-shuffled surrogate (peak-segment permutation).
        MPH = 0
        MPD = fs
        inds = find_peaks(sig, height=MPH, distance=MPD)[0]
        st = sig[:inds[0]]
        en = sig[inds[-1]:]
        surr = np.zeros((N, np.max(sig.shape)))

        parts = {}
        for i in range(len(inds) - 1):
            parts[i] = sig[inds[i]:inds[i + 1]]

        for k in range(N):
            surr[k, :] = np.unwrap(np.concatenate(
                ([st]
                 + [parts[randi] for randi in np.random.permutation(len(inds) - 1)]
                 + [en])))

    else:
        raise Exception("mehod should be one of ['RP', 'FT', 'AAFT','tshift', 'CSS']")

    return surr


# def multi_uni(signal, al=2):
#     """
#     Python wrapper around JoinDisc for the slow pure-Python complexity().
#     Production code uses C multi_uni via the DLL instead.
#     """
#     if len(signal.shape) == 2:
#         sig = JoinDisc(signal, alpha=al)
#     elif len(signal.shape) == 1:
#         sig = list(signal.copy())
#     else:
#         raise Exception('not proper input')
#     return sig


# def complexity(sequence, alpha=2):
#     """
#     Pure-Python Kaspar-Schuster Lempel-Ziv (reference implementation).

#     Same logic as C complexity(), but far slower. Kept for debugging /
#     education. Prefer the DLL for real analyses.
#     """
#     if type(sequence) != list:
#         sequence = multi_uni(sequence, al=2)
#     nt = len(sequence)

#     l = 1
#     m = 1
#     c = 1.0
#     i = 0
#     k = 1
#     kmax = 1

#     while (1):
#         if sequence[i + k - 1] == sequence[l + k - 1]:
#             k += 1
#             if l + k > nt:
#                 c += 1.0
#                 break
#             else:
#                 continue
#         else:
#             if k > kmax:
#                 kmax = k
#             i += 1
#             if i == l:
#                 c += 1.0
#                 m += 1
#                 l += kmax
#                 if l + 1 > nt:
#                     break
#                 else:
#                     i = 0
#                     k = 1
#                     kmax = 1
#                     continue
#             else:
#                 k = 1
#                 continue

#     return c


def _call_complexity_1d(lib, bin_data):
    """
    ctypes wrapper for C complexity().

    bin_data must be C-contiguous float64 with shape (nc, nt).
    Used for concat (after reshape to 1 x n_samples) and for any
    single packed series path.
    """
    bin_data = np.ascontiguousarray(bin_data, dtype=np.float64)
    nc, nt = bin_data.shape
    # Workspace for the packed scalar series inside C.
    sig = (ctypes.c_double * nt)()
    out = ctypes.c_double()

    fn = lib.complexity
    fn.argtypes = [
        ctypes.c_int,   # nc
        ctypes.c_int,   # nt
        np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),
        ctypes.c_double,  # alphabet size (2)
        ctypes.POINTER(ctypes.c_double),  # sig workspace
        ctypes.POINTER(ctypes.c_double),  # output c
    ]
    fn.restype = None
    fn(nc, nt, bin_data, 2.0, sig, ctypes.byref(out))
    return out.value


def _call_complexity_joint(lib, bin_data):
    """
    ctypes wrapper for C complexity_joint().

    Automatically uses n_groups = ceil(nc / MAX_CH_PER_GROUP) inside C.
    No Python-side channel splitting needed (unlike the old hd / hd2 API).
    """
    bin_data = np.ascontiguousarray(bin_data, dtype=np.float64)
    nc, nt = bin_data.shape
    out = ctypes.c_double()

    fn = lib.complexity_joint
    fn.argtypes = [
        ctypes.c_int,   # nc
        ctypes.c_int,   # nt
        np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),
        ctypes.c_double,  # alphabet size (2)
        ctypes.POINTER(ctypes.c_double),  # output c
    ]
    fn.restype = None
    fn(nc, nt, bin_data, 2.0, ctypes.byref(out))
    return out.value


def FJZC(signal, info, mode='joint'):
    """
    Normalized Lempel-Ziv complexity for one window (Toker-style).

    Parameters
    ----------
    signal : ndarray, shape (n_channels, n_times)
        Continuous EEG for one window.
    info : dict
        Must contain 'sampling_frequency' (used by FT surrogates).
    mode : {'joint', 'concat', 'univariate'}
        'joint'      - Zozor joint LZC across channels (default).
        'concat'     - Schartner concatenation into one binary string.
        'univariate' - LZC per channel (one value per channel).

    Returns
    -------
    float
        For 'joint' / 'concat':
            norm_LZC = LZC(data) / LZC(FT surrogate).
    ndarray, shape (n_channels,)
        For 'univariate':
            per-channel norm_LZC_ch = LZC_ch / LZC_ch_surrogate.
            Toker's paper summary is median(this array); that median is
            computed in FJZC_parallel (and can be recomputed by the caller).

    Pipeline (same as Toker fJLZC.m)
    --------------------------------
    1. Build one FT surrogate per channel (Lancaster).
    2. On data and surrogate: detrend -> demean -> |Hilbert| ->
       threshold at channel mean -> binary matrix.
    3. Run C LZC (joint / concat / per-channel) on both binaries.
    4. Return the ratio (or per-channel ratios for univariate).
    """
    if mode not in ('joint', 'concat', 'univariate'):
        raise Exception(
            'complexity mode is not defined! '
            'It should be "joint", "concat", or "univariate"'
        )

    num_channels = signal.shape[0]
    fs = info['sampling_frequency']

    # --- Null model: phase-randomized surrogate, independently per channel ---
    rand_data = np.zeros_like(signal)
    for ch in range(num_channels):
        rand_data[ch, :] = surrogate(signal[ch, :], 1, 'FT', fs)

    # --- Toker binarization on the real signal ---
    data = detrend(signal)
    data = bsxfun_minus(data)
    data = np.abs(hilbert(data, axis=1))  # instantaneous amplitude
    bin_data = bsxfun_greater(data).astype(np.float64)

    # --- Same binarization on the surrogate ---
    rand_data = detrend(rand_data)
    rand_data = bsxfun_minus(rand_data)
    rand_data = np.abs(hilbert(rand_data, axis=1))
    bin_rand_data = bsxfun_greater(rand_data).astype(np.float64)

    lib = _load_lib()

    if mode == 'univariate':
        # One normalized LZC per channel (kept for Snooz / topography).
        # Each channel is a 1 x nt series -> C complexity() with nc=1.
        channel_norm_LZC = np.empty(num_channels, dtype=np.float64)
        for ch in range(num_channels):
            ch_data = np.ascontiguousarray(bin_data[ch:ch + 1, :], dtype=np.float64)
            ch_rand = np.ascontiguousarray(
                bin_rand_data[ch:ch + 1, :], dtype=np.float64
            )
            LZC = _call_complexity_1d(lib, ch_data)
            rand_LZC = _call_complexity_1d(lib, ch_rand)
            if rand_LZC == 0:
                raise ZeroDivisionError(
                    f'Surrogate Lempel-Ziv complexity was zero for channel {ch}.'
                )
            channel_norm_LZC[ch] = LZC / rand_LZC
        return channel_norm_LZC

    if mode == 'concat':
        # Schartner: stack channels time-point by time-point into one 1D string.
        # Shape becomes (1, n_channels * n_times); C complexity() with nc=1.
        bin_data = bin_data.T.reshape((1, -1))
        bin_rand_data = bin_rand_data.T.reshape((1, -1))
        LZC = _call_complexity_1d(lib, bin_data)
        rand_LZC = _call_complexity_1d(lib, bin_rand_data)
    else:
        # Zozor joint: C packs channels in groups of <= MAX_CH_PER_GROUP.
        LZC = _call_complexity_joint(lib, bin_data)
        rand_LZC = _call_complexity_joint(lib, bin_rand_data)

    if rand_LZC == 0:
        raise ZeroDivisionError('Surrogate Lempel-Ziv complexity was zero.')

    # Toker / Brito normalization against spectral null.
    return LZC / rand_LZC


def FJZC_parallel(windowed_signal, info, mode='joint', n_jobs=-1):
    """
    Apply FJZC to each window (joblib-parallel) and summarize.

    The LZ kernel stays in C (ctypes). Parallelism is over windows
    (same pattern as AECConnectivity). Uses Snooz commons.parallel_utils.

    Parameters
    ----------
    windowed_signal : ndarray, shape (n_windows, n_channels, n_times)
    info, mode : same as FJZC()
    n_jobs : int, default -1
        Parallel workers (-1 = all cores).

    Returns
    -------
    dict
        Common keys:
            'per_epoch_lzc' : ndarray
                For joint/concat: shape (n_windows,).
                For univariate: shape (n_windows,) = median across channels
                (Toker's univariate summary per window).
            'average_lzc' : float
                Mean of 'per_epoch_lzc' over windows.
            'mode' : str
        Univariate-only keys:
            'per_epoch_per_channel_lzc' : ndarray, shape (n_windows, n_channels)
            'average_per_channel_lzc' : ndarray, shape (n_channels,)
                Mean over windows of each channel's norm LZC.
        For joint/concat those two keys are None.
    """
    num_windows = windowed_signal.shape[0]

    def process_window(win_i):
        return FJZC(windowed_signal[win_i, :, :], info, mode=mode)

    effective_n_jobs = normalize_n_jobs(n_jobs, num_windows)

    if effective_n_jobs == 1 or num_windows <= 1:
        results = [process_window(w) for w in range(num_windows)]
    else:
        backend = select_joblib_backend()
        parallel_kwargs = {'n_jobs': effective_n_jobs, 'backend': backend}
        if backend == 'threading':
            parallel_kwargs['prefer'] = 'threads'
        results = Parallel(**parallel_kwargs)(
            delayed(process_window)(w) for w in range(num_windows)
        )

    if mode == 'univariate':
        # results[i] is (n_channels,)
        per_epoch_per_channel = np.stack(results, axis=0)
        # Toker univariate summary for each window
        per_epoch_lzc = np.median(per_epoch_per_channel, axis=1)
        average_per_channel = np.mean(per_epoch_per_channel, axis=0)
        return {
            'per_epoch_lzc': per_epoch_lzc,
            'average_lzc': float(np.mean(per_epoch_lzc)),
            'per_epoch_per_channel_lzc': per_epoch_per_channel,
            'average_per_channel_lzc': average_per_channel,
            'mode': mode,
        }

    per_epoch_lzc = np.asarray(results, dtype=np.float64)
    return {
        'per_epoch_lzc': per_epoch_lzc,
        'average_lzc': float(np.mean(per_epoch_lzc)),
        'per_epoch_per_channel_lzc': None,
        'average_per_channel_lzc': None,
        'mode': mode,
    }
