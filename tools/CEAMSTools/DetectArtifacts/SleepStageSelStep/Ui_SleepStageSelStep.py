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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_SleepStageSelStep(object):
    def setupUi(self, SleepStageSelStep):
        if not SleepStageSelStep.objectName():
            SleepStageSelStep.setObjectName(u"SleepStageSelStep")
        SleepStageSelStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(SleepStageSelStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(SleepStageSelStep)
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

        self.stages_card = QFrame(self.content_widget)
        self.stages_card.setObjectName(u"stages_card")
        self.stages_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.stages_card.setFrameShadow(QFrame.Shadow.Raised)
        self.stages_card_layout = QVBoxLayout(self.stages_card)
        self.stages_card_layout.setSpacing(10)
        self.stages_card_layout.setObjectName(u"stages_card_layout")
        self.stages_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_7 = QLabel(self.stages_card)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setBold(True)
        self.label_7.setFont(font1)

        self.stages_card_layout.addWidget(self.label_7)

        self.stages_help_label = QLabel(self.stages_card)
        self.stages_help_label.setObjectName(u"stages_help_label")
        self.stages_help_label.setWordWrap(True)
        self.stages_help_label.setProperty(u"variant", u"help")

        self.stages_card_layout.addWidget(self.stages_help_label)

        self.stages_layout = QHBoxLayout()
        self.stages_layout.setSpacing(22)
        self.stages_layout.setObjectName(u"stages_layout")
        self.checkBox_1 = QCheckBox(self.stages_card)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setChecked(True)

        self.stages_layout.addWidget(self.checkBox_1)

        self.checkBox_2 = QCheckBox(self.stages_card)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.stages_layout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.stages_card)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)

        self.stages_layout.addWidget(self.checkBox_3)

        self.checkBox_5 = QCheckBox(self.stages_card)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setChecked(False)

        self.stages_layout.addWidget(self.checkBox_5)

        self.checkBox_0 = QCheckBox(self.stages_card)
        self.checkBox_0.setObjectName(u"checkBox_0")

        self.stages_layout.addWidget(self.checkBox_0)

        self.stages_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.stages_layout.addItem(self.stages_spacer)


        self.stages_card_layout.addLayout(self.stages_layout)

        self.checkBox_9 = QCheckBox(self.stages_card)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.stages_card_layout.addWidget(self.checkBox_9)

        self.unscored_help_label = QLabel(self.stages_card)
        self.unscored_help_label.setObjectName(u"unscored_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.unscored_help_label.setFont(font2)
        self.unscored_help_label.setWordWrap(True)
        self.unscored_help_label.setIndent(26)
        self.unscored_help_label.setProperty(u"variant", u"help")

        self.stages_card_layout.addWidget(self.unscored_help_label)


        self.content_layout.addWidget(self.stages_card)

        self.stages_info = QFrame(self.content_widget)
        self.stages_info.setObjectName(u"stages_info")
        self.stages_info.setFrameShape(QFrame.Shape.NoFrame)
        self.stages_info.setProperty(u"variant", u"info")
        self.stages_info_layout = QHBoxLayout(self.stages_info)
        self.stages_info_layout.setObjectName(u"stages_info_layout")
        self.stages_info_layout.setContentsMargins(14, 10, 14, 10)
        self.stages_info_label = QLabel(self.stages_info)
        self.stages_info_label.setObjectName(u"stages_info_label")
        self.stages_info_label.setTextFormat(Qt.TextFormat.RichText)
        self.stages_info_label.setWordWrap(True)

        self.stages_info_layout.addWidget(self.stages_info_label)


        self.content_layout.addWidget(self.stages_info)

        self.sets_card = QFrame(self.content_widget)
        self.sets_card.setObjectName(u"sets_card")
        self.sets_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.sets_card.setFrameShadow(QFrame.Shadow.Raised)
        self.sets_card_layout = QVBoxLayout(self.sets_card)
        self.sets_card_layout.setSpacing(10)
        self.sets_card_layout.setObjectName(u"sets_card_layout")
        self.sets_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.sets_card)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.sets_card_layout.addWidget(self.label)

        self.sets_layout = QVBoxLayout()
        self.sets_layout.setSpacing(8)
        self.sets_layout.setObjectName(u"sets_layout")
        self.sets_layout_1_layout = QVBoxLayout()
        self.sets_layout_1_layout.setSpacing(2)
        self.sets_layout_1_layout.setObjectName(u"sets_layout_1_layout")
        self.radioButton_set1 = QRadioButton(self.sets_card)
        self.Theshold_sets = QButtonGroup(SleepStageSelStep)
        self.Theshold_sets.setObjectName(u"Theshold_sets")
        self.Theshold_sets.addButton(self.radioButton_set1)
        self.radioButton_set1.setObjectName(u"radioButton_set1")
        self.radioButton_set1.setChecked(True)

        self.sets_layout_1_layout.addWidget(self.radioButton_set1)

        self.set1_help_label = QLabel(self.sets_card)
        self.set1_help_label.setObjectName(u"set1_help_label")
        self.set1_help_label.setFont(font2)
        self.set1_help_label.setWordWrap(True)
        self.set1_help_label.setIndent(26)
        self.set1_help_label.setProperty(u"variant", u"help")

        self.sets_layout_1_layout.addWidget(self.set1_help_label)


        self.sets_layout.addLayout(self.sets_layout_1_layout)

        self.sets_layout_line_1 = QFrame(self.sets_card)
        self.sets_layout_line_1.setObjectName(u"sets_layout_line_1")
        self.sets_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.sets_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.sets_layout.addWidget(self.sets_layout_line_1)

        self.sets_layout_2_layout = QVBoxLayout()
        self.sets_layout_2_layout.setSpacing(2)
        self.sets_layout_2_layout.setObjectName(u"sets_layout_2_layout")
        self.radioButton_set2 = QRadioButton(self.sets_card)
        self.Theshold_sets.addButton(self.radioButton_set2)
        self.radioButton_set2.setObjectName(u"radioButton_set2")

        self.sets_layout_2_layout.addWidget(self.radioButton_set2)

        self.set2_help_label = QLabel(self.sets_card)
        self.set2_help_label.setObjectName(u"set2_help_label")
        self.set2_help_label.setFont(font2)
        self.set2_help_label.setWordWrap(True)
        self.set2_help_label.setIndent(26)
        self.set2_help_label.setProperty(u"variant", u"help")

        self.sets_layout_2_layout.addWidget(self.set2_help_label)


        self.sets_layout.addLayout(self.sets_layout_2_layout)


        self.sets_card_layout.addLayout(self.sets_layout)

        self.label_5 = QLabel(self.sets_card)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setWordWrap(True)
        self.label_5.setProperty(u"variant", u"help")

        self.sets_card_layout.addWidget(self.label_5)

        self.sets_table = QGridLayout()
        self.sets_table.setObjectName(u"sets_table")
        self.sets_table.setHorizontalSpacing(20)
        self.sets_table.setVerticalSpacing(6)
        self.sets_table_header_0 = QLabel(self.sets_card)
        self.sets_table_header_0.setObjectName(u"sets_table_header_0")
        self.sets_table_header_0.setTextFormat(Qt.TextFormat.RichText)
        self.sets_table_header_0.setWordWrap(True)
        self.sets_table_header_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_header_0, 0, 0, 1, 1)

        self.sets_table_header_1 = QLabel(self.sets_card)
        self.sets_table_header_1.setObjectName(u"sets_table_header_1")
        self.sets_table_header_1.setTextFormat(Qt.TextFormat.RichText)
        self.sets_table_header_1.setWordWrap(True)
        self.sets_table_header_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_header_1, 0, 1, 1, 1)

        self.sets_table_header_2 = QLabel(self.sets_card)
        self.sets_table_header_2.setObjectName(u"sets_table_header_2")
        self.sets_table_header_2.setTextFormat(Qt.TextFormat.RichText)
        self.sets_table_header_2.setWordWrap(True)
        self.sets_table_header_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_header_2, 0, 2, 1, 1)

        self.sets_table_line = QFrame(self.sets_card)
        self.sets_table_line.setObjectName(u"sets_table_line")
        self.sets_table_line.setFrameShape(QFrame.Shape.HLine)
        self.sets_table_line.setFrameShadow(QFrame.Shadow.Plain)

        self.sets_table.addWidget(self.sets_table_line, 1, 0, 1, 3)

        self.sets_table_1_0 = QLabel(self.sets_card)
        self.sets_table_1_0.setObjectName(u"sets_table_1_0")
        self.sets_table_1_0.setWordWrap(True)
        self.sets_table_1_0.setProperty(u"variant", u"help")
        self.sets_table_1_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_1_0, 2, 0, 1, 1)

        self.sets_table_1_1 = QLabel(self.sets_card)
        self.sets_table_1_1.setObjectName(u"sets_table_1_1")
        self.sets_table_1_1.setWordWrap(True)
        self.sets_table_1_1.setProperty(u"variant", u"help")
        self.sets_table_1_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_1_1, 2, 1, 1, 1)

        self.sets_table_1_2 = QLabel(self.sets_card)
        self.sets_table_1_2.setObjectName(u"sets_table_1_2")
        self.sets_table_1_2.setWordWrap(True)
        self.sets_table_1_2.setProperty(u"variant", u"help")
        self.sets_table_1_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_1_2, 2, 2, 1, 1)

        self.sets_table_2_0 = QLabel(self.sets_card)
        self.sets_table_2_0.setObjectName(u"sets_table_2_0")
        self.sets_table_2_0.setWordWrap(True)
        self.sets_table_2_0.setProperty(u"variant", u"help")
        self.sets_table_2_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_2_0, 3, 0, 1, 1)

        self.sets_table_2_1 = QLabel(self.sets_card)
        self.sets_table_2_1.setObjectName(u"sets_table_2_1")
        self.sets_table_2_1.setWordWrap(True)
        self.sets_table_2_1.setProperty(u"variant", u"help")
        self.sets_table_2_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_2_1, 3, 1, 1, 1)

        self.sets_table_2_2 = QLabel(self.sets_card)
        self.sets_table_2_2.setObjectName(u"sets_table_2_2")
        self.sets_table_2_2.setWordWrap(True)
        self.sets_table_2_2.setProperty(u"variant", u"help")
        self.sets_table_2_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_2_2, 3, 2, 1, 1)

        self.sets_table_3_0 = QLabel(self.sets_card)
        self.sets_table_3_0.setObjectName(u"sets_table_3_0")
        self.sets_table_3_0.setWordWrap(True)
        self.sets_table_3_0.setProperty(u"variant", u"help")
        self.sets_table_3_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_3_0, 4, 0, 1, 1)

        self.sets_table_3_1 = QLabel(self.sets_card)
        self.sets_table_3_1.setObjectName(u"sets_table_3_1")
        self.sets_table_3_1.setWordWrap(True)
        self.sets_table_3_1.setProperty(u"variant", u"help")
        self.sets_table_3_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_3_1, 4, 1, 1, 1)

        self.sets_table_3_2 = QLabel(self.sets_card)
        self.sets_table_3_2.setObjectName(u"sets_table_3_2")
        self.sets_table_3_2.setWordWrap(True)
        self.sets_table_3_2.setProperty(u"variant", u"help")
        self.sets_table_3_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_3_2, 4, 2, 1, 1)

        self.sets_table_4_0 = QLabel(self.sets_card)
        self.sets_table_4_0.setObjectName(u"sets_table_4_0")
        self.sets_table_4_0.setWordWrap(True)
        self.sets_table_4_0.setProperty(u"variant", u"help")
        self.sets_table_4_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_4_0, 5, 0, 1, 1)

        self.sets_table_4_1 = QLabel(self.sets_card)
        self.sets_table_4_1.setObjectName(u"sets_table_4_1")
        self.sets_table_4_1.setWordWrap(True)
        self.sets_table_4_1.setProperty(u"variant", u"help")
        self.sets_table_4_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_4_1, 5, 1, 1, 1)

        self.sets_table_4_2 = QLabel(self.sets_card)
        self.sets_table_4_2.setObjectName(u"sets_table_4_2")
        self.sets_table_4_2.setWordWrap(True)
        self.sets_table_4_2.setProperty(u"variant", u"help")
        self.sets_table_4_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_4_2, 5, 2, 1, 1)

        self.sets_table_5_0 = QLabel(self.sets_card)
        self.sets_table_5_0.setObjectName(u"sets_table_5_0")
        self.sets_table_5_0.setWordWrap(True)
        self.sets_table_5_0.setProperty(u"variant", u"help")
        self.sets_table_5_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_5_0, 6, 0, 1, 1)

        self.sets_table_5_1 = QLabel(self.sets_card)
        self.sets_table_5_1.setObjectName(u"sets_table_5_1")
        self.sets_table_5_1.setWordWrap(True)
        self.sets_table_5_1.setProperty(u"variant", u"help")
        self.sets_table_5_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_5_1, 6, 1, 1, 1)

        self.sets_table_5_2 = QLabel(self.sets_card)
        self.sets_table_5_2.setObjectName(u"sets_table_5_2")
        self.sets_table_5_2.setWordWrap(True)
        self.sets_table_5_2.setProperty(u"variant", u"help")
        self.sets_table_5_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_5_2, 6, 2, 1, 1)

        self.sets_table_6_0 = QLabel(self.sets_card)
        self.sets_table_6_0.setObjectName(u"sets_table_6_0")
        self.sets_table_6_0.setWordWrap(True)
        self.sets_table_6_0.setProperty(u"variant", u"help")
        self.sets_table_6_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_6_0, 7, 0, 1, 1)

        self.sets_table_6_1 = QLabel(self.sets_card)
        self.sets_table_6_1.setObjectName(u"sets_table_6_1")
        self.sets_table_6_1.setWordWrap(True)
        self.sets_table_6_1.setProperty(u"variant", u"help")
        self.sets_table_6_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_6_1, 7, 1, 1, 1)

        self.sets_table_6_2 = QLabel(self.sets_card)
        self.sets_table_6_2.setObjectName(u"sets_table_6_2")
        self.sets_table_6_2.setWordWrap(True)
        self.sets_table_6_2.setProperty(u"variant", u"help")
        self.sets_table_6_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.sets_table.addWidget(self.sets_table_6_2, 7, 2, 1, 1)

        self.sets_table.setColumnStretch(1, 1)
        self.sets_table.setColumnStretch(2, 1)

        self.sets_card_layout.addLayout(self.sets_table)

        self.sets_note_label = QLabel(self.sets_card)
        self.sets_note_label.setObjectName(u"sets_note_label")
        self.sets_note_label.setFont(font2)
        self.sets_note_label.setWordWrap(True)
        self.sets_note_label.setProperty(u"variant", u"help")

        self.sets_card_layout.addWidget(self.sets_note_label)


        self.content_layout.addWidget(self.sets_card)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SleepStageSelStep)
        self.radioButton_set1.clicked.connect(SleepStageSelStep.radio_threshold_slot)
        self.radioButton_set2.clicked.connect(SleepStageSelStep.radio_threshold_slot)
        self.checkBox_0.clicked.connect(SleepStageSelStep.check_stages_slot)
        self.checkBox_1.clicked.connect(SleepStageSelStep.check_stages_slot)
        self.checkBox_2.clicked.connect(SleepStageSelStep.check_stages_slot)
        self.checkBox_3.clicked.connect(SleepStageSelStep.check_stages_slot)
        self.checkBox_5.clicked.connect(SleepStageSelStep.check_stages_slot)
        self.checkBox_9.clicked.connect(SleepStageSelStep.check_stages_slot)

        QMetaObject.connectSlotsByName(SleepStageSelStep)
    # setupUi

    def retranslateUi(self, SleepStageSelStep):
        SleepStageSelStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("SleepStageSelStep", u"Stage Selection", None))
        self.subtitle_label.setText(QCoreApplication.translate("SleepStageSelStep", u"Select the sleep stages in which artifacts are detected, then a set of default thresholds.", None))
        self.label_7.setText(QCoreApplication.translate("SleepStageSelStep", u"Sleep stages", None))
        self.stages_help_label.setText(QCoreApplication.translate("SleepStageSelStep", u"Select the stages in which artifacts are detected.", None))
        self.checkBox_1.setText(QCoreApplication.translate("SleepStageSelStep", u"N1", None))
        self.checkBox_2.setText(QCoreApplication.translate("SleepStageSelStep", u"N2", None))
        self.checkBox_3.setText(QCoreApplication.translate("SleepStageSelStep", u"N3", None))
        self.checkBox_5.setText(QCoreApplication.translate("SleepStageSelStep", u"R", None))
        self.checkBox_0.setText(QCoreApplication.translate("SleepStageSelStep", u"Awake", None))
        self.checkBox_9.setText(QCoreApplication.translate("SleepStageSelStep", u"Unscored", None))
        self.unscored_help_label.setText(QCoreApplication.translate("SleepStageSelStep", u"Select \"Unscored\" when the recordings have no sleep stages. The detection then runs on any EEG recording.", None))
        self.stages_info_label.setText(QCoreApplication.translate("SleepStageSelStep", u"<b>Run the detection once per kind of stage</b><br/>The detection works better when the selected stages are alike, because several thresholds depend on their power distribution. Run the tool separately for NREM, REM and Awake, with a different group or name each time.", None))
        self.label.setText(QCoreApplication.translate("SleepStageSelStep", u"Default thresholds", None))
        self.radioButton_set1.setText(QCoreApplication.translate("SleepStageSelStep", u"Set 1, for NREM sleep", None))
        self.set1_help_label.setText(QCoreApplication.translate("SleepStageSelStep", u"Also for the Awake or Unscored stages.", None))
        self.radioButton_set2.setText(QCoreApplication.translate("SleepStageSelStep", u"Set 2, for REM sleep", None))
        self.set2_help_label.setText(QCoreApplication.translate("SleepStageSelStep", u"More sensitive.", None))
        self.label_5.setText(QCoreApplication.translate("SleepStageSelStep", u"Choosing a set gives its values to all the detectors. You can then edit them in the page of each detector.", None))
        self.sets_table_header_0.setText(QCoreApplication.translate("SleepStageSelStep", u"<b>Detector</b>", None))
        self.sets_table_header_1.setText(QCoreApplication.translate("SleepStageSelStep", u"<b>Set 1</b>", None))
        self.sets_table_header_2.setText(QCoreApplication.translate("SleepStageSelStep", u"<b>Set 2</b>", None))
        self.sets_table_1_0.setText(QCoreApplication.translate("SleepStageSelStep", u"Flatline", None))
        self.sets_table_1_1.setText(QCoreApplication.translate("SleepStageSelStep", u"0.25 \u00b5V\u00b2", None))
        self.sets_table_1_2.setText(QCoreApplication.translate("SleepStageSelStep", u"0.25 \u00b5V\u00b2", None))
        self.sets_table_2_0.setText(QCoreApplication.translate("SleepStageSelStep", u"High frequency burst", None))
        self.sets_table_2_1.setText(QCoreApplication.translate("SleepStageSelStep", u"A 4 \u00d7 SD, B 8 \u00d7 median, C 0.1", None))
        self.sets_table_2_2.setText(QCoreApplication.translate("SleepStageSelStep", u"A 3 \u00d7 SD, B 6 \u00d7 median, C 0.1", None))
        self.sets_table_3_0.setText(QCoreApplication.translate("SleepStageSelStep", u"Persistent noise", None))
        self.sets_table_3_1.setText(QCoreApplication.translate("SleepStageSelStep", u"A 4 \u00d7 SD, B 0.1", None))
        self.sets_table_3_2.setText(QCoreApplication.translate("SleepStageSelStep", u"A 2 \u00d7 SD, B 0.1", None))
        self.sets_table_4_0.setText(QCoreApplication.translate("SleepStageSelStep", u"Power line contamination", None))
        self.sets_table_4_1.setText(QCoreApplication.translate("SleepStageSelStep", u"A 0 \u00d7 SD, B 0.1", None))
        self.sets_table_4_2.setText(QCoreApplication.translate("SleepStageSelStep", u"A 0 \u00d7 SD, B 0.1", None))
        self.sets_table_5_0.setText(QCoreApplication.translate("SleepStageSelStep", u"Baseline variation", None))
        self.sets_table_5_1.setText(QCoreApplication.translate("SleepStageSelStep", u"4 \u00d7 SD", None))
        self.sets_table_5_2.setText(QCoreApplication.translate("SleepStageSelStep", u"2.5 \u00d7 SD", None))
        self.sets_table_6_0.setText(QCoreApplication.translate("SleepStageSelStep", u"Muscle artifact", None))
        self.sets_table_6_1.setText(QCoreApplication.translate("SleepStageSelStep", u"A 8, B 5, C 5 \u00d7 median", None))
        self.sets_table_6_2.setText(QCoreApplication.translate("SleepStageSelStep", u"A 4, B 3, C 3 \u00d7 median", None))
        self.sets_note_label.setText(QCoreApplication.translate("SleepStageSelStep", u"SD is the standard deviation of the main Gaussian component of the power distribution, median the median power of the baseline.", None))
    # retranslateUi

