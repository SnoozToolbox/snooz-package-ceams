import math

from qtpy import QtWidgets

from CEAMSTools.EEGSpectralAnalysis.SpectralSettings.Ui_SpectralSettings import Ui_SpectralSettings
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog


class SpectralSettings(BaseStepView, Ui_SpectralSettings, QtWidgets.QWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self)
        self._fields = {
            "4bb8c9ac-64e8-4cec-9c2c-5a00c80b4eae.first_freq": self.first_freq_lineEdit,
            "4bb8c9ac-64e8-4cec-9c2c-5a00c80b4eae.last_freq": self.last_freq_lineEdit,
            "159bfdad-5000-474b-ae38-8e95ff4142b2.win_len_sec": self.win_len_lineEdit,
            "159bfdad-5000-474b-ae38-8e95ff4142b2.win_step_sec": self.win_step_lineEdit,
        }
        for topic in getattr(self, "_fields", {}):
            self._pub_sub_manager.subscribe(self, topic)

    def load_settings(self):
        for topic in self._fields:
            self._pub_sub_manager.publish(self, topic, "ping")

    def on_topic_response(self, topic, message, sender):
        if topic in self._fields:
            self._fields[topic].setText(str(message))

    def on_apply_settings(self):
        for topic, field in self._fields.items():
            self._pub_sub_manager.publish(self, topic, field.text().strip())

    def on_validate_settings(self):
        try:
            first = float(self.first_freq_lineEdit.text())
            last = float(self.last_freq_lineEdit.text())
            length = float(self.win_len_lineEdit.text())
            step = float(self.win_step_lineEdit.text())
        except ValueError:
            WarningDialog("Enter numeric values in Spectral Settings.")
            return False

        if not all(math.isfinite(value) for value in (first, last, length, step)):
            WarningDialog("Enter finite values in Spectral Settings.")
            return False
        if not 0 <= first < last:
            WarningDialog("The first frequency must be non-negative and below the last frequency.")
            return False
        if length < 1 or not length.is_integer():
            WarningDialog("Use a positive whole number of seconds for the window length with 1 Hz bands.")
            return False
        if not 0 < step <= length:
            WarningDialog("The window step must be positive and no longer than the window length.")
            return False
        if 0 < first < 1 and first + 1 / length > 1:
            WarningDialog("The first frequency is too close to the upper edge of the first 1 Hz band.")
            return False
        return True

    def __del__(self):
        if getattr(self, "_pub_sub_manager", None) is not None:
            for topic in self._fields:
                self._pub_sub_manager.unsubscribe(self, topic)
