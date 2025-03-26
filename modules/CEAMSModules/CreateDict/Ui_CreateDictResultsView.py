# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_CreateDictResultsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_CreateDictResultsView(object):
    def setupUi(self, CreateDictResultsView):
        if not CreateDictResultsView.objectName():
            CreateDictResultsView.setObjectName(u"CreateDictResultsView")
        CreateDictResultsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        CreateDictResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(CreateDictResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(CreateDictResultsView)

        QMetaObject.connectSlotsByName(CreateDictResultsView)
    # setupUi

    def retranslateUi(self, CreateDictResultsView):
        CreateDictResultsView.setWindowTitle(QCoreApplication.translate("CreateDictResultsView", u"Form", None))
    # retranslateUi

