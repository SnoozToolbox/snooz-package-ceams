"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the Intro plugin
"""

from qtpy import QtWidgets
from PySide2.QtGui import QPixmap

from CEAMSTools.DetectArtifacts.ArtIntroStepPL.Ui_ArtIntroStepPL import Ui_ArtIntroStepPL
from commons.BaseStepView import BaseStepView

class ArtIntroStepPL( BaseStepView,  Ui_ArtIntroStepPL, QtWidgets.QWidget):
    """
        ArtIntroStepPL displays the a few examples of artifact and describes the tool.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        pic_ref=QPixmap(u":/intro/2_amplitude_v2.png")
        self.label_6.setPixmap(pic_ref.copy())
        pic_ref1=QPixmap(u":/intro/3_burst_noise_v2.png")
        self.label_8.setPixmap(pic_ref1.copy())
        pic_ref2=QPixmap(u":/intro/3b_persistent_noise.png")
        self.label_5.setPixmap(pic_ref2.copy())
        pic_ref3=QPixmap(u":/intro/4_powerLine_v2.png")
        self.label_9.setPixmap(pic_ref3.copy())
        pic_ref4=QPixmap(u":/intro/5_BSLVar_v2.png")
        self.label_10.setPixmap(pic_ref4.copy())
        pic_ref5=QPixmap(u":/intro/6_muscular_v2.png")
        self.label_11.setPixmap(pic_ref5.copy())


    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass