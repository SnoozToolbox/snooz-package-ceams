# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DominoConverterSettingsView.ui'
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

class Ui_DominoConverterSettingsView(object):
    def setupUi(self, DominoConverterSettingsView):
        if not DominoConverterSettingsView.objectName():
            DominoConverterSettingsView.setObjectName(u"DominoConverterSettingsView")
        DominoConverterSettingsView.resize(900, 700)
        self.verticalLayout = QVBoxLayout(DominoConverterSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(DominoConverterSettingsView)
        self.content_widget.setObjectName(u"content_widget")
        self.content_widget.setMaximumSize(QSize(800, 16777215))
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setSpacing(16)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.folders_card = QFrame(self.content_widget)
        self.folders_card.setObjectName(u"folders_card")
        self.folders_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.folders_card.setFrameShadow(QFrame.Shadow.Raised)
        self.folders_card_layout = QVBoxLayout(self.folders_card)
        self.folders_card_layout.setSpacing(10)
        self.folders_card_layout.setObjectName(u"folders_card_layout")
        self.folders_card_layout.setContentsMargins(10, 10, 10, 10)
        self.folders_label = QLabel(self.folders_card)
        self.folders_label.setObjectName(u"folders_label")
        font = QFont()
        font.setBold(True)
        self.folders_label.setFont(font)

        self.folders_card_layout.addWidget(self.folders_label)

        self.folders_help_label = QLabel(self.folders_card)
        self.folders_help_label.setObjectName(u"folders_help_label")
        self.folders_help_label.setWordWrap(True)
        self.folders_help_label.setProperty(u"variant", u"help")

        self.folders_card_layout.addWidget(self.folders_help_label)

        self.folders_lineedit = QLineEdit(self.folders_card)
        self.folders_lineedit.setObjectName(u"folders_lineedit")

        self.folders_card_layout.addWidget(self.folders_lineedit)

        self.folders_buttons_layout = QHBoxLayout()
        self.folders_buttons_layout.setSpacing(8)
        self.folders_buttons_layout.setObjectName(u"folders_buttons_layout")
        self.folders_output_label = QLabel(self.folders_card)
        self.folders_output_label.setObjectName(u"folders_output_label")
        font1 = QFont()
        font1.setPointSize(10)
        self.folders_output_label.setFont(font1)
        self.folders_output_label.setWordWrap(True)
        self.folders_output_label.setProperty(u"variant", u"help")

        self.folders_buttons_layout.addWidget(self.folders_output_label)

        self.pushButton_add_folder = QPushButton(self.folders_card)
        self.pushButton_add_folder.setObjectName(u"pushButton_add_folder")

        self.folders_buttons_layout.addWidget(self.pushButton_add_folder)

        self.folders_buttons_layout.setStretch(0, 1)

        self.folders_card_layout.addLayout(self.folders_buttons_layout)


        self.content_layout.addWidget(self.folders_card)

        self.log_card = QFrame(self.content_widget)
        self.log_card.setObjectName(u"log_card")
        self.log_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.log_card.setFrameShadow(QFrame.Shadow.Raised)
        self.log_card_layout = QVBoxLayout(self.log_card)
        self.log_card_layout.setSpacing(10)
        self.log_card_layout.setObjectName(u"log_card_layout")
        self.log_card_layout.setContentsMargins(10, 10, 10, 10)
        self.log_title_label = QLabel(self.log_card)
        self.log_title_label.setObjectName(u"log_title_label")
        self.log_title_label.setFont(font)

        self.log_card_layout.addWidget(self.log_title_label)

        self.label_4 = QLabel(self.log_card)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)
        self.label_4.setProperty(u"variant", u"help")

        self.log_card_layout.addWidget(self.label_4)

        self.log_layout = QHBoxLayout()
        self.log_layout.setSpacing(8)
        self.log_layout.setObjectName(u"log_layout")
        self.lineEdit_logfilename = QLineEdit(self.log_card)
        self.lineEdit_logfilename.setObjectName(u"lineEdit_logfilename")

        self.log_layout.addWidget(self.lineEdit_logfilename)

        self.pushButton_browse_log = QPushButton(self.log_card)
        self.pushButton_browse_log.setObjectName(u"pushButton_browse_log")

        self.log_layout.addWidget(self.pushButton_browse_log)


        self.log_card_layout.addLayout(self.log_layout)


        self.content_layout.addWidget(self.log_card)

        self.about_log_layout = QVBoxLayout()
        self.about_log_layout.setSpacing(6)
        self.about_log_layout.setObjectName(u"about_log_layout")
        self.about_log_title_label = QLabel(self.content_widget)
        self.about_log_title_label.setObjectName(u"about_log_title_label")
        self.about_log_title_label.setFont(font)

        self.about_log_layout.addWidget(self.about_log_title_label)

        self.about_log_label = QLabel(self.content_widget)
        self.about_log_label.setObjectName(u"about_log_label")
        self.about_log_label.setWordWrap(True)
        self.about_log_label.setProperty(u"variant", u"help")

        self.about_log_layout.addWidget(self.about_log_label)

        self.log_table = QGridLayout()
        self.log_table.setObjectName(u"log_table")
        self.log_table.setHorizontalSpacing(20)
        self.log_table.setVerticalSpacing(6)
        self.log_table_header_0 = QLabel(self.content_widget)
        self.log_table_header_0.setObjectName(u"log_table_header_0")
        self.log_table_header_0.setTextFormat(Qt.TextFormat.RichText)
        self.log_table_header_0.setWordWrap(True)
        self.log_table_header_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_header_0, 0, 0, 1, 1)

        self.log_table_header_1 = QLabel(self.content_widget)
        self.log_table_header_1.setObjectName(u"log_table_header_1")
        self.log_table_header_1.setTextFormat(Qt.TextFormat.RichText)
        self.log_table_header_1.setWordWrap(True)
        self.log_table_header_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_header_1, 0, 1, 1, 1)

        self.log_table_header_2 = QLabel(self.content_widget)
        self.log_table_header_2.setObjectName(u"log_table_header_2")
        self.log_table_header_2.setTextFormat(Qt.TextFormat.RichText)
        self.log_table_header_2.setWordWrap(True)
        self.log_table_header_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_header_2, 0, 2, 1, 1)

        self.log_table_line = QFrame(self.content_widget)
        self.log_table_line.setObjectName(u"log_table_line")
        self.log_table_line.setFrameShape(QFrame.Shape.HLine)
        self.log_table_line.setFrameShadow(QFrame.Shadow.Plain)

        self.log_table.addWidget(self.log_table_line, 1, 0, 1, 3)

        self.log_table_1_0 = QLabel(self.content_widget)
        self.log_table_1_0.setObjectName(u"log_table_1_0")
        self.log_table_1_0.setWordWrap(True)
        self.log_table_1_0.setProperty(u"variant", u"help")
        self.log_table_1_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_1_0, 2, 0, 1, 1)

        self.log_table_1_1 = QLabel(self.content_widget)
        self.log_table_1_1.setObjectName(u"log_table_1_1")
        self.log_table_1_1.setWordWrap(True)
        self.log_table_1_1.setProperty(u"variant", u"help")
        self.log_table_1_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_1_1, 2, 1, 1, 1)

        self.log_table_1_2 = QLabel(self.content_widget)
        self.log_table_1_2.setObjectName(u"log_table_1_2")
        self.log_table_1_2.setWordWrap(True)
        self.log_table_1_2.setProperty(u"variant", u"help")
        self.log_table_1_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_1_2, 2, 2, 1, 1)

        self.log_table_2_0 = QLabel(self.content_widget)
        self.log_table_2_0.setObjectName(u"log_table_2_0")
        self.log_table_2_0.setWordWrap(True)
        self.log_table_2_0.setProperty(u"variant", u"help")
        self.log_table_2_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_2_0, 3, 0, 1, 1)

        self.log_table_2_1 = QLabel(self.content_widget)
        self.log_table_2_1.setObjectName(u"log_table_2_1")
        self.log_table_2_1.setWordWrap(True)
        self.log_table_2_1.setProperty(u"variant", u"help")
        self.log_table_2_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_2_1, 3, 1, 1, 1)

        self.log_table_2_2 = QLabel(self.content_widget)
        self.log_table_2_2.setObjectName(u"log_table_2_2")
        self.log_table_2_2.setWordWrap(True)
        self.log_table_2_2.setProperty(u"variant", u"help")
        self.log_table_2_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_2_2, 3, 2, 1, 1)

        self.log_table_3_0 = QLabel(self.content_widget)
        self.log_table_3_0.setObjectName(u"log_table_3_0")
        self.log_table_3_0.setWordWrap(True)
        self.log_table_3_0.setProperty(u"variant", u"help")
        self.log_table_3_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_3_0, 4, 0, 1, 1)

        self.log_table_3_1 = QLabel(self.content_widget)
        self.log_table_3_1.setObjectName(u"log_table_3_1")
        self.log_table_3_1.setWordWrap(True)
        self.log_table_3_1.setProperty(u"variant", u"help")
        self.log_table_3_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_3_1, 4, 1, 1, 1)

        self.log_table_3_2 = QLabel(self.content_widget)
        self.log_table_3_2.setObjectName(u"log_table_3_2")
        self.log_table_3_2.setWordWrap(True)
        self.log_table_3_2.setProperty(u"variant", u"help")
        self.log_table_3_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_3_2, 4, 2, 1, 1)

        self.log_table_4_0 = QLabel(self.content_widget)
        self.log_table_4_0.setObjectName(u"log_table_4_0")
        self.log_table_4_0.setWordWrap(True)
        self.log_table_4_0.setProperty(u"variant", u"help")
        self.log_table_4_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_4_0, 5, 0, 1, 1)

        self.log_table_4_1 = QLabel(self.content_widget)
        self.log_table_4_1.setObjectName(u"log_table_4_1")
        self.log_table_4_1.setWordWrap(True)
        self.log_table_4_1.setProperty(u"variant", u"help")
        self.log_table_4_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_4_1, 5, 1, 1, 1)

        self.log_table_4_2 = QLabel(self.content_widget)
        self.log_table_4_2.setObjectName(u"log_table_4_2")
        self.log_table_4_2.setWordWrap(True)
        self.log_table_4_2.setProperty(u"variant", u"help")
        self.log_table_4_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_4_2, 5, 2, 1, 1)

        self.log_table_5_0 = QLabel(self.content_widget)
        self.log_table_5_0.setObjectName(u"log_table_5_0")
        self.log_table_5_0.setWordWrap(True)
        self.log_table_5_0.setProperty(u"variant", u"help")
        self.log_table_5_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_5_0, 6, 0, 1, 1)

        self.log_table_5_1 = QLabel(self.content_widget)
        self.log_table_5_1.setObjectName(u"log_table_5_1")
        self.log_table_5_1.setWordWrap(True)
        self.log_table_5_1.setProperty(u"variant", u"help")
        self.log_table_5_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_5_1, 6, 1, 1, 1)

        self.log_table_5_2 = QLabel(self.content_widget)
        self.log_table_5_2.setObjectName(u"log_table_5_2")
        self.log_table_5_2.setWordWrap(True)
        self.log_table_5_2.setProperty(u"variant", u"help")
        self.log_table_5_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.log_table.addWidget(self.log_table_5_2, 6, 2, 1, 1)

        self.log_table.setColumnStretch(1, 1)
        self.log_table.setColumnStretch(2, 1)

        self.about_log_layout.addLayout(self.log_table)


        self.content_layout.addLayout(self.about_log_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(DominoConverterSettingsView)
        self.pushButton_add_folder.clicked.connect(DominoConverterSettingsView.add_folder_slot)
        self.pushButton_browse_log.clicked.connect(DominoConverterSettingsView.browse_log_slot)

        QMetaObject.connectSlotsByName(DominoConverterSettingsView)
    # setupUi

    def retranslateUi(self, DominoConverterSettingsView):
        DominoConverterSettingsView.setWindowTitle("")
        self.folders_label.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Recording folders", None))
        self.folders_help_label.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Each folder holds the EDF file of a recording and all its ASCII files exported from DOMINO (ANALYSIS DATA - WITHOUT SLEEP PROFILE).", None))
        self.folders_lineedit.setPlaceholderText(QCoreApplication.translate("DominoConverterSettingsView", u"Choose the folders to convert.", None))
        self.folders_output_label.setText(QCoreApplication.translate("DominoConverterSettingsView", u"A Snooz annotation file (.tsv) is written in each folder, named after its EDF file.", None))
        self.pushButton_add_folder.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Choose folders", None))
        self.log_title_label.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Log file", None))
        self.label_4.setText(QCoreApplication.translate("DominoConverterSettingsView", u"For each DOMINO file, the log file says Success or gives the reason it was not converted.", None))
        self.lineEdit_logfilename.setPlaceholderText(QCoreApplication.translate("DominoConverterSettingsView", u"Choose the log file (.tsv).", None))
        self.pushButton_browse_log.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Browse", None))
        self.about_log_title_label.setText(QCoreApplication.translate("DominoConverterSettingsView", u"About the log file", None))
        self.about_log_label.setText(QCoreApplication.translate("DominoConverterSettingsView", u"A .tsv file with one row per DOMINO file, for example:", None))
        self.log_table_header_0.setText(QCoreApplication.translate("DominoConverterSettingsView", u"<b>recording</b>", None))
        self.log_table_header_1.setText(QCoreApplication.translate("DominoConverterSettingsView", u"<b>filename</b>", None))
        self.log_table_header_2.setText(QCoreApplication.translate("DominoConverterSettingsView", u"<b>warning</b>", None))
        self.log_table_1_0.setText(QCoreApplication.translate("DominoConverterSettingsView", u"patient_xxxx", None))
        self.log_table_1_1.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Flow Events", None))
        self.log_table_1_2.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Success", None))
        self.log_table_2_0.setText(QCoreApplication.translate("DominoConverterSettingsView", u"patient_xxxx", None))
        self.log_table_2_1.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Sleep profile", None))
        self.log_table_2_2.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Success", None))
        self.log_table_3_0.setText(QCoreApplication.translate("DominoConverterSettingsView", u"patient_xxxx", None))
        self.log_table_3_1.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Average Frequency Value", None))
        self.log_table_3_2.setText(QCoreApplication.translate("DominoConverterSettingsView", u"2 columns format but no Rate", None))
        self.log_table_4_0.setText(QCoreApplication.translate("DominoConverterSettingsView", u"patient_xxxx", None))
        self.log_table_4_1.setText(QCoreApplication.translate("DominoConverterSettingsView", u"CAP", None))
        self.log_table_4_2.setText(QCoreApplication.translate("DominoConverterSettingsView", u"empty", None))
        self.log_table_5_0.setText(QCoreApplication.translate("DominoConverterSettingsView", u"patient_xxxx", None))
        self.log_table_5_1.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Spindle K", None))
        self.log_table_5_2.setText(QCoreApplication.translate("DominoConverterSettingsView", u"Success", None))
    # retranslateUi

