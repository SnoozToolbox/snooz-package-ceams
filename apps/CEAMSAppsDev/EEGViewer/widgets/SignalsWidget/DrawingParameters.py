"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from qtpy.QtCore import Signal, QObject, QTimer

class DrawingParameters(QObject):
    drawing_parameters_changed = Signal(QObject)

    def __init__(self):
        super().__init__()
        self._emit_timer = QTimer()
        self._emit_timer.setSingleShot(True)
        self._emit_timer.timeout.connect(self.emit_changed_signal)
        self._pixel_per_second = 0
        self._time_offset = 0
        self._display_width = 0
        self._display_height = 0
        self._seconds_per_page = 30
        self._amp_scale = 1
        self._amp_scale_step = 0.1
        self._signal_row_height = 40
        self._channels_sections_width = 50

    @property
    def channels_sections_width(self):
        return self._channels_sections_width
    
    @channels_sections_width.setter
    def channels_sections_width(self, value):
        if value != self._channels_sections_width:
            self._channels_sections_width = value

    @property
    def pixel_per_second(self):
        return self._pixel_per_second
    
    @pixel_per_second.setter
    def pixel_per_second(self, value):
        if value != self._pixel_per_second:
            self._pixel_per_second = value
            self._start_timer()

    @property
    def signal_row_height(self):
        return self._signal_row_height
    
    @signal_row_height.setter
    def signal_row_height(self, value):
        if value != self._signal_row_height:
            self._signal_row_height = value
            self._start_timer()
    
    @property
    def seconds_per_page(self):
        return self._seconds_per_page
    
    @seconds_per_page.setter
    def seconds_per_page(self, value):
        if value != self._seconds_per_page:
            self._seconds_per_page = value
            self._start_timer()

    @property
    def display_width(self):
        return self._display_width
    
    @display_width.setter
    def display_width(self, value):
        if value != self._display_width:
            self._display_width = value
            self._start_timer()
    
    @property
    def display_height(self):
        return self._display_height
    
    @display_height.setter
    def display_height(self, value):
        if value != self._display_height:
            self._display_height = value
            self._start_timer()

    @property
    def time_offset(self):
        return self._time_offset
    
    @time_offset.setter
    def time_offset(self, value):
        if value != self._time_offset:
            self._time_offset = value
            self._start_timer()

    @property
    def amp_scale(self):
        return self._amp_scale
    
    @amp_scale.setter
    def amp_scale(self, value):
        if value != self._amp_scale:
            self._amp_scale = value
            self._start_timer()

    ## PRIVATE FUNCTIONS
    def _start_timer(self):
        self._emit_timer.start(100)

    def emit_changed_signal(self):
        self.drawing_parameters_changed.emit(self)
