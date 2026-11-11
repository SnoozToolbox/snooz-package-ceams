"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Settings viewer of the LempZivComplexity plugin
"""

from qtpy import QtWidgets

from CEAMSModules.LempZivComplexity.Ui_LempZivComplexitySettingsView import Ui_LempZivComplexitySettingsView
from commons.BaseSettingsView import BaseSettingsView

class LempZivComplexitySettingsView(BaseSettingsView, Ui_LempZivComplexitySettingsView, QtWidgets.QWidget):
    """
        LempZivComplexityView set the LempZivComplexity settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        # Hint for mode line edit (epochs/events are usually wired in the graph)
        if hasattr(self, 'mode_lineedit'):
            self.mode_lineedit.setPlaceholderText('joint | concat | univariate')

        # Subscribe to the proper topics to send/get data from the node
        self._epochs_topic = f'{self._parent_node.identifier}.epochs'
        self._pub_sub_manager.subscribe(self, self._epochs_topic)
        self._events_topic = f'{self._parent_node.identifier}.events'
        self._pub_sub_manager.subscribe(self, self._events_topic)
        self._mode_topic = f'{self._parent_node.identifier}.mode'
        self._pub_sub_manager.subscribe(self, self._mode_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._epochs_topic, 'ping')
        self._pub_sub_manager.publish(self, self._events_topic, 'ping')
        self._pub_sub_manager.publish(self, self._mode_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to LempZivComplexity
        self._pub_sub_manager.publish(self, self._epochs_topic, str(self.epochs_lineedit.text()))
        self._pub_sub_manager.publish(self, self._events_topic, str(self.events_lineedit.text()))
        self._pub_sub_manager.publish(self, self._mode_topic, str(self.mode_lineedit.text()))
        


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._epochs_topic:
            self.epochs_lineedit.setText(message)
        if topic == self._events_topic:
            self.events_lineedit.setText(message)
        if topic == self._mode_topic:
            self.mode_lineedit.setText(message)
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._epochs_topic)
            self._pub_sub_manager.unsubscribe(self, self._events_topic)
            self._pub_sub_manager.unsubscribe(self, self._mode_topic)
            