# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_InputFiles.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_InputFiles(object):
    def setupUi(self, InputFiles):
        if not InputFiles.objectName():
            InputFiles.setObjectName(u"InputFiles")
        InputFiles.resize(900, 700)
        self.verticalLayout = QVBoxLayout(InputFiles)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.header_layout = QVBoxLayout()
        self.header_layout.setSpacing(6)
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(InputFiles)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.header_layout.addWidget(self.title_label)

        self.subtitle_label = QLabel(InputFiles)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setProperty(u"variant", u"help")

        self.header_layout.addWidget(self.subtitle_label)


        self.verticalLayout.addLayout(self.header_layout)

        self.char_files_card = QFrame(InputFiles)
        self.char_files_card.setObjectName(u"char_files_card")
        self.char_files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.char_files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.char_files_card_layout = QVBoxLayout(self.char_files_card)
        self.char_files_card_layout.setSpacing(10)
        self.char_files_card_layout.setObjectName(u"char_files_card_layout")
        self.char_files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.char_files_title_label = QLabel(self.char_files_card)
        self.char_files_title_label.setObjectName(u"char_files_title_label")
        font1 = QFont()
        font1.setBold(True)
        self.char_files_title_label.setFont(font1)

        self.char_files_card_layout.addWidget(self.char_files_title_label)

        self.char_files_help_label = QLabel(self.char_files_card)
        self.char_files_help_label.setObjectName(u"char_files_help_label")
        self.char_files_help_label.setWordWrap(True)
        self.char_files_help_label.setProperty(u"variant", u"help")

        self.char_files_card_layout.addWidget(self.char_files_help_label)

        self.tableWidget_char_files = QTableWidget(self.char_files_card)
        self.tableWidget_char_files.setObjectName(u"tableWidget_char_files")
        self.tableWidget_char_files.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tableWidget_char_files.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_char_files.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.char_files_card_layout.addWidget(self.tableWidget_char_files)

        self.char_files_buttons_layout = QHBoxLayout()
        self.char_files_buttons_layout.setSpacing(8)
        self.char_files_buttons_layout.setObjectName(u"char_files_buttons_layout")
        self.char_files_folder_label = QLabel(self.char_files_card)
        self.char_files_folder_label.setObjectName(u"char_files_folder_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.char_files_folder_label.setFont(font2)
        self.char_files_folder_label.setWordWrap(True)
        self.char_files_folder_label.setProperty(u"variant", u"help")

        self.char_files_buttons_layout.addWidget(self.char_files_folder_label)

        self.pushButton_choose = QPushButton(self.char_files_card)
        self.pushButton_choose.setObjectName(u"pushButton_choose")

        self.char_files_buttons_layout.addWidget(self.pushButton_choose)

        self.pushButton_clear = QPushButton(self.char_files_card)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.char_files_buttons_layout.addWidget(self.pushButton_clear)

        self.char_files_buttons_layout.setStretch(0, 1)

        self.char_files_card_layout.addLayout(self.char_files_buttons_layout)


        self.verticalLayout.addWidget(self.char_files_card)

        self.cohort_card = QFrame(InputFiles)
        self.cohort_card.setObjectName(u"cohort_card")
        self.cohort_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.cohort_card.setFrameShadow(QFrame.Shadow.Raised)
        self.cohort_card_layout = QVBoxLayout(self.cohort_card)
        self.cohort_card_layout.setSpacing(10)
        self.cohort_card_layout.setObjectName(u"cohort_card_layout")
        self.cohort_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.cohort_card)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.cohort_card_layout.addWidget(self.label_2)

        self.label_4 = QLabel(self.cohort_card)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)
        self.label_4.setProperty(u"variant", u"help")

        self.cohort_card_layout.addWidget(self.label_4)

        self.cohort_file_layout = QHBoxLayout()
        self.cohort_file_layout.setSpacing(8)
        self.cohort_file_layout.setObjectName(u"cohort_file_layout")
        self.lineEdit_cohort_file = QLineEdit(self.cohort_card)
        self.lineEdit_cohort_file.setObjectName(u"lineEdit_cohort_file")

        self.cohort_file_layout.addWidget(self.lineEdit_cohort_file)

        self.pushButton_choose_cohort = QPushButton(self.cohort_card)
        self.pushButton_choose_cohort.setObjectName(u"pushButton_choose_cohort")

        self.cohort_file_layout.addWidget(self.pushButton_choose_cohort)


        self.cohort_card_layout.addLayout(self.cohort_file_layout)


        self.verticalLayout.addWidget(self.cohort_card)

        self.stage_files_card = QFrame(InputFiles)
        self.stage_files_card.setObjectName(u"stage_files_card")
        self.stage_files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.stage_files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.stage_files_card_layout = QVBoxLayout(self.stage_files_card)
        self.stage_files_card_layout.setSpacing(10)
        self.stage_files_card_layout.setObjectName(u"stage_files_card_layout")
        self.stage_files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.stage_files_title_label = QLabel(self.stage_files_card)
        self.stage_files_title_label.setObjectName(u"stage_files_title_label")
        self.stage_files_title_label.setFont(font1)

        self.stage_files_card_layout.addWidget(self.stage_files_title_label)

        self.stage_files_help_label = QLabel(self.stage_files_card)
        self.stage_files_help_label.setObjectName(u"stage_files_help_label")
        self.stage_files_help_label.setWordWrap(True)
        self.stage_files_help_label.setProperty(u"variant", u"help")

        self.stage_files_card_layout.addWidget(self.stage_files_help_label)

        self.tableWidget_stage_files = QTableWidget(self.stage_files_card)
        self.tableWidget_stage_files.setObjectName(u"tableWidget_stage_files")
        self.tableWidget_stage_files.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tableWidget_stage_files.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_stage_files.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.stage_files_card_layout.addWidget(self.tableWidget_stage_files)

        self.stage_files_buttons_layout = QHBoxLayout()
        self.stage_files_buttons_layout.setSpacing(8)
        self.stage_files_buttons_layout.setObjectName(u"stage_files_buttons_layout")
        self.stage_files_folder_label = QLabel(self.stage_files_card)
        self.stage_files_folder_label.setObjectName(u"stage_files_folder_label")
        self.stage_files_folder_label.setFont(font2)
        self.stage_files_folder_label.setWordWrap(True)
        self.stage_files_folder_label.setProperty(u"variant", u"help")

        self.stage_files_buttons_layout.addWidget(self.stage_files_folder_label)

        self.pushButton_choose_stage = QPushButton(self.stage_files_card)
        self.pushButton_choose_stage.setObjectName(u"pushButton_choose_stage")

        self.stage_files_buttons_layout.addWidget(self.pushButton_choose_stage)

        self.pushButton_clear_stage = QPushButton(self.stage_files_card)
        self.pushButton_clear_stage.setObjectName(u"pushButton_clear_stage")

        self.stage_files_buttons_layout.addWidget(self.pushButton_clear_stage)

        self.stage_files_buttons_layout.setStretch(0, 1)

        self.stage_files_card_layout.addLayout(self.stage_files_buttons_layout)


        self.verticalLayout.addWidget(self.stage_files_card)

        self.about_files_layout = QVBoxLayout()
        self.about_files_layout.setSpacing(6)
        self.about_files_layout.setObjectName(u"about_files_layout")
        self.about_files_title_label = QLabel(InputFiles)
        self.about_files_title_label.setObjectName(u"about_files_title_label")
        self.about_files_title_label.setFont(font1)

        self.about_files_layout.addWidget(self.about_files_title_label)

        self.about_files_label = QLabel(InputFiles)
        self.about_files_label.setObjectName(u"about_files_label")
        self.about_files_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_files_label.setWordWrap(True)
        self.about_files_label.setProperty(u"variant", u"help")

        self.about_files_layout.addWidget(self.about_files_label)


        self.verticalLayout.addLayout(self.about_files_layout)


        self.retranslateUi(InputFiles)
        self.pushButton_clear.clicked.connect(InputFiles.clear_slot)
        self.pushButton_choose.clicked.connect(InputFiles.choose_slot)
        self.pushButton_choose_cohort.clicked.connect(InputFiles.choose_cohort_slot)
        self.pushButton_choose_stage.clicked.connect(InputFiles.choose_stage_slot)
        self.pushButton_clear_stage.clicked.connect(InputFiles.clear_stage_slot)

        QMetaObject.connectSlotsByName(InputFiles)
    # setupUi

    def retranslateUi(self, InputFiles):
        InputFiles.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("InputFiles", u"Input Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("InputFiles", u"Add the files written by \"Detect Slow Waves\" for the recordings of your cohort.", None))
        self.char_files_title_label.setText(QCoreApplication.translate("InputFiles", u"Slow wave characteristics files", None))
        self.char_files_help_label.setText(QCoreApplication.translate("InputFiles", u"The distribution of their transition frequencies is used to classify the slow waves.", None))
        self.char_files_folder_label.setText(QCoreApplication.translate("InputFiles", u"In the folder \"slow_wave_characteristics\", next to the cohort report. Choosing files again replaces the list.", None))
        self.pushButton_choose.setText(QCoreApplication.translate("InputFiles", u"Choose files", None))
        self.pushButton_clear.setText(QCoreApplication.translate("InputFiles", u"Clear all", None))
        self.label_2.setText(QCoreApplication.translate("InputFiles", u"Slow wave cohort report", None))
        self.label_4.setText(QCoreApplication.translate("InputFiles", u"The valid duration of each recording and of each sleep cycle. Snooz uses them to compute the slow wave density of each category.", None))
        self.lineEdit_cohort_file.setPlaceholderText(QCoreApplication.translate("InputFiles", u"Choose the cohort report of the slow wave characteristics files", None))
        self.pushButton_choose_cohort.setText(QCoreApplication.translate("InputFiles", u"Choose file", None))
        self.stage_files_title_label.setText(QCoreApplication.translate("InputFiles", u"Sleep stages files", None))
        self.stage_files_help_label.setText(QCoreApplication.translate("InputFiles", u"The epochs in which the detector ran. Snooz uses their start and duration to compute the slow wave density per division of the night.", None))
        self.stage_files_folder_label.setText(QCoreApplication.translate("InputFiles", u"In the folder \"slow_wave_sleep_stages\", next to the cohort report. Choosing files again replaces the list.", None))
        self.pushButton_choose_stage.setText(QCoreApplication.translate("InputFiles", u"Choose files", None))
        self.pushButton_clear_stage.setText(QCoreApplication.translate("InputFiles", u"Clear all", None))
        self.about_files_title_label.setText(QCoreApplication.translate("InputFiles", u"About the files", None))
        self.about_files_label.setText(QCoreApplication.translate("InputFiles", u"\u2022 The list of recordings comes from the slow wave characteristics files.<br/>\u2022 Snooz finds the sleep stages file and the rows of the cohort report of each recording by its name. Keep the names written by \"Detect Slow Waves\".<br/>\u2022 For example, with slow wave events named sw_carrier, learn-nsrr01_sw_carrier.tsv goes with learn-nsrr01_sw_carrier_stages.tsv and with the rows of learn-nsrr01 in the cohort report.<br/>\u2022 The cohort report must hold the slow waves of a single event name.<br/>\u2022 Before the classification, Snooz checks the files and lists the missing ones.", None))
    # retranslateUi

