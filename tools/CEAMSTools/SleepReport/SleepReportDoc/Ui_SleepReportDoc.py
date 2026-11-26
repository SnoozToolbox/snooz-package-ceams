# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SleepReportDoc.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_SleepReportDoc(object):
    def setupUi(self, SleepReportDoc):
        if not SleepReportDoc.objectName():
            SleepReportDoc.setObjectName(u"SleepReportDoc")
        SleepReportDoc.resize(900, 700)
        self.verticalLayout = QVBoxLayout(SleepReportDoc)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(SleepReportDoc)
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

        self.common_settings_info = QFrame(self.content_widget)
        self.common_settings_info.setObjectName(u"common_settings_info")
        self.common_settings_info.setFrameShape(QFrame.Shape.NoFrame)
        self.common_settings_info.setProperty(u"variant", u"info")
        self.common_settings_info_layout = QHBoxLayout(self.common_settings_info)
        self.common_settings_info_layout.setObjectName(u"common_settings_info_layout")
        self.common_settings_info_layout.setContentsMargins(14, 10, 14, 10)
        self.common_settings_info_label = QLabel(self.common_settings_info)
        self.common_settings_info_label.setObjectName(u"common_settings_info_label")
        self.common_settings_info_label.setTextFormat(Qt.TextFormat.RichText)
        self.common_settings_info_label.setWordWrap(True)

        self.common_settings_info_layout.addWidget(self.common_settings_info_label)


        self.content_layout.addWidget(self.common_settings_info)

        self.steps_section_layout = QVBoxLayout()
        self.steps_section_layout.setSpacing(8)
        self.steps_section_layout.setObjectName(u"steps_section_layout")
        self.steps_title_label = QLabel(self.content_widget)
        self.steps_title_label.setObjectName(u"steps_title_label")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.steps_title_label.setFont(font1)

        self.steps_section_layout.addWidget(self.steps_title_label)

        self.steps_card = QFrame(self.content_widget)
        self.steps_card.setObjectName(u"steps_card")
        self.steps_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.steps_card.setFrameShadow(QFrame.Shadow.Raised)
        self.steps_card_layout = QVBoxLayout(self.steps_card)
        self.steps_card_layout.setSpacing(10)
        self.steps_card_layout.setObjectName(u"steps_card_layout")
        self.steps_card_layout.setContentsMargins(10, 10, 10, 10)
        self.steps_grid = QGridLayout()
        self.steps_grid.setObjectName(u"steps_grid")
        self.steps_grid.setHorizontalSpacing(12)
        self.steps_grid.setVerticalSpacing(10)
        self.step_1_number_label = QLabel(self.steps_card)
        self.step_1_number_label.setObjectName(u"step_1_number_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.step_1_number_label.setFont(font2)
        self.step_1_number_label.setProperty(u"variant", u"step_number")
        self.step_1_number_label.setMinimumSize(QSize(24, 24))
        self.step_1_number_label.setMaximumSize(QSize(24, 24))
        self.step_1_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.steps_grid.addWidget(self.step_1_number_label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.step_1_name_label = QLabel(self.steps_card)
        self.step_1_name_label.setObjectName(u"step_1_name_label")
        font3 = QFont()
        font3.setBold(True)
        self.step_1_name_label.setFont(font3)
        self.step_1_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_1_name_label, 0, 1, 1, 1)

        self.steps_gap = QSpacerItem(16, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.steps_grid.addItem(self.steps_gap, 0, 2, 1, 1)

        self.step_1_label = QLabel(self.steps_card)
        self.step_1_label.setObjectName(u"step_1_label")
        self.step_1_label.setWordWrap(True)
        self.step_1_label.setProperty(u"variant", u"help")
        self.step_1_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_1_label, 0, 3, 1, 1)

        self.step_line_2 = QFrame(self.steps_card)
        self.step_line_2.setObjectName(u"step_line_2")
        self.step_line_2.setFrameShape(QFrame.Shape.HLine)
        self.step_line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.steps_grid.addWidget(self.step_line_2, 1, 0, 1, 4)

        self.step_2_number_label = QLabel(self.steps_card)
        self.step_2_number_label.setObjectName(u"step_2_number_label")
        self.step_2_number_label.setFont(font2)
        self.step_2_number_label.setProperty(u"variant", u"step_number")
        self.step_2_number_label.setMinimumSize(QSize(24, 24))
        self.step_2_number_label.setMaximumSize(QSize(24, 24))
        self.step_2_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.steps_grid.addWidget(self.step_2_number_label, 2, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.step_2_name_label = QLabel(self.steps_card)
        self.step_2_name_label.setObjectName(u"step_2_name_label")
        self.step_2_name_label.setFont(font3)
        self.step_2_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_2_name_label, 2, 1, 1, 1)

        self.step_2_label = QLabel(self.steps_card)
        self.step_2_label.setObjectName(u"step_2_label")
        self.step_2_label.setWordWrap(True)
        self.step_2_label.setProperty(u"variant", u"help")
        self.step_2_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_2_label, 2, 3, 1, 1)

        self.step_line_3 = QFrame(self.steps_card)
        self.step_line_3.setObjectName(u"step_line_3")
        self.step_line_3.setFrameShape(QFrame.Shape.HLine)
        self.step_line_3.setFrameShadow(QFrame.Shadow.Plain)

        self.steps_grid.addWidget(self.step_line_3, 3, 0, 1, 4)

        self.step_3_number_label = QLabel(self.steps_card)
        self.step_3_number_label.setObjectName(u"step_3_number_label")
        self.step_3_number_label.setFont(font2)
        self.step_3_number_label.setProperty(u"variant", u"step_number")
        self.step_3_number_label.setMinimumSize(QSize(24, 24))
        self.step_3_number_label.setMaximumSize(QSize(24, 24))
        self.step_3_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.steps_grid.addWidget(self.step_3_number_label, 4, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.step_3_name_label = QLabel(self.steps_card)
        self.step_3_name_label.setObjectName(u"step_3_name_label")
        self.step_3_name_label.setFont(font3)
        self.step_3_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_3_name_label, 4, 1, 1, 1)

        self.step_3_label = QLabel(self.steps_card)
        self.step_3_label.setObjectName(u"step_3_label")
        self.step_3_label.setWordWrap(True)
        self.step_3_label.setProperty(u"variant", u"help")
        self.step_3_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_3_label, 4, 3, 1, 1)

        self.step_line_4 = QFrame(self.steps_card)
        self.step_line_4.setObjectName(u"step_line_4")
        self.step_line_4.setFrameShape(QFrame.Shape.HLine)
        self.step_line_4.setFrameShadow(QFrame.Shadow.Plain)

        self.steps_grid.addWidget(self.step_line_4, 5, 0, 1, 4)

        self.step_4_number_label = QLabel(self.steps_card)
        self.step_4_number_label.setObjectName(u"step_4_number_label")
        self.step_4_number_label.setFont(font2)
        self.step_4_number_label.setProperty(u"variant", u"step_number")
        self.step_4_number_label.setMinimumSize(QSize(24, 24))
        self.step_4_number_label.setMaximumSize(QSize(24, 24))
        self.step_4_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.steps_grid.addWidget(self.step_4_number_label, 6, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.step_4_name_label = QLabel(self.steps_card)
        self.step_4_name_label.setObjectName(u"step_4_name_label")
        self.step_4_name_label.setFont(font3)
        self.step_4_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_4_name_label, 6, 1, 1, 1)

        self.step_4_label = QLabel(self.steps_card)
        self.step_4_label.setObjectName(u"step_4_label")
        self.step_4_label.setWordWrap(True)
        self.step_4_label.setProperty(u"variant", u"help")
        self.step_4_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_4_label, 6, 3, 1, 1)

        self.steps_grid.setColumnStretch(3, 1)

        self.steps_card_layout.addLayout(self.steps_grid)


        self.steps_section_layout.addWidget(self.steps_card)


        self.content_layout.addLayout(self.steps_section_layout)

        self.reports_section_layout = QVBoxLayout()
        self.reports_section_layout.setSpacing(8)
        self.reports_section_layout.setObjectName(u"reports_section_layout")
        self.reports_title_label = QLabel(self.content_widget)
        self.reports_title_label.setObjectName(u"reports_title_label")
        self.reports_title_label.setFont(font1)

        self.reports_section_layout.addWidget(self.reports_title_label)

        self.reports_card = QFrame(self.content_widget)
        self.reports_card.setObjectName(u"reports_card")
        self.reports_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.reports_card.setFrameShadow(QFrame.Shadow.Raised)
        self.reports_card_layout = QVBoxLayout(self.reports_card)
        self.reports_card_layout.setSpacing(10)
        self.reports_card_layout.setObjectName(u"reports_card_layout")
        self.reports_card_layout.setContentsMargins(10, 10, 10, 10)
        self.report_grid = QGridLayout()
        self.report_grid.setObjectName(u"report_grid")
        self.report_grid.setHorizontalSpacing(32)
        self.report_grid.setVerticalSpacing(10)
        self.report_1_name_label = QLabel(self.reports_card)
        self.report_1_name_label.setObjectName(u"report_1_name_label")
        self.report_1_name_label.setFont(font3)
        self.report_1_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.report_grid.addWidget(self.report_1_name_label, 0, 0, 1, 1)

        self.report_1_label = QLabel(self.reports_card)
        self.report_1_label.setObjectName(u"report_1_label")
        self.report_1_label.setWordWrap(True)

        self.report_grid.addWidget(self.report_1_label, 0, 1, 1, 1)

        self.report_2_name_label = QLabel(self.reports_card)
        self.report_2_name_label.setObjectName(u"report_2_name_label")
        self.report_2_name_label.setFont(font3)
        self.report_2_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.report_grid.addWidget(self.report_2_name_label, 1, 0, 1, 1)

        self.report_2_label = QLabel(self.reports_card)
        self.report_2_label.setObjectName(u"report_2_label")
        self.report_2_label.setWordWrap(True)

        self.report_grid.addWidget(self.report_2_label, 1, 1, 1, 1)

        self.report_3_name_label = QLabel(self.reports_card)
        self.report_3_name_label.setObjectName(u"report_3_name_label")
        self.report_3_name_label.setFont(font3)
        self.report_3_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.report_grid.addWidget(self.report_3_name_label, 2, 0, 1, 1)

        self.report_3_label = QLabel(self.reports_card)
        self.report_3_label.setObjectName(u"report_3_label")
        self.report_3_label.setWordWrap(True)

        self.report_grid.addWidget(self.report_3_label, 2, 1, 1, 1)

        self.report_grid.setColumnStretch(1, 1)

        self.reports_card_layout.addLayout(self.report_grid)

        self.reports_note_label = QLabel(self.reports_card)
        self.reports_note_label.setObjectName(u"reports_note_label")
        self.reports_note_label.setFont(font2)
        self.reports_note_label.setWordWrap(True)
        self.reports_note_label.setProperty(u"variant", u"help")

        self.reports_card_layout.addWidget(self.reports_note_label)


        self.reports_section_layout.addWidget(self.reports_card)


        self.content_layout.addLayout(self.reports_section_layout)

        self.files_section_layout = QVBoxLayout()
        self.files_section_layout.setSpacing(8)
        self.files_section_layout.setObjectName(u"files_section_layout")
        self.files_title_label = QLabel(self.content_widget)
        self.files_title_label.setObjectName(u"files_title_label")
        self.files_title_label.setFont(font1)

        self.files_section_layout.addWidget(self.files_title_label)

        self.files_card = QFrame(self.content_widget)
        self.files_card.setObjectName(u"files_card")
        self.files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.files_card_layout = QVBoxLayout(self.files_card)
        self.files_card_layout.setSpacing(10)
        self.files_card_layout.setObjectName(u"files_card_layout")
        self.files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.files_grid = QGridLayout()
        self.files_grid.setObjectName(u"files_grid")
        self.files_grid.setHorizontalSpacing(32)
        self.files_grid.setVerticalSpacing(6)
        self.file_1_name_label = QLabel(self.files_card)
        self.file_1_name_label.setObjectName(u"file_1_name_label")
        self.file_1_name_label.setFont(font3)

        self.files_grid.addWidget(self.file_1_name_label, 0, 0, 1, 1)

        self.file_1_label = QLabel(self.files_card)
        self.file_1_label.setObjectName(u"file_1_label")
        self.file_1_label.setWordWrap(True)

        self.files_grid.addWidget(self.file_1_label, 0, 1, 1, 1)

        self.file_2_name_label = QLabel(self.files_card)
        self.file_2_name_label.setObjectName(u"file_2_name_label")
        self.file_2_name_label.setFont(font3)

        self.files_grid.addWidget(self.file_2_name_label, 1, 0, 1, 1)

        self.file_2_label = QLabel(self.files_card)
        self.file_2_label.setObjectName(u"file_2_label")
        self.file_2_label.setWordWrap(True)

        self.files_grid.addWidget(self.file_2_label, 1, 1, 1, 1)

        self.file_3_name_label = QLabel(self.files_card)
        self.file_3_name_label.setObjectName(u"file_3_name_label")
        self.file_3_name_label.setFont(font3)

        self.files_grid.addWidget(self.file_3_name_label, 2, 0, 1, 1)

        self.file_3_label = QLabel(self.files_card)
        self.file_3_label.setObjectName(u"file_3_label")
        self.file_3_label.setTextFormat(Qt.TextFormat.RichText)
        self.file_3_label.setWordWrap(True)

        self.files_grid.addWidget(self.file_3_label, 2, 1, 1, 1)

        self.files_grid.setColumnStretch(1, 1)

        self.files_card_layout.addLayout(self.files_grid)


        self.files_section_layout.addWidget(self.files_card)


        self.content_layout.addLayout(self.files_section_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SleepReportDoc)

        QMetaObject.connectSlotsByName(SleepReportDoc)
    # setupUi

    def retranslateUi(self, SleepReportDoc):
        SleepReportDoc.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("SleepReportDoc", u"Report Sleep Variables", None))
        self.subtitle_label.setText(QCoreApplication.translate("SleepReportDoc", u"Generates three types of reports from your polysomnography (PSG) files: the sleep report, the events reports and the temporal links reports.", None))
        self.common_settings_info_label.setText(QCoreApplication.translate("SleepReportDoc", u"<b>Before you start</b><br/>Define the sleep cycle configuration to use for the analysis: \"Common settings\" \u203a \"Sleep Cycles\", in the left panel.", None))
        self.steps_title_label.setText(QCoreApplication.translate("SleepReportDoc", u"What you will do", None))
        self.step_1_number_label.setText(QCoreApplication.translate("SleepReportDoc", u"1", None))
        self.step_1_name_label.setText(QCoreApplication.translate("SleepReportDoc", u"Input Files", None))
        self.step_1_label.setText(QCoreApplication.translate("SleepReportDoc", u"Add the PSG files. The reports are generated from the sleep stages and the events of the accessory file, but the header of the PSG file is also needed. Check the information of each subject.", None))
        self.step_2_number_label.setText(QCoreApplication.translate("SleepReportDoc", u"2", None))
        self.step_2_name_label.setText(QCoreApplication.translate("SleepReportDoc", u"Events Report", None))
        self.step_2_label.setText(QCoreApplication.translate("SleepReportDoc", u"Add an events report to an event group or name: a predefined report or a new one with your criteria. You can also combine events to create a new group.", None))
        self.step_3_number_label.setText(QCoreApplication.translate("SleepReportDoc", u"3", None))
        self.step_3_name_label.setText(QCoreApplication.translate("SleepReportDoc", u"Temporal Links", None))
        self.step_3_label.setText(QCoreApplication.translate("SleepReportDoc", u"Check the pairs of events reports to link, then set the analysis window: the maximum delay between two linked events (0.5 s by default).", None))
        self.step_4_number_label.setText(QCoreApplication.translate("SleepReportDoc", u"4", None))
        self.step_4_name_label.setText(QCoreApplication.translate("SleepReportDoc", u"Generate Reports", None))
        self.step_4_label.setText(QCoreApplication.translate("SleepReportDoc", u"Choose the output directory and the prefix of the report filenames, then check the list of the reports to generate.", None))
        self.reports_title_label.setText(QCoreApplication.translate("SleepReportDoc", u"Reports", None))
        self.report_1_name_label.setText(QCoreApplication.translate("SleepReportDoc", u"Sleep report", None))
        self.report_1_label.setText(QCoreApplication.translate("SleepReportDoc", u"The distribution of the sleep stages across the sleep cycles, the thirds and the halves of the night, and the transitions between the sleep stages.", None))
        self.report_2_name_label.setText(QCoreApplication.translate("SleepReportDoc", u"Events reports", None))
        self.report_2_label.setText(QCoreApplication.translate("SleepReportDoc", u"The selected events by sleep stage, sleep cycle, and thirds and halves of the night, kept by the criteria of the report. Predefined reports: arousals, bruxism, periodic limb movements (PLM: sleep only, recording time, awake in the sleep period, before sleep onset), respiratory events, snoring, and events without criteria (sleep only, EOG_Phasic, EOG_Tonic).", None))
        self.report_3_name_label.setText(QCoreApplication.translate("SleepReportDoc", u"Temporal links reports", None))
        self.report_3_label.setText(QCoreApplication.translate("SleepReportDoc", u"The events of two events reports that occur together: one starts within the analysis window (0.5 s by default) after the start or the end of the other, or the two overlap. For example, arousals that start just after the end of respiratory events.", None))
        self.reports_note_label.setText(QCoreApplication.translate("SleepReportDoc", u"Each report is a .tsv file: one row per PSG recording and one column per variable, defined in the _info.tsv file written with the report.", None))
        self.files_title_label.setText(QCoreApplication.translate("SleepReportDoc", u"Accepted files", None))
        self.file_1_name_label.setText(QCoreApplication.translate("SleepReportDoc", u"EDF", None))
        self.file_1_label.setText(QCoreApplication.translate("SleepReportDoc", u"The .edf and .tsv files have the same filename and are in the same directory.", None))
        self.file_2_name_label.setText(QCoreApplication.translate("SleepReportDoc", u"Stellate", None))
        self.file_2_label.setText(QCoreApplication.translate("SleepReportDoc", u"The .sig and .sts files have the same filename and are in the same directory.", None))
        self.file_3_name_label.setText(QCoreApplication.translate("SleepReportDoc", u"NATUS", None))
        self.file_3_label.setText(QCoreApplication.translate("SleepReportDoc", u"The entire NATUS subject folder is required <i>(for CEAMS users)</i>.", None))
    # retranslateUi

