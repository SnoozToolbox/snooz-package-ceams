"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
"""
    SpindleDetectionDoc
    Description of the tool to detect spindles with the SUMO algorithm.
"""

from qtpy import QtWidgets
from qtpy.QtGui import QPixmap, QImage
from qtpy.QtCore import QFile, QTimer, Slot

from . import spindle_rc  # keep the module loaded

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
        self._spindle_rc_ref = spindle_rc  # prevent it from being garbage collected
        # resources - makes Snooz crash on "img = QImage(image_path)"
        self.image_path = ":/spindle_moda/e0004-b1-01-05-0001-smp303751_res80.png"
        #self.image_path = "C:/Users/klacourse/Documents/snooz_workspace/snooz-package-ceams/tools/CEAMSTools/SpindleDetectionSumo/SpindleDetectionDoc/e0004-b1-01-05-0001-smp303751_res80.png"
        self._image_loaded = False


    def load_settings(self):
        pass


    def on_apply_settings(self):
        pass


    def showEvent(self, event):
        super().showEvent(event)
        if not self._image_loaded:
            self._load_pixmap(self.image_path)
            self._image_loaded = True


    #@Slot(str)
    def _load_pixmap(self, image_path: str):
        image = QImage(image_path)
        pixmap = QPixmap.fromImage(image)
        self.spindle_image.setPixmap(pixmap)
