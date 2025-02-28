# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SignalStatsSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_SignalStatsSettingsView(object):
    def setupUi(self, SignalStatsSettingsView):
        if not SignalStatsSettingsView.objectName():
            SignalStatsSettingsView.setObjectName(u"SignalStatsSettingsView")
        SignalStatsSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        SignalStatsSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(SignalStatsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signals_horizontalLayout = QHBoxLayout()
        self.signals_horizontalLayout.setObjectName(u"signals_horizontalLayout")
        self.signals_label = QLabel(SignalStatsSettingsView)
        self.signals_label.setObjectName(u"signals_label")

        self.signals_horizontalLayout.addWidget(self.signals_label)

        self.signals_lineedit = QLineEdit(SignalStatsSettingsView)
        self.signals_lineedit.setObjectName(u"signals_lineedit")

        self.signals_horizontalLayout.addWidget(self.signals_lineedit)


        self.verticalLayout.addLayout(self.signals_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SignalStatsSettingsView)

        QMetaObject.connectSlotsByName(SignalStatsSettingsView)
    # setupUi

    def retranslateUi(self, SignalStatsSettingsView):
        SignalStatsSettingsView.setWindowTitle(QCoreApplication.translate("SignalStatsSettingsView", u"Form", None))
        self.signals_label.setText(QCoreApplication.translate("SignalStatsSettingsView", u"signals", None))
    # retranslateUi

