"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the DefineEventGroup plugin
"""

from qtpy import QtWidgets

from CEAMSModules.DefineEventGroup.Ui_DefineEventGroupSettingsView import Ui_DefineEventGroupSettingsView
from commons.BaseSettingsView import BaseSettingsView

class DefineEventGroupSettingsView(BaseSettingsView, Ui_DefineEventGroupSettingsView, QtWidgets.QWidget):
    """
        DefineEventGroupView set the DefineEventGroup settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._events_topic = f'{self._parent_node.identifier}.events'
        self._pub_sub_manager.subscribe(self, self._events_topic)
        self._groups_topic = f'{self._parent_node.identifier}.groups'
        self._pub_sub_manager.subscribe(self, self._groups_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        
        self._pub_sub_manager.publish(self, self._events_topic, 'ping')
        self._pub_sub_manager.publish(self, self._groups_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        
        # Send the settings to the publisher for inputs to DefineEventGroup
        self._pub_sub_manager.publish(self, self._events_topic, str(self.events_lineedit.text()))
        self._pub_sub_manager.publish(self, self._groups_topic, str(self.groups_lineedit.text()))
        

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """

        if topic == self._events_topic:
            self.events_lineedit.setText(message)
        if topic == self._groups_topic:
            self.groups_lineedit.setText(message)
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._events_topic)
            self._pub_sub_manager.unsubscribe(self, self._groups_topic)
            