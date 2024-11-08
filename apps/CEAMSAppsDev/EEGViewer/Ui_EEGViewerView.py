# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EEGViewerView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EEGViewerView(object):
    def setupUi(self, EEGViewerView):
        if not EEGViewerView.objectName():
            EEGViewerView.setObjectName(u"EEGViewerView")
        EEGViewerView.resize(772, 496)
        self.verticalLayout_2 = QVBoxLayout(EEGViewerView)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.nav_buttons_widget = QWidget(EEGViewerView)
        self.nav_buttons_widget.setObjectName(u"nav_buttons_widget")
        self.horizontalLayout = QHBoxLayout(self.nav_buttons_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.open_file_pushButton = QPushButton(self.nav_buttons_widget)
        self.open_file_pushButton.setObjectName(u"open_file_pushButton")

        self.horizontalLayout.addWidget(self.open_file_pushButton)

        self.save_file_pushButton = QPushButton(self.nav_buttons_widget)
        self.save_file_pushButton.setObjectName(u"save_file_pushButton")

        self.horizontalLayout.addWidget(self.save_file_pushButton)

        self.close_file_pushButton = QPushButton(self.nav_buttons_widget)
        self.close_file_pushButton.setObjectName(u"close_file_pushButton")

        self.horizontalLayout.addWidget(self.close_file_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.event_pushButton = QPushButton(self.nav_buttons_widget)
        self.event_pushButton.setObjectName(u"event_pushButton")

        self.horizontalLayout.addWidget(self.event_pushButton)

        self.channels_pushButton = QPushButton(self.nav_buttons_widget)
        self.channels_pushButton.setObjectName(u"channels_pushButton")

        self.horizontalLayout.addWidget(self.channels_pushButton)

        self.hypnogram_pushButton = QPushButton(self.nav_buttons_widget)
        self.hypnogram_pushButton.setObjectName(u"hypnogram_pushButton")

        self.horizontalLayout.addWidget(self.hypnogram_pushButton)

        self.oxymeter_pushButton = QPushButton(self.nav_buttons_widget)
        self.oxymeter_pushButton.setObjectName(u"oxymeter_pushButton")

        self.horizontalLayout.addWidget(self.oxymeter_pushButton)


        self.verticalLayout_2.addWidget(self.nav_buttons_widget)

        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")

        self.verticalLayout_2.addLayout(self.main_layout)

        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(EEGViewerView)
        self.event_pushButton.clicked.connect(EEGViewerView.events_clicked)
        self.channels_pushButton.clicked.connect(EEGViewerView.channels_clicked)
        self.hypnogram_pushButton.clicked.connect(EEGViewerView.hypnogram_clicked)
        self.oxymeter_pushButton.clicked.connect(EEGViewerView.oxymeter_clicked)
        self.open_file_pushButton.clicked.connect(EEGViewerView.open_file)
        self.save_file_pushButton.clicked.connect(EEGViewerView.save_file)
        self.close_file_pushButton.clicked.connect(EEGViewerView.close_file)

        QMetaObject.connectSlotsByName(EEGViewerView)
    # setupUi

    def retranslateUi(self, EEGViewerView):
        EEGViewerView.setWindowTitle(QCoreApplication.translate("EEGViewerView", u"Form", None))
        self.open_file_pushButton.setText(QCoreApplication.translate("EEGViewerView", u"Open file", None))
        self.save_file_pushButton.setText(QCoreApplication.translate("EEGViewerView", u"Save file", None))
        self.close_file_pushButton.setText(QCoreApplication.translate("EEGViewerView", u"Close file", None))
        self.event_pushButton.setText(QCoreApplication.translate("EEGViewerView", u"Events editor", None))
        self.channels_pushButton.setText(QCoreApplication.translate("EEGViewerView", u"Channels selection", None))
        self.hypnogram_pushButton.setText(QCoreApplication.translate("EEGViewerView", u"Hypnogram", None))
        self.oxymeter_pushButton.setText(QCoreApplication.translate("EEGViewerView", u"Oxymeter", None))
    # retranslateUi

