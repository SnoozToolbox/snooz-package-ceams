# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\klacourse\Documents\NGosselin\gitRepos\ceamscarms\Stand_alone_apps\snooz-toolbox\src\main\python\plugins\MovingRMS\Ui_MovingRMSSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_MovingRMSSettingsView(object):
    def setupUi(self, MovingRMSSettingsView):
        MovingRMSSettingsView.setObjectName("MovingRMSSettingsView")
        MovingRMSSettingsView.resize(711, 333)
        self.verticalLayout = QtWidgets.QVBoxLayout(MovingRMSSettingsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signals_horizontalLayout = QtWidgets.QHBoxLayout()
        self.signals_horizontalLayout.setObjectName("signals_horizontalLayout")
        self.verticalLayout.addLayout(self.signals_horizontalLayout)
        self.win_len_sec_horizontalLayout = QtWidgets.QHBoxLayout()
        self.win_len_sec_horizontalLayout.setObjectName("win_len_sec_horizontalLayout")
        self.win_len_sec_label = QtWidgets.QLabel(MovingRMSSettingsView)
        self.win_len_sec_label.setMinimumSize(QtCore.QSize(105, 0))
        self.win_len_sec_label.setObjectName("win_len_sec_label")
        self.win_len_sec_horizontalLayout.addWidget(self.win_len_sec_label)
        self.win_len_sec_lineedit = QtWidgets.QLineEdit(MovingRMSSettingsView)
        self.win_len_sec_lineedit.setObjectName("win_len_sec_lineedit")
        self.win_len_sec_horizontalLayout.addWidget(self.win_len_sec_lineedit)
        self.verticalLayout.addLayout(self.win_len_sec_horizontalLayout)
        self.win_step_sec_horizontalLayout = QtWidgets.QHBoxLayout()
        self.win_step_sec_horizontalLayout.setObjectName("win_step_sec_horizontalLayout")
        self.win_step_sec_label = QtWidgets.QLabel(MovingRMSSettingsView)
        self.win_step_sec_label.setMinimumSize(QtCore.QSize(105, 0))
        self.win_step_sec_label.setObjectName("win_step_sec_label")
        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_label)
        self.win_step_sec_lineedit = QtWidgets.QLineEdit(MovingRMSSettingsView)
        self.win_step_sec_lineedit.setObjectName("win_step_sec_lineedit")
        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_lineedit)
        self.verticalLayout.addLayout(self.win_step_sec_horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(MovingRMSSettingsView)
        QtCore.QMetaObject.connectSlotsByName(MovingRMSSettingsView)

    def retranslateUi(self, MovingRMSSettingsView):
        _translate = QtCore.QCoreApplication.translate
        MovingRMSSettingsView.setWindowTitle(_translate("MovingRMSSettingsView", "Form"))
        self.win_len_sec_label.setText(_translate("MovingRMSSettingsView", "Window length (sec)"))
        self.win_step_sec_label.setText(_translate("MovingRMSSettingsView", "Window step (sec)"))
