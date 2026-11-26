# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SleepStagesImporterSettingsView.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_SleepStagesImporterSettingsView(object):
    def setupUi(self, SleepStagesImporterSettingsView):
        if not SleepStagesImporterSettingsView.objectName():
            SleepStagesImporterSettingsView.setObjectName(u"SleepStagesImporterSettingsView")
        SleepStagesImporterSettingsView.resize(900, 700)
        self.verticalLayout = QVBoxLayout(SleepStagesImporterSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(SleepStagesImporterSettingsView)
        self.content_widget.setObjectName(u"content_widget")
        self.content_widget.setMaximumSize(QSize(800, 16777215))
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setSpacing(16)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.stages_files_card = QFrame(self.content_widget)
        self.stages_files_card.setObjectName(u"stages_files_card")
        self.stages_files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.stages_files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.stages_files_card_layout = QVBoxLayout(self.stages_files_card)
        self.stages_files_card_layout.setSpacing(10)
        self.stages_files_card_layout.setObjectName(u"stages_files_card_layout")
        self.stages_files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.stages_files_title_label = QLabel(self.stages_files_card)
        self.stages_files_title_label.setObjectName(u"stages_files_title_label")
        font = QFont()
        font.setBold(True)
        self.stages_files_title_label.setFont(font)

        self.stages_files_card_layout.addWidget(self.stages_files_title_label)

        self.tableWidget_files = QTableWidget(self.stages_files_card)
        self.tableWidget_files.setObjectName(u"tableWidget_files")
        self.tableWidget_files.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.stages_files_card_layout.addWidget(self.tableWidget_files)

        self.stages_files_buttons_layout = QHBoxLayout()
        self.stages_files_buttons_layout.setSpacing(8)
        self.stages_files_buttons_layout.setObjectName(u"stages_files_buttons_layout")
        self.files_help_label = QLabel(self.stages_files_card)
        self.files_help_label.setObjectName(u"files_help_label")
        font1 = QFont()
        font1.setPointSize(10)
        self.files_help_label.setFont(font1)
        self.files_help_label.setWordWrap(True)
        self.files_help_label.setProperty(u"variant", u"help")

        self.stages_files_buttons_layout.addWidget(self.files_help_label)

        self.pushButton_choose = QPushButton(self.stages_files_card)
        self.pushButton_choose.setObjectName(u"pushButton_choose")

        self.stages_files_buttons_layout.addWidget(self.pushButton_choose)

        self.pushButton_clear = QPushButton(self.stages_files_card)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.stages_files_buttons_layout.addWidget(self.pushButton_clear)

        self.stages_files_buttons_layout.setStretch(0, 1)

        self.stages_files_card_layout.addLayout(self.stages_files_buttons_layout)


        self.content_layout.addWidget(self.stages_files_card)

        self.settings_cards_layout = QHBoxLayout()
        self.settings_cards_layout.setSpacing(16)
        self.settings_cards_layout.setObjectName(u"settings_cards_layout")
        self.name_format_layout = QVBoxLayout()
        self.name_format_layout.setSpacing(16)
        self.name_format_layout.setObjectName(u"name_format_layout")
        self.name_card = QFrame(self.content_widget)
        self.name_card.setObjectName(u"name_card")
        self.name_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.name_card.setFrameShadow(QFrame.Shadow.Raised)
        self.name_card_layout = QVBoxLayout(self.name_card)
        self.name_card_layout.setSpacing(10)
        self.name_card_layout.setObjectName(u"name_card_layout")
        self.name_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_16 = QLabel(self.name_card)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.name_card_layout.addWidget(self.label_16)

        self.label_17 = QLabel(self.name_card)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setWordWrap(True)
        self.label_17.setProperty(u"variant", u"help")

        self.name_card_layout.addWidget(self.label_17)

        self.name_grid = QGridLayout()
        self.name_grid.setObjectName(u"name_grid")
        self.name_grid.setHorizontalSpacing(12)
        self.name_grid.setVerticalSpacing(10)
        self.label_18 = QLabel(self.name_card)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(60, 0))

        self.name_grid.addWidget(self.label_18, 0, 0, 1, 1)

        self.lineEdit_prefix = QLineEdit(self.name_card)
        self.lineEdit_prefix.setObjectName(u"lineEdit_prefix")

        self.name_grid.addWidget(self.lineEdit_prefix, 0, 1, 1, 1)

        self.label_19 = QLabel(self.name_card)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(60, 0))

        self.name_grid.addWidget(self.label_19, 1, 0, 1, 1)

        self.lineEdit_suffix = QLineEdit(self.name_card)
        self.lineEdit_suffix.setObjectName(u"lineEdit_suffix")

        self.name_grid.addWidget(self.lineEdit_suffix, 1, 1, 1, 1)

        self.name_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.name_grid.addItem(self.name_grid_spacer, 0, 3, 1, 1)


        self.name_card_layout.addLayout(self.name_grid)

        self.checkBox_case_sensitive = QCheckBox(self.name_card)
        self.checkBox_case_sensitive.setObjectName(u"checkBox_case_sensitive")
        self.checkBox_case_sensitive.setChecked(True)

        self.name_card_layout.addWidget(self.checkBox_case_sensitive)

        self.textEdit = QLabel(self.name_card)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font1)
        self.textEdit.setWordWrap(True)
        self.textEdit.setProperty(u"variant", u"help")

        self.name_card_layout.addWidget(self.textEdit)

        self.name_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.name_card_layout.addItem(self.name_stretch)


        self.name_format_layout.addWidget(self.name_card)

        self.format_card = QFrame(self.content_widget)
        self.format_card.setObjectName(u"format_card")
        self.format_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.format_card.setFrameShadow(QFrame.Shadow.Raised)
        self.format_card_layout = QVBoxLayout(self.format_card)
        self.format_card_layout.setSpacing(10)
        self.format_card_layout.setObjectName(u"format_card_layout")
        self.format_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.format_card)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.format_card_layout.addWidget(self.label)

        self.format_grid = QGridLayout()
        self.format_grid.setObjectName(u"format_grid")
        self.format_grid.setHorizontalSpacing(12)
        self.format_grid.setVerticalSpacing(10)
        self.label_3 = QLabel(self.format_card)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(220, 0))

        self.format_grid.addWidget(self.label_3, 0, 0, 1, 1)

        self.spinBox_n_rows = QSpinBox(self.format_card)
        self.spinBox_n_rows.setObjectName(u"spinBox_n_rows")

        self.format_grid.addWidget(self.spinBox_n_rows, 0, 1, 1, 1)

        self.label_2 = QLabel(self.format_card)
        self.label_2.setObjectName(u"label_2")

        self.format_grid.addWidget(self.label_2, 1, 0, 1, 1)

        self.comboBox_sep = QComboBox(self.format_card)
        self.comboBox_sep.addItem("")
        self.comboBox_sep.addItem("")
        self.comboBox_sep.addItem("")
        self.comboBox_sep.addItem("")
        self.comboBox_sep.addItem("")
        self.comboBox_sep.setObjectName(u"comboBox_sep")

        self.format_grid.addWidget(self.comboBox_sep, 1, 1, 1, 1)

        self.label_13 = QLabel(self.format_card)
        self.label_13.setObjectName(u"label_13")

        self.format_grid.addWidget(self.label_13, 2, 0, 1, 1)

        self.comboBox_encoding = QComboBox(self.format_card)
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.setObjectName(u"comboBox_encoding")

        self.format_grid.addWidget(self.comboBox_encoding, 2, 1, 1, 1)

        self.label_14 = QLabel(self.format_card)
        self.label_14.setObjectName(u"label_14")

        self.format_grid.addWidget(self.label_14, 3, 0, 1, 1)

        self.spinBox_colstage = QSpinBox(self.format_card)
        self.spinBox_colstage.setObjectName(u"spinBox_colstage")
        self.spinBox_colstage.setMinimum(1)

        self.format_grid.addWidget(self.spinBox_colstage, 3, 1, 1, 1)

        self.label_15 = QLabel(self.format_card)
        self.label_15.setObjectName(u"label_15")

        self.format_grid.addWidget(self.label_15, 4, 0, 1, 1)

        self.comboBox_stage_s = QComboBox(self.format_card)
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.addItem("")
        self.comboBox_stage_s.setObjectName(u"comboBox_stage_s")

        self.format_grid.addWidget(self.comboBox_stage_s, 4, 1, 1, 1)

        self.stage_duration_unit_label = QLabel(self.format_card)
        self.stage_duration_unit_label.setObjectName(u"stage_duration_unit_label")
        self.stage_duration_unit_label.setProperty(u"variant", u"help")

        self.format_grid.addWidget(self.stage_duration_unit_label, 4, 2, 1, 1)

        self.format_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.format_grid.addItem(self.format_grid_spacer, 0, 3, 1, 1)


        self.format_card_layout.addLayout(self.format_grid)

        self.label_20 = QLabel(self.format_card)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setWordWrap(True)
        self.label_20.setProperty(u"variant", u"help")

        self.format_card_layout.addWidget(self.label_20)

        self.format_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.format_card_layout.addItem(self.format_stretch)


        self.name_format_layout.addWidget(self.format_card)


        self.settings_cards_layout.addLayout(self.name_format_layout)

        self.renaming_card = QFrame(self.content_widget)
        self.renaming_card.setObjectName(u"renaming_card")
        self.renaming_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.renaming_card.setFrameShadow(QFrame.Shadow.Raised)
        self.renaming_card_layout = QVBoxLayout(self.renaming_card)
        self.renaming_card_layout.setSpacing(10)
        self.renaming_card_layout.setObjectName(u"renaming_card_layout")
        self.renaming_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_4 = QLabel(self.renaming_card)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.renaming_card_layout.addWidget(self.label_4)

        self.renaming_help_label = QLabel(self.renaming_card)
        self.renaming_help_label.setObjectName(u"renaming_help_label")
        self.renaming_help_label.setWordWrap(True)
        self.renaming_help_label.setProperty(u"variant", u"help")

        self.renaming_card_layout.addWidget(self.renaming_help_label)

        self.renaming_grid = QGridLayout()
        self.renaming_grid.setObjectName(u"renaming_grid")
        self.renaming_grid.setHorizontalSpacing(16)
        self.renaming_grid.setVerticalSpacing(8)
        self.stage_header_label = QLabel(self.renaming_card)
        self.stage_header_label.setObjectName(u"stage_header_label")
        self.stage_header_label.setFont(font)

        self.renaming_grid.addWidget(self.stage_header_label, 0, 0, 1, 1)

        self.label_43 = QLabel(self.renaming_card)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)

        self.renaming_grid.addWidget(self.label_43, 0, 1, 1, 1)

        self.label_46 = QLabel(self.renaming_card)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)

        self.renaming_grid.addWidget(self.label_46, 0, 2, 1, 1)

        self.renaming_line = QFrame(self.renaming_card)
        self.renaming_line.setObjectName(u"renaming_line")
        self.renaming_line.setFrameShape(QFrame.Shape.HLine)
        self.renaming_line.setFrameShadow(QFrame.Shadow.Plain)

        self.renaming_grid.addWidget(self.renaming_line, 1, 0, 1, 3)

        self.stage_0_label = QLabel(self.renaming_card)
        self.stage_0_label.setObjectName(u"stage_0_label")

        self.renaming_grid.addWidget(self.stage_0_label, 2, 0, 1, 1)

        self.lineEdit_ori_0 = QLineEdit(self.renaming_card)
        self.lineEdit_ori_0.setObjectName(u"lineEdit_ori_0")

        self.renaming_grid.addWidget(self.lineEdit_ori_0, 2, 1, 1, 1)

        self.snooz_label_0 = QLabel(self.renaming_card)
        self.snooz_label_0.setObjectName(u"snooz_label_0")
        self.snooz_label_0.setProperty(u"variant", u"help")

        self.renaming_grid.addWidget(self.snooz_label_0, 2, 2, 1, 1)

        self.stage_1_label = QLabel(self.renaming_card)
        self.stage_1_label.setObjectName(u"stage_1_label")

        self.renaming_grid.addWidget(self.stage_1_label, 3, 0, 1, 1)

        self.lineEdit_ori_1 = QLineEdit(self.renaming_card)
        self.lineEdit_ori_1.setObjectName(u"lineEdit_ori_1")

        self.renaming_grid.addWidget(self.lineEdit_ori_1, 3, 1, 1, 1)

        self.snooz_label_1 = QLabel(self.renaming_card)
        self.snooz_label_1.setObjectName(u"snooz_label_1")
        self.snooz_label_1.setProperty(u"variant", u"help")

        self.renaming_grid.addWidget(self.snooz_label_1, 3, 2, 1, 1)

        self.stage_2_label = QLabel(self.renaming_card)
        self.stage_2_label.setObjectName(u"stage_2_label")

        self.renaming_grid.addWidget(self.stage_2_label, 4, 0, 1, 1)

        self.lineEdit_ori_2 = QLineEdit(self.renaming_card)
        self.lineEdit_ori_2.setObjectName(u"lineEdit_ori_2")

        self.renaming_grid.addWidget(self.lineEdit_ori_2, 4, 1, 1, 1)

        self.snooz_label_2 = QLabel(self.renaming_card)
        self.snooz_label_2.setObjectName(u"snooz_label_2")
        self.snooz_label_2.setProperty(u"variant", u"help")

        self.renaming_grid.addWidget(self.snooz_label_2, 4, 2, 1, 1)

        self.stage_3_label = QLabel(self.renaming_card)
        self.stage_3_label.setObjectName(u"stage_3_label")

        self.renaming_grid.addWidget(self.stage_3_label, 5, 0, 1, 1)

        self.lineEdit_ori_3 = QLineEdit(self.renaming_card)
        self.lineEdit_ori_3.setObjectName(u"lineEdit_ori_3")

        self.renaming_grid.addWidget(self.lineEdit_ori_3, 5, 1, 1, 1)

        self.snooz_label_3 = QLabel(self.renaming_card)
        self.snooz_label_3.setObjectName(u"snooz_label_3")
        self.snooz_label_3.setProperty(u"variant", u"help")

        self.renaming_grid.addWidget(self.snooz_label_3, 5, 2, 1, 1)

        self.stage_5_label = QLabel(self.renaming_card)
        self.stage_5_label.setObjectName(u"stage_5_label")

        self.renaming_grid.addWidget(self.stage_5_label, 6, 0, 1, 1)

        self.lineEdit_ori_5 = QLineEdit(self.renaming_card)
        self.lineEdit_ori_5.setObjectName(u"lineEdit_ori_5")

        self.renaming_grid.addWidget(self.lineEdit_ori_5, 6, 1, 1, 1)

        self.snooz_label_5 = QLabel(self.renaming_card)
        self.snooz_label_5.setObjectName(u"snooz_label_5")
        self.snooz_label_5.setProperty(u"variant", u"help")

        self.renaming_grid.addWidget(self.snooz_label_5, 6, 2, 1, 1)

        self.label_40 = QLabel(self.renaming_card)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(20, 0))
        self.label_40.setMaximumSize(QSize(100, 16777215))

        self.renaming_grid.addWidget(self.label_40, 7, 0, 1, 1)

        self.lineEdit_ori_6 = QLineEdit(self.renaming_card)
        self.lineEdit_ori_6.setObjectName(u"lineEdit_ori_6")

        self.renaming_grid.addWidget(self.lineEdit_ori_6, 7, 1, 1, 1)

        self.snooz_label_6 = QLabel(self.renaming_card)
        self.snooz_label_6.setObjectName(u"snooz_label_6")
        self.snooz_label_6.setProperty(u"variant", u"help")

        self.renaming_grid.addWidget(self.snooz_label_6, 7, 2, 1, 1)

        self.label_41 = QLabel(self.renaming_card)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(90, 0))

        self.renaming_grid.addWidget(self.label_41, 8, 0, 1, 1)

        self.lineEdit_ori_7 = QLineEdit(self.renaming_card)
        self.lineEdit_ori_7.setObjectName(u"lineEdit_ori_7")

        self.renaming_grid.addWidget(self.lineEdit_ori_7, 8, 1, 1, 1)

        self.snooz_label_7 = QLabel(self.renaming_card)
        self.snooz_label_7.setObjectName(u"snooz_label_7")
        self.snooz_label_7.setProperty(u"variant", u"help")

        self.renaming_grid.addWidget(self.snooz_label_7, 8, 2, 1, 1)

        self.stage_9_label = QLabel(self.renaming_card)
        self.stage_9_label.setObjectName(u"stage_9_label")

        self.renaming_grid.addWidget(self.stage_9_label, 9, 0, 1, 1)

        self.lineEdit_ori_9 = QLineEdit(self.renaming_card)
        self.lineEdit_ori_9.setObjectName(u"lineEdit_ori_9")

        self.renaming_grid.addWidget(self.lineEdit_ori_9, 9, 1, 1, 1)

        self.snooz_label_9 = QLabel(self.renaming_card)
        self.snooz_label_9.setObjectName(u"snooz_label_9")
        self.snooz_label_9.setProperty(u"variant", u"help")

        self.renaming_grid.addWidget(self.snooz_label_9, 9, 2, 1, 1)

        self.renaming_grid.setColumnStretch(1, 1)

        self.renaming_card_layout.addLayout(self.renaming_grid)

        self.renaming_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.renaming_card_layout.addItem(self.renaming_stretch)


        self.settings_cards_layout.addWidget(self.renaming_card)

        self.settings_cards_layout.setStretch(0, 1)
        self.settings_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.settings_cards_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SleepStagesImporterSettingsView)
        self.pushButton_choose.clicked.connect(SleepStagesImporterSettingsView.choose_slot)
        self.pushButton_clear.clicked.connect(SleepStagesImporterSettingsView.clear_slot)

        QMetaObject.connectSlotsByName(SleepStagesImporterSettingsView)
    # setupUi

    def retranslateUi(self, SleepStagesImporterSettingsView):
        SleepStagesImporterSettingsView.setWindowTitle("")
#if QT_CONFIG(tooltip)
        self.stages_files_title_label.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"One sleep stage file per PSG file, as a text file (.csv, .tsv or .txt).", None))
#endif // QT_CONFIG(tooltip)
        self.stages_files_title_label.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Sleep stage files", None))
        self.files_help_label.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Snooz pairs each PSG file with its sleep stage file by name (see \"Sleep stage file names\").", None))
        self.pushButton_choose.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Choose files", None))
        self.pushButton_clear.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Clear all", None))
        self.label_16.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Sleep stage file names", None))
        self.label_17.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"The name of the sleep stage file of a PSG file is the prefix, then the PSG file name, then the suffix. Leave the prefix and the suffix empty when the sleep stage file has the name of the PSG file.", None))
        self.label_18.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Prefix", None))
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Optionally, define the prefix to insert before the PSG filename to identify the stages filename.", None))
#endif // QT_CONFIG(tooltip)
        self.label_19.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Suffix", None))
#if QT_CONFIG(tooltip)
        self.label_19.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Optionally, define the suffix to append to the PSG filename to identify the stages filename.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_case_sensitive.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Uncheck if the sleep stage filename has a different case than the EDF filename.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_case_sensitive.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Filenames are case sensitive", None))
        self.textEdit.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"For example, with the prefix hyp_ and the suffix _annotation, the sleep stage file of subject1.edf is hyp_subject1_annotation, with any extension (.txt, .csv...).", None))
        self.label.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Sleep stage file format", None))
        self.label_3.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Rows to skip", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Number of rows to skip before reading the sleep stages.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Item separator", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Delimiter character or pattern for the sleep stages file.\n"
"Set to None if unknown, and the engine will detect it.\n"
"Open the file in a text editor to see the separator.", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_sep.setItemText(0, QCoreApplication.translate("SleepStagesImporterSettingsView", u"None", None))
        self.comboBox_sep.setItemText(1, QCoreApplication.translate("SleepStagesImporterSettingsView", u"\\t", None))
        self.comboBox_sep.setItemText(2, QCoreApplication.translate("SleepStagesImporterSettingsView", u";", None))
        self.comboBox_sep.setItemText(3, QCoreApplication.translate("SleepStagesImporterSettingsView", u",", None))
        self.comboBox_sep.setItemText(4, QCoreApplication.translate("SleepStagesImporterSettingsView", u"\\r", None))

        self.label_13.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Encoding", None))
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Define the sleep stage file encoding. You can open in Notepad++ to find out.", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_encoding.setItemText(0, QCoreApplication.translate("SleepStagesImporterSettingsView", u"utf-8", None))
        self.comboBox_encoding.setItemText(1, QCoreApplication.translate("SleepStagesImporterSettingsView", u"latin-1", None))
        self.comboBox_encoding.setItemText(2, QCoreApplication.translate("SleepStagesImporterSettingsView", u"utf-16", None))
        self.comboBox_encoding.setItemText(3, QCoreApplication.translate("SleepStagesImporterSettingsView", u"utf-32", None))
        self.comboBox_encoding.setItemText(4, QCoreApplication.translate("SleepStagesImporterSettingsView", u"iso-8859", None))
        self.comboBox_encoding.setItemText(5, QCoreApplication.translate("SleepStagesImporterSettingsView", u"ascii", None))

        self.label_14.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Column of the stages", None))
#if QT_CONFIG(tooltip)
        self.label_14.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Define the column index to extract the stage labels. 1 means the first column.", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Stage duration", None))
#if QT_CONFIG(tooltip)
        self.label_15.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Define the duration (s) of the stage corresponding to one row in the sleep stages text file.", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_stage_s.setItemText(0, QCoreApplication.translate("SleepStagesImporterSettingsView", u"1", None))
        self.comboBox_stage_s.setItemText(1, QCoreApplication.translate("SleepStagesImporterSettingsView", u"2", None))
        self.comboBox_stage_s.setItemText(2, QCoreApplication.translate("SleepStagesImporterSettingsView", u"3", None))
        self.comboBox_stage_s.setItemText(3, QCoreApplication.translate("SleepStagesImporterSettingsView", u"5", None))
        self.comboBox_stage_s.setItemText(4, QCoreApplication.translate("SleepStagesImporterSettingsView", u"6", None))
        self.comboBox_stage_s.setItemText(5, QCoreApplication.translate("SleepStagesImporterSettingsView", u"10", None))
        self.comboBox_stage_s.setItemText(6, QCoreApplication.translate("SleepStagesImporterSettingsView", u"15", None))
        self.comboBox_stage_s.setItemText(7, QCoreApplication.translate("SleepStagesImporterSettingsView", u"30", None))

        self.comboBox_stage_s.setCurrentText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"1", None))
        self.stage_duration_unit_label.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"s", None))
        self.label_20.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Do not skip the row with the column titles, if any. Unknown separator or encoding? Open a sleep stage file in Notepad++. It shows the separator (comma, tab or semicolon) and the encoding (menu \"Encoding\").", None))
        self.label_4.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Stage renaming", None))
        self.renaming_help_label.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"The label of each stage in the sleep stage files, and the Snooz label it becomes. Every label used in the sleep stage files must be in the table.", None))
        self.stage_header_label.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Stage", None))
        self.label_43.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Label to import", None))
        self.label_46.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Snooz label", None))
        self.stage_0_label.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Wake", None))
        self.lineEdit_ori_0.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"W", None))
        self.snooz_label_0.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"0", None))
        self.stage_1_label.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"N1", None))
        self.lineEdit_ori_1.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"N1", None))
        self.snooz_label_1.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"1", None))
        self.stage_2_label.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"N2", None))
        self.lineEdit_ori_2.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"N2", None))
        self.snooz_label_2.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"2", None))
        self.stage_3_label.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"N3", None))
        self.lineEdit_ori_3.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"N3", None))
        self.snooz_label_3.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"3", None))
        self.stage_5_label.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"REM", None))
        self.lineEdit_ori_5.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"R", None))
        self.snooz_label_5.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"5", None))
        self.label_40.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Movement", None))
#if QT_CONFIG(tooltip)
        self.label_40.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Let the default label when not applicable.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit_ori_6.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEdit_ori_6.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Mov", None))
        self.snooz_label_6.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"6", None))
        self.label_41.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Technician\n"
"intervention", None))
#if QT_CONFIG(tooltip)
        self.label_41.setToolTip(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Let the default label when not applicable.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit_ori_7.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEdit_ori_7.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Tech", None))
        self.snooz_label_7.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"7", None))
        self.stage_9_label.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Unscored", None))
        self.lineEdit_ori_9.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"Unscored", None))
        self.snooz_label_9.setText(QCoreApplication.translate("SleepStagesImporterSettingsView", u"9", None))
    # retranslateUi

