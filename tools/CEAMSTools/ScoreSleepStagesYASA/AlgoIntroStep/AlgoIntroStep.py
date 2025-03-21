"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the Intro plugin
"""

from qtpy import QtWidgets

from CEAMSTools.ScoreSleepStagesYASA.AlgoIntroStep.Ui_AlgoIntroStep import Ui_AlgoIntroStep
from commons.BaseStepView import BaseStepView

class AlgoIntroStep( BaseStepView, Ui_AlgoIntroStep, QtWidgets.QWidget):
    """
        AlgoIntroStep displays the a few examples of artifact and describes the tool.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass