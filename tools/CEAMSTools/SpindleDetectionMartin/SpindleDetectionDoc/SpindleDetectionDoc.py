"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    SpindleDetectionDoc
    Description of the tool to detect spindles with the Martin algorithm.
"""
from qtpy import QtWidgets

from CEAMSTools.SpindleDetectionA7.SpindleDetectionDoc.SpindleDetectionDoc import SpindleDrawing
from CEAMSTools.SpindleDetectionMartin.SpindleDetectionDoc.Ui_SpindleDetectionDoc import Ui_SpindleDetectionDoc
from commons.BaseStepView import BaseStepView


class SpindleDetectionDoc( BaseStepView,  Ui_SpindleDetectionDoc, QtWidgets.QWidget):
    """
        SpindleDetectionDoc
        Description of the tool to detect spindles with the Martin algorithm.
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
