"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from PySide2.QtCore import Slot, Signal, QObject

from CEAMSModules.PSGReader.PSGReaderManager import PSGReaderManager
from pandas import DataFrame

class EventsManager(QObject):
    events_loaded = Signal(DataFrame)
    sleep_stages_loaded = Signal(DataFrame)

    def __init__(self):
        super().__init__()
        self._events = None
        self._sleep_stages = None
        self._current_filename = None

    @property
    def events(self):
        return self._events
    
    @events.setter
    def events(self, events):
        self._events = events

    def clear(self):
        self._events = None
        self._sleep_stages = None
        self._current_filename = None

    def load_events(self, filename):
        self._current_filename = filename
        psg_reader_manager = PSGReaderManager()
        psg_reader_manager._init_readers()
        psg_reader_manager.open_file(filename)
        self._events = psg_reader_manager.get_events()
        psg_reader_manager.close_file()
        self.events_loaded.emit(self._events)

    def reload_events(self):
        if self._current_filename is not None:
            self.load_events(self._current_filename)

    def load_sleep_stages(self, filename):
        psg_reader_manager = PSGReaderManager()
        psg_reader_manager._init_readers()
        psg_reader_manager.open_file(filename)
        self._sleep_stages = psg_reader_manager.get_sleep_stages()
        psg_reader_manager.close_file()
        self.sleep_stages_loaded.emit(self._sleep_stages)

    def reload_sleep_stages(self):
        if self._current_filename is not None:
            self.load_sleep_stages(self._current_filename)