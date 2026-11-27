#! /usr/bin/env python3
"""
    SSWCIntroStep
    Settings viewer of the Intro plugin for the Slow Wave Classifier tool
"""
from qtpy import QtWidgets

from CEAMSTools.SlowWaveClassification.SSWCIntroStep.Ui_SSWCIntroStep import Ui_SSWCIntroStep
from CEAMSTools.SlowWaveClassification.SSWCIntroStep.classification_drawing import ClassificationDrawing
from commons.BaseStepView import BaseStepView

class SSWCIntroStep( BaseStepView,  Ui_SSWCIntroStep, QtWidgets.QWidget):
    """
        SSWCIntroStep
        Displays the functionnalities of the slow wave classifier.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        # The histogram of the classification: drawn by the code, in the colors of the theme
        self._classification_drawing = ClassificationDrawing(self.image_hist)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
