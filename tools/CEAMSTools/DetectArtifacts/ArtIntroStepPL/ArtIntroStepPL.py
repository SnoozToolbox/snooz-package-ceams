"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the Intro plugin
"""

from qtpy import QtWidgets

from CEAMSTools.DetectArtifacts.ArtIntroStepPL.Ui_ArtIntroStepPL import Ui_ArtIntroStepPL
from CEAMSTools.DetectArtifacts.artifact_drawing import ArtifactDrawing, SMALL_HEIGHT
from commons.BaseStepView import BaseStepView

class ArtIntroStepPL( BaseStepView,  Ui_ArtIntroStepPL, QtWidgets.QWidget):
    """
        ArtIntroStepPL displays the a few examples of artifact and describes the tool.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        self._load_embedded_images()

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass

    def _load_embedded_images(self):
        """The illustrations of the six artifacts (simulated EEG), drawn on their labels."""
        self._artifact_drawings = [
            ArtifactDrawing(label, kind, height=SMALL_HEIGHT, show_name=False) for label, kind in (
                (self.label_6, "flatline"), (self.label_8, "high_frequency_burst"),
                (self.label_5, "persistent_noise"), (self.label_9, "power_line"),
                (self.label_10, "baseline_variation"), (self.label_11, "muscle"))]
