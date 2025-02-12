"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
DEBUG = False
from pandas import DataFrame
from qtpy import QtWidgets, QtCore
from qtpy.QtWidgets import QFrame

from CEAMSApps.EEGViewer.Dialogs.ChannelSelectionDialog import ChannelSelectionDialog
from CEAMSApps.EEGViewer.Ui_EEGViewerView import Ui_EEGViewerView
from CEAMSApps.EEGViewer.Managers.SignalsManager import SignalsManager
from CEAMSApps.EEGViewer.widgets.SignalsWidget.SignalsWidget import SignalsWidget
from CEAMSApps.EEGViewer.Models.EventModel import EventModel
from CEAMSApps.EEGViewer.Models.SignalModel import SignalModel
from CEAMSApps.EEGViewer.widgets.Oxymeter import Oxymeter

from CEAMSModules.PSGReader.PSGReaderManager import PSGReaderManager

class EEGViewerView(Ui_EEGViewerView, QtWidgets.QWidget):
    """
    """
    def __init__(self, managers, params, **kwargs):
        super().__init__(**kwargs)
        self._managers = managers
        self._params = params
        self._selected_montage = None
        self._selected_channels = []
        self._selected_oxymeter = None
        self._current_filename = None
        
        self._signals_manager = SignalsManager()
        self._signals_manager.signals_loaded.connect(self.signal_loaded)

       
        # init UI
        self.setupUi(self)

        self._signals_widget = SignalsWidget(self)
        self.main_layout.addWidget(self._signals_widget)

        # Move the control buttons to the navigation bar
        self._managers.navigation_manager.add_app_widget(self.open_file_pushButton)
        self._managers.navigation_manager.add_app_widget(self.save_file_pushButton)
        self._managers.navigation_manager.add_app_widget(self.close_file_pushButton)

        # Create horizontal line widget
        self._line = QtWidgets.QFrame()
        self._line.setObjectName(u"line")
        self._line.setFrameShape(QFrame.HLine)
        self._line.setFrameShadow(QFrame.Sunken)

        self._managers.navigation_manager.add_app_widget(self._line)
        self._managers.navigation_manager.add_app_widget(self.channels_pushButton)
        self._managers.navigation_manager.add_app_widget(self.event_pushButton)
        self._managers.navigation_manager.add_app_widget(self.hypnogram_pushButton)
        self._managers.navigation_manager.add_app_widget(self.oxymeter_pushButton)
        self.nav_buttons_widget.setVisible(False)
        

        if params is not None and "startup_action" in params and params["startup_action"] == "open_file":
            self.open_file()
    
    def close_app(self):
        self._managers.navigation_manager.remove_app_widget(self.open_file_pushButton)
        self._managers.navigation_manager.remove_app_widget(self.save_file_pushButton)
        self._managers.navigation_manager.remove_app_widget(self.close_file_pushButton)
        self._managers.navigation_manager.remove_app_widget(self._line)
        self._managers.navigation_manager.remove_app_widget(self.channels_pushButton)
        self._managers.navigation_manager.remove_app_widget(self.event_pushButton)
        self._managers.navigation_manager.remove_app_widget(self.hypnogram_pushButton)
        self._managers.navigation_manager.remove_app_widget(self.oxymeter_pushButton)

    def _ask_user_file(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        dlg.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        psg_reader_manager = PSGReaderManager()
        psg_reader_manager._init_readers()
        dlg.setNameFilters(psg_reader_manager.get_file_extensions_filters())

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            return filenames[0]
        return None

    def events_clicked(self): 
        print("events_clicked")

    def channels_clicked(self):
        self._channels_selection()

    def hypnogram_clicked(self):
        print("hypnogram_clicked")

    def oxymeter_clicked(self):
        print("oxymeter_clicked")
        if self._signals_manager.is_loaded(self._selected_oxymeter):
            self._oxymeter = Oxymeter(self._signal_models, self._selected_montage, self._selected_oxymeter)
            # open oxymeter in dialog
            self._oxymeter.show()

    def open_file(self):
        filename = self._ask_user_file()
        if filename is not None:
            self._current_filename = filename
            self._open_file_best(self._current_filename)
            self._channels_selection()

    def save_file(self):
        print("save_file")

    def close_file(self):
        self._signal_models = []
        self._signals_widget.remove_all_signals()
        self._signals_manager.clear()
        self._selected_montage = None
        self._selected_oxymeter = None
        self._selected_channels = []
        self._current_filename = None

    def _open_file_best(self, filename):

        psg_reader_manager = PSGReaderManager()
        psg_reader_manager._init_readers()
        psg_reader_manager.open_file(filename)

        self._events = psg_reader_manager.get_events() # Type DataFrame
        self._sleep_stages = psg_reader_manager.get_sleep_stages()
        self._montages = psg_reader_manager.get_montages()
        self._channels = {}
        for montage in self._montages:
            channels = psg_reader_manager.get_channels(montage.index)
            self._channels[montage.name] = channels

        psg_reader_manager.close_file()
   
    def _channels_selection(self):
        if self._current_filename is None:
            return
        
        dialog = ChannelSelectionDialog(self._channels, 
                                         self._selected_montage, 
                                         self._selected_channels,
                                         self._selected_oxymeter)
        if dialog.exec_():
            self._selected_montage = dialog.montage_selection
            self._selected_channels = dialog.channels_selection
            self._selected_oxymeter = dialog.oxymeter_selection

            self._signals_manager.load_signals(self._current_filename,
                self._selected_montage,
                self._selected_channels)

    # Slot
    @QtCore.Slot()
    def signal_loaded(self):
        # Create models
        self._signal_models = []

        for channel_name, signal_models in self._signals_manager.signals.items():
            signal_model = SignalModel(channel_name)
            signal_model.signal_chunks = signal_models
            
            # iterate row of events dataframe
            for row in self._events.itertuples():
                if channel_name in row.channels:
                    event_model = EventModel()
                    event_model.start_sec = row.start_sec
                    event_model.duration_sec = row.duration_sec
                    event_model.group = row.group
                    event_model.name = row.name
                    signal_model.add_event_model(event_model)

            self._signal_models.append(signal_model)
        
        self._signals_widget.remove_all_signals()
        self._signals_widget.create_signals_item(self._signal_models)


    @QtCore.Slot()
    def _events_loaded(self, events:DataFrame):
        self._signals_widget.on_events_changed(events)

    @QtCore.Slot()
    def _sleep_stages_loaded(self, sleep_stages:DataFrame):
        if sleep_stages is not None:
            print(len(sleep_stages))
