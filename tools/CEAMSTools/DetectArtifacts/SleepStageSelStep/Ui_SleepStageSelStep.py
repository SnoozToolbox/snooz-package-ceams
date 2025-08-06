# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SleepStageSelStep.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QButtonGroup, QCheckBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QPlainTextEdit, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_SleepStageSelStep(object):
    def setupUi(self, SleepStageSelStep):
        if not SleepStageSelStep.objectName():
            SleepStageSelStep.setObjectName(u"SleepStageSelStep")
        SleepStageSelStep.resize(980, 739)
        SleepStageSelStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(SleepStageSelStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(SleepStageSelStep)
        self.label_7.setObjectName(u"label_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_7)

        self.plainTextEdit = QPlainTextEdit(SleepStageSelStep)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy1)
        self.plainTextEdit.setMinimumSize(QSize(0, 200))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 200))
        self.plainTextEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.plainTextEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_1 = QCheckBox(SleepStageSelStep)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_1, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(SleepStageSelStep)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 2)

        self.checkBox_3 = QCheckBox(SleepStageSelStep)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_3, 0, 3, 1, 1)

        self.checkBox_5 = QCheckBox(SleepStageSelStep)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_5, 0, 4, 1, 1)

        self.checkBox_9 = QCheckBox(SleepStageSelStep)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout.addWidget(self.checkBox_9, 1, 0, 1, 2)

        self.checkBox_0 = QCheckBox(SleepStageSelStep)
        self.checkBox_0.setObjectName(u"checkBox_0")

        self.gridLayout.addWidget(self.checkBox_0, 1, 2, 1, 2)


        self.horizontalLayout_4.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(SleepStageSelStep)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(SleepStageSelStep)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(SleepStageSelStep)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_4)

        self.radioButton_set1 = QRadioButton(SleepStageSelStep)
        self.Theshold_sets = QButtonGroup(SleepStageSelStep)
        self.Theshold_sets.setObjectName(u"Theshold_sets")
        self.Theshold_sets.addButton(self.radioButton_set1)
        self.radioButton_set1.setObjectName(u"radioButton_set1")
        self.radioButton_set1.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_set1)

        self.radioButton_set2 = QRadioButton(SleepStageSelStep)
        self.Theshold_sets.addButton(self.radioButton_set2)
        self.radioButton_set2.setObjectName(u"radioButton_set2")

        self.verticalLayout.addWidget(self.radioButton_set2)

        self.label_2 = QLabel(SleepStageSelStep)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(SleepStageSelStep)

        QMetaObject.connectSlotsByName(SleepStageSelStep)
    # setupUi

    def retranslateUi(self, SleepStageSelStep):
        SleepStageSelStep.setWindowTitle("")
        self.label_7.setText(QCoreApplication.translate("SleepStageSelStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep Stage Selection</span></p></body></html>", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("SleepStageSelStep", u"Select the sleep stages in which you want to detect artifacts.\n"
"\n"
"Artifact detection performs better when similar sleep stages are selected, as the power distribution can be modeled more accurately. \n"
"Some detectors use a 3-component Gaussian Mixture Model (GMM) to estimate the standard deviation of non-corrupted data, \n"
"which is then used to define the threshold value.\n"
"\n"
"* We recommend running artifact detection separately for NREM, REM, and Awake stages.\n"
"* Make sur to have different annotation group or name to avoid confusion.\n"
"\n"
"Please select \"Unscored\" if your data does not include sleep stages.", None))
        self.checkBox_1.setText(QCoreApplication.translate("SleepStageSelStep", u"N1", None))
        self.checkBox_2.setText(QCoreApplication.translate("SleepStageSelStep", u"N2", None))
        self.checkBox_3.setText(QCoreApplication.translate("SleepStageSelStep", u"N3", None))
        self.checkBox_5.setText(QCoreApplication.translate("SleepStageSelStep", u"R", None))
        self.checkBox_9.setText(QCoreApplication.translate("SleepStageSelStep", u"Unscored", None))
        self.checkBox_0.setText(QCoreApplication.translate("SleepStageSelStep", u"Awake", None))
        self.label.setText(QCoreApplication.translate("SleepStageSelStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Default threshold values</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("SleepStageSelStep", u"Threshold values for the different algorithms can be edited in \"Step 5 \u2013 Detector Settings\".", None))
        self.label_4.setText(QCoreApplication.translate("SleepStageSelStep", u"However, we also provide two sets of default values:", None))
        self.radioButton_set1.setText(QCoreApplication.translate("SleepStageSelStep", u"Set 1 : is intended for NREM sleep stages and can also be used for Awake or Unscored stages.", None))
        self.radioButton_set2.setText(QCoreApplication.translate("SleepStageSelStep", u"Set 2 is more sensitive and intended for REM sleep stages.", None))
        self.label_2.setText("")
    # retranslateUi

