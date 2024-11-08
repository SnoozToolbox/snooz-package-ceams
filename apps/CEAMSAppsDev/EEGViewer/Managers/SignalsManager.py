"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from qtpy import QtCore

from CEAMSModules.PSGReader.PSGReaderManager import PSGReaderManager
from CEAMSApps.EEGViewer.Models.SignalModel import SignalModel
from qtpy.QtWidgets import QProgressDialog
from scipy import signal, fft
import numpy as np
import time

class SignalsLoader(QtCore.QObject):
    finished = QtCore.Signal()
    signals_ready = QtCore.Signal(list)

    def __init__(self, filename, montage_name, channels):
        super().__init__()
        self._filename = filename
        self._montage_name = montage_name
        self._channels = channels

    @QtCore.Slot()
    def load_signals(self):
         # Now open the file and read the missing signals
        print("SignalsLoader.Loading signals")
        print(self._channels)
        print(self._montage_name)

        psg_reader_manager = PSGReaderManager()
        psg_reader_manager._init_readers()
        psg_reader_manager.open_file(self._filename)

        # Get montage_index
        montage_index = psg_reader_manager.get_montage_index(self._montage_name)
        signal_models = []
        if montage_index is not None:
            signal_models = psg_reader_manager.get_signal_models(channel_names=self._channels,
                                                                montage_index=montage_index)
            
        psg_reader_manager.close_file()

        print("Loading signals DONE emitting")
        self.signals_ready.emit(signal_models)
        print("DONE emitting")
        self.finished.emit()

class SignalsManager(QtCore.QObject):
    # signal
    signals_loaded = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self._signals = {}
        self._current_montage_name = None
        self._current_filename = None

    @property
    def signals(self):
        return self._signals
    
    def clear(self):
        self._signals = {}
        self._current_montage_name = None
        self._current_filename = None

    def load_signals(self, filename, montage_name, channel_names):
        if self._current_filename != filename or self._current_montage_name != montage_name:
            # Remove all loaded channels
            self._signals = {}
            self._oxy_signals = []
            self._current_filename = filename
            self._current_montage_name = montage_name

        # Make a list of channels to load based on the one that are already
        # loaded.
        channels_to_load = []
        for channel_name in channel_names:
            if not self.is_loaded(channel_name):
                channels_to_load.append(channel_name)

        # Unload the one we don't need anymore
        channels_to_remove = []
        for channel_name in self._signals.keys():
            if channel_name not in channel_names:
                channels_to_remove.append(channel_name)

        for channel_name in channels_to_remove:
            del self._signals[channel_name]
        
        self._thread = QtCore.QThread()
        self.signals_loader = SignalsLoader(self._current_filename,
                                        self._current_montage_name, 
                                        channel_names)
        self.signals_loader.signals_ready.connect(self.on_signals_ready)
        self.signals_loader.finished.connect(self._thread.quit)
        
        self.signals_loader.moveToThread(self._thread)
        self._thread.started.connect(self.signals_loader.load_signals)

        self._thread.start()
        self._open_loading_dialog()
        
    @QtCore.Slot(list)
    def on_signals_ready(self, signal_models):
        print("on_signals_ready")
        for signal_model in signal_models:
            if signal_model.channel not in self._signals:
                self._signals[signal_model.channel] = []
            self._signals[signal_model.channel].append(signal_model)
        self._close_loading_dialog()
        self.signals_loaded.emit()
        self.signals_loader = None

    def resample_signal(signal_model: SignalModel, target_sample_rate: int) -> SignalModel:
        resampled_signal_model = signal_model.clone(clone_samples=False)

        #sample_rate = int(sample_rate)
        factor = signal_model.sample_rate / target_sample_rate
        nsamples = signal_model.samples.size

        # Since resample is using the fft, we want to have dyadic number of samples to speed up performance
        fast_size = fft.next_fast_len(nsamples)
        num = int(fast_size / factor)
        real_num = int(round(nsamples / factor,0)) # final number of samples (without fast_size)
        
        # Since resample is using the fft, we zeros pad to have dyadic number of samples to speed up performance
        total_pading = (fast_size-nsamples)
        n_pad_start = int(total_pading/2) if (total_pading % 2) == 0 else int(total_pading/2)+1
        n_pad_end = int(total_pading/2)
        n_pad_resampled = int(round(n_pad_start/factor,0))
        resampled_samples = signal.resample(np.pad(signal_model.samples,(n_pad_start,n_pad_end)), num)[n_pad_resampled:real_num+n_pad_resampled]
        resampled_signal_model.samples = resampled_samples
        resampled_signal_model.sample_rate = target_sample_rate
        return resampled_signal_model

    def get_signal(self, channel_name: str) -> [SignalModel]:
        if channel_name in self._signals:
            return self._signals[channel_name]
        return None

    def is_loaded(self, channel_name: str) -> bool:
        for loaded_channel_name in self._signals.keys():
            if loaded_channel_name == channel_name:
                return True
        return False
    
    def _open_loading_dialog(self):
        self._progress = QProgressDialog("Loading ...", None, 0, 1)
        self._progress.setWindowModality(QtCore.Qt.ApplicationModal)
        self._progress.setMinimumDuration(0) # Settings a minimum time greater than 0 makes the UI update slower
        self._progress.show()

    def _close_loading_dialog(self):
        if self._progress is not None:
            self._progress.setValue(1)
            self._progress.close()
            self._progress = None