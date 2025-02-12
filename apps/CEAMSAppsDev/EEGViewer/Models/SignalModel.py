"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from qtpy.QtCore import Signal
from qtpy import QtWidgets, QtCore

class SignalModel(QtCore.QObject):
    data_changed = Signal()

    def __init__(self, channel_name):
        super().__init__()
        self._channel_name = channel_name
        self._event_models = []
        self._signal_chunks = None
        self._sample_rate = None
        self._amp_scale = 1.0

    @property
    def channel_name(self):
        return self._channel_name
    
    @property
    def amp_scale(self):
        return self._amp_scale
    
    @amp_scale.setter
    def amp_scale(self, amp_scale):
        self._amp_scale = amp_scale
        self.data_changed.emit()
    
    @property
    def signal_chunks(self):
        return self._signal_chunks
    
    # Setter
    @signal_chunks.setter
    def signal_chunks(self, signal_chunks):
        self._signal_chunks = signal_chunks

    @property
    def event_models(self):
        return self._event_models
    
    @property
    def sample_rate(self):
        return self._signal_chunks[0].sample_rate
    
    def add_event_model(self, event_model):
        self._event_models.append(event_model)       

    def get_duration(self):
        max_duration = 0
        
        for signal_chunk in self._signal_chunks:
            start_time = signal_chunk.start_time
            duration = signal_chunk.duration
            max_duration = max(max_duration, start_time + duration)

        return max_duration
    
    def get_total_sample_count(self):
        """ Get the total sample count, ignoring any discontinuities between 
        signal chunks.
        
        Returns:
            int: The total sample count.
        """
        return int(self.get_duration() * self.sample_rate)
    
    def get_sample_by_index(self, sample_index:int):
        """ Get sample value by its index.

        Args:
            sample_index (int): The index of the sample

        Returns:
            float: the value of the sample
        """
        for signal_chunk in self._signal_chunks:
            start_time = signal_chunk.start_time
            duration = signal_chunk.duration
            sample_time = sample_index / self.sample_rate
            if start_time <= sample_time < start_time + duration:
                sample_time = sample_time - start_time
                sample_index = int(sample_time * self.sample_rate)
                return signal_chunk.samples[sample_index]
        return None
