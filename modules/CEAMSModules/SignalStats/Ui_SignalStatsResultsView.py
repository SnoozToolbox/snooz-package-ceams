# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SignalStatsResultsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_SignalStatsResultsView(object):
    def setupUi(self, SignalStatsResultsView):
        if not SignalStatsResultsView.objectName():
            SignalStatsResultsView.setObjectName(u"SignalStatsResultsView")
        SignalStatsResultsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        SignalStatsResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(SignalStatsResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(SignalStatsResultsView)

        QMetaObject.connectSlotsByName(SignalStatsResultsView)
    # setupUi

    def retranslateUi(self, SignalStatsResultsView):
        SignalStatsResultsView.setWindowTitle(QCoreApplication.translate("SignalStatsResultsView", u"Form", None))
    # retranslateUi

