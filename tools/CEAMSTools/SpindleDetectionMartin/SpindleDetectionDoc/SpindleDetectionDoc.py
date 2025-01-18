"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    SpindleDetectionDoc
    TODO CLASS DESCRIPTION
"""

from qtpy import QtWidgets
from PySide2.QtGui import QPixmap

from CEAMSTools.SpindleDetectionMartin.SpindleDetectionDoc.Ui_SpindleDetectionDoc import Ui_SpindleDetectionDoc
from commons.BaseStepView import BaseStepView

class SpindleDetectionDoc( BaseStepView,  Ui_SpindleDetectionDoc, QtWidgets.QWidget):
    """
        SpindleDetectionDoc
        TODO CLASS DESCRIPTION
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # init UI
        self.setupUi(self)
        pic_ref = QPixmap(u":/spindle_moda/e0004-b1-01-05-0001-smp303751_res80.png")
        self.spindle_image.setPixmap(pic_ref.copy())

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
