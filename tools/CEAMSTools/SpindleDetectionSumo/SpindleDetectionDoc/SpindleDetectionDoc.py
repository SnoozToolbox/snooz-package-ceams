"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
"""
    SpindleDetectionDoc
    Description of the tool to detect spindles with the SUMO algorithm.
"""

from qtpy import QtWidgets

from CEAMSTools.SpindleDetectionA7.SpindleDetectionDoc.SpindleDetectionDoc import SpindleDrawing
from .Ui_SpindleDetectionDoc import Ui_SpindleDetectionDoc
from commons.BaseStepView import BaseStepView

class SpindleDetectionDoc( BaseStepView,  Ui_SpindleDetectionDoc, QtWidgets.QWidget):
    """
        SpindleDetectionDoc
        Description of the tool to detect spindles with the SUMO algorithm.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # init UI
        self.setupUi(self)
        # The illustration of a spindle (simulated EEG), painted on spindle_image
        self._spindle_drawing = SpindleDrawing(self.spindle_image)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
