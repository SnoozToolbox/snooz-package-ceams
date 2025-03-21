# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ResultSummarySettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_ResultSummarySettingsView(object):
    def setupUi(self, ResultSummarySettingsView):
        if not ResultSummarySettingsView.objectName():
            ResultSummarySettingsView.setObjectName(u"ResultSummarySettingsView")
        ResultSummarySettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        ResultSummarySettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(ResultSummarySettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ResultsDataframe_horizontalLayout = QHBoxLayout()
        self.ResultsDataframe_horizontalLayout.setObjectName(u"ResultsDataframe_horizontalLayout")
        self.ResultsDataframe_label = QLabel(ResultSummarySettingsView)
        self.ResultsDataframe_label.setObjectName(u"ResultsDataframe_label")

        self.ResultsDataframe_horizontalLayout.addWidget(self.ResultsDataframe_label)

        self.ResultsDataframe_lineedit = QLineEdit(ResultSummarySettingsView)
        self.ResultsDataframe_lineedit.setObjectName(u"ResultsDataframe_lineedit")

        self.ResultsDataframe_horizontalLayout.addWidget(self.ResultsDataframe_lineedit)


        self.verticalLayout.addLayout(self.ResultsDataframe_horizontalLayout)

        self.Additional_horizontalLayout = QHBoxLayout()
        self.Additional_horizontalLayout.setObjectName(u"Additional_horizontalLayout")
        self.Additional_label = QLabel(ResultSummarySettingsView)
        self.Additional_label.setObjectName(u"Additional_label")

        self.Additional_horizontalLayout.addWidget(self.Additional_label)

        self.Additional_lineedit = QLineEdit(ResultSummarySettingsView)
        self.Additional_lineedit.setObjectName(u"Additional_lineedit")

        self.Additional_horizontalLayout.addWidget(self.Additional_lineedit)


        self.verticalLayout.addLayout(self.Additional_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ResultSummarySettingsView)

        QMetaObject.connectSlotsByName(ResultSummarySettingsView)
    # setupUi

    def retranslateUi(self, ResultSummarySettingsView):
        ResultSummarySettingsView.setWindowTitle(QCoreApplication.translate("ResultSummarySettingsView", u"Form", None))
        self.ResultsDataframe_label.setText(QCoreApplication.translate("ResultSummarySettingsView", u"ResultsDataframe", None))
        self.Additional_label.setText(QCoreApplication.translate("ResultSummarySettingsView", u"Additional", None))
    # retranslateUi

