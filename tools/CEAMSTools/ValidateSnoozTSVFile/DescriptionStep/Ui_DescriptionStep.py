# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DescriptionStep.ui'
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

class Ui_DescriptionStep(object):
    def setupUi(self, DescriptionStep):
        if not DescriptionStep.objectName():
            DescriptionStep.setObjectName(u"DescriptionStep")
        DescriptionStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(DescriptionStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(DescriptionStep)
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

        self.checks_section_layout = QVBoxLayout()
        self.checks_section_layout.setSpacing(8)
        self.checks_section_layout.setObjectName(u"checks_section_layout")
        self.checks_title_label = QLabel(self.content_widget)
        self.checks_title_label.setObjectName(u"checks_title_label")
        self.checks_title_label.setFont(font1)

        self.checks_section_layout.addWidget(self.checks_title_label)

        self.checks_card = QFrame(self.content_widget)
        self.checks_card.setObjectName(u"checks_card")
        self.checks_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.checks_card.setFrameShadow(QFrame.Shadow.Raised)
        self.checks_card_layout = QVBoxLayout(self.checks_card)
        self.checks_card_layout.setSpacing(10)
        self.checks_card_layout.setObjectName(u"checks_card_layout")
        self.checks_card_layout.setContentsMargins(10, 10, 10, 10)
        self.checks_grid = QGridLayout()
        self.checks_grid.setObjectName(u"checks_grid")
        self.checks_grid.setHorizontalSpacing(32)
        self.checks_grid.setVerticalSpacing(10)
        self.check_1_name_label = QLabel(self.checks_card)
        self.check_1_name_label.setObjectName(u"check_1_name_label")
        self.check_1_name_label.setFont(font3)
        self.check_1_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.checks_grid.addWidget(self.check_1_name_label, 0, 0, 1, 1)

        self.check_1_label = QLabel(self.checks_card)
        self.check_1_label.setObjectName(u"check_1_label")
        self.check_1_label.setWordWrap(True)
        self.check_1_label.setProperty(u"variant", u"help")

        self.checks_grid.addWidget(self.check_1_label, 0, 1, 1, 1)

        self.check_line_2 = QFrame(self.checks_card)
        self.check_line_2.setObjectName(u"check_line_2")
        self.check_line_2.setFrameShape(QFrame.Shape.HLine)
        self.check_line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.checks_grid.addWidget(self.check_line_2, 1, 0, 1, 2)

        self.check_2_name_label = QLabel(self.checks_card)
        self.check_2_name_label.setObjectName(u"check_2_name_label")
        self.check_2_name_label.setFont(font3)
        self.check_2_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.checks_grid.addWidget(self.check_2_name_label, 2, 0, 1, 1)

        self.check_2_label = QLabel(self.checks_card)
        self.check_2_label.setObjectName(u"check_2_label")
        self.check_2_label.setWordWrap(True)
        self.check_2_label.setProperty(u"variant", u"help")

        self.checks_grid.addWidget(self.check_2_label, 2, 1, 1, 1)

        self.check_line_3 = QFrame(self.checks_card)
        self.check_line_3.setObjectName(u"check_line_3")
        self.check_line_3.setFrameShape(QFrame.Shape.HLine)
        self.check_line_3.setFrameShadow(QFrame.Shadow.Plain)

        self.checks_grid.addWidget(self.check_line_3, 3, 0, 1, 2)

        self.check_3_name_label = QLabel(self.checks_card)
        self.check_3_name_label.setObjectName(u"check_3_name_label")
        self.check_3_name_label.setFont(font3)
        self.check_3_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.checks_grid.addWidget(self.check_3_name_label, 4, 0, 1, 1)

        self.check_3_label = QLabel(self.checks_card)
        self.check_3_label.setObjectName(u"check_3_label")
        self.check_3_label.setWordWrap(True)
        self.check_3_label.setProperty(u"variant", u"help")

        self.checks_grid.addWidget(self.check_3_label, 4, 1, 1, 1)

        self.check_line_4 = QFrame(self.checks_card)
        self.check_line_4.setObjectName(u"check_line_4")
        self.check_line_4.setFrameShape(QFrame.Shape.HLine)
        self.check_line_4.setFrameShadow(QFrame.Shadow.Plain)

        self.checks_grid.addWidget(self.check_line_4, 5, 0, 1, 2)

        self.check_4_name_label = QLabel(self.checks_card)
        self.check_4_name_label.setObjectName(u"check_4_name_label")
        self.check_4_name_label.setFont(font3)
        self.check_4_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.checks_grid.addWidget(self.check_4_name_label, 6, 0, 1, 1)

        self.check_4_label = QLabel(self.checks_card)
        self.check_4_label.setObjectName(u"check_4_label")
        self.check_4_label.setWordWrap(True)
        self.check_4_label.setProperty(u"variant", u"help")

        self.checks_grid.addWidget(self.check_4_label, 6, 1, 1, 1)

        self.check_order_line = QFrame(self.checks_card)
        self.check_order_line.setObjectName(u"check_order_line")
        self.check_order_line.setFrameShape(QFrame.Shape.HLine)
        self.check_order_line.setFrameShadow(QFrame.Shadow.Plain)

        self.checks_grid.addWidget(self.check_order_line, 7, 0, 1, 2)

        self.checks_order_label = QLabel(self.checks_card)
        self.checks_order_label.setObjectName(u"checks_order_label")
        self.checks_order_label.setFont(font2)
        self.checks_order_label.setWordWrap(True)
        self.checks_order_label.setProperty(u"variant", u"help")

        self.checks_grid.addWidget(self.checks_order_label, 8, 0, 1, 2)

        self.checks_grid.setColumnStretch(1, 1)

        self.checks_card_layout.addLayout(self.checks_grid)


        self.checks_section_layout.addWidget(self.checks_card)


        self.content_layout.addLayout(self.checks_section_layout)

        self.about_reports_layout = QVBoxLayout()
        self.about_reports_layout.setSpacing(6)
        self.about_reports_layout.setObjectName(u"about_reports_layout")
        self.about_reports_title_label = QLabel(self.content_widget)
        self.about_reports_title_label.setObjectName(u"about_reports_title_label")
        self.about_reports_title_label.setFont(font3)

        self.about_reports_layout.addWidget(self.about_reports_title_label)

        self.about_reports_label = QLabel(self.content_widget)
        self.about_reports_label.setObjectName(u"about_reports_label")
        self.about_reports_label.setWordWrap(True)
        self.about_reports_label.setProperty(u"variant", u"help")

        self.about_reports_layout.addWidget(self.about_reports_label)


        self.content_layout.addLayout(self.about_reports_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(DescriptionStep)

        QMetaObject.connectSlotsByName(DescriptionStep)
    # setupUi

    def retranslateUi(self, DescriptionStep):
        DescriptionStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("DescriptionStep", u"Validate Snooz Annotation File", None))
        self.subtitle_label.setText(QCoreApplication.translate("DescriptionStep", u"Checks that annotation files (.tsv) meet the format required by Snooz and are ready for use with the other Snooz tools.", None))
        self.steps_title_label.setText(QCoreApplication.translate("DescriptionStep", u"What you will do", None))
        self.step_1_number_label.setText(QCoreApplication.translate("DescriptionStep", u"1", None))
        self.step_1_name_label.setText(QCoreApplication.translate("DescriptionStep", u"Input/Output Files", None))
        self.step_1_label.setText(QCoreApplication.translate("DescriptionStep", u"Add the annotation files to validate, then choose the folder of the validation reports.", None))
        self.files_title_label.setText(QCoreApplication.translate("DescriptionStep", u"Accepted files", None))
        self.file_1_name_label.setText(QCoreApplication.translate("DescriptionStep", u"Annotations", None))
        self.file_1_label.setText(QCoreApplication.translate("DescriptionStep", u"Snooz annotation files (.tsv, tab-separated values), one file or a batch.", None))
        self.file_2_name_label.setText(QCoreApplication.translate("DescriptionStep", u"PSG", None))
        self.file_2_label.setText(QCoreApplication.translate("DescriptionStep", u"Not needed: only the annotation files are checked.", None))
        self.checks_title_label.setText(QCoreApplication.translate("DescriptionStep", u"What the tool verifies", None))
        self.check_1_name_label.setText(QCoreApplication.translate("DescriptionStep", u"Encoding", None))
        self.check_1_label.setText(QCoreApplication.translate("DescriptionStep", u"The file is UTF-8, so special characters (\u00e9, \u00fc) display correctly.", None))
        self.check_2_name_label.setText(QCoreApplication.translate("DescriptionStep", u"Columns", None))
        self.check_2_label.setText(QCoreApplication.translate("DescriptionStep", u"The first row has the column titles, in this order: group, name, start_sec, duration_sec, channels. A sixth column, time elapsed (HH:MM:SS), is accepted. Every row has these columns, separated by tabs.", None))
        self.check_3_name_label.setText(QCoreApplication.translate("DescriptionStep", u"Values", None))
        self.check_3_label.setText(QCoreApplication.translate("DescriptionStep", u"No value is empty. group and channels are text, name is text or a whole number, start_sec and duration_sec are numbers (seconds).", None))
        self.check_4_name_label.setText(QCoreApplication.translate("DescriptionStep", u"Sleep stages", None))
        self.check_4_label.setText(QCoreApplication.translate("DescriptionStep", u"The file has sleep stages (group stage), each named with a Snooz stage value from 0 to 9. Stage 4 is reported: rename it with \"Edit Snooz Annotations\", for example to 3\u00a0(N3).", None))
        self.checks_order_label.setText(QCoreApplication.translate("DescriptionStep", u"The checks run in this order. A file that is not UTF-8 gets no other check; a file with wrong columns gets no check of its values and sleep stages.", None))
        self.about_reports_title_label.setText(QCoreApplication.translate("DescriptionStep", u"About the reports", None))
        self.about_reports_label.setText(QCoreApplication.translate("DescriptionStep", u"One report per annotation file, saved in the chosen folder as &lt;name&gt;_validation_log.txt. It says \"Validation successful. No issues found.\" or lists the issues found, numbered.", None))
    # retranslateUi

