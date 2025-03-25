# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ExportResultsStep.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import themes_rc

class Ui_ExportResultsStep(object):
    def setupUi(self, ExportResultsStep):
        if not ExportResultsStep.objectName():
            ExportResultsStep.setObjectName(u"ExportResultsStep")
        ExportResultsStep.resize(943, 659)
        ExportResultsStep.setStyleSheet(u"font: 12pt \"Roboto\";background-color: rgb(255, 255, 255);")
        self.verticalLayout_10 = QVBoxLayout(ExportResultsStep)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(ExportResultsStep)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label.setLineWidth(0)

        self.verticalLayout_4.addWidget(self.label)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setLineWidth(0)

        self.verticalLayout_6.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLineWidth(0)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.checkBox)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLineWidth(0)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        self.frame_5 = QFrame(ExportResultsStep)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_2 = QCheckBox(self.frame_5)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font)

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLineWidth(0)

        self.verticalLayout_5.addWidget(self.label_5)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLineWidth(0)

        self.horizontalLayout_6.addWidget(self.label_6)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame_5)


        self.verticalLayout_10.addLayout(self.verticalLayout)


        self.retranslateUi(ExportResultsStep)
        self.pushButton.clicked.connect(ExportResultsStep.browse_slot) # Connect the browse button to the browse_slot function
        QMetaObject.connectSlotsByName(ExportResultsStep)
    # setupUi

    def retranslateUi(self, ExportResultsStep):
        ExportResultsStep.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("ExportResultsStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Export Scoring</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("ExportResultsStep", u"In this step, you can either apply a prediction or perform validation if you have expert-annotated sleep stage files.\n"
"The sleep stage scoring from the YASA algorithm will then be exported.", None))
        self.label_2.setText(QCoreApplication.translate("ExportResultsStep", u"<html><head/><body><p>Define a name for the predicted sleep stages group name in the accessory file.</p></body></html>", None))
        self.lineEdit_2.setText("")
        self.checkBox.setText(QCoreApplication.translate("ExportResultsStep", u"Automatic Scoring", None))
        self.label_3.setText(QCoreApplication.translate("ExportResultsStep", u"<html><head/><body><p>Be careful! Changing the group name <span style=\" font-weight:700;\">'stage'</span> to a different value may prevent Snooz from correctly identifying sleep stages<br/>in other tools.</p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("ExportResultsStep", u"Compare with Expert Scoring", None))
        self.label_5.setText(QCoreApplication.translate("ExportResultsStep", u"<html><head/><body><p>To perform validation, place the expert annotation files in the same directory as the PSG files and convert them to .tsv format<br/>to ensure compatibility with PSGReader.</p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("ExportResultsStep", u"Select the folder where the exported files are supposed to be saved", None))
        self.pushButton.setText(QCoreApplication.translate("ExportResultsStep", u"Choose", None))
        self.label_6.setText(QCoreApplication.translate("ExportResultsStep", u"<html><head/><body><p>The exported file includes, the expert annotated hypnogram, the predicted hypnogram, confusion matrix, accuracy, and<br/>the average confidence.</p></body></html>", None))
    # retranslateUi

