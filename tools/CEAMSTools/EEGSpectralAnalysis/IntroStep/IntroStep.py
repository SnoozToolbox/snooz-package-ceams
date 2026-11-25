#! /usr/bin/env python3
"""
    IntroStep
    Introduction of the tool EEG Spectral Power Analysis.
"""
from qtpy import QtWidgets

from CEAMSTools.EEGSpectralAnalysis.IntroStep.Ui_IntroStep import Ui_IntroStep
from CEAMSTools.EEGSpectralAnalysis.IntroStep.spectra_drawing import SpectraDrawing
from commons.BaseStepView import BaseStepView

class IntroStep(BaseStepView, Ui_IntroStep, QtWidgets.QWidget):
    """
        IntroStep
        Introduction of the tool EEG Spectral Power Analysis.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        # The example spectra (N2 and N3 on two channels), painted on spectra_image
        self._spectra_drawing = SpectraDrawing(self.spectra_image)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
