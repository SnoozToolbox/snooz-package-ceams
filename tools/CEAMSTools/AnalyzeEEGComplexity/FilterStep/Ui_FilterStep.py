# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_FilterStep.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QRadioButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_FilterStep(object):
    def setupUi(self, FilterStep):
        if not FilterStep.objectName():
            FilterStep.setObjectName(u"FilterStep")
        FilterStep.resize(873, 662)
        FilterStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_3 = QVBoxLayout(FilterStep)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(FilterStep)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMouseTracking(True)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.fullband_radioButton = QRadioButton(self.frame)
        self.buttonGroup = QButtonGroup(FilterStep)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.fullband_radioButton)
        self.fullband_radioButton.setObjectName(u"fullband_radioButton")
        self.fullband_radioButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.fullband_radioButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.delta_radioButton = QRadioButton(self.frame)
        self.buttonGroup.addButton(self.delta_radioButton)
        self.delta_radioButton.setObjectName(u"delta_radioButton")

        self.horizontalLayout.addWidget(self.delta_radioButton)

        self.theta_radioButton = QRadioButton(self.frame)
        self.buttonGroup.addButton(self.theta_radioButton)
        self.theta_radioButton.setObjectName(u"theta_radioButton")

        self.horizontalLayout.addWidget(self.theta_radioButton)

        self.alpha_radioButton = QRadioButton(self.frame)
        self.buttonGroup.addButton(self.alpha_radioButton)
        self.alpha_radioButton.setObjectName(u"alpha_radioButton")

        self.horizontalLayout.addWidget(self.alpha_radioButton)

        self.beta_radioButton = QRadioButton(self.frame)
        self.buttonGroup.addButton(self.beta_radioButton)
        self.beta_radioButton.setObjectName(u"beta_radioButton")

        self.horizontalLayout.addWidget(self.beta_radioButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.custom_radioButton = QRadioButton(self.frame)
        self.buttonGroup.addButton(self.custom_radioButton)
        self.custom_radioButton.setObjectName(u"custom_radioButton")

        self.horizontalLayout_4.addWidget(self.custom_radioButton)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.low_cutoff_label = QLabel(self.frame)
        self.low_cutoff_label.setObjectName(u"low_cutoff_label")

        self.horizontalLayout_2.addWidget(self.low_cutoff_label)

        self.low_cutoff_doubleSpinBox = QDoubleSpinBox(self.frame)
        self.low_cutoff_doubleSpinBox.setObjectName(u"low_cutoff_doubleSpinBox")
        self.low_cutoff_doubleSpinBox.setMinimum(1.000000000000000)
        self.low_cutoff_doubleSpinBox.setMaximum(30.000000000000000)
        self.low_cutoff_doubleSpinBox.setValue(10.000000000000000)

        self.horizontalLayout_2.addWidget(self.low_cutoff_doubleSpinBox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.high_cutoff_doubleSpinBox = QDoubleSpinBox(self.frame)
        self.high_cutoff_doubleSpinBox.setObjectName(u"high_cutoff_doubleSpinBox")
        self.high_cutoff_doubleSpinBox.setMinimum(1.000000000000000)
        self.high_cutoff_doubleSpinBox.setMaximum(30.000000000000000)
        self.high_cutoff_doubleSpinBox.setValue(10.000000000000000)

        self.horizontalLayout_3.addWidget(self.high_cutoff_doubleSpinBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(FilterStep)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.unscored_radioButton = QRadioButton(self.frame_2)
        self.buttonGroup_2 = QButtonGroup(FilterStep)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.unscored_radioButton)
        self.unscored_radioButton.setObjectName(u"unscored_radioButton")
        self.unscored_radioButton.setChecked(True)

        self.horizontalLayout_5.addWidget(self.unscored_radioButton)

        self.sleep_stages_radioButton = QRadioButton(self.frame_2)
        self.buttonGroup_2.addButton(self.sleep_stages_radioButton)
        self.sleep_stages_radioButton.setObjectName(u"sleep_stages_radioButton")

        self.horizontalLayout_5.addWidget(self.sleep_stages_radioButton)

        self.specific_annotations_radioButton = QRadioButton(self.frame_2)
        self.buttonGroup_2.addButton(self.specific_annotations_radioButton)
        self.specific_annotations_radioButton.setObjectName(u"specific_annotations_radioButton")

        self.horizontalLayout_5.addWidget(self.specific_annotations_radioButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.wake_checkBox = QCheckBox(self.frame_2)
        self.wake_checkBox.setObjectName(u"wake_checkBox")

        self.horizontalLayout_6.addWidget(self.wake_checkBox)

        self.rem_checkBox = QCheckBox(self.frame_2)
        self.rem_checkBox.setObjectName(u"rem_checkBox")

        self.horizontalLayout_6.addWidget(self.rem_checkBox)

        self.n1_checkBox = QCheckBox(self.frame_2)
        self.n1_checkBox.setObjectName(u"n1_checkBox")

        self.horizontalLayout_6.addWidget(self.n1_checkBox)

        self.n2_checkBox = QCheckBox(self.frame_2)
        self.n2_checkBox.setObjectName(u"n2_checkBox")

        self.horizontalLayout_6.addWidget(self.n2_checkBox)

        self.n3_checkBox = QCheckBox(self.frame_2)
        self.n3_checkBox.setObjectName(u"n3_checkBox")

        self.horizontalLayout_6.addWidget(self.n3_checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_9.addWidget(self.checkBox)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.start_time_doubleSpinBox = QDoubleSpinBox(self.frame_2)
        self.start_time_doubleSpinBox.setObjectName(u"start_time_doubleSpinBox")

        self.horizontalLayout_8.addWidget(self.start_time_doubleSpinBox)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.duration_doubleSpinBox = QDoubleSpinBox(self.frame_2)
        self.duration_doubleSpinBox.setObjectName(u"duration_doubleSpinBox")
        self.duration_doubleSpinBox.setMaximum(2000.000000000000000)

        self.horizontalLayout_7.addWidget(self.duration_doubleSpinBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.retranslateUi(FilterStep)

        QMetaObject.connectSlotsByName(FilterStep)
    # setupUi

    def retranslateUi(self, FilterStep):
        FilterStep.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("FilterStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Frequency Band Selection<br/></span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("FilterStep", u"<html><head/><body><p>Select the frequency band that best matches your research objectives. <br/>This step filters the EEG signal into one of the standard bands, allowing you to focus your analysis on specific brain oscillations:<br/></p></body></html>", None))
        self.fullband_radioButton.setText(QCoreApplication.translate("FilterStep", u"Full Frequency Band (0.1\u201345 Hz)", None))
        self.delta_radioButton.setText(QCoreApplication.translate("FilterStep", u"Delta (0.16\u20134 Hz)", None))
        self.theta_radioButton.setText(QCoreApplication.translate("FilterStep", u"Theta (4\u20138 Hz)", None))
        self.alpha_radioButton.setText(QCoreApplication.translate("FilterStep", u"Alpha (8\u201313 Hz)", None))
        self.beta_radioButton.setText(QCoreApplication.translate("FilterStep", u"Beta (13\u201330 Hz)", None))
        self.custom_radioButton.setText(QCoreApplication.translate("FilterStep", u"Custom Frequency Band", None))
        self.low_cutoff_label.setText(QCoreApplication.translate("FilterStep", u"Low cutoff", None))
        self.label_4.setText(QCoreApplication.translate("FilterStep", u"high_cutoff_label", None))
        self.textEdit.setHtml(QCoreApplication.translate("FilterStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Filter Design</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The filter is a Butterworth design implemen"
                        "ted in second-order-section (SOS) form and applied using bidirectional zero-phase filtering. This approach preserves the requested magnitude response while eliminating phase distortion.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   Bandpass filter parameters:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      - Type : IIR bandpass</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      - Order : 6 (internally halved before the forward/backward pass)</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("FilterStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Recording Scope Selection<br/></span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("FilterStep", u"<html><head/><body><p>Select <span style=\" font-weight:700;\">Sleep Stages</span> to choose specific sleep stages for connectivity analysis.<br/>Select <span style=\" font-weight:700;\">Unscored</span> to analyze the entire recording or a selected time segment.<br/>Select <span style=\" font-weight:700;\">Specific Annotations</span> to perform the analysis based on event annotations.</p></body></html>", None))
        self.unscored_radioButton.setText(QCoreApplication.translate("FilterStep", u"Unscored", None))
        self.sleep_stages_radioButton.setText(QCoreApplication.translate("FilterStep", u"Sleep Stages", None))
        self.specific_annotations_radioButton.setText(QCoreApplication.translate("FilterStep", u"Specific Annotations (Select on next step)", None))
        self.wake_checkBox.setText(QCoreApplication.translate("FilterStep", u"Wake", None))
        self.rem_checkBox.setText(QCoreApplication.translate("FilterStep", u"REM", None))
        self.n1_checkBox.setText(QCoreApplication.translate("FilterStep", u"N1", None))
        self.n2_checkBox.setText(QCoreApplication.translate("FilterStep", u"N2", None))
        self.n3_checkBox.setText(QCoreApplication.translate("FilterStep", u"N3", None))
        self.checkBox.setText(QCoreApplication.translate("FilterStep", u"Trim Signal", None))
        self.label_6.setText(QCoreApplication.translate("FilterStep", u"Start Time", None))
        self.label_7.setText(QCoreApplication.translate("FilterStep", u"Duration", None))
    # retranslateUi

