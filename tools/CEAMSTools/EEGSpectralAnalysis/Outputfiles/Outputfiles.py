from qtpy import QtWidgets

from CEAMSTools.EEGSpectralAnalysis.Outputfiles.Ui_Outputfiles import Ui_Outputfiles
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog


class Outputfiles(BaseStepView, Ui_Outputfiles, QtWidgets.QWidget):
    _filename_topic = "4bb8c9ac-64e8-4cec-9c2c-5a00c80b4eae.filename"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self)
        self._pub_sub_manager.subscribe(self, self._filename_topic)
        self.choose_pushButton.clicked.connect(self.choose_button_slot)

    def load_settings(self):
        self._pub_sub_manager.publish(self, self._filename_topic, "ping")

    def on_topic_response(self, topic, message, sender):
        if topic == self._filename_topic:
            self.filename_lineEdit.setText(message)

    def on_validate_settings(self):
        if not self.filename_lineEdit.text().strip().lower().endswith(".tsv"):
            WarningDialog("Choose a .tsv file in Output File.")
            return False
        return True

    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._filename_topic, self.filename_lineEdit.text().strip())

    def choose_button_slot(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save spectral power report", self.filename_lineEdit.text(), "TSV (*.tsv)",
            options=QtWidgets.QFileDialog.DontConfirmOverwrite,
        )
        if filename:
            if not filename.lower().endswith(".tsv"):
                filename += ".tsv"
            self.filename_lineEdit.setText(filename)

    def __del__(self):
        if getattr(self, "_pub_sub_manager", None) is not None:
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)
