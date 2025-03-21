# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ResultSummaryResultsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_ResultSummaryResultsView(object):
    def setupUi(self, ResultSummaryResultsView):
        if not ResultSummaryResultsView.objectName():
            ResultSummaryResultsView.setObjectName(u"ResultSummaryResultsView")
        ResultSummaryResultsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        ResultSummaryResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(ResultSummaryResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(ResultSummaryResultsView)

        QMetaObject.connectSlotsByName(ResultSummaryResultsView)
    # setupUi

    def retranslateUi(self, ResultSummaryResultsView):
        ResultSummaryResultsView.setWindowTitle(QCoreApplication.translate("ResultSummaryResultsView", u"Form", None))
    # retranslateUi

