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

        self.coverage_info = QFrame(self.content_widget)
        self.coverage_info.setObjectName(u"coverage_info")
        self.coverage_info.setFrameShape(QFrame.Shape.NoFrame)
        self.coverage_info.setProperty(u"variant", u"info")
        self.coverage_info_layout = QHBoxLayout(self.coverage_info)
        self.coverage_info_layout.setObjectName(u"coverage_info_layout")
        self.coverage_info_layout.setContentsMargins(14, 10, 14, 10)
        self.coverage_info_label = QLabel(self.coverage_info)
        self.coverage_info_label.setObjectName(u"coverage_info_label")
        self.coverage_info_label.setTextFormat(Qt.TextFormat.RichText)
        self.coverage_info_label.setWordWrap(True)

        self.coverage_info_layout.addWidget(self.coverage_info_label)


        self.content_layout.addWidget(self.coverage_info)

        self.about_import_layout = QVBoxLayout()
        self.about_import_layout.setSpacing(6)
        self.about_import_layout.setObjectName(u"about_import_layout")
        self.about_import_title_label = QLabel(self.content_widget)
        self.about_import_title_label.setObjectName(u"about_import_title_label")
        self.about_import_title_label.setFont(font3)

        self.about_import_layout.addWidget(self.about_import_title_label)

        self.about_import_label = QLabel(self.content_widget)
        self.about_import_label.setObjectName(u"about_import_label")
        self.about_import_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_import_label.setWordWrap(True)
        self.about_import_label.setProperty(u"variant", u"help")

        self.about_import_layout.addWidget(self.about_import_label)


        self.content_layout.addLayout(self.about_import_layout)


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
        self.title_label.setText(QCoreApplication.translate("IntroStep", u"Import Sleep Stage Text Vector", None))
        self.subtitle_label.setText(QCoreApplication.translate("IntroStep", u"Imports sleep stages written in text files, one stage per row, into the Snooz accessory file (.tsv) of each PSG file.", None))
        self.steps_title_label.setText(QCoreApplication.translate("IntroStep", u"What you will do", None))
        self.step_1_number_label.setText(QCoreApplication.translate("IntroStep", u"1", None))
        self.step_1_name_label.setText(QCoreApplication.translate("IntroStep", u"Input PSG Files", None))
        self.step_1_label.setText(QCoreApplication.translate("IntroStep", u"Add the PSG files that receive the sleep stages.", None))
        self.step_2_number_label.setText(QCoreApplication.translate("IntroStep", u"2", None))
        self.step_2_name_label.setText(QCoreApplication.translate("IntroStep", u"Input Stages Files", None))
        self.step_2_label.setText(QCoreApplication.translate("IntroStep", u"Add one sleep stage file per PSG file, then set how Snooz finds it by name, how to read it and its stage labels.", None))
        self.files_title_label.setText(QCoreApplication.translate("IntroStep", u"Accepted files", None))
        self.file_1_name_label.setText(QCoreApplication.translate("IntroStep", u"PSG files", None))
        self.file_1_label.setText(QCoreApplication.translate("IntroStep", u"EDF files (.edf), the only format supported. The Snooz accessory file (.tsv) of a PSG file is optional. Snooz creates it when it is absent.", None))
        self.file_2_name_label.setText(QCoreApplication.translate("IntroStep", u"Sleep stage files", None))
        self.file_2_label.setText(QCoreApplication.translate("IntroStep", u"Text files (.csv, .tsv or .txt), one per PSG file, with one sleep stage per row. When a sleep stage file has several columns, choose the column of the stages in \"Input Stages Files\".", None))
        self.coverage_info_label.setText(QCoreApplication.translate("IntroStep", u"<b>How Snooz places the stages</b><br/>A sleep stage file has no times. Snooz places its stages in order, from the start of the recording.<br/>\u2022 The first stage goes to the first epoch (0 to 30\u00a0s), the second stage to the second epoch (30 to 60\u00a0s), and so on.<br/>\u2022 Every epoch needs a stage. Write Unscored for an epoch without a stage. If a stage is missing, all the stages after it are shifted.<br/>\u2022 If the sleep stage file has fewer stages than the recording has epochs, the last epochs keep the stage they already have in the accessory file. They are Unscored if the accessory file had no stages.<br/>\u2022 If the sleep stage file has more stages than the recording has epochs, it is not imported.", None))
        self.about_import_title_label.setText(QCoreApplication.translate("IntroStep", u"About the import", None))
        self.about_import_label.setText(QCoreApplication.translate("IntroStep", u"<b>Finding the sleep stage file</b><br/>Snooz finds the sleep stage file of each PSG file by its name. This name is the prefix, then the PSG file name, then the suffix, with any extension.<br/><br/><b>Reading the stages</b><br/>Snooz reads the stages in the chosen column. It renames each stage with its Snooz label, from the \"Stage renaming\" table.<br/>Snooz epochs last 30 s. With a shorter stage duration, Snooz keeps one stage every 30 s. For example, with a stage duration of 10 s, it keeps every third row.<br/><br/><b>Errors</b><br/>The log shows an error for a PSG file in two cases.<br/>\u2022 The PSG file has no sleep stage file.<br/>\u2022 Its sleep stage file has a label that is not in the \"Stage renaming\" table.<br/><br/><b>Writing the stages</b><br/>Each stage becomes an event in the accessory file of the PSG file. The event has these columns.<br/>\u2022 group is stage.<br/>\u2022 name is the Snooz label, for example 2.<br/>\u2022 start_sec is the start of the epoch in seconds, for example 300.<br/>"
                        "\u2022 duration_sec is 30.<br/>\u2022 channels is empty.<br/>Snooz first removes the old stages of the accessory file that have the same name as an imported stage. The other events of the accessory file are kept.", None))
    # retranslateUi

