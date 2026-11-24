#! /usr/bin/env python3
"""
    IntroStep
    TODO CLASS DESCRIPTION
"""
import base64
from qtpy import QtWidgets
from qtpy.QtGui import QPixmap

from CEAMSTools.EEGSpectralAnalysis.IntroStep.Ui_IntroStep import Ui_IntroStep
from commons.BaseStepView import BaseStepView

class IntroStep(BaseStepView, Ui_IntroStep, QtWidgets.QWidget):
    """
        IntroStep
        TODO CLASS DESCRIPTION
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        # init UI
        self.setupUi(self)
        self._load_embedded_image()

    def _load_embedded_image(self):
        """Load the embedded base64 image data into spindle_image."""
        from .image_data_base64 import IMAGE_BASE64_CZ, IMAGE_BASE64_O1
        
        image_bytes = base64.b64decode(IMAGE_BASE64_CZ)
        pixmap = QPixmap()
        pixmap.loadFromData(image_bytes)
        self.spectra_CZ_image.setPixmap(pixmap)

        image_bytes = base64.b64decode(IMAGE_BASE64_O1)
        pixmap = QPixmap()
        pixmap.loadFromData(image_bytes)
        self.spectra_O1_image.setPixmap(pixmap)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
