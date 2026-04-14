#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    ConnectivitySettings
    Settings step for connectivity analysis (wPLI/dPLI, parameters, and routing).
"""

from qtpy import QtWidgets

from CEAMSTools.AnalyzeEEGConnectivity.ConnectivitySettings.Ui_ConnectivitySettings import Ui_ConnectivitySettings
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState

class ConnectivitySettings(BaseStepView, Ui_ConnectivitySettings, QtWidgets.QWidget):
    """
    Step to let the user:
    - Pick between wPLI, dPLI, and AEC (radio buttons)
    - Set epoch and connectivity parameters (line edits)
    - Automatically routes/activates all modules and sends parameters to the correct nodes.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self)

        # --- Node IDs for WPLI and DPLI chains ---
        self.connectivitydetails_node_id_wpli = "803b6207-918f-4e3e-b5be-48ad9fc8b01c"
        self.wpliconnectivity_node_id = "3cace954-8d81-4039-8730-b2a90a67c93b"
        self.epochsignal_node_id_wpli = "b680606e-dd88-442e-8969-19b71ea377a0"
        self.networkproperties_node_id = "02d58c3b-80ec-4e80-8a3c-33d9ee521c18"
        

        self.connectivitydetails_node_id_dpli = "cc042193-2e41-49e0-b80e-973b1174cdb9"
        self.dpliconnectivity_node_id = "327736b2-6d0a-4186-a123-f0e93a85d232"
        self.epochsignal_node_id_dpli = "fdc0c057-3fb5-4c9f-92f5-23b1474f7a2d"


        self.connectivitydetails_node_id_aec = "838795ca-9563-4370-918e-f8f92cc23220"
        self.aecconnectivity_node_id = "a8b8a023-ed8d-4a5c-a896-1d7051ee058c"
        self.epochsignal_node_id_aec = "829d7060-7e36-412a-9857-bfa39dfacaf0"

        # --- Connect radio buttons to method change handler ---
        self.dpli_radioButton.toggled.connect(self.on_method_changed)
        self.wpli_radioButton.toggled.connect(self.on_method_changed)
        self.aec_radioButton.toggled.connect(self.on_method_changed)
        self.custom_threshold_radioButton.toggled.connect(self.on_threshold_mode_changed)
        self.mst_radioButton.toggled.connect(self.on_threshold_mode_changed)

        self.on_threshold_mode_changed()  # Initialize threshold mode UI state
        self.on_method_changed()  # Initialize method selection and module activation

        # # --- Default to wPLI checked and modules activated ---
        # self.wpli_radioButton.setChecked(True)
        # self.on_method_changed()  # Ensures everything is initialized correctly


    def on_threshold_mode_changed(self):
        if self.custom_threshold_radioButton.isChecked():
            self.threshold_val_doubleSpinBox.setEnabled(True)
            self.threshold_val_label.setEnabled(True)
        else:
            self.threshold_val_doubleSpinBox.setEnabled(False)
            self.threshold_val_label.setEnabled(False)


    def on_method_changed(self):
        """
        When user switches between wPLI and dPLI, activate the relevant modules
        and deactivate the irrelevant ones.
        """
        if self.wpli_radioButton.isChecked():
            # Activate wPLI modules, deactivate dPLI modules and aec modules
            self.activate_node(self.connectivitydetails_node_id_wpli)
            self.activate_node(self.wpliconnectivity_node_id)
            self.activate_node(self.epochsignal_node_id_wpli)
            self.activate_node(self.networkproperties_node_id)

            self.connectivity_settings_header_label.setEnabled(True)
            self.connectivity_settings_label.setEnabled(True)

            self.num_surr_label.setEnabled(True)
            self.num_surr_lineedit.setEnabled(True)
            self.p_value_label.setEnabled(True)
            self.p_value_lineedit.setEnabled(True)

            self.network_properties_header_label.setEnabled(True)
            self.network_properties_textEdit.setEnabled(True)
            self.select_mode_label.setEnabled(True)

            self.custom_threshold_radioButton.setEnabled(True)
            self.mst_radioButton.setEnabled(True)
            self.threshold_val_doubleSpinBox.setEnabled(True)
            self.threshold_val_label.setEnabled(True)


            self.deactivate_node(self.connectivitydetails_node_id_dpli)
            self.deactivate_node(self.dpliconnectivity_node_id)
            self.deactivate_node(self.epochsignal_node_id_dpli)

            self.deactivate_node(self.connectivitydetails_node_id_aec)
            self.deactivate_node(self.aecconnectivity_node_id)
            self.deactivate_node(self.epochsignal_node_id_aec)


            self.on_threshold_mode_changed()  # Update threshold mode UI based on current selection
            

        elif self.dpli_radioButton.isChecked():
            # Activate dPLI modules, deactivate wPLI modules and aec modules
            self.activate_node(self.connectivitydetails_node_id_dpli)
            self.activate_node(self.dpliconnectivity_node_id)
            self.activate_node(self.epochsignal_node_id_dpli)

            self.connectivity_settings_header_label.setEnabled(True)
            self.connectivity_settings_label.setEnabled(True)

            self.num_surr_label.setEnabled(True)
            self.num_surr_lineedit.setEnabled(True)
            self.p_value_label.setEnabled(True)
            self.p_value_lineedit.setEnabled(True)

            self.deactivate_node(self.connectivitydetails_node_id_wpli)
            self.deactivate_node(self.wpliconnectivity_node_id)
            self.deactivate_node(self.epochsignal_node_id_wpli)
            self.deactivate_node(self.networkproperties_node_id)

            self.deactivate_node(self.connectivitydetails_node_id_aec)
            self.deactivate_node(self.aecconnectivity_node_id)
            self.deactivate_node(self.epochsignal_node_id_aec)

            self.network_properties_header_label.setEnabled(False)
            self.network_properties_textEdit.setEnabled(False)
            self.select_mode_label.setEnabled(False)

            self.custom_threshold_radioButton.setEnabled(False)
            self.mst_radioButton.setEnabled(False)
            self.threshold_val_doubleSpinBox.setEnabled(False)
            self.threshold_val_label.setEnabled(False)
        
        elif self.aec_radioButton.isChecked():
            # Activate AEC modules, deactivate wPLI and dPLI modules
            self.activate_node(self.connectivitydetails_node_id_aec)
            self.activate_node(self.aecconnectivity_node_id)
            self.activate_node(self.epochsignal_node_id_aec)

            self.deactivate_node(self.connectivitydetails_node_id_wpli)
            self.deactivate_node(self.wpliconnectivity_node_id)
            self.deactivate_node(self.epochsignal_node_id_wpli)
            self.deactivate_node(self.networkproperties_node_id)

            self.deactivate_node(self.connectivitydetails_node_id_dpli)
            self.deactivate_node(self.dpliconnectivity_node_id)
            self.deactivate_node(self.epochsignal_node_id_dpli)
            
            # For AEC, disable thresholding options and stats parameters as they are not relevant
            self.connectivity_settings_header_label.setEnabled(False)
            self.connectivity_settings_label.setEnabled(False)

            self.network_properties_header_label.setEnabled(False)
            self.network_properties_textEdit.setEnabled(False)
            self.select_mode_label.setEnabled(False)
            
            self.num_surr_label.setEnabled(False)
            self.num_surr_lineedit.setEnabled(False)
            self.p_value_label.setEnabled(False)
            self.p_value_lineedit.setEnabled(False)


            self.custom_threshold_radioButton.setEnabled(False)
            self.mst_radioButton.setEnabled(False)
            self.threshold_val_doubleSpinBox.setEnabled(False)
            self.threshold_val_label.setEnabled(False)

    def activate_node(self, node_id):
        """
        Helper to activate a module/node by its ID.
        """
        self._pub_sub_manager.publish(
            self, f"{node_id}.activation_state_change", ActivationState.ACTIVATED
        )

    def deactivate_node(self, node_id):
        """
        Helper to deactivate a module/node by its ID.
        """
        self._pub_sub_manager.publish(
            self, f"{node_id}.activation_state_change", ActivationState.DEACTIVATED
        )

    def on_apply_settings(self):
        """
        When user hits Apply/OK, push the lineEdit values to the right modules,
        depending on method selected (wPLI or dPLI).
        """
        epoch_length = self.epoch_length_lineEdit.text().strip()
        epoch_overlap = self.epoch_overlap_lineEdit.text().strip()
        num_surr = self.num_surr_lineedit.text().strip()
        p_value = self.p_value_lineedit.text().strip()

        if self.wpli_radioButton.isChecked():
            # Push epoch parameters to epochsignal_node_id_wpli
            self._pub_sub_manager.publish(self, f"{self.epochsignal_node_id_wpli}.epoch_length_sec", epoch_length)
            self._pub_sub_manager.publish(self, f"{self.epochsignal_node_id_wpli}.overlap_sec", epoch_overlap)
            # Push connectivity params to wpliconnectivity_node_id
            self._pub_sub_manager.publish(self, f"{self.wpliconnectivity_node_id}.num_surr", num_surr)
            self._pub_sub_manager.publish(self, f"{self.wpliconnectivity_node_id}.p_value", p_value)

            if self.custom_threshold_radioButton.isChecked():
                threshold = self.threshold_val_doubleSpinBox.value()
                self._pub_sub_manager.publish(self, f"{self.networkproperties_node_id}.threshold_value", threshold)
                self._pub_sub_manager.publish(self, f"{self.networkproperties_node_id}.threshold_mode", 'custom_threshold')

            elif self.mst_radioButton.isChecked():
                self._pub_sub_manager.publish(self, f"{self.networkproperties_node_id}.threshold_mode", 'minimally_spanning_tree')

        elif self.dpli_radioButton.isChecked():
            # Push epoch parameters to epochsignal_node_id_dpli
            self._pub_sub_manager.publish(self, f"{self.epochsignal_node_id_dpli}.epoch_length_sec", epoch_length)
            self._pub_sub_manager.publish(self, f"{self.epochsignal_node_id_dpli}.overlap_sec", epoch_overlap)
            # Push connectivity params to dpliconnectivity_node_id
            self._pub_sub_manager.publish(self, f"{self.dpliconnectivity_node_id}.num_surr", num_surr)
            self._pub_sub_manager.publish(self, f"{self.dpliconnectivity_node_id}.p_value", p_value)

        elif self.aec_radioButton.isChecked():
            # Push epoch parameters to epochsignal_node_id_aec
            self._pub_sub_manager.publish(self, f"{self.epochsignal_node_id_aec}.epoch_length_sec", epoch_length)
            self._pub_sub_manager.publish(self, f"{self.epochsignal_node_id_aec}.overlap_sec", epoch_overlap)

    def load_settings(self):
        # Could ping nodes for initial values to display (optional, not strictly needed)
        pass

    def on_validate_settings(self):
        """
        Optional: Check if all fields are filled before allowing to apply settings.
        """
        # You could add more checks here if needed
        return True

    def on_topic_update(self, topic, message, sender):
        # Not used, but could be for advanced sync
        pass

    def on_topic_response(self, topic, message, sender):
        # Not used, but could be for advanced sync
        pass
