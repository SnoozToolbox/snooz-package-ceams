# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_IntroStep.ui'
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

class Ui_IntroStep(object):
    def setupUi(self, IntroStep):
        if not IntroStep.objectName():
            IntroStep.setObjectName(u"IntroStep")
        IntroStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(IntroStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(IntroStep)
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

        self.steps_grid.setColumnStretch(3, 1)

        self.steps_card_layout.addLayout(self.steps_grid)


        self.steps_section_layout.addWidget(self.steps_card)


        self.content_layout.addLayout(self.steps_section_layout)

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

        self.files_grid.setColumnStretch(1, 1)

        self.files_card_layout.addLayout(self.files_grid)


        self.files_section_layout.addWidget(self.files_card)


        self.content_layout.addLayout(self.files_section_layout)

        self.replace_warning = QFrame(self.content_widget)
        self.replace_warning.setObjectName(u"replace_warning")
        self.replace_warning.setFrameShape(QFrame.Shape.NoFrame)
        self.replace_warning.setProperty(u"variant", u"warning")
        self.replace_warning_layout = QHBoxLayout(self.replace_warning)
        self.replace_warning_layout.setObjectName(u"replace_warning_layout")
        self.replace_warning_layout.setContentsMargins(14, 10, 14, 10)
        self.replace_warning_label = QLabel(self.replace_warning)
        self.replace_warning_label.setObjectName(u"replace_warning_label")
        self.replace_warning_label.setTextFormat(Qt.TextFormat.RichText)
        self.replace_warning_label.setWordWrap(True)

        self.replace_warning_layout.addWidget(self.replace_warning_label)


        self.content_layout.addWidget(self.replace_warning)

        self.filename_info = QFrame(self.content_widget)
        self.filename_info.setObjectName(u"filename_info")
        self.filename_info.setFrameShape(QFrame.Shape.NoFrame)
        self.filename_info.setProperty(u"variant", u"info")
        self.filename_info_layout = QHBoxLayout(self.filename_info)
        self.filename_info_layout.setObjectName(u"filename_info_layout")
        self.filename_info_layout.setContentsMargins(14, 10, 14, 10)
        self.filename_info_label = QLabel(self.filename_info)
        self.filename_info_label.setObjectName(u"filename_info_label")
        self.filename_info_label.setTextFormat(Qt.TextFormat.RichText)
        self.filename_info_label.setWordWrap(True)

        self.filename_info_layout.addWidget(self.filename_info_label)


        self.content_layout.addWidget(self.filename_info)

        self.about_conversion_layout = QVBoxLayout()
        self.about_conversion_layout.setSpacing(6)
        self.about_conversion_layout.setObjectName(u"about_conversion_layout")
        self.about_conversion_title_label = QLabel(self.content_widget)
        self.about_conversion_title_label.setObjectName(u"about_conversion_title_label")
        self.about_conversion_title_label.setFont(font3)

        self.about_conversion_layout.addWidget(self.about_conversion_title_label)

        self.about_conversion_label = QLabel(self.content_widget)
        self.about_conversion_label.setObjectName(u"about_conversion_label")
        self.about_conversion_label.setWordWrap(True)
        self.about_conversion_label.setProperty(u"variant", u"help")

        self.about_conversion_layout.addWidget(self.about_conversion_label)

        self.conversion_layout = QHBoxLayout()
        self.conversion_layout.setSpacing(16)
        self.conversion_layout.setObjectName(u"conversion_layout")
        self.events_conversion_label = QLabel(self.content_widget)
        self.events_conversion_label.setObjectName(u"events_conversion_label")
        self.events_conversion_label.setTextFormat(Qt.TextFormat.RichText)
        self.events_conversion_label.setWordWrap(True)
        self.events_conversion_label.setProperty(u"variant", u"help")
        self.events_conversion_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.conversion_layout.addWidget(self.events_conversion_label)

        self.stages_conversion_label = QLabel(self.content_widget)
        self.stages_conversion_label.setObjectName(u"stages_conversion_label")
        self.stages_conversion_label.setTextFormat(Qt.TextFormat.RichText)
        self.stages_conversion_label.setWordWrap(True)
        self.stages_conversion_label.setProperty(u"variant", u"help")
        self.stages_conversion_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.conversion_layout.addWidget(self.stages_conversion_label)

        self.conversion_layout.setStretch(0, 1)
        self.conversion_layout.setStretch(1, 1)

        self.about_conversion_layout.addLayout(self.conversion_layout)


        self.content_layout.addLayout(self.about_conversion_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(IntroStep)

        QMetaObject.connectSlotsByName(IntroStep)
    # setupUi

    def retranslateUi(self, IntroStep):
        IntroStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("IntroStep", u"Convert Annotations from XML", None))
        self.subtitle_label.setText(QCoreApplication.translate("IntroStep", u"Converts the events and the sleep stages of Compumedics Profusion XML annotation files to Snooz annotation files (.tsv), written next to them with the same name.", None))
        self.steps_title_label.setText(QCoreApplication.translate("IntroStep", u"What you will do", None))
        self.step_1_number_label.setText(QCoreApplication.translate("IntroStep", u"1", None))
        self.step_1_name_label.setText(QCoreApplication.translate("IntroStep", u"Input Files", None))
        self.step_1_label.setText(QCoreApplication.translate("IntroStep", u"Add the XML annotation files to convert.", None))
        self.files_title_label.setText(QCoreApplication.translate("IntroStep", u"Accepted files", None))
        self.file_1_name_label.setText(QCoreApplication.translate("IntroStep", u"XML", None))
        self.file_1_label.setText(QCoreApplication.translate("IntroStep", u"Compumedics Profusion XML annotation files.", None))
        self.file_2_name_label.setText(QCoreApplication.translate("IntroStep", u"PSG", None))
        self.file_2_label.setText(QCoreApplication.translate("IntroStep", u"Not needed: only the XML files are converted.", None))
        self.replace_warning_label.setText(QCoreApplication.translate("IntroStep", u"<b>Existing files are replaced</b><br/>A .tsv file with the same name, next to the XML file, is replaced by the converted file.", None))
        self.filename_info_label.setText(QCoreApplication.translate("IntroStep", u"<b>To open the converted files in Snooz</b><br/>The PSG file must have the same name as the annotation file: subject1.edf with subject1.tsv, not with subject1_annotation.tsv.", None))
        self.about_conversion_title_label.setText(QCoreApplication.translate("IntroStep", u"About the conversion", None))
        self.about_conversion_label.setText(QCoreApplication.translate("IntroStep", u"The events and the sleep stages of the XML file become events with the columns of the Snooz annotation file: group, name, start_sec, duration_sec and channels.", None))
        self.events_conversion_label.setText(QCoreApplication.translate("IntroStep", u"<b>Events</b> (ScoredEvent)<br/>\u2022 Name \u2192 group<br/>\u2022 EventName \u2192 name (Name when there is no EventName)<br/>\u2022 Start \u2192 start_sec<br/>\u2022 Duration \u2192 duration_sec<br/>\u2022 Input \u2192 channels", None))
        self.stages_conversion_label.setText(QCoreApplication.translate("IntroStep", u"<b>Sleep stages</b> (SleepStage table, one event per epoch)<br/>\u2022 group: stage<br/>\u2022 name: the value of the table: 0\u00a0(wake), 1\u00a0(N1), 2\u00a0(N2), 3\u00a0(N3), 4\u00a0(N4), 5\u00a0(REM), 6\u00a0(movement), 7\u00a0(technician\u00a0intervention) or 9\u00a0(unscored)<br/>\u2022 start_sec: start of the epoch (s)<br/>\u2022 duration_sec: EpochLength (from the XML file)", None))
    # retranslateUi

