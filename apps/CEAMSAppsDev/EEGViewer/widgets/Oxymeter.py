"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2 import QtCore

from CEAMSApps.EEGViewer.Managers.EventsManager import EventsManager
from CEAMSApps.EEGViewer.Managers.SignalsManager import SignalsManager
#from managers.PubSubManager import PubSubManager

#from models.UserContextModel import UserContextModel
#from models.FileInfoModel import FileInfoModel

from CEAMSApps.EEGViewer.ui.oxymeter import Ui_Oxymeter

from CEAMSModules.PSGReader.PSGReaderManager import PSGReaderManager

# Subclass QMainWindow to customize your application's main window
class Oxymeter(QWidget, Ui_Oxymeter):
    def __init__(self, signal_models, selected_montage, selected_oxymeter_channel):
        super().__init__()

        self.setupUi(self)

        # init variables
        self._signal_models = signal_models
        self._selected_montage = selected_montage
        self._selected_oxymeter_channel = selected_oxymeter_channel
        self._current_user_context = None
        self._current_filename = None
        self._current_montage_name = None
        self._current_oxymeter_channel_name = None
        self._current_montage_index = None
        self._pub_sub_manager = None
        self._current_signal_models = []
        self._event_name = "art_SpO2"
        self._group_name = "SpO2"

        self.ymin_comboBox.setCurrentText("80")

        if self._selected_oxymeter_channel is None:
            return
        
        # Find the oxymeter signal model
        #self._oxymeter_signal_model = None
        self._current_signal_models = []
        for signal_model in self._signal_models:
            if signal_model.channel == self._selected_oxymeter_channel:
                for oxy_signal_model in signal_model.signal_chunks:
                    resampled_signal_model = SignalsManager.resample_signal(oxy_signal_model, 1)
                    self._current_signal_models.append(resampled_signal_model)

                #self._oxymeter_signal_model = signal_model
                break
        
        if len(self._current_signal_models) == 0:
            return
        
        self.oxymeter_draw_area.set_signal_models(self._current_signal_models)
        self.set_exclusion_events()


    # @property
    # def pub_sub_manager(self):
    #     return self._pub_sub_manager

    # @pub_sub_manager.setter
    # def pub_sub_manager(self, pub_sub_manager: PubSubManager):
    #     self._pub_sub_manager = pub_sub_manager
    #     self.oxymeter_draw_area.pub_sub_manager = pub_sub_manager

    # @property
    # def signals_manager(self):
    #     return self._signals_manager

    # @signals_manager.setter
    # def signals_manager(self, signals_manager: SignalsManager):
    #     self._signals_manager = signals_manager
    
    # @property
    # def events_manager(self):
    #     return self._events_manager
    
    # @events_manager.setter
    # def events_manager(self, events_manager: EventsManager):
    #     self._events_manager = events_manager

    # @QtCore.Slot()
    # def on_settings_changed(self, user_context: UserContextModel, file_info_model:FileInfoModel):
    #     if user_context.current_filename != self._current_filename or \
    #         user_context.current_montage_name != self._current_montage_name or \
    #         user_context.current_oxymeter_channel_name != self._current_oxymeter_channel_name:

    #         self._current_user_context = user_context
    #         self._current_filename = user_context.current_filename
    #         self._current_montage_name = user_context.current_montage_name
    #         self._current_oxymeter_channel_name = user_context.current_oxymeter_channel_name

    #         if self._current_oxymeter_channel_name is None:
    #             self._current_signal_models = []
    #             self.oxymeter_draw_area.reset_exclusion_events()
    #         else:
    #             oxy_signal_models = self._signals_manager.get_signal(user_context.current_oxymeter_channel_name)
    #             self._current_signal_models = []
    #             for oxy_signal_model in oxy_signal_models:
    #                 resampled_signal_model = SignalsManager.resample_signal(oxy_signal_model, 1)
    #                 self._current_signal_models.append(resampled_signal_model)

    #         self.set_exclusion_events()
    #         self.oxymeter_draw_area.set_signal_models(self._current_signal_models)
    
    # def register_listeners(self):
    #     self._pub_sub_manager.subscribe(self, "file_loaded")
    #     self._pub_sub_manager.subscribe(self, "time_cursor_changed")

    # def unregister_listeners(self):
    #     self._pub_sub_manager.unsubscribe(self, "file_loaded")
    #     self._pub_sub_manager.unsubscribe(self, "time_cursor_changed")

    # def on_topic_update(self, topic, message, sender):
    #     if topic == "file_loaded":
    #         self.oxymeter_draw_area.file_info = message.file_info
    #     elif topic == "time_cursor_changed":
    #         self.oxymeter_draw_area.time_cursor = message

    def set_exclusion_events(self):
        #if self._events_manager.events is None:
        #    self.oxymeter_draw_area.exclusion_events = []
        #    return
        if self._selected_oxymeter_channel is None:
            return
        
        _signal_models = self._signal_models
        # Find the oxymeter signal model
        oxymeter_signal_model = None
        for signal_model in _signal_models:
            if signal_model.channel_name == self._selected_oxymeter_channel:
                oxymeter_signal_model = signal_model
                break

        if oxymeter_signal_model is None:
            return

        exclusion_events = []
        for event_model in oxymeter_signal_model.event_models:
            if event_model.name == self._event_name and event_model.group == self._group_name:
                end_sec = event_model.start_sec + event_model.duration_sec
                exclusion_events.append((event_model.start_sec, end_sec))
        
        self.oxymeter_draw_area.exclusion_events = exclusion_events

        #exclusion_events = self._events_manager.events[self._events_manager.events["group"] == self._group_name]
        #exclusion_events = exclusion_events[exclusion_events["name"] == self._event_name]

        # events = []
        # for index, row in exclusion_events.iterrows():
        #     start_time = row["start_sec"]
        #     end_time = start_time + row["duration_sec"]
        #     events.append((start_time, end_time))
        
        # self.oxymeter_draw_area.exclusion_events = events

    def on_apply(self):
        if self._current_filename is None:
            return
        
        # Remove all previous exclusion events

        # Add selected exclusion events



        for row in self._events.itertuples():
            if channel_name in row.channels:
                event_model = EventModel()
                event_model.start_sec = row.start_sec
                event_model.duration_sec = row.duration_sec
                event_model.group = row.group
                event_model.name = row.name
                signal_model.add_event_model(event_model)

        self._signal_models.append(signal_model)


        # Show a confirmation message box
        confirmation = QMessageBox()
        confirmation.setIcon(QMessageBox.Question)
        confirmation.setText("Are you sure you want to apply the changes?")
        confirmation.setWindowTitle("Confirmation")
        confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirmation.setDefaultButton(QMessageBox.No)
        result = confirmation.exec_()
        
        if result == QMessageBox.No:
            return

        psg_reader_manager = PSGReaderManager()
        success = psg_reader_manager.open_file(self._current_filename)
        if not success:
            log_msg = QMessageBox()
            log_msg.setWindowTitle("Error")
            log_msg.setText(f"Could not save file {self._current_filename}")
            log_msg.setIcon(QMessageBox.Critical)
            log_msg.exec_()

            psg_reader_manager.close_file()
            return
        
        psg_reader_manager.remove_events_by_name(self._event_name, self._group_name)
        for exclusion_event in self.oxymeter_draw_area.exclusion_events:
            start_time = min(exclusion_event)
            end_time = max(exclusion_event)
            duration = end_time - start_time
            montage_index = psg_reader_manager.get_montage_index(self._current_montage_name)
            success = psg_reader_manager.add_event("art_SpO2", "SpO2", start_time, duration, \
                                         self._current_oxymeter_channel_name, \
                                         montage_index)
            if not success:
                error_message = psg_reader_manager.get_last_error()
                log_msg = QMessageBox()
                log_msg.setWindowTitle("Error")
                log_msg.setText(f"Could not add event to file: {error_message}")
                log_msg.setIcon(QMessageBox.Critical)
                log_msg.exec_()
                psg_reader_manager.close_file()
                return

        psg_reader_manager.save_file()
        psg_reader_manager.close_file()
        self._events_manager.reload_events()
        self.set_exclusion_events()

        # Show a completion message box
        completion = QMessageBox()
        completion.setIcon(QMessageBox.Information)
        completion.setText("File saved successfully!")
        completion.setWindowTitle("Completion")
        completion.setStandardButtons(QMessageBox.Ok)
        completion.exec_()
        
    def remove_all_clicked(self):
        self.oxymeter_draw_area.reset_exclusion_events()

    def on_reset(self):
        self.set_exclusion_events()

    def min_saturation_change(self, text):
        self.oxymeter_draw_area.min_saturation = int(text)
        self.oxymeter_draw_area.update()
