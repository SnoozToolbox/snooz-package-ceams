# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\klacourse\Documents\NGosselin\gitRepos\ceamscarms\Stand_alone_apps\snooz-toolbox\src\main\python\plugins\EventCombine\Ui_EventCombineSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_EventCombineSettingsView(object):
    def setupUi(self, EventCombineSettingsView):
        EventCombineSettingsView.setObjectName("EventCombineSettingsView")
        EventCombineSettingsView.resize(432, 430)
        self.gridLayout_3 = QtWidgets.QGridLayout(EventCombineSettingsView)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(EventCombineSettingsView)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_2 = QtWidgets.QFrame(EventCombineSettingsView)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.chan_wise_checkBox = QtWidgets.QCheckBox(EventCombineSettingsView)
        self.chan_wise_checkBox.setChecked(True)
        self.chan_wise_checkBox.setObjectName("chan_wise_checkBox")
        self.verticalLayout.addWidget(self.chan_wise_checkBox)
        self.label_9 = QtWidgets.QLabel(EventCombineSettingsView)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(EventCombineSettingsView)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.event1_name_lineedit = QtWidgets.QLineEdit(EventCombineSettingsView)
        self.event1_name_lineedit.setObjectName("event1_name_lineedit")
        self.gridLayout.addWidget(self.event1_name_lineedit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(EventCombineSettingsView)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.event2_name_lineedit = QtWidgets.QLineEdit(EventCombineSettingsView)
        self.event2_name_lineedit.setObjectName("event2_name_lineedit")
        self.gridLayout.addWidget(self.event2_name_lineedit, 1, 1, 1, 1)
        self.chan1_label = QtWidgets.QLabel(EventCombineSettingsView)
        self.chan1_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chan1_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.chan1_label.setObjectName("chan1_label")
        self.gridLayout.addWidget(self.chan1_label, 2, 0, 1, 1)
        self.channel1_lineedit = QtWidgets.QLineEdit(EventCombineSettingsView)
        self.channel1_lineedit.setObjectName("channel1_lineedit")
        self.gridLayout.addWidget(self.channel1_lineedit, 2, 1, 1, 1)
        self.chan2_label = QtWidgets.QLabel(EventCombineSettingsView)
        self.chan2_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chan2_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.chan2_label.setObjectName("chan2_label")
        self.gridLayout.addWidget(self.chan2_label, 3, 0, 1, 1)
        self.channel2_lineedit = QtWidgets.QLineEdit(EventCombineSettingsView)
        self.channel2_lineedit.setObjectName("channel2_lineedit")
        self.gridLayout.addWidget(self.channel2_lineedit, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(EventCombineSettingsView)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.behavior_comboBox = QComboBoxLive(EventCombineSettingsView)
        self.behavior_comboBox.setObjectName("behavior_comboBox")
        self.behavior_comboBox.addItem("")
        self.behavior_comboBox.addItem("")
        self.behavior_comboBox.addItem("")
        self.gridLayout.addWidget(self.behavior_comboBox, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line = QtWidgets.QFrame(EventCombineSettingsView)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(EventCombineSettingsView)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.rename_checkBox = QtWidgets.QCheckBox(EventCombineSettingsView)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rename_checkBox.setFont(font)
        self.rename_checkBox.setText("")
        self.rename_checkBox.setObjectName("rename_checkBox")
        self.horizontalLayout.addWidget(self.rename_checkBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(EventCombineSettingsView)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.new_event_group_lineedit = QtWidgets.QLineEdit(EventCombineSettingsView)
        self.new_event_group_lineedit.setEnabled(False)
        self.new_event_group_lineedit.setObjectName("new_event_group_lineedit")
        self.gridLayout_2.addWidget(self.new_event_group_lineedit, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(EventCombineSettingsView)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.new_event_name_lineedit = QtWidgets.QLineEdit(EventCombineSettingsView)
        self.new_event_name_lineedit.setEnabled(False)
        self.new_event_name_lineedit.setObjectName("new_event_name_lineedit")
        self.gridLayout_2.addWidget(self.new_event_name_lineedit, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(EventCombineSettingsView)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.event_channel_lineedit = QtWidgets.QLineEdit(EventCombineSettingsView)
        self.event_channel_lineedit.setEnabled(False)
        self.event_channel_lineedit.setObjectName("event_channel_lineedit")
        self.gridLayout_2.addWidget(self.event_channel_lineedit, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(EventCombineSettingsView)
        self.rename_checkBox.stateChanged['int'].connect(EventCombineSettingsView.on_modify_checkbox)
        self.chan_wise_checkBox.stateChanged['int'].connect(EventCombineSettingsView.on_chan_wise_checkbox)
        QtCore.QMetaObject.connectSlotsByName(EventCombineSettingsView)

    def retranslateUi(self, EventCombineSettingsView):
        _translate = QtCore.QCoreApplication.translate
        EventCombineSettingsView.setWindowTitle(_translate("EventCombineSettingsView", "Form"))
        self.label_5.setText(_translate("EventCombineSettingsView", "Event Combine settings "))
        self.chan_wise_checkBox.setToolTip(_translate("EventCombineSettingsView", "Check to work with channel specific events only (if checked sleep stages are discarded).  Events are combined per channel."))
        self.chan_wise_checkBox.setText(_translate("EventCombineSettingsView", "Channel Wise"))
        self.label_9.setText(_translate("EventCombineSettingsView", "Select the events to combine"))
        self.label.setText(_translate("EventCombineSettingsView", "Event 1 name"))
        self.event1_name_lineedit.setToolTip(_translate("EventCombineSettingsView", "To filter events with a specific name otherwise all events will be combined."))
        self.label_2.setText(_translate("EventCombineSettingsView", "Event 2 name"))
        self.event2_name_lineedit.setToolTip(_translate("EventCombineSettingsView", "To filter events with a specific name otherwise all events will be combined."))
        self.chan1_label.setText(_translate("EventCombineSettingsView", "Channel1 label"))
        self.channel1_lineedit.setToolTip(_translate("EventCombineSettingsView", "To filter events based on a channel label, otherwise all events are combined per channel."))
        self.chan2_label.setText(_translate("EventCombineSettingsView", "Channel2 label"))
        self.channel2_lineedit.setToolTip(_translate("EventCombineSettingsView", "To filter events based on a channel label, otherwise all events are combined per channel."))
        self.label_3.setText(_translate("EventCombineSettingsView", "Behavior"))
        self.behavior_comboBox.setToolTip(_translate("EventCombineSettingsView", "Select how to combine events : union (all events), union without concurrent events (events merge) or intersection (concurrent events only)."))
        self.behavior_comboBox.setItemText(0, _translate("EventCombineSettingsView", "union"))
        self.behavior_comboBox.setItemText(1, _translate("EventCombineSettingsView", "union without concurrent events"))
        self.behavior_comboBox.setItemText(2, _translate("EventCombineSettingsView", "intersection"))
        self.label_8.setText(_translate("EventCombineSettingsView", "Modify the combined events"))
        self.rename_checkBox.setToolTip(_translate("EventCombineSettingsView", "Check to rename the combined events."))
        self.label_7.setText(_translate("EventCombineSettingsView", "New event group"))
        self.new_event_group_lineedit.setToolTip(_translate("EventCombineSettingsView", "Event group is mandatory to rename combined events.  Can be left blank if the \"New event name\" is also left blank."))
        self.label_4.setText(_translate("EventCombineSettingsView", "New event name"))
        self.new_event_name_lineedit.setToolTip(_translate("EventCombineSettingsView", "To rename the combined events. The name of the source is taken if it is left blank."))
        self.label_6.setText(_translate("EventCombineSettingsView", "New event channel"))
        self.event_channel_lineedit.setToolTip(_translate("EventCombineSettingsView", "On which channel new created events are added.  If blank, the channel from events 1 is taken."))
from widgets.QComboBoxLive import QComboBoxLive
