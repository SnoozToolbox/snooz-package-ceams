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
from qtpy.QtCore import QFile

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
        _spindle_rc_ref = spindle_rc  # prevent it from being garbage collected
        # init UI
        self.setupUi(self)
        image_path = ":/spindle_moda/e0004-b1-01-05-0001-smp303751_res80.png"
        self.label.setPixmap(self.load_safe_pixmap(image_path))
        #self.spindle_image.setPixmap(QPixmap(u":/spindle_moda/e0004-b1-01-05-0001-smp303751_res80.png"))

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass

    def load_safe_pixmap(self, image_path: str) -> QPixmap:
        """
        Load a QImage in the **main Qt thread**, then convert to QPixmap.
        This avoids random access-violation crashes on Windows.
        """
        # Verify if this resource exists : ":/spindle_moda/e0004-b1-01-05-0001-smp303751_res80.png"
        if QFile.exists(image_path):
            img = QImage(image_path)
        else:
            return QPixmap()
        return QPixmap.fromImage(img)