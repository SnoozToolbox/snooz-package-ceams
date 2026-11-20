# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SleepCyclesDelimiterSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QRadioButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_SleepCyclesDelimiterSettingsView(object):
    def setupUi(self, SleepCyclesDelimiterSettingsView):
        if not SleepCyclesDelimiterSettingsView.objectName():
            SleepCyclesDelimiterSettingsView.setObjectName(u"SleepCyclesDelimiterSettingsView")
        SleepCyclesDelimiterSettingsView.resize(900, 700)
        self.verticalLayout = QVBoxLayout(SleepCyclesDelimiterSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(SleepCyclesDelimiterSettingsView)
        self.content_widget.setObjectName(u"content_widget")
        self.content_widget.setMaximumSize(QSize(800, 16777215))
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setSpacing(16)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.intro_label = QLabel(self.content_widget)
        self.intro_label.setObjectName(u"intro_label")
        self.intro_label.setWordWrap(True)
        self.intro_label.setProperty(u"variant", u"help")

        self.content_layout.addWidget(self.intro_label)

        self.settings_cards_layout = QHBoxLayout()
        self.settings_cards_layout.setSpacing(16)
        self.settings_cards_layout.setObjectName(u"settings_cards_layout")
        self.criteria_card = QFrame(self.content_widget)
        self.criteria_card.setObjectName(u"criteria_card")
        self.criteria_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.criteria_card.setFrameShadow(QFrame.Shadow.Raised)
        self.criteria_card_layout = QVBoxLayout(self.criteria_card)
        self.criteria_card_layout.setSpacing(10)
        self.criteria_card_layout.setObjectName(u"criteria_card_layout")
        self.criteria_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_3 = QLabel(self.criteria_card)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)

        self.criteria_card_layout.addWidget(self.label_3)

        self.radioButton_Min = QRadioButton(self.criteria_card)
        self.radioButton_Min.setObjectName(u"radioButton_Min")
        self.radioButton_Min.setChecked(False)

        self.criteria_card_layout.addWidget(self.radioButton_Min)

        self.radioButton_Floyd = QRadioButton(self.criteria_card)
        self.radioButton_Floyd.setObjectName(u"radioButton_Floyd")
        self.radioButton_Floyd.setChecked(False)

        self.criteria_card_layout.addWidget(self.radioButton_Floyd)

        self.radioButton_Aesch = QRadioButton(self.criteria_card)
        self.radioButton_Aesch.setObjectName(u"radioButton_Aesch")
        self.radioButton_Aesch.setChecked(True)

        self.criteria_card_layout.addWidget(self.radioButton_Aesch)

        self.radioButton_Mice = QRadioButton(self.criteria_card)
        self.radioButton_Mice.setObjectName(u"radioButton_Mice")
        self.radioButton_Mice.setEnabled(False)

        self.criteria_card_layout.addWidget(self.radioButton_Mice)

        self.criteria_help_label = QLabel(self.criteria_card)
        self.criteria_help_label.setObjectName(u"criteria_help_label")
        font1 = QFont()
        font1.setPointSize(10)
        self.criteria_help_label.setFont(font1)
        self.criteria_help_label.setWordWrap(True)
        self.criteria_help_label.setProperty(u"variant", u"help")

        self.criteria_card_layout.addWidget(self.criteria_help_label)

        self.criteria_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.criteria_card_layout.addItem(self.criteria_stretch)


        self.settings_cards_layout.addWidget(self.criteria_card)

        self.rem_card = QFrame(self.content_widget)
        self.rem_card.setObjectName(u"rem_card")
        self.rem_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.rem_card.setFrameShadow(QFrame.Shadow.Raised)
        self.rem_card_layout = QVBoxLayout(self.rem_card)
        self.rem_card_layout.setSpacing(10)
        self.rem_card_layout.setObjectName(u"rem_card_layout")
        self.rem_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_4 = QLabel(self.rem_card)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.rem_card_layout.addWidget(self.label_4)

        self.rem_grid = QGridLayout()
        self.rem_grid.setObjectName(u"rem_grid")
        self.rem_grid.setHorizontalSpacing(12)
        self.rem_grid.setVerticalSpacing(10)
        self.label_9 = QLabel(self.rem_card)
        self.label_9.setObjectName(u"label_9")

        self.rem_grid.addWidget(self.label_9, 0, 0, 1, 1)

        self.minL_REM_first_lineEdit = QLineEdit(self.rem_card)
        self.minL_REM_first_lineEdit.setObjectName(u"minL_REM_first_lineEdit")
        self.minL_REM_first_lineEdit.setEnabled(True)
        self.minL_REM_first_lineEdit.setMaximumSize(QSize(75, 16777215))
        self.minL_REM_first_lineEdit.setStyleSheet(u"")
        self.minL_REM_first_lineEdit.setReadOnly(False)

        self.rem_grid.addWidget(self.minL_REM_first_lineEdit, 0, 1, 1, 1)

        self.rem_first_unit_label = QLabel(self.rem_card)
        self.rem_first_unit_label.setObjectName(u"rem_first_unit_label")
        self.rem_first_unit_label.setProperty(u"variant", u"help")

        self.rem_grid.addWidget(self.rem_first_unit_label, 0, 2, 1, 1)

        self.label_8 = QLabel(self.rem_card)
        self.label_8.setObjectName(u"label_8")

        self.rem_grid.addWidget(self.label_8, 1, 0, 1, 1)

        self.minL_REM_mid_lineEdit = QLineEdit(self.rem_card)
        self.minL_REM_mid_lineEdit.setObjectName(u"minL_REM_mid_lineEdit")
        self.minL_REM_mid_lineEdit.setEnabled(True)
        self.minL_REM_mid_lineEdit.setMaximumSize(QSize(75, 16777215))
        self.minL_REM_mid_lineEdit.setStyleSheet(u"")
        self.minL_REM_mid_lineEdit.setReadOnly(False)

        self.rem_grid.addWidget(self.minL_REM_mid_lineEdit, 1, 1, 1, 1)

        self.rem_mid_unit_label = QLabel(self.rem_card)
        self.rem_mid_unit_label.setObjectName(u"rem_mid_unit_label")
        self.rem_mid_unit_label.setProperty(u"variant", u"help")

        self.rem_grid.addWidget(self.rem_mid_unit_label, 1, 2, 1, 1)

        self.label_7 = QLabel(self.rem_card)
        self.label_7.setObjectName(u"label_7")

        self.rem_grid.addWidget(self.label_7, 2, 0, 1, 1)

        self.minL_REM_last_lineEdit = QLineEdit(self.rem_card)
        self.minL_REM_last_lineEdit.setObjectName(u"minL_REM_last_lineEdit")
        self.minL_REM_last_lineEdit.setEnabled(True)
        self.minL_REM_last_lineEdit.setMaximumSize(QSize(75, 16777215))
        self.minL_REM_last_lineEdit.setStyleSheet(u"")
        self.minL_REM_last_lineEdit.setReadOnly(False)

        self.rem_grid.addWidget(self.minL_REM_last_lineEdit, 2, 1, 1, 1)

        self.rem_last_unit_label = QLabel(self.rem_card)
        self.rem_last_unit_label.setObjectName(u"rem_last_unit_label")
        self.rem_last_unit_label.setProperty(u"variant", u"help")

        self.rem_grid.addWidget(self.rem_last_unit_label, 2, 2, 1, 1)

        self.rem_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rem_grid.addItem(self.rem_grid_spacer, 0, 3, 1, 1)


        self.rem_card_layout.addLayout(self.rem_grid)

        self.rem_help_label = QLabel(self.rem_card)
        self.rem_help_label.setObjectName(u"rem_help_label")
        self.rem_help_label.setFont(font1)
        self.rem_help_label.setWordWrap(True)
        self.rem_help_label.setProperty(u"variant", u"help")

        self.rem_card_layout.addWidget(self.rem_help_label)

        self.rem_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.rem_card_layout.addItem(self.rem_stretch)


        self.settings_cards_layout.addWidget(self.rem_card)

        self.settings_cards_layout.setStretch(0, 1)
        self.settings_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.settings_cards_layout)

        self.cycle_cards_layout = QHBoxLayout()
        self.cycle_cards_layout.setSpacing(16)
        self.cycle_cards_layout.setObjectName(u"cycle_cards_layout")
        self.incomplete_card = QFrame(self.content_widget)
        self.incomplete_card.setObjectName(u"incomplete_card")
        self.incomplete_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.incomplete_card.setFrameShadow(QFrame.Shadow.Raised)
        self.incomplete_card_layout = QVBoxLayout(self.incomplete_card)
        self.incomplete_card_layout.setSpacing(10)
        self.incomplete_card_layout.setObjectName(u"incomplete_card_layout")
        self.incomplete_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_5 = QLabel(self.incomplete_card)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.incomplete_card_layout.addWidget(self.label_5)

        self.incomplete_label = QLabel(self.incomplete_card)
        self.incomplete_label.setObjectName(u"incomplete_label")
        self.incomplete_label.setWordWrap(True)
        self.incomplete_label.setProperty(u"variant", u"help")

        self.incomplete_card_layout.addWidget(self.incomplete_label)

        self.incomplete_layout = QVBoxLayout()
        self.incomplete_layout.setSpacing(6)
        self.incomplete_layout.setObjectName(u"incomplete_layout")
        self.checkBox_incl_SOREMP = QCheckBox(self.incomplete_card)
        self.checkBox_incl_SOREMP.setObjectName(u"checkBox_incl_SOREMP")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_incl_SOREMP.sizePolicy().hasHeightForWidth())
        self.checkBox_incl_SOREMP.setSizePolicy(sizePolicy)
        self.checkBox_incl_SOREMP.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_incl_SOREMP.setChecked(True)

        self.incomplete_layout.addWidget(self.checkBox_incl_SOREMP)

        self.checkBox_incl_last = QCheckBox(self.incomplete_card)
        self.checkBox_incl_last.setObjectName(u"checkBox_incl_last")
        sizePolicy.setHeightForWidth(self.checkBox_incl_last.sizePolicy().hasHeightForWidth())
        self.checkBox_incl_last.setSizePolicy(sizePolicy)
        self.checkBox_incl_last.setMinimumSize(QSize(0, 0))
        self.checkBox_incl_last.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_incl_last.setChecked(True)

        self.incomplete_layout.addWidget(self.checkBox_incl_last)

        self.checkBox_incl_all = QCheckBox(self.incomplete_card)
        self.checkBox_incl_all.setObjectName(u"checkBox_incl_all")
        sizePolicy.setHeightForWidth(self.checkBox_incl_all.sizePolicy().hasHeightForWidth())
        self.checkBox_incl_all.setSizePolicy(sizePolicy)
        self.checkBox_incl_all.setChecked(True)

        self.incomplete_layout.addWidget(self.checkBox_incl_all)


        self.incomplete_card_layout.addLayout(self.incomplete_layout)

        self.incomplete_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.incomplete_card_layout.addItem(self.incomplete_stretch)


        self.cycle_cards_layout.addWidget(self.incomplete_card)

        self.rem_end_card = QFrame(self.content_widget)
        self.rem_end_card.setObjectName(u"rem_end_card")
        self.rem_end_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.rem_end_card.setFrameShadow(QFrame.Shadow.Raised)
        self.rem_end_card_layout = QVBoxLayout(self.rem_end_card)
        self.rem_end_card_layout.setSpacing(10)
        self.rem_end_card_layout.setObjectName(u"rem_end_card_layout")
        self.rem_end_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_6 = QLabel(self.rem_end_card)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.rem_end_card_layout.addWidget(self.label_6)

        self.rem_end_layout = QVBoxLayout()
        self.rem_end_layout.setSpacing(2)
        self.rem_end_layout.setObjectName(u"rem_end_layout")
        self.mv_end_checkBox = QCheckBox(self.rem_end_card)
        self.mv_end_checkBox.setObjectName(u"mv_end_checkBox")
        sizePolicy.setHeightForWidth(self.mv_end_checkBox.sizePolicy().hasHeightForWidth())
        self.mv_end_checkBox.setSizePolicy(sizePolicy)
        self.mv_end_checkBox.setStyleSheet(u"")
        self.mv_end_checkBox.setCheckable(True)

        self.rem_end_layout.addWidget(self.mv_end_checkBox)

        self.plainTextEdit = QLabel(self.rem_end_card)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFont(font1)
        self.plainTextEdit.setWordWrap(True)
        self.plainTextEdit.setIndent(26)
        self.plainTextEdit.setProperty(u"variant", u"help")

        self.rem_end_layout.addWidget(self.plainTextEdit)


        self.rem_end_card_layout.addLayout(self.rem_end_layout)

        self.rem_end_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.rem_end_card_layout.addItem(self.rem_end_stretch)


        self.cycle_cards_layout.addWidget(self.rem_end_card)

        self.cycle_cards_layout.setStretch(0, 1)
        self.cycle_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.cycle_cards_layout)

        self.about_cycles_layout = QVBoxLayout()
        self.about_cycles_layout.setSpacing(6)
        self.about_cycles_layout.setObjectName(u"about_cycles_layout")
        self.about_cycles_title_label = QLabel(self.content_widget)
        self.about_cycles_title_label.setObjectName(u"about_cycles_title_label")
        self.about_cycles_title_label.setFont(font)

        self.about_cycles_layout.addWidget(self.about_cycles_title_label)

        self.definitions_layout = QHBoxLayout()
        self.definitions_layout.setSpacing(16)
        self.definitions_layout.setObjectName(u"definitions_layout")
        self.textEdit = QLabel(self.content_widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setTextFormat(Qt.TextFormat.RichText)
        self.textEdit.setWordWrap(True)
        self.textEdit.setProperty(u"variant", u"help")

        self.definitions_layout.addWidget(self.textEdit)

        self.textEdit_3 = QLabel(self.content_widget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setTextFormat(Qt.TextFormat.RichText)
        self.textEdit_3.setWordWrap(True)
        self.textEdit_3.setProperty(u"variant", u"help")

        self.definitions_layout.addWidget(self.textEdit_3)

        self.definitions_layout.setStretch(0, 1)
        self.definitions_layout.setStretch(1, 1)

        self.about_cycles_layout.addLayout(self.definitions_layout)

        self.image = QLabel(self.content_widget)
        self.image.setObjectName(u"image")
        self.image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.about_cycles_layout.addWidget(self.image)


        self.content_layout.addLayout(self.about_cycles_layout)

        self.about_criteria_layout = QVBoxLayout()
        self.about_criteria_layout.setSpacing(6)
        self.about_criteria_layout.setObjectName(u"about_criteria_layout")
        self.about_criteria_title_label = QLabel(self.content_widget)
        self.about_criteria_title_label.setObjectName(u"about_criteria_title_label")
        self.about_criteria_title_label.setFont(font)

        self.about_criteria_layout.addWidget(self.about_criteria_title_label)

        self.textBrowser = QTextBrowser(self.content_widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setProperty(u"variant", u"help")
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setStyleSheet(u"")
        self.textBrowser.setFrameShape(QFrame.Shape.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Shadow.Plain)
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(True)

        self.about_criteria_layout.addWidget(self.textBrowser)

        self.references_layout = QVBoxLayout()
        self.references_layout.setSpacing(8)
        self.references_layout.setObjectName(u"references_layout")
        self.references_layout.setContentsMargins(0, 6, 0, 0)
        self.references_line = QFrame(self.content_widget)
        self.references_line.setObjectName(u"references_line")
        self.references_line.setFrameShape(QFrame.Shape.HLine)
        self.references_line.setFrameShadow(QFrame.Shadow.Plain)

        self.references_layout.addWidget(self.references_line)

        self.references_label = QLabel(self.content_widget)
        self.references_label.setObjectName(u"references_label")
        self.references_label.setFont(font1)
        self.references_label.setTextFormat(Qt.TextFormat.RichText)
        self.references_label.setWordWrap(True)
        self.references_label.setOpenExternalLinks(True)
        self.references_label.setProperty(u"variant", u"help")

        self.references_layout.addWidget(self.references_label)


        self.about_criteria_layout.addLayout(self.references_layout)


        self.content_layout.addLayout(self.about_criteria_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SleepCyclesDelimiterSettingsView)
        self.radioButton_Aesch.clicked.connect(SleepCyclesDelimiterSettingsView.on_options_changed)
        self.radioButton_Min.clicked.connect(SleepCyclesDelimiterSettingsView.on_options_changed)
        self.radioButton_Floyd.clicked.connect(SleepCyclesDelimiterSettingsView.on_options_changed)
        self.radioButton_Mice.clicked.connect(SleepCyclesDelimiterSettingsView.on_options_changed)
        self.checkBox_incl_all.clicked.connect(SleepCyclesDelimiterSettingsView.include_incomplete_cycle_slot)
        self.checkBox_incl_SOREMP.clicked.connect(SleepCyclesDelimiterSettingsView.include_SOREMP_slot)
        self.checkBox_incl_last.clicked.connect(SleepCyclesDelimiterSettingsView.include_last_incomplete_slot)

        QMetaObject.connectSlotsByName(SleepCyclesDelimiterSettingsView)
    # setupUi

    def retranslateUi(self, SleepCyclesDelimiterSettingsView):
        SleepCyclesDelimiterSettingsView.setWindowTitle("")
        self.intro_label.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Define how the sleep cycles are delimited in the sleep stages.", None))
        self.label_3.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Period duration criteria", None))
        self.radioButton_Min.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Minimum Criteria", None))
        self.radioButton_Floyd.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Feinberg and Floyd 1979", None))
        self.radioButton_Aesch.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Aeschbach 1993", None))
        self.radioButton_Mice.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Mice Criteria", None))
        self.criteria_help_label.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Choosing criteria sets the settings below to their values. The criteria are described at the end of the page.", None))
        self.label_4.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Minimum duration of the REM periods", None))
        self.label_9.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"First cycle", None))
        self.minL_REM_first_lineEdit.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"0", None))
        self.rem_first_unit_label.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"min", None))
        self.label_8.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Middle cycles", None))
        self.minL_REM_mid_lineEdit.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"0", None))
        self.rem_mid_unit_label.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"min", None))
        self.label_7.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Last cycle", None))
        self.minL_REM_last_lineEdit.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"0", None))
        self.rem_last_unit_label.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"min", None))
        self.rem_help_label.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"A REM period shorter than its minimum duration is joined to the preceding one.", None))
        self.label_5.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Incomplete cycles", None))
        self.incomplete_label.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"A cycle is incomplete when its NREM or REM period does not meet the minimum duration.", None))
#if QT_CONFIG(tooltip)
        self.checkBox_incl_SOREMP.setToolTip(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Check to include incomplete cycle because of SOREMP (Sleep Onset in REMP).", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_incl_SOREMP.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Include SOREMP", None))
#if QT_CONFIG(tooltip)
        self.checkBox_incl_last.setToolTip(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Check to include the last cycle even if incomplete.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_incl_last.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Include incomplete ending", None))
#if QT_CONFIG(tooltip)
        self.checkBox_incl_all.setToolTip(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Check to include any incomplete cycles even middle sleep cycles.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_incl_all.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Include all", None))
        self.label_6.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"End of the REM period", None))
        self.mv_end_checkBox.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"Move the end of the REM period", None))
        self.plainTextEdit.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"The end of the REM period is moved to the start of the following NREM period, so there is no gap between two cycles.", None))
        self.about_cycles_title_label.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"About the sleep cycles", None))
        self.textEdit.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"<b>NREM period (NREMP)</b><br/>\u2022 The first NREMP begins at the first NREM stage of the recording.<br/>\u2022 The central NREMPs begin at the next NREM stage following the end of a REMP.<br/>\u2022 A NREMP ends at the start of a REMP.", None))
        self.textEdit_3.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"<b>REM period (REMP)</b><br/>\u2022 A REMP begins at the first R stage.<br/>\u2022 It ends when there are 15 min without an R stage (except in the last cycle).<br/>\u2022 Its end is the last R stage of the REMP, or the beginning of the next NREMP.", None))
        self.about_criteria_title_label.setText(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"About the selected criteria", None))
        self.textBrowser.setHtml(QCoreApplication.translate("SleepCyclesDelimiterSettingsView", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.references_label.setText("")
    # retranslateUi

