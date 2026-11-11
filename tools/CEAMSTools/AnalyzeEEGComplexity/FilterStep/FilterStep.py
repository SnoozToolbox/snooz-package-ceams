#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    FilterStep
    Settings step for the frequency band and the recording scope of the
    complexity analysis.

    The step sends the selected band-pass cutoff to the Filter Signal module.
    It also selects the recording scope, which routes the pipeline: the
    analysis runs either on sleep stages, on specific annotations, or on the
    unscored recording (optionally trimmed). Each scope has its own chain
    (events, epoching and complexity), and only the chain of the current scope
    is activated. The scope is shared with the other steps through the context.
"""

from qtpy import QtWidgets

from CEAMSTools.AnalyzeEEGComplexity.FilterStep.Ui_FilterStep import Ui_FilterStep
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState
from widgets.WarningDialog import WarningDialog


class FilterStep(BaseStepView, Ui_FilterStep, QtWidgets.QWidget):
    """
        FilterStep
        Class to send messages between the step-by-step interface and the plugins.
        The goal is to inform the Filter Signal module of the selected cutoff and
        to activate the chain (Sleep Stage Events, Signals From Events, Epoch
        Signal and LempZiv Complexity) matching the selected recording scope.
    """

    # Keys for the context shared with the other steps of the preset
    context_Con_annot_selection = "annotation_selection"
    context_Con_sleep_stages = "sleep_stages_selection"
    # Recording scope : "sleep_stages" | "specific_annotations" | "unscored"
    context_Con_scope = "complexity_scope"

    # Cutoff sent to the Filter Signal module for each standard band
    BAND_CUTOFFS = {
        "fullband": "0.1 45",
        "delta": "0.16 4",
        "theta": "4 8",
        "alpha": "8 13",
        "beta": "13 30",
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        self._node_id_bandpass_filter = "02efc124-b260-4b42-b45f-9e56e800908a"
        self._node_id_trim_signal = "d2c2451f-9888-4ce0-8809-0af5a30baaae"

        # Chain analysing the selected sleep stages.
        self._sleep_chain = {
            "stage_events": "3119a475-6f61-471e-86bb-00e90c6dbbb3",  # Sleep Stage Events
            "signals": "f9750bb2-b03c-4c0c-8504-823fb1f22c05",       # Signals From Events
            "epoch": "332c530d-6115-4b6b-82c6-6e9e739430d5",         # Epoch Signal
            "complexity": "7ab4b952-e314-420d-b70c-a52f1b3febc6",    # LempZiv Complexity
        }
        # Chain analysing the selected annotations or the unscored recording.
        self._annotation_chain = {
            "signals": "d322fe3a-7e09-474b-aee5-9f202836dee4",       # Signals From Events
            "epoch": "4397e29a-9dd8-46d4-83a4-798d45af21eb",         # Epoch Signal
            "complexity": "7799144a-6620-45c7-bcd4-015d270c9c68",    # LempZiv Complexity
        }

        # Subscribe to the topics of the nodes we want to talk to
        self._low_high_cutoff_topic = f'{self._node_id_bandpass_filter}.cutoff'
        self._pub_sub_manager.subscribe(self, self._low_high_cutoff_topic)
        self._trim_start_time_topic = f'{self._node_id_trim_signal}.start_sec'
        self._pub_sub_manager.subscribe(self, self._trim_start_time_topic)
        self._trim_duration_time_topic = f'{self._node_id_trim_signal}.duration_sec'
        self._pub_sub_manager.subscribe(self, self._trim_duration_time_topic)
        self._sleep_stages_topic = f'{self._sleep_chain["stage_events"]}.stages'

        # The custom cutoffs are only editable for the custom band.
        self.enable_custom_cutoff_widgets(False)
        # The signal is trimmed only on demand, for the unscored recording.
        self.checkBox.setChecked(False)
        self.bypass_node(self._node_id_trim_signal)
        self.enable_trim_widgets(False)

        self.sleep_stages_names = ''

        self.custom_radioButton.toggled.connect(self.on_custom_radio_toggled)
        self.checkBox.toggled.connect(self.on_trim_checkbox_toggled)
        self.unscored_radioButton.toggled.connect(self.on_unscored_toggled)
        self.sleep_stages_radioButton.toggled.connect(self.on_sleep_stages_toggled)
        self.specific_annotations_radioButton.toggled.connect(self.on_specific_annotations_toggled)

        # Align the widgets, the pipeline and the context with the default scope.
        self.apply_scope(self.get_current_scope())

    # -------------------------------------------------------------------------
    # Recording scope
    # -------------------------------------------------------------------------
    def get_current_scope(self):
        """ Return the recording scope currently selected by the user. """
        if self.sleep_stages_radioButton.isChecked():
            return "sleep_stages"
        if self.specific_annotations_radioButton.isChecked():
            return "specific_annotations"
        return "unscored"

    def apply_scope(self, scope):
        """ Align the widgets, the pipeline and the context with the scope. """
        self.enable_scope_widgets(scope)
        self.set_scope_nodes(scope)
        self.update_context(scope)

    def enable_scope_widgets(self, scope):
        """ Enable the sleep stages for the sleep scope and the trim for the
            unscored scope only.
        """
        sleep_stage_scope = scope == "sleep_stages"
        for stage_checkbox in (self.wake_checkBox, self.n1_checkBox,
                               self.n2_checkBox, self.n3_checkBox,
                               self.rem_checkBox):
            stage_checkbox.setEnabled(sleep_stage_scope)

        unscored_scope = scope == "unscored"
        self.checkBox.setEnabled(unscored_scope)
        if not unscored_scope:
            # The whole recording is already cropped by the events.
            self.checkBox.setChecked(False)

    def set_scope_nodes(self, scope):
        """ Activate the whole chain of the selected scope and deactivate the
            chain of the other scope.

            The chain includes the events modules, the Epoch Signal module and
            the LempZiv Complexity module, in order to avoid running a branch
            without input.

            For the unscored scope, the Signals From Events module of the
            annotation chain is bypassed : the (trimmed) recording is passed
            through without being cropped by events, and the rest of that
            chain stays activated to compute the complexity.
        """
        if scope == "sleep_stages":
            self.activate_chain(self._sleep_chain)
            self.deactivate_chain(self._annotation_chain)
        elif scope == "specific_annotations":
            self.deactivate_chain(self._sleep_chain)
            self.activate_chain(self._annotation_chain)
        else:
            self.deactivate_chain(self._sleep_chain)
            self.activate_chain(self._annotation_chain)
            self.bypass_node(self._annotation_chain["signals"])

    def update_context(self, scope):
        """ Share the recording scope with the other steps of the preset. """
        self._context_manager[FilterStep.context_Con_scope] = scope
        self._context_manager[FilterStep.context_Con_annot_selection] = \
            1 if scope == "specific_annotations" else 0
        self._context_manager[FilterStep.context_Con_sleep_stages] = \
            self.sleep_stages_names if scope == "sleep_stages" else ''

    # -------------------------------------------------------------------------
    # Activation state of the modules
    # -------------------------------------------------------------------------
    def activate_node(self, node_id):
        """ Activate a module from its node identifier. """
        self._pub_sub_manager.publish(
            self, f"{node_id}.activation_state_change", ActivationState.ACTIVATED)

    def bypass_node(self, node_id):
        """ Bypass a module from its node identifier. """
        self._pub_sub_manager.publish(
            self, f"{node_id}.activation_state_change", ActivationState.BYPASS)

    def deactivate_node(self, node_id):
        """ Deactivate a module from its node identifier. """
        self._pub_sub_manager.publish(
            self, f"{node_id}.activation_state_change", ActivationState.DEACTIVATED)

    def activate_chain(self, chain):
        """ Activate every module of a chain. """
        for node_id in chain.values():
            self.activate_node(node_id)

    def deactivate_chain(self, chain):
        """ Deactivate every module of a chain. """
        for node_id in chain.values():
            self.deactivate_node(node_id)

    # -------------------------------------------------------------------------
    # Widgets
    # -------------------------------------------------------------------------
    def enable_custom_cutoff_widgets(self, bool_flag):
        self.low_cutoff_label.setEnabled(bool_flag)
        self.low_cutoff_doubleSpinBox.setEnabled(bool_flag)
        self.label_4.setEnabled(bool_flag)
        self.high_cutoff_doubleSpinBox.setEnabled(bool_flag)

    def enable_trim_widgets(self, bool_flag):
        self.label_6.setEnabled(bool_flag)
        self.start_time_doubleSpinBox.setEnabled(bool_flag)
        self.label_7.setEnabled(bool_flag)
        self.duration_doubleSpinBox.setEnabled(bool_flag)

    # Called when the user selects the custom frequency band
    def on_custom_radio_toggled(self, checked):
        self.enable_custom_cutoff_widgets(checked)

    # Called when the user selects the unscored recording scope
    def on_unscored_toggled(self, checked):
        if checked:
            self.apply_scope("unscored")

    # Called when the user selects the sleep stages recording scope
    def on_sleep_stages_toggled(self, checked):
        if checked:
            self.apply_scope("sleep_stages")

    # Called when the user selects the specific annotations recording scope
    def on_specific_annotations_toggled(self, checked):
        if checked:
            self.apply_scope("specific_annotations")

    # Called when the user asks to trim the recording
    def on_trim_checkbox_toggled(self, checked):
        self.enable_trim_widgets(checked)
        if checked:
            self.activate_node(self._node_id_trim_signal)
        else:
            self.bypass_node(self._node_id_trim_signal)

    # -------------------------------------------------------------------------
    # Communication with the pipeline
    # -------------------------------------------------------------------------
    # To ping specific nodes to call on_topic_response
    def load_settings(self):
        self._pub_sub_manager.publish(self, self._low_high_cutoff_topic, 'ping')
        self._pub_sub_manager.publish(self, self._trim_start_time_topic, 'ping')
        self._pub_sub_manager.publish(self, self._trim_duration_time_topic, 'ping')
        self._pub_sub_manager.publish(
            self, self._node_id_trim_signal + ".get_activation_state", None)

        # Make sure the pipeline and the context match the scope selection.
        self.apply_scope(self.get_current_scope())

    def on_topic_update(self, topic, message, sender):
        pass

    # Answer to a ping
    #  The UI is updated from the pipeline.json
    def on_topic_response(self, topic, message, sender):
        if topic == self._low_high_cutoff_topic:
            if message:
                self.select_band_from_cutoff(message)
        elif topic == self._trim_start_time_topic:
            if message:
                self.checkBox.setChecked(True)
                try:
                    self.start_time_doubleSpinBox.setValue(float(message))
                except (TypeError, ValueError):
                    print(f"FilterStep : failed to read the start time {message}")
        elif topic == self._trim_duration_time_topic:
            if message:
                self.checkBox.setChecked(True)
                try:
                    self.duration_doubleSpinBox.setValue(float(message))
                except (TypeError, ValueError):
                    print(f"FilterStep : failed to read the duration {message}")
        elif topic == self._node_id_trim_signal + ".get_activation_state":
            self.checkBox.setChecked(message == ActivationState.ACTIVATED)

    def select_band_from_cutoff(self, cutoff):
        """ Check the radio button matching the cutoff read from the pipeline. """
        try:
            low, high = map(float, str(cutoff).split())
        except (TypeError, ValueError):
            print(f"FilterStep : failed to read the cutoff {cutoff}")
            return

        band_buttons = {
            "fullband": self.fullband_radioButton,
            "delta": self.delta_radioButton,
            "theta": self.theta_radioButton,
            "alpha": self.alpha_radioButton,
            "beta": self.beta_radioButton,
        }
        selected_button = self.custom_radioButton
        for band, band_cutoff in FilterStep.BAND_CUTOFFS.items():
            band_low, band_high = map(float, band_cutoff.split())
            if (low, high) == (band_low, band_high):
                selected_button = band_buttons[band]
                break
        selected_button.setChecked(True)
        self.low_cutoff_doubleSpinBox.setValue(low)
        self.high_cutoff_doubleSpinBox.setValue(high)

    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # Returning False will prevent the process from executing.
        if self.sleep_stages_radioButton.isChecked():
            if not (self.wake_checkBox.isChecked() or self.n1_checkBox.isChecked()
                    or self.n2_checkBox.isChecked() or self.n3_checkBox.isChecked()
                    or self.rem_checkBox.isChecked()):
                WarningDialog(
                    "If you have selected <<Sleep Stages>> for the scope of analysis, "
                    "select at least one sleep stage in the step 'Filter Settings'.")
                return False
        if self.custom_radioButton.isChecked():
            if self.high_cutoff_doubleSpinBox.value() <= self.low_cutoff_doubleSpinBox.value():
                WarningDialog(
                    "In the step 'Filter Settings', the high cutoff of the custom "
                    "frequency band must be higher than the low cutoff.")
                return False
        return True

    # Called when the user clicks on RUN or when the pipeline is saved
    # Message are sent to the publisher
    def on_apply_settings(self):
        # Send the cutoff of the selected frequency band to the Filter Signal module
        if self.custom_radioButton.isChecked():
            cutoff = f"{self.low_cutoff_doubleSpinBox.value()} " \
                     f"{self.high_cutoff_doubleSpinBox.value()}"
        elif self.delta_radioButton.isChecked():
            cutoff = FilterStep.BAND_CUTOFFS["delta"]
        elif self.theta_radioButton.isChecked():
            cutoff = FilterStep.BAND_CUTOFFS["theta"]
        elif self.alpha_radioButton.isChecked():
            cutoff = FilterStep.BAND_CUTOFFS["alpha"]
        elif self.beta_radioButton.isChecked():
            cutoff = FilterStep.BAND_CUTOFFS["beta"]
        else:
            cutoff = FilterStep.BAND_CUTOFFS["fullband"]
        self._pub_sub_manager.publish(self, self._low_high_cutoff_topic, cutoff)

        # Activate the chain matching the selected recording scope
        scope = self.get_current_scope()
        self.set_scope_nodes(scope)

        # Send the selected sleep stages to the Sleep Stage Events module
        if scope == "sleep_stages":
            # Snooz stage codes : Wake=0, N1=1, N2=2, N3=3, REM=5
            selected_stages = []
            if self.wake_checkBox.isChecked():
                selected_stages.append("0")
            if self.n1_checkBox.isChecked():
                selected_stages.append("1")
            if self.n2_checkBox.isChecked():
                selected_stages.append("2")
            if self.n3_checkBox.isChecked():
                selected_stages.append("3")
            if self.rem_checkBox.isChecked():
                selected_stages.append("5")
            self.sleep_stages_names = ','.join(selected_stages)
            self._pub_sub_manager.publish(
                self, self._sleep_stages_topic, self.sleep_stages_names)
        else:
            self.sleep_stages_names = ''
        self.update_context(scope)

        # Send the trim settings to the Trim Signal module
        if self.checkBox.isChecked():
            self.activate_node(self._node_id_trim_signal)
            self._pub_sub_manager.publish(
                self, self._trim_start_time_topic, self.start_time_doubleSpinBox.value())
            self._pub_sub_manager.publish(
                self, self._trim_duration_time_topic, self.duration_doubleSpinBox.value())
        else:
            self.bypass_node(self._node_id_trim_signal)

    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._low_high_cutoff_topic)
            self._pub_sub_manager.unsubscribe(self, self._trim_start_time_topic)
            self._pub_sub_manager.unsubscribe(self, self._trim_duration_time_topic)
