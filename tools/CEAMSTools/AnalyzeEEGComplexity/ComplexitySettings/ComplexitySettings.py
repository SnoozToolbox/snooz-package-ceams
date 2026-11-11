#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    ComplexitySettings
    Settings step for the complexity mode, the epoching and the output files.

    The step sends the selected complexity mode, the cohort report and the
    flag to save the detailed tables to the LempZiv Complexity module, and
    the epoch length and the overlap to the Epoch Signal module.

    The pipeline holds two chains, one for the sleep stages scope and one for
    the annotations or unscored scope. The settings are sent to both chains
    since only the chain selected in the Filter step is activated.
"""

import os

from qtpy import QtWidgets

from CEAMSTools.AnalyzeEEGComplexity.ComplexitySettings.Ui_ComplexitySettings import Ui_ComplexitySettings
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog


class ComplexitySettings(BaseStepView, Ui_ComplexitySettings, QtWidgets.QWidget):
    """
        ComplexitySettings
        Class to send messages between the step-by-step interface and the plugins.
        The goal is to inform the LempZiv Complexity module of the complexity
        mode and of the output files, and the Epoch Signal module of the epoch
        length and of the overlap.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Chain analysing the selected sleep stages.
        self._sleep_chain = {
            "epoch": "332c530d-6115-4b6b-82c6-6e9e739430d5",         # Epoch Signal
            "complexity": "7ab4b952-e314-420d-b70c-a52f1b3febc6",    # LempZiv Complexity
        }
        # Chain analysing the selected annotations or the unscored recording.
        self._annotation_chain = {
            "epoch": "4397e29a-9dd8-46d4-83a4-798d45af21eb",         # Epoch Signal
            "complexity": "7799144a-6620-45c7-bcd4-015d270c9c68",    # LempZiv Complexity
        }
        self._chains = [self._sleep_chain, self._annotation_chain]

        # Topics used to read back the settings already stored in the pipeline.
        # The sleep chain is used as the reference since both chains always hold
        # the same settings.
        self._mode_topic = f'{self._sleep_chain["complexity"]}.mode'
        self._pub_sub_manager.subscribe(self, self._mode_topic)
        self._cohort_file_topic = f'{self._sleep_chain["complexity"]}.cohort_filename'
        self._pub_sub_manager.subscribe(self, self._cohort_file_topic)
        self._export_details_topic = f'{self._sleep_chain["complexity"]}.export_details'
        self._pub_sub_manager.subscribe(self, self._export_details_topic)
        self._epoch_length_topic = f'{self._sleep_chain["epoch"]}.epoch_length_sec'
        self._pub_sub_manager.subscribe(self, self._epoch_length_topic)
        self._overlap_topic = f'{self._sleep_chain["epoch"]}.overlap_sec'
        self._pub_sub_manager.subscribe(self, self._overlap_topic)

        # Radio button of the interface for each mode of the module.
        self._mode_radio_buttons = {
            "univariate": self.univariate_radioButton,
            "joint": self.joint_radioButton,
            "concat": self.concat_radioButton,
        }

        self.cohort_pushButton.clicked.connect(self.on_choose_cohort_file)

    # -------------------------------------------------------------------------
    # Complexity mode
    # -------------------------------------------------------------------------
    def get_current_mode(self):
        """ Return the complexity mode currently selected by the user. """
        for mode, radio_button in self._mode_radio_buttons.items():
            if radio_button.isChecked():
                return mode
        return ""

    def select_mode(self, mode):
        """ Check the radio button matching the mode read from the pipeline. """
        mode = str(mode).strip().lower() if mode is not None else ""
        if mode in self._mode_radio_buttons:
            self._mode_radio_buttons[mode].setChecked(True)

    # -------------------------------------------------------------------------
    # Output files
    # -------------------------------------------------------------------------
    def on_choose_cohort_file(self):
        """ Slot called when the user presses Choose to define the cohort report.

        The user types a new file name or selects an existing report. The file
        is not created here, the LempZiv Complexity module creates it during
        the run. The overwrite warning is turned off since an existing report
        is not replaced, the new results are appended to it (as in PSA).
        """
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save file as', self.cohort_lineEdit.text(), 'TSV (*.tsv)',
            options=QtWidgets.QFileDialog.DontConfirmOverwrite)
        if filename:
            if not filename.endswith('.tsv'):
                filename = filename + '.tsv'
            self.cohort_lineEdit.setText(filename)

    # -------------------------------------------------------------------------
    # BaseStepView interface
    # -------------------------------------------------------------------------
    def load_settings(self):
        """ Ask the pipeline for the settings already stored in the modules. """
        self._pub_sub_manager.publish(self, self._mode_topic, 'ping')
        self._pub_sub_manager.publish(self, self._cohort_file_topic, 'ping')
        self._pub_sub_manager.publish(self, self._export_details_topic, 'ping')
        self._pub_sub_manager.publish(self, self._epoch_length_topic, 'ping')
        self._pub_sub_manager.publish(self, self._overlap_topic, 'ping')

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Update the interface with the settings stored in the pipeline. """
        if topic == self._mode_topic:
            self.select_mode(message)
        elif topic == self._cohort_file_topic:
            self.cohort_lineEdit.setText(str(message).strip() if message is not None else "")
        elif topic == self._export_details_topic:
            self.export_details_checkBox.setChecked(
                str(message).strip().lower() in ('true', '1'))
        elif topic == self._epoch_length_topic:
            if message is not None and str(message).strip() != "":
                self.epoch_length_doubleSpinBox.setValue(float(message))
        elif topic == self._overlap_topic:
            if message is not None and str(message).strip() != "":
                self.overlap_length_doubleSpinBox.setValue(float(message))

    def on_validate_settings(self):
        """ Validate the settings selected by the user. """
        if self.get_current_mode() == "":
            WarningDialog("Select the complexity mode to compute.")
            return False

        epoch_length = self.epoch_length_doubleSpinBox.value()
        overlap = self.overlap_length_doubleSpinBox.value()
        if epoch_length <= 0:
            WarningDialog("The epoch length must be greater than 0 second.")
            return False
        if overlap < 0:
            WarningDialog("The overlap length must be greater or equal to 0 second.")
            return False
        if overlap >= epoch_length:
            WarningDialog("The overlap length must be shorter than the epoch length.")
            return False

        # The cohort report is mandatory, as in PSA, it is the main output of
        # the tool.
        cohort_filename = self.cohort_lineEdit.text().strip()
        if cohort_filename == "":
            WarningDialog("Choose the file to save the cohort complexity report.")
            return False
        if not os.path.isdir(os.path.dirname(cohort_filename)):
            WarningDialog("The folder of the cohort report does not exist : "
                          f"{os.path.dirname(cohort_filename)}")
            return False
        return True

    def on_apply_settings(self):
        """ Send the settings to the modules of both chains. """
        mode = self.get_current_mode()
        epoch_length = str(self.epoch_length_doubleSpinBox.value())
        overlap = str(self.overlap_length_doubleSpinBox.value())
        cohort_filename = self.cohort_lineEdit.text().strip()
        export_details = str(self.export_details_checkBox.isChecked())

        for chain in self._chains:
            self._pub_sub_manager.publish(
                self, f'{chain["epoch"]}.epoch_length_sec', epoch_length)
            self._pub_sub_manager.publish(
                self, f'{chain["epoch"]}.overlap_sec', overlap)
            self._pub_sub_manager.publish(
                self, f'{chain["complexity"]}.mode', mode)
            self._pub_sub_manager.publish(
                self, f'{chain["complexity"]}.cohort_filename', cohort_filename)
            self._pub_sub_manager.publish(
                self, f'{chain["complexity"]}.export_details', export_details)

    def __del__(self):
        self._pub_sub_manager.unsubscribe(self, self._mode_topic)
        self._pub_sub_manager.unsubscribe(self, self._cohort_file_topic)
        self._pub_sub_manager.unsubscribe(self, self._export_details_topic)
        self._pub_sub_manager.unsubscribe(self, self._epoch_length_topic)
        self._pub_sub_manager.unsubscribe(self, self._overlap_topic)
