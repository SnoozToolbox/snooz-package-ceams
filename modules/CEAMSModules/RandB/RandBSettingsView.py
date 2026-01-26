"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the RandB plugin
"""

from qtpy import QtWidgets

from CEAMSModules.RandB.Ui_RandBSettingsView import Ui_RandBSettingsView
from commons.BaseSettingsView import BaseSettingsView

class RandBSettingsView(BaseSettingsView, Ui_RandBSettingsView, QtWidgets.QWidget):
    """
        RandBView set the RandB settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._win_len_sec_topic = f'{self._parent_node.identifier}.win_len_sec'
        self._pub_sub_manager.subscribe(self, self._win_len_sec_topic)
        self._win_step_sec_topic = f'{self._parent_node.identifier}.win_step_sec'
        self._pub_sub_manager.subscribe(self, self._win_step_sec_topic)
        self._window_name_topic = f'{self._parent_node.identifier}.window_name'
        self._pub_sub_manager.subscribe(self, self._window_name_topic)
        self._first_freq_topic = f'{self._parent_node.identifier}.first_freq'
        self._pub_sub_manager.subscribe(self, self._first_freq_topic)
        self._last_freq_topic = f'{self._parent_node.identifier}.last_freq'
        self._pub_sub_manager.subscribe(self, self._last_freq_topic)        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._win_len_sec_topic, 'ping')
        self._pub_sub_manager.publish(self, self._win_step_sec_topic, 'ping')
        self._pub_sub_manager.publish(self, self._window_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._first_freq_topic, 'ping')
        self._pub_sub_manager.publish(self, self._last_freq_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to RandB
        self._pub_sub_manager.publish(self, self._win_len_sec_topic, str(self.win_len_sec_lineedit.text()))
        self._pub_sub_manager.publish(self, self._win_step_sec_topic, str(self.win_step_sec_lineedit.text()))
        self._pub_sub_manager.publish(self, self._window_name_topic, str(self.window_name_lineedit.text()))
        self._pub_sub_manager.publish(self, self._last_freq_topic, str(self.last_freq_lineedit.text()))
        self._pub_sub_manager.publish(self, self._first_freq_topic, str(self.first_freq_lineedit.text()))
        

    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._win_len_sec_topic:
            self.win_len_sec_lineedit.setText(message)
        if topic == self._win_step_sec_topic:
            self.win_step_sec_lineedit.setText(message)
        if topic == self._window_name_topic:
            self.window_name_lineedit.setText(message)
        if topic == self._first_freq_topic:
            self.first_freq_lineedit.setText(message)
        if topic == self._last_freq_topic:
            self.last_freq_lineedit.setText(message)    
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._win_len_sec_topic)
            self._pub_sub_manager.unsubscribe(self, self._win_step_sec_topic)
            self._pub_sub_manager.unsubscribe(self, self._window_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._last_freq_topic)
            self._pub_sub_manager.unsubscribe(self, self._first_freq_topic)
           
            
