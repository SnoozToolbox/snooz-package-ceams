# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\sampo\Python\PycharmProjects\scinode\scinodes_poc\src\main\python\plugins\PerformanceByEvent\Ui_PerformanceByEventSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_PerformanceByEventSettingsView(object):
    def setupUi(self, PerformanceByEventSettingsView):
        PerformanceByEventSettingsView.setObjectName("PerformanceByEventSettingsView")
        PerformanceByEventSettingsView.resize(469, 380)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(PerformanceByEventSettingsView)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(PerformanceByEventSettingsView)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.line_2 = QtWidgets.QFrame(PerformanceByEventSettingsView)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.jaccord_lineEdit = QtWidgets.QLineEdit(PerformanceByEventSettingsView)
        self.jaccord_lineEdit.setObjectName("jaccord_lineEdit")
        self.gridLayout.addWidget(self.jaccord_lineEdit, 4, 1, 1, 1)
        self.chan_label = QtWidgets.QLabel(PerformanceByEventSettingsView)
        self.chan_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chan_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.chan_label.setObjectName("chan_label")
        self.gridLayout.addWidget(self.chan_label, 2, 0, 1, 1)
        self.event1_name_lineedit = QtWidgets.QLineEdit(PerformanceByEventSettingsView)
        self.event1_name_lineedit.setObjectName("event1_name_lineedit")
        self.gridLayout.addWidget(self.event1_name_lineedit, 0, 1, 1, 1)
        self.event2_name_lineedit = QtWidgets.QLineEdit(PerformanceByEventSettingsView)
        self.event2_name_lineedit.setObjectName("event2_name_lineedit")
        self.gridLayout.addWidget(self.event2_name_lineedit, 1, 1, 1, 1)
        self.channel1_lineedit = QtWidgets.QLineEdit(PerformanceByEventSettingsView)
        self.channel1_lineedit.setObjectName("channel1_lineedit")
        self.gridLayout.addWidget(self.channel1_lineedit, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(PerformanceByEventSettingsView)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(PerformanceByEventSettingsView)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(PerformanceByEventSettingsView)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(PerformanceByEventSettingsView)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.channel2_lineedit = QtWidgets.QLineEdit(PerformanceByEventSettingsView)
        self.channel2_lineedit.setObjectName("channel2_lineedit")
        self.gridLayout.addWidget(self.channel2_lineedit, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.label_4 = QtWidgets.QLabel(PerformanceByEventSettingsView)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.line = QtWidgets.QFrame(PerformanceByEventSettingsView)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(PerformanceByEventSettingsView)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.filename_lineEdit = QtWidgets.QLineEdit(PerformanceByEventSettingsView)
        self.filename_lineEdit.setObjectName("filename_lineEdit")
        self.horizontalLayout.addWidget(self.filename_lineEdit)
        self.browse_pushButton = QtWidgets.QPushButton(PerformanceByEventSettingsView)
        self.browse_pushButton.setObjectName("browse_pushButton")
        self.horizontalLayout.addWidget(self.browse_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(PerformanceByEventSettingsView)
        self.browse_pushButton.clicked.connect(PerformanceByEventSettingsView.on_choose)
        QtCore.QMetaObject.connectSlotsByName(PerformanceByEventSettingsView)

    def retranslateUi(self, PerformanceByEventSettingsView):
        _translate = QtCore.QCoreApplication.translate
        PerformanceByEventSettingsView.setWindowTitle(_translate("PerformanceByEventSettingsView", "Form"))
        self.label_5.setText(_translate("PerformanceByEventSettingsView", "Input settings"))
        self.jaccord_lineEdit.setToolTip(_translate("PerformanceByEventSettingsView", "Enter the Jaccord index (similarity) threshold (from 0 et 1) to mark an event as valid."))
        self.jaccord_lineEdit.setText(_translate("PerformanceByEventSettingsView", "0.2"))
        self.chan_label.setText(_translate("PerformanceByEventSettingsView", "Channel label event 1"))
        self.event1_name_lineedit.setToolTip(_translate("PerformanceByEventSettingsView", "Enter the event label to evaluate."))
        self.event2_name_lineedit.setToolTip(_translate("PerformanceByEventSettingsView", "Enter the event label to evaluate."))
        self.channel1_lineedit.setToolTip(_translate("PerformanceByEventSettingsView", "Enter the channel to filter events 1 to evaluate.  Let it empty to compare the events from all channels."))
        self.label.setText(_translate("PerformanceByEventSettingsView", "Event 1 name"))
        self.label_6.setText(_translate("PerformanceByEventSettingsView", "Jaccord Index threshold"))
        self.label_2.setText(_translate("PerformanceByEventSettingsView", "Event 2 name"))
        self.label_7.setText(_translate("PerformanceByEventSettingsView", "Channel label event 2"))
        self.channel2_lineedit.setToolTip(_translate("PerformanceByEventSettingsView", "Enter the channel to filter events 2 to evaluate.  Let it empty to compare the events from all channels."))
        self.label_4.setText(_translate("PerformanceByEventSettingsView", "Output settings"))
        self.label_3.setText(_translate("PerformanceByEventSettingsView", "Filename"))
        self.filename_lineEdit.setToolTip(_translate("PerformanceByEventSettingsView", "Filename to save performance evaluation. "))
        self.browse_pushButton.setText(_translate("PerformanceByEventSettingsView", "Browse"))
