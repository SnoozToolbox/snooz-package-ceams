# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_OutputFileStep.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_OutputFileStep(object):
    def setupUi(self, OutputFileStep):
        if not OutputFileStep.objectName():
            OutputFileStep.setObjectName(u"OutputFileStep")
        OutputFileStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(OutputFileStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(OutputFileStep)
        self.content_widget.setObjectName(u"content_widget")
        self.content_widget.setMaximumSize(QSize(800, 16777215))
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setSpacing(16)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout = QVBoxLayout()
        self.header_layout.setSpacing(6)
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(self.content_widget)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.header_layout.addWidget(self.title_label)

        self.subtitle_label = QLabel(self.content_widget)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setProperty(u"variant", u"help")

        self.header_layout.addWidget(self.subtitle_label)


        self.content_layout.addLayout(self.header_layout)

        self.events_info = QFrame(self.content_widget)
        self.events_info.setObjectName(u"events_info")
        self.events_info.setFrameShape(QFrame.Shape.NoFrame)
        self.events_info.setProperty(u"variant", u"info")
        self.events_info_layout = QHBoxLayout(self.events_info)
        self.events_info_layout.setObjectName(u"events_info_layout")
        self.events_info_layout.setContentsMargins(14, 10, 14, 10)
        self.events_info_label = QLabel(self.events_info)
        self.events_info_label.setObjectName(u"events_info_label")
        self.events_info_label.setTextFormat(Qt.TextFormat.RichText)
        self.events_info_label.setWordWrap(True)

        self.events_info_layout.addWidget(self.events_info_label)


        self.content_layout.addWidget(self.events_info)

        self.cohort_card = QFrame(self.content_widget)
        self.cohort_card.setObjectName(u"cohort_card")
        self.cohort_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.cohort_card.setFrameShadow(QFrame.Shadow.Raised)
        self.cohort_card_layout = QVBoxLayout(self.cohort_card)
        self.cohort_card_layout.setSpacing(10)
        self.cohort_card_layout.setObjectName(u"cohort_card_layout")
        self.cohort_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.cohort_card)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)

        self.cohort_card_layout.addWidget(self.label)

        self.cohort_label = QLabel(self.cohort_card)
        self.cohort_label.setObjectName(u"cohort_label")
        self.cohort_label.setWordWrap(True)
        self.cohort_label.setProperty(u"variant", u"help")

        self.cohort_card_layout.addWidget(self.cohort_label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setVerticalSpacing(10)
        self.label_3 = QLabel(self.cohort_card)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit_CohortFilename = QLineEdit(self.cohort_card)
        self.lineEdit_CohortFilename.setObjectName(u"lineEdit_CohortFilename")

        self.gridLayout.addWidget(self.lineEdit_CohortFilename, 0, 1, 1, 1)

        self.pushButton_CohortFilename = QPushButton(self.cohort_card)
        self.pushButton_CohortFilename.setObjectName(u"pushButton_CohortFilename")

        self.gridLayout.addWidget(self.pushButton_CohortFilename, 0, 2, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.cohort_card_layout.addLayout(self.gridLayout)

        self.cohort_help_label = QLabel(self.cohort_card)
        self.cohort_help_label.setObjectName(u"cohort_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.cohort_help_label.setFont(font2)
        self.cohort_help_label.setWordWrap(True)
        self.cohort_help_label.setProperty(u"variant", u"help")

        self.cohort_card_layout.addWidget(self.cohort_help_label)


        self.content_layout.addWidget(self.cohort_card)

        self.about_characteristics_layout = QVBoxLayout()
        self.about_characteristics_layout.setSpacing(6)
        self.about_characteristics_layout.setObjectName(u"about_characteristics_layout")
        self.label_4 = QLabel(self.content_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.about_characteristics_layout.addWidget(self.label_4)

        self.characteristics_layout = QHBoxLayout()
        self.characteristics_layout.setSpacing(16)
        self.characteristics_layout.setObjectName(u"characteristics_layout")
        self.label_6 = QLabel(self.content_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.TextFormat.RichText)
        self.label_6.setWordWrap(True)
        self.label_6.setProperty(u"variant", u"help")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.characteristics_layout.addWidget(self.label_6)

        self.label_2 = QLabel(self.content_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.TextFormat.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setProperty(u"variant", u"help")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.characteristics_layout.addWidget(self.label_2)

        self.characteristics_layout.setStretch(0, 1)
        self.characteristics_layout.setStretch(1, 1)

        self.about_characteristics_layout.addLayout(self.characteristics_layout)


        self.content_layout.addLayout(self.about_characteristics_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(OutputFileStep)

        QMetaObject.connectSlotsByName(OutputFileStep)
    # setupUi

    def retranslateUi(self, OutputFileStep):
        OutputFileStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("OutputFileStep", u"Output File", None))
        self.subtitle_label.setText(QCoreApplication.translate("OutputFileStep", u"Choose the file of the REM report for the cohort.", None))
        self.events_info_label.setText(QCoreApplication.translate("OutputFileStep", u"<b>REM events and mini-epochs</b><br/>They are added to the accessory file (.tsv, .sts or .ent) as [group, name, start_sec, duration_sec, channels]. The events of the file with the same group and name are replaced.", None))
        self.label.setText(QCoreApplication.translate("OutputFileStep", u"REM report for the cohort", None))
        self.cohort_label.setText(QCoreApplication.translate("OutputFileStep", u"One line per recording.", None))
        self.label_3.setText(QCoreApplication.translate("OutputFileStep", u"Filename", None))
        self.lineEdit_CohortFilename.setPlaceholderText(QCoreApplication.translate("OutputFileStep", u"Select a .tsv file", None))
        self.pushButton_CohortFilename.setText(QCoreApplication.translate("OutputFileStep", u"Browse", None))
        self.cohort_help_label.setText(QCoreApplication.translate("OutputFileStep", u"The characteristics of each REM are saved in a folder named \"rems_characteristics\", next to this file. The report needs scored sleep stages (\"Detector Step\"); the number of hours and cycles reported is set in \"Hours and Cycles\", in the left panel.", None))
        self.label_4.setText(QCoreApplication.translate("OutputFileStep", u"About the REM characteristics", None))
        self.label_6.setText(QCoreApplication.translate("OutputFileStep", u"<b>For each REM</b><br/>\u2022 events file: the REM events in the Snooz annotation format<br/>\u2022 summary file: start, peak and end times, duration, absolute amplitude of LOC and ROC at the peak of the REM (\u00b5V), absolute rise and fall slopes of LOC and ROC (\u00b5V/s)", None))
        self.label_2.setText(QCoreApplication.translate("OutputFileStep", u"<b>For the cohort</b><br/>\u2022 REM count<br/>\u2022 duration of the REMs (s)<br/>\u2022 amplitude of the REMs: difference between the peak and the trough of LOC \u2212 ROC<br/>\u2022 density of the REMs per sleep cycle and per hour<br/>\u2022 variability of the densities<br/>\u2022 percentage of phasic and tonic REM sleep<br/>\u2022 peak-to-peak energy (\u00b5V\u00b2)<br/>\u2022 peak-to-peak activity index<br/>The averages are reported:<br/>&nbsp;&nbsp;\u2013 total (all night)<br/>&nbsp;&nbsp;\u2013 per sleep cycle<br/>&nbsp;&nbsp;\u2013 per clock hour<br/>&nbsp;&nbsp;\u2013 per hour spent in each stage", None))
    # retranslateUi

