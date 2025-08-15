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
from qtpy.QtCore import QFile, QTimer

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
        self.image_path = ":/spindle_moda/e0004-b1-01-05-0001-smp303751_res80.png"
        # defer image loading
        self._load_image_timer = QTimer(self)
        self._load_image_timer.setSingleShot(True)
        self._load_image_timer.timeout.connect(self._load_pixmap)
        self._load_image_timer.start(0)
        self.destroyed.connect(self._load_image_timer.stop)


    def load_settings(self):
        pass


    def on_apply_settings(self):
        pass


    def _load_pixmap(self):
        if not self.isVisible():
            return
        pixmap = self.load_safe_pixmap(self.image_path)
        self.spindle_image.setPixmap(pixmap)


    def load_safe_pixmap(self, image_path: str) -> QPixmap:
        if not QFile.exists(image_path):
            return QPixmap()
        img = QImage(image_path)
        return QPixmap.fromImage(img)