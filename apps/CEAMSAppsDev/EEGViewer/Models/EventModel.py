"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from qtpy import QtCore
from qtpy.QtCore import Signal

class EventModel(QtCore.QObject):
    data_changed = Signal()
    def __init__(self):
        super().__init__()
        self._channels = []
        self.start_sec = 0
        self.duration_sec = 0
        self.group = ""
        self.name = ""