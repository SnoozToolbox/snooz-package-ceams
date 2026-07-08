#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    ConnectivitySettings
    Settings step for connectivity analysis (wPLI/dPLI/AEC, parameters, and routing).

    The pipeline has two branches (annotation and sleep stages) and three
    connectivity methods (wPLI, dPLI, AEC). This step activates only the chain
    matching the current scope (from FilterStep) and the selected method, and
    routes the epoch / connectivity / network-properties parameters to it.
"""

from qtpy import QtWidgets

from CEAMSTools.AnalyzeEEGConnectivity.ConnectivitySettings.Ui_ConnectivitySettings import Ui_ConnectivitySettings
from CEAMSTools.AnalyzeEEGConnectivity.FilterStep.FilterStep import FilterStep
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState

class ConnectivitySettings(BaseStepView, Ui_ConnectivitySettings, QtWidgets.QWidget):
    """
    Step to let the user:
    - Pick between wPLI, dPLI, and AEC (radio buttons)
    - Set epoch and connectivity parameters (line edits)
    - Automatically routes/activates the correct chain for the current scope
      (annotation vs sleep stages) and sends parameters to the correct nodes.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self)

        # --- Node IDs grouped by scope + method chains ---
        # Each chain: epoch -> connectivity -> details (+ network for wPLI).
        self.annotation_wpli = {
            "epoch":   "b680606e-dd88-442e-8969-19b71ea377a0",
            "conn":    "3cace954-8d81-4039-8730-b2a90a67c93b",
            "details": "803b6207-918f-4e3e-b5be-48ad9fc8b01c",
            "network": "02d58c3b-80ec-4e80-8a3c-33d9ee521c18",
        }
        self.annotation_dpli = {
            "epoch":   "fdc0c057-3fb5-4c9f-92f5-23b1474f7a2d",
            "conn":    "327736b2-6d0a-4186-a123-f0e93a85d232",
            "details": "cc042193-2e41-49e0-b80e-973b1174cdb9",
        }
        self.annotation_aec = {
            "epoch":   "829d7060-7e36-412a-9857-bfa39dfacaf0",
            "conn":    "a8b8a023-ed8d-4a5c-a896-1d7051ee058c",
            "details": "838795ca-9563-4370-918e-f8f92cc23220",
        }
        self.sleep_wpli = {
            "epoch":   "5a62634e-6fad-4e52-8d8a-01e4f3ce6dbd",
            "conn":    "727ba862-fd21-43df-82b9-f399918f587d",
            "details": "209980db-ecf3-4d88-9f66-c27373268a3b",
            "network": "9b9b5bb5-f0a3-44f4-8d31-b3ee1896f725",
        }
        self.sleep_dpli = {
            "epoch":   "a120bd2f-4d9b-4e08-8e45-ce51d577ae9f",
            "conn":    "2c8437e3-9a1b-4584-86b0-54308d9bb6f2",
            "details": "82b687e5-9cb4-43bc-80a8-b1cd735ded9b",
        }
        self.sleep_aec = {
            "epoch":   "41f96138-814c-492c-bac8-fe01b4c3f65e",
            "conn":    "2d967628-7e28-4b27-98f7-2abb069204df",
            "details": "7f93939c-b105-4637-a8e9-eae8fc40ceb1",
        }

        # --- Connect radio buttons to method change handler ---
        self.dpli_radioButton.toggled.connect(self.on_method_changed)
        self.wpli_radioButton.toggled.connect(self.on_method_changed)
        self.aec_radioButton.toggled.connect(self.on_method_changed)
        self.custom_threshold_radioButton.toggled.connect(self.on_threshold_mode_changed)
        self.mst_radioButton.toggled.connect(self.on_threshold_mode_changed)

        self.on_method_changed()  # Initialize method selection and module activation


    # ------------------------------------------------------------------ #
    #  Scope / method helpers
    # ------------------------------------------------------------------ #
    def _all_chains(self):
        return [
            self.annotation_wpli, self.annotation_dpli, self.annotation_aec,
            self.sleep_wpli, self.sleep_dpli, self.sleep_aec,
        ]

    def _active_scope_branch(self):
        """
        Return "sleep" when the FilterStep scope is sleep stages, "annotation"
        otherwise (specific annotations OR unscored both use the annotation
        branch nodes, the latter with SignalsFromEvents bypassed).
        """
        try:
            scope = self._context_manager[FilterStep.context_Con_scope]
        except (KeyError, TypeError):
            scope = "sleep_stages"
        return "sleep" if scope == "sleep_stages" else "annotation"

    def _active_method(self):
        if self.dpli_radioButton.isChecked():
            return "dpli"
        if self.aec_radioButton.isChecked():
            return "aec"
        return "wpli"

    def _active_chain(self):
        return getattr(self, f"{self._active_scope_branch()}_{self._active_method()}")

    def _sync_activation(self):
        """Deactivate every chain, then activate only the active scope+method chain."""
        for chain in self._all_chains():
            for node_id in chain.values():
                self.deactivate_node(node_id)
        for node_id in self._active_chain().values():
            self.activate_node(node_id)


    # ------------------------------------------------------------------ #
    #  UI widget state
    # ------------------------------------------------------------------ #
    def on_threshold_mode_changed(self):
        is_wpli = (self._active_method() == "wpli")
        if is_wpli and self.custom_threshold_radioButton.isChecked():
            self.threshold_val_doubleSpinBox.setEnabled(True)
            self.threshold_val_label.setEnabled(True)
        else:
            self.threshold_val_doubleSpinBox.setEnabled(False)
            self.threshold_val_label.setEnabled(False)

    def _update_method_widgets(self):
        method = self._active_method()
        is_wpli = (method == "wpli")
        is_stats = method in ("wpli", "dpli")  # surrogate-based statistics

        self.connectivity_settings_header_label.setEnabled(is_stats)
        self.connectivity_settings_label.setEnabled(is_stats)
        self.num_surr_label.setEnabled(is_stats)
        self.num_surr_lineedit.setEnabled(is_stats)
        self.p_value_label.setEnabled(is_stats)
        self.p_value_lineedit.setEnabled(is_stats)

        # Network properties (and its thresholding) are only relevant for wPLI.
        self.network_properties_header_label.setEnabled(is_wpli)
        self.network_properties_textEdit.setEnabled(is_wpli)
        self.select_mode_label.setEnabled(is_wpli)
        self.custom_threshold_radioButton.setEnabled(is_wpli)
        self.mst_radioButton.setEnabled(is_wpli)
        self.threshold_val_doubleSpinBox.setEnabled(is_wpli)
        self.threshold_val_label.setEnabled(is_wpli)

    def on_method_changed(self):
        """
        When the user switches method, activate the correct chain for the current
        scope and update which parameter widgets are enabled.
        """
        self._sync_activation()
        self._update_method_widgets()
        self.on_threshold_mode_changed()


    # ------------------------------------------------------------------ #
    #  Node activation helpers
    # ------------------------------------------------------------------ #
    def activate_node(self, node_id):
        """Helper to activate a module/node by its ID."""
        self._pub_sub_manager.publish(
            self, f"{node_id}.activation_state_change", ActivationState.ACTIVATED
        )

    def deactivate_node(self, node_id):
        """Helper to deactivate a module/node by its ID."""
        self._pub_sub_manager.publish(
            self, f"{node_id}.activation_state_change", ActivationState.DEACTIVATED
        )


    # ------------------------------------------------------------------ #
    #  Settings lifecycle
    # ------------------------------------------------------------------ #
    def on_apply_settings(self):
        """
        Push the lineEdit values to the active chain, depending on the selected
        scope (annotation/sleep) and method (wPLI/dPLI/AEC).
        """
        epoch_length = self.epoch_length_lineEdit.text().strip()
        epoch_overlap = self.epoch_overlap_lineEdit.text().strip()
        num_surr = self.num_surr_lineedit.text().strip()
        p_value = self.p_value_lineedit.text().strip()

        chain = self._active_chain()
        method = self._active_method()

        # Epoch parameters (all methods use EpochSignal).
        self._pub_sub_manager.publish(self, f"{chain['epoch']}.epoch_length_sec", epoch_length)
        self._pub_sub_manager.publish(self, f"{chain['epoch']}.overlap_sec", epoch_overlap)

        # Surrogate-based statistics (wPLI and dPLI only).
        if method in ("wpli", "dpli"):
            self._pub_sub_manager.publish(self, f"{chain['conn']}.num_surr", num_surr)
            self._pub_sub_manager.publish(self, f"{chain['conn']}.p_value", p_value)

        # Network properties thresholding (wPLI only).
        if method == "wpli" and "network" in chain:
            if self.custom_threshold_radioButton.isChecked():
                threshold = self.threshold_val_doubleSpinBox.value()
                self._pub_sub_manager.publish(self, f"{chain['network']}.threshold_value", threshold)
                self._pub_sub_manager.publish(self, f"{chain['network']}.threshold_mode", 'custom_threshold')
            elif self.mst_radioButton.isChecked():
                self._pub_sub_manager.publish(self, f"{chain['network']}.threshold_mode", 'minimally_spanning_tree')

    def load_settings(self):
        # Re-sync activation with the scope selected in FilterStep (the scope may
        # have changed before this step was opened).
        self._sync_activation()
        self._update_method_widgets()
        self.on_threshold_mode_changed()

    def on_validate_settings(self):
        """
        Optional: Check if all fields are filled before allowing to apply settings.
        """
        return True

    def on_topic_update(self, topic, message, sender):
        # React to a scope change from FilterStep by re-routing the active chain.
        if topic == self._context_manager.topic:
            if message == FilterStep.context_Con_scope:
                self._sync_activation()

    def on_topic_response(self, topic, message, sender):
        # Not used, but could be for advanced sync
        pass
