# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SleepCycleDoc.ui'
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

class Ui_SleepCycleDoc(object):
    def setupUi(self, SleepCycleDoc):
        if not SleepCycleDoc.objectName():
            SleepCycleDoc.setObjectName(u"SleepCycleDoc")
        SleepCycleDoc.resize(900, 700)
        self.verticalLayout = QVBoxLayout(SleepCycleDoc)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(SleepCycleDoc)
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

        self.picture_card = QFrame(self.content_widget)
        self.picture_card.setObjectName(u"picture_card")
        self.picture_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.picture_card.setFrameShadow(QFrame.Shadow.Raised)
        self.picture_card_layout = QVBoxLayout(self.picture_card)
        self.picture_card_layout.setSpacing(10)
        self.picture_card_layout.setObjectName(u"picture_card_layout")
        self.picture_card_layout.setContentsMargins(10, 10, 10, 10)
        self.hypnogram_pic = QLabel(self.picture_card)
        self.hypnogram_pic.setObjectName(u"hypnogram_pic")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hypnogram_pic.sizePolicy().hasHeightForWidth())
        self.hypnogram_pic.setSizePolicy(sizePolicy)

        self.picture_card_layout.addWidget(self.hypnogram_pic)

        self.picture_caption_label = QLabel(self.picture_card)
        self.picture_caption_label.setObjectName(u"picture_caption_label")
        font1 = QFont()
        font1.setPointSize(10)
        self.picture_caption_label.setFont(font1)
        self.picture_caption_label.setWordWrap(True)
        self.picture_caption_label.setProperty(u"variant", u"help")

        self.picture_card_layout.addWidget(self.picture_caption_label)


        self.content_layout.addWidget(self.picture_card)

        self.steps_section_layout = QVBoxLayout()
        self.steps_section_layout.setSpacing(8)
        self.steps_section_layout.setObjectName(u"steps_section_layout")
        self.steps_title_label = QLabel(self.content_widget)
        self.steps_title_label.setObjectName(u"steps_title_label")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.steps_title_label.setFont(font2)

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
        self.step_1_number_label.setFont(font1)
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
        self.step_2_number_label.setFont(font1)
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
        self.step_3_number_label.setFont(font1)
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

        self.steps_grid.setColumnStretch(3, 1)

        self.steps_card_layout.addLayout(self.steps_grid)


        self.steps_section_layout.addWidget(self.steps_card)


        self.content_layout.addLayout(self.steps_section_layout)

        self.files_section_layout = QVBoxLayout()
        self.files_section_layout.setSpacing(8)
        self.files_section_layout.setObjectName(u"files_section_layout")
        self.files_title_label = QLabel(self.content_widget)
        self.files_title_label.setObjectName(u"files_title_label")
        self.files_title_label.setFont(font2)

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

        self.about_cycles_layout = QVBoxLayout()
        self.about_cycles_layout.setSpacing(6)
        self.about_cycles_layout.setObjectName(u"about_cycles_layout")
        self.about_cycles_title_label = QLabel(self.content_widget)
        self.about_cycles_title_label.setObjectName(u"about_cycles_title_label")
        self.about_cycles_title_label.setFont(font3)

        self.about_cycles_layout.addWidget(self.about_cycles_title_label)

        self.about_cycles_label = QLabel(self.content_widget)
        self.about_cycles_label.setObjectName(u"about_cycles_label")
        self.about_cycles_label.setWordWrap(True)
        self.about_cycles_label.setProperty(u"variant", u"help")

        self.about_cycles_layout.addWidget(self.about_cycles_label)

        self.definitions_layout = QHBoxLayout()
        self.definitions_layout.setSpacing(16)
        self.definitions_layout.setObjectName(u"definitions_layout")
        self.nremp_label = QLabel(self.content_widget)
        self.nremp_label.setObjectName(u"nremp_label")
        self.nremp_label.setTextFormat(Qt.TextFormat.RichText)
        self.nremp_label.setWordWrap(True)
        self.nremp_label.setProperty(u"variant", u"help")
        self.nremp_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.definitions_layout.addWidget(self.nremp_label)

        self.remp_label = QLabel(self.content_widget)
        self.remp_label.setObjectName(u"remp_label")
        self.remp_label.setTextFormat(Qt.TextFormat.RichText)
        self.remp_label.setWordWrap(True)
        self.remp_label.setProperty(u"variant", u"help")
        self.remp_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.definitions_layout.addWidget(self.remp_label)

        self.definitions_layout.setStretch(0, 1)
        self.definitions_layout.setStretch(1, 1)

        self.about_cycles_layout.addLayout(self.definitions_layout)


        self.content_layout.addLayout(self.about_cycles_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SleepCycleDoc)

        QMetaObject.connectSlotsByName(SleepCycleDoc)
    # setupUi

    def retranslateUi(self, SleepCycleDoc):
        SleepCycleDoc.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("SleepCycleDoc", u"Report Sleep Cycle", None))
        self.subtitle_label.setText(QCoreApplication.translate("SleepCycleDoc", u"Delimits the sleep cycles (NREM and REM periods) in the sleep stages of your polysomnography (PSG) files and reports them for the cohort, with the hypnogram of each recording.", None))
        self.picture_caption_label.setText(QCoreApplication.translate("SleepCycleDoc", u"Hypnogram of learn-nsrr01 and its sleep cycles (minimum criteria): six complete cycles (C1\u2013C6), each a NREM period (blue) then a REM period (green), and an incomplete cycle at the end of the night (gray).", None))
        self.steps_title_label.setText(QCoreApplication.translate("SleepCycleDoc", u"What you will do", None))
        self.step_1_number_label.setText(QCoreApplication.translate("SleepCycleDoc", u"1", None))
        self.step_1_name_label.setText(QCoreApplication.translate("SleepCycleDoc", u"Input Files", None))
        self.step_1_label.setText(QCoreApplication.translate("SleepCycleDoc", u"Add the PSG files. The analysis is based on the sleep stages, but information from the PSG header file is also required.", None))
        self.step_2_number_label.setText(QCoreApplication.translate("SleepCycleDoc", u"2", None))
        self.step_2_name_label.setText(QCoreApplication.translate("SleepCycleDoc", u"Cycle Definition", None))
        self.step_2_label.setText(QCoreApplication.translate("SleepCycleDoc", u"Select or define the duration criteria of the NREM and REM periods.", None))
        self.step_3_number_label.setText(QCoreApplication.translate("SleepCycleDoc", u"3", None))
        self.step_3_name_label.setText(QCoreApplication.translate("SleepCycleDoc", u"Output Files", None))
        self.step_3_label.setText(QCoreApplication.translate("SleepCycleDoc", u"Choose the cohort report and the suffix of the hypnogram images. The sleep stages and periods of each recording, and a log of the warnings, are saved next to its PSG file.", None))
        self.files_title_label.setText(QCoreApplication.translate("SleepCycleDoc", u"Accepted files", None))
        self.file_1_name_label.setText(QCoreApplication.translate("SleepCycleDoc", u"EDF", None))
        self.file_1_label.setText(QCoreApplication.translate("SleepCycleDoc", u"The .edf and .tsv files have the same filename and are in the same directory.", None))
        self.file_2_name_label.setText(QCoreApplication.translate("SleepCycleDoc", u"Stellate", None))
        self.file_2_label.setText(QCoreApplication.translate("SleepCycleDoc", u"The .sig and .sts files have the same filename and are in the same directory.", None))
        self.file_3_name_label.setText(QCoreApplication.translate("SleepCycleDoc", u"NATUS", None))
        self.file_3_label.setText(QCoreApplication.translate("SleepCycleDoc", u"The entire NATUS subject folder is required <i>(for CEAMS users)</i>.", None))
        self.about_cycles_title_label.setText(QCoreApplication.translate("SleepCycleDoc", u"About the sleep cycles", None))
        self.about_cycles_label.setText(QCoreApplication.translate("SleepCycleDoc", u"Sleep cycles typically last between 90 minutes and 2 hours, during which the brain alternates between slow-wave sleep and REM sleep. A sleep cycle consists of successive NREM\u2013REM periods.", None))
        self.nremp_label.setText(QCoreApplication.translate("SleepCycleDoc", u"<b>NREM period (NREMP)</b><br/>\u2022 The first NREMP begins at the first NREM stage of the recording.<br/>\u2022 The central NREMPs begin at the next NREM stage following the end of a REMP.<br/>\u2022 A NREMP ends at the start of a REMP.", None))
        self.remp_label.setText(QCoreApplication.translate("SleepCycleDoc", u"<b>REM period (REMP)</b><br/>\u2022 A REMP begins at the first R stage.<br/>\u2022 It ends when there are 15 min without an R stage (except in the last cycle).<br/>\u2022 Its end is the last R stage of the REMP, or the beginning of the next NREMP.", None))
    # retranslateUi

