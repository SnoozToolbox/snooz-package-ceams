# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'channel_selection2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ChannelSelection(object):
    def setupUi(self, ChannelSelection):
        if not ChannelSelection.objectName():
            ChannelSelection.setObjectName(u"ChannelSelection")
        ChannelSelection.resize(593, 542)
        self.verticalLayout = QVBoxLayout(ChannelSelection)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(ChannelSelection)
        self.tabWidget.setObjectName(u"tabWidget")
        self.channels_selection_tab = QWidget()
        self.channels_selection_tab.setObjectName(u"channels_selection_tab")
        self.verticalLayout_4 = QVBoxLayout(self.channels_selection_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_3 = QGroupBox(self.channels_selection_tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.montages_comboBox = QComboBox(self.groupBox_3)
        self.montages_comboBox.setObjectName(u"montages_comboBox")

        self.horizontalLayout.addWidget(self.montages_comboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.label_2 = QLabel(self.channels_selection_tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.channels_tableWidget = QTableWidget(self.channels_selection_tab)
        self.channels_tableWidget.setObjectName(u"channels_tableWidget")
        self.channels_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.channels_tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.channels_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.channels_tableWidget.setSortingEnabled(True)
        self.channels_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.channels_tableWidget.verticalHeader().setVisible(False)
        self.channels_tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.channels_tableWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.unselect_all_pushButton = QPushButton(self.channels_selection_tab)
        self.unselect_all_pushButton.setObjectName(u"unselect_all_pushButton")

        self.horizontalLayout_3.addWidget(self.unselect_all_pushButton)

        self.select_all_pushButton = QPushButton(self.channels_selection_tab)
        self.select_all_pushButton.setObjectName(u"select_all_pushButton")

        self.horizontalLayout_3.addWidget(self.select_all_pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.groupBox_4 = QGroupBox(self.channels_selection_tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.oxy_channel_comboBox = QComboBox(self.groupBox_4)
        self.oxy_channel_comboBox.setObjectName(u"oxy_channel_comboBox")

        self.horizontalLayout_2.addWidget(self.oxy_channel_comboBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.tabWidget.addTab(self.channels_selection_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(ChannelSelection)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ChannelSelection)
        self.buttonBox.accepted.connect(ChannelSelection.accept)
        self.buttonBox.rejected.connect(ChannelSelection.reject)
        self.select_all_pushButton.clicked.connect(ChannelSelection.select_all)
        self.unselect_all_pushButton.clicked.connect(ChannelSelection.unselect_all)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ChannelSelection)
    # setupUi

    def retranslateUi(self, ChannelSelection):
        ChannelSelection.setWindowTitle(QCoreApplication.translate("ChannelSelection", u"Channels selection", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ChannelSelection", u"Montage", None))
        self.label_2.setText(QCoreApplication.translate("ChannelSelection", u"Channels", None))
        self.unselect_all_pushButton.setText(QCoreApplication.translate("ChannelSelection", u"Unselect all", None))
        self.select_all_pushButton.setText(QCoreApplication.translate("ChannelSelection", u"Select all", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ChannelSelection", u"Oxymeter channel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.channels_selection_tab), QCoreApplication.translate("ChannelSelection", u"Channels selection", None))
    # retranslateUi

