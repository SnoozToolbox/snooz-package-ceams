# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'oxymeter.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from CEAMSApps.EEGViewer.widgets.OxymeterDrawArea import OxymeterDrawArea


class Ui_Oxymeter(object):
    def setupUi(self, Oxymeter):
        if not Oxymeter.objectName():
            Oxymeter.setObjectName(u"Oxymeter")
        Oxymeter.resize(815, 496)
        self.verticalLayout = QVBoxLayout(Oxymeter)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Oxymeter)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.ymin_comboBox = QComboBox(Oxymeter)
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.addItem("")
        self.ymin_comboBox.setObjectName(u"ymin_comboBox")

        self.horizontalLayout_2.addWidget(self.ymin_comboBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.oxymeter_draw_area = OxymeterDrawArea(Oxymeter)
        self.oxymeter_draw_area.setObjectName(u"oxymeter_draw_area")

        self.verticalLayout.addWidget(self.oxymeter_draw_area)

        self.label_2 = QLabel(Oxymeter)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.line = QFrame(Oxymeter)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(Oxymeter)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.reset_pushButton = QPushButton(Oxymeter)
        self.reset_pushButton.setObjectName(u"reset_pushButton")

        self.horizontalLayout.addWidget(self.reset_pushButton)

        self.remove_all_pushButton = QPushButton(Oxymeter)
        self.remove_all_pushButton.setObjectName(u"remove_all_pushButton")

        self.horizontalLayout.addWidget(self.remove_all_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.apply_pushButton = QPushButton(Oxymeter)
        self.apply_pushButton.setObjectName(u"apply_pushButton")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.apply_pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.apply_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Oxymeter)
        self.apply_pushButton.clicked.connect(Oxymeter.on_apply)
        self.remove_all_pushButton.clicked.connect(Oxymeter.remove_all_clicked)
        self.reset_pushButton.clicked.connect(Oxymeter.on_reset)
        self.ymin_comboBox.currentTextChanged.connect(Oxymeter.min_saturation_change)

        QMetaObject.connectSlotsByName(Oxymeter)
    # setupUi

    def retranslateUi(self, Oxymeter):
        Oxymeter.setWindowTitle(QCoreApplication.translate("Oxymeter", u"Form", None))
        self.label.setText(QCoreApplication.translate("Oxymeter", u"Min. Saturation (%)", None))
        self.ymin_comboBox.setItemText(0, QCoreApplication.translate("Oxymeter", u"0", None))
        self.ymin_comboBox.setItemText(1, QCoreApplication.translate("Oxymeter", u"10", None))
        self.ymin_comboBox.setItemText(2, QCoreApplication.translate("Oxymeter", u"20", None))
        self.ymin_comboBox.setItemText(3, QCoreApplication.translate("Oxymeter", u"30", None))
        self.ymin_comboBox.setItemText(4, QCoreApplication.translate("Oxymeter", u"40", None))
        self.ymin_comboBox.setItemText(5, QCoreApplication.translate("Oxymeter", u"50", None))
        self.ymin_comboBox.setItemText(6, QCoreApplication.translate("Oxymeter", u"60", None))
        self.ymin_comboBox.setItemText(7, QCoreApplication.translate("Oxymeter", u"70", None))
        self.ymin_comboBox.setItemText(8, QCoreApplication.translate("Oxymeter", u"80", None))
        self.ymin_comboBox.setItemText(9, QCoreApplication.translate("Oxymeter", u"90", None))

        self.label_2.setText(QCoreApplication.translate("Oxymeter", u"(Note: Gray sections represent discontinuities in the signal.)", None))
        self.label_3.setText(QCoreApplication.translate("Oxymeter", u"Left-click and drag to select invalid sections.", None))
#if QT_CONFIG(tooltip)
        self.reset_pushButton.setToolTip(QCoreApplication.translate("Oxymeter", u"Cancel current modification and set it back to the last recorded values.", None))
#endif // QT_CONFIG(tooltip)
        self.reset_pushButton.setText(QCoreApplication.translate("Oxymeter", u"Cancel current changes", None))
        self.remove_all_pushButton.setText(QCoreApplication.translate("Oxymeter", u"Remove all sections", None))
        self.apply_pushButton.setText(QCoreApplication.translate("Oxymeter", u"Apply to file", None))
    # retranslateUi

