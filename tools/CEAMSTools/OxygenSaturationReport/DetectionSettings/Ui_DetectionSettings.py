# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DetectionSettings.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QHBoxLayout,
    QLabel, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_DetectionSettings(object):
    def setupUi(self, DetectionSettings):
        if not DetectionSettings.objectName():
            DetectionSettings.setObjectName(u"DetectionSettings")
        DetectionSettings.resize(1544, 759)
        DetectionSettings.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(DetectionSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_10 = QLabel(DetectionSettings)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_10.setFont(font)

        self.verticalLayout.addWidget(self.label_10)

        self.label_11 = QLabel(DetectionSettings)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.label_11)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_14 = QLabel(DetectionSettings)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 0, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_12, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.label = QLabel(DetectionSettings)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_pic = QLabel(DetectionSettings)
        self.label_pic.setObjectName(u"label_pic")
        self.label_pic.setMaximumSize(QSize(16777215, 185))

        self.horizontalLayout_2.addWidget(self.label_pic)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)

        self.label_7 = QLabel(DetectionSettings)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_13 = QLabel(DetectionSettings)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.label_13)

        self.label_15 = QLabel(DetectionSettings)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.label_15)

        self.label_3 = QLabel(DetectionSettings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(DetectionSettings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.radioButton_20s = QRadioButton(DetectionSettings)
        self.buttonGroup_2 = QButtonGroup(DetectionSettings)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_20s)
        self.radioButton_20s.setObjectName(u"radioButton_20s")
        self.radioButton_20s.setMinimumSize(QSize(115, 0))

        self.gridLayout.addWidget(self.radioButton_20s, 1, 3, 1, 1)

        self.radioButton_3perc = QRadioButton(DetectionSettings)
        self.buttonGroup = QButtonGroup(DetectionSettings)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_3perc)
        self.radioButton_3perc.setObjectName(u"radioButton_3perc")
        self.radioButton_3perc.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_3perc, 0, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(118, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_10, 1, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 0, 4, 1, 1)

        self.radioButton_hold_5s = QRadioButton(DetectionSettings)
        self.buttonGroup_3 = QButtonGroup(DetectionSettings)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton_hold_5s)
        self.radioButton_hold_5s.setObjectName(u"radioButton_hold_5s")

        self.gridLayout.addWidget(self.radioButton_hold_5s, 2, 3, 1, 1)

        self.label_4 = QLabel(DetectionSettings)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)

        self.radioButton_4perc = QRadioButton(DetectionSettings)
        self.buttonGroup.addButton(self.radioButton_4perc)
        self.radioButton_4perc.setObjectName(u"radioButton_4perc")

        self.gridLayout.addWidget(self.radioButton_4perc, 0, 3, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(108, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_11, 2, 4, 1, 1)

        self.label_17 = QLabel(DetectionSettings)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 1, 1, 1, 1)

        self.radioButton_180s = QRadioButton(DetectionSettings)
        self.buttonGroup_2.addButton(self.radioButton_180s)
        self.radioButton_180s.setObjectName(u"radioButton_180s")
        self.radioButton_180s.setMinimumSize(QSize(115, 0))
        self.radioButton_180s.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_180s, 1, 2, 1, 1)

        self.radioButton_hold_10s = QRadioButton(DetectionSettings)
        self.buttonGroup_3.addButton(self.radioButton_hold_10s)
        self.radioButton_hold_10s.setObjectName(u"radioButton_hold_10s")
        self.radioButton_hold_10s.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_hold_10s, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.label_8 = QLabel(DetectionSettings)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.label_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_16 = QLabel(DetectionSettings)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 30))
        self.label_16.setFont(font)
        self.label_16.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_16)

        self.label_5 = QLabel(DetectionSettings)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_7 = QSpacerItem(20, 139, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)


        self.retranslateUi(DetectionSettings)

        QMetaObject.connectSlotsByName(DetectionSettings)
    # setupUi

    def retranslateUi(self, DetectionSettings):
        DetectionSettings.setWindowTitle("")
        self.label_10.setText(QCoreApplication.translate("DetectionSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Oxygen Saturation Pre-processing</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("DetectionSettings", u"The oxygen channel is low-pass filtered to 0.4 Hz and downsampled to 1 Hz.\n"
"All values are expressed in %, ranging from 0 to 100%.", None))
        self.label_14.setText(QCoreApplication.translate("DetectionSettings", u"Low-pass filter : \n"
"IIR filter, order 6, applied forward and backward to cancel the phase delay. \n"
"The order is divided by 2 when applied since is it applied twice.", None))
        self.label.setText(QCoreApplication.translate("DetectionSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Oxygen Desaturation Crtieria</span></p></body></html>", None))
        self.label_pic.setText("")
        self.label_7.setText(QCoreApplication.translate("DetectionSettings", u"AASM criteria [1]", None))
        self.label_13.setText(QCoreApplication.translate("DetectionSettings", u"Minimum oxygen desaturation drop : 3% or 4%", None))
        self.label_15.setText(QCoreApplication.translate("DetectionSettings", u"The desaturation ends when there is a resaturation of at least 2%", None))
        self.label_3.setText(QCoreApplication.translate("DetectionSettings", u"Maximum recovery duration (the mimimum value between):\n"
"120 s and 2 x duration of desaturation", None))
        self.label_2.setText(QCoreApplication.translate("DetectionSettings", u"The oxygen level drop", None))
        self.radioButton_20s.setText(QCoreApplication.translate("DetectionSettings", u"20 sec [CEAMS]", None))
        self.radioButton_3perc.setText(QCoreApplication.translate("DetectionSettings", u"3 %", None))
        self.radioButton_hold_5s.setText(QCoreApplication.translate("DetectionSettings", u"5 sec [2, CEAMS]", None))
        self.label_4.setText(QCoreApplication.translate("DetectionSettings", u"Minimum hold duration", None))
        self.radioButton_4perc.setText(QCoreApplication.translate("DetectionSettings", u"4 %", None))
        self.label_17.setText(QCoreApplication.translate("DetectionSettings", u"Maximum desaturation time", None))
        self.radioButton_180s.setText(QCoreApplication.translate("DetectionSettings", u"180 sec [2]", None))
        self.radioButton_hold_10s.setText(QCoreApplication.translate("DetectionSettings", u"10 sec [2]", None))
        self.label_8.setText(QCoreApplication.translate("DetectionSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">References</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("DetectionSettings", u"[1] Iber, C., American Academy of Sleep Medicine, 2007. The AASM Manual for the Scoring of Sleep and Associated Events: Rules, Terminology and Technical Specifications. American Academy of Sleep Medicine.", None))
        self.label_5.setText(QCoreApplication.translate("DetectionSettings", u"[2] Karhu, T., Lepp\u00e4nen, T., T\u00f6yr\u00e4s, J., Oksenberg, A., Myllymaa, S., & Nikkonen, S. (2022). ABOSA \u2013 Freely available automatic blood oxygen saturation signal analysis software\u202f: Structure and validation. Computer Methods and Programs in Biomedicine, 226, 107120. https://doi.org/10.1016/j.cmpb.2022.107120\n"
"", None))
    # retranslateUi

