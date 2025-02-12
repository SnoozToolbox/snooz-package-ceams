"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QDialog, QTableWidgetItem, QCheckBox
from CEAMSApps.EEGViewer.ui.channel_selection import Ui_ChannelSelection

# Subclass QMainWindow to customize your application's main window
class ChannelSelectionDialog(QDialog, Ui_ChannelSelection):
    def __init__(self, channels:dict, selected_montage:str, selected_channels:list, selected_oxymeter:str):
        super().__init__()
        self.setupUi(self)
        self._previous_selected_montage = selected_montage
        self._previous_selected_channels = selected_channels
        self._previous_selected_oxymeter = selected_oxymeter
        self._channels = channels
        self._montage_selection = None
        self._oxymeter_selection = None
        self._channels_selection = []

        #For each key value in _channels
        for montage_name, channels in self._channels.items():
            self.montages_comboBox.addItem(montage_name)

        if self._previous_selected_montage is not None:
            self.montages_comboBox.setCurrentText(self._previous_selected_montage)
            channels = self._channels[self._previous_selected_montage]
            self.update_channels(channels, self._previous_selected_montage)
        else:
            montage_name = self.montages_comboBox.currentText()
            channels = self._channels[montage_name]
            self.update_channels(channels, montage_name)
        self.montages_comboBox.currentIndexChanged.connect(self.montage_change)
        self.montage_change(None)

    # Properties
    @property
    def channels_selection(self):
        return self._channels_selection
    
    @property
    def montage_selection(self):
        return self._montage_selection
    
    @property
    def oxymeter_selection(self):
        return self._oxymeter_selection
        
    def montage_change(self, _):
        montage_name = self.montages_comboBox.currentText()
        channels = self._channels[montage_name]
        self.update_channels(channels, montage_name)
        self._update_oxy_channel(channels)

    def update_channels(self, channels, montage_name):
        self.channels_tableWidget.clear()
        self.channels_tableWidget.setColumnCount(3)
        self.channels_tableWidget.setHorizontalHeaderLabels(["Visible", "Name", "Sample rate (Hz)"])
        self.channels_tableWidget.setRowCount(len(channels))

        for idx, channel in enumerate(channels):
            selection_checkbox = QCheckBox()

            if channel.name in self._previous_selected_channels and montage_name == self._previous_selected_montage:
                selection_checkbox.setCheckState(Qt.Checked)

            self.channels_tableWidget.setCellWidget(idx, 0, selection_checkbox)

            channel_item = QTableWidgetItem(channel.name)
            self.channels_tableWidget.setItem(idx, 1, channel_item)

            sample_rate_item = QTableWidgetItem(str(channel.sample_rate))
            self.channels_tableWidget.setItem(idx, 2, sample_rate_item)

    def select_all(self):
        for row in range(self.channels_tableWidget.rowCount()):	
            item = self.channels_tableWidget.cellWidget(row, 0)
            item.setCheckState(Qt.Checked)

    def unselect_all(self):
        for row in range(self.channels_tableWidget.rowCount()):
            item = self.channels_tableWidget.cellWidget(row, 0)
            item.setCheckState(Qt.Unchecked)

    def accept(self):
        if self.oxy_channel_comboBox.currentText() == "None":
            self._oxymeter_selection = None
        else:
            self._oxymeter_selection = self.oxy_channel_comboBox.currentText()

        self._montage_selection = self.montages_comboBox.currentText()
        
        for row in range(self.channels_tableWidget.rowCount()):
            item = self.channels_tableWidget.cellWidget(row, 0)
            if item and item.checkState() == Qt.Checked:
                channel_name = self.channels_tableWidget.item(row, 1).text()
                self._channels_selection.append(channel_name)

        super().accept()

    def _update_oxy_channel(self, channels):
        self.oxy_channel_comboBox.clear()
        self.oxy_channel_comboBox.addItem("None")
        for channel in channels:
            self.oxy_channel_comboBox.addItem(channel.name)

        # Automatic default selection
        known_oxymeter_channels = ["spo2", "oxy", "osat", "oxymetre"]
        for channel in channels:
            if channel.name.lower() in known_oxymeter_channels:
                self.oxy_channel_comboBox.setCurrentText(channel.name)
                break
        
        # If it's the previously selected montage, select what was selected.
        if self._previous_selected_montage == self.montages_comboBox.currentText():
            if self._previous_selected_oxymeter is not None:
                self.oxy_channel_comboBox.setCurrentText(self._previous_selected_oxymeter)
                
