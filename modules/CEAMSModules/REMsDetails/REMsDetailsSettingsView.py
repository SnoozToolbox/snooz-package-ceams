"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the REMsDetails plugin
"""

from qtpy import QtWidgets

from CEAMSModules.REMsDetails.Ui_REMsDetailsSettingsView import Ui_REMsDetailsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class REMsDetailsSettingsView(BaseSettingsView, Ui_REMsDetailsSettingsView, QtWidgets.QWidget):
    """
        REMsDetailsView set the REMsDetails settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._recording_path_topic = f'{self._parent_node.identifier}.recording_path'
        self._pub_sub_manager.subscribe(self, self._recording_path_topic)
        self._subject_info_topic = f'{self._parent_node.identifier}.subject_info'
        self._pub_sub_manager.subscribe(self, self._subject_info_topic)
        self._signals_topic = f'{self._parent_node.identifier}.signals'
        self._pub_sub_manager.subscribe(self, self._signals_topic)
        self._rems_events_details_topic = f'{self._parent_node.identifier}.rems_events_details'
        self._pub_sub_manager.subscribe(self, self._rems_events_details_topic)
        self._artifact_events_topic = f'{self._parent_node.identifier}.artifact_events'
        self._pub_sub_manager.subscribe(self, self._artifact_events_topic)
        self._sleep_cycle_param_topic = f'{self._parent_node.identifier}.sleep_cycle_param'
        self._pub_sub_manager.subscribe(self, self._sleep_cycle_param_topic)
        self._rems_det_param_topic = f'{self._parent_node.identifier}.rems_det_param'
        self._pub_sub_manager.subscribe(self, self._rems_det_param_topic)
        self._cohort_filename_topic = f'{self._parent_node.identifier}.cohort_filename'
        self._pub_sub_manager.subscribe(self, self._cohort_filename_topic)
        self._export_rems_topic = f'{self._parent_node.identifier}.export_rems'
        self._pub_sub_manager.subscribe(self, self._export_rems_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        pass

    def save_settings(self):
        """ Called when the user click on the save button
        Publish the settings to the node
        """
        pass

