# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SleepBoutsSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_SleepBoutsSettingsView(object):
    def setupUi(self, SleepBoutsSettingsView):
        if not SleepBoutsSettingsView.objectName():
            SleepBoutsSettingsView.setObjectName(u"SleepBoutsSettingsView")
        SleepBoutsSettingsView.resize(900, 700)
        self.verticalLayout = QVBoxLayout(SleepBoutsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(SleepBoutsSettingsView)
        self.content_widget.setObjectName(u"content_widget")
        self.content_widget.setMaximumSize(QSize(800, 16777215))
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setSpacing(16)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.output_card = QFrame(self.content_widget)
        self.output_card.setObjectName(u"output_card")
        self.output_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.output_card.setFrameShadow(QFrame.Shadow.Raised)
        self.output_card_layout = QVBoxLayout(self.output_card)
        self.output_card_layout.setSpacing(10)
        self.output_card_layout.setObjectName(u"output_card_layout")
        self.output_card_layout.setContentsMargins(10, 10, 10, 10)
        self.output_title_label = QLabel(self.output_card)
        self.output_title_label.setObjectName(u"output_title_label")
        font = QFont()
        font.setBold(True)
        self.output_title_label.setFont(font)

        self.output_card_layout.addWidget(self.output_title_label)

        self.output_file_layout = QHBoxLayout()
        self.output_file_layout.setSpacing(8)
        self.output_file_layout.setObjectName(u"output_file_layout")
        self.label = QLabel(self.output_card)
        self.label.setObjectName(u"label")

        self.output_file_layout.addWidget(self.label)

        self.output_file_lineedit = QLineEdit(self.output_card)
        self.output_file_lineedit.setObjectName(u"output_file_lineedit")

        self.output_file_layout.addWidget(self.output_file_lineedit)

        self.choose_file_pushbutton = QPushButton(self.output_card)
        self.choose_file_pushbutton.setObjectName(u"choose_file_pushbutton")

        self.output_file_layout.addWidget(self.choose_file_pushbutton)


        self.output_card_layout.addLayout(self.output_file_layout)

        self.output_help_label = QLabel(self.output_card)
        self.output_help_label.setObjectName(u"output_help_label")
        font1 = QFont()
        font1.setPointSize(10)
        self.output_help_label.setFont(font1)
        self.output_help_label.setWordWrap(True)
        self.output_help_label.setProperty(u"variant", u"help")

        self.output_card_layout.addWidget(self.output_help_label)

        self.output_line = QFrame(self.output_card)
        self.output_line.setObjectName(u"output_line")
        self.output_line.setFrameShape(QFrame.Shape.HLine)
        self.output_line.setFrameShadow(QFrame.Shadow.Plain)

        self.output_card_layout.addWidget(self.output_line)

        self.unit_label = QLabel(self.output_card)
        self.unit_label.setObjectName(u"unit_label")
        self.unit_label.setWordWrap(True)
        self.unit_label.setProperty(u"variant", u"help")

        self.output_card_layout.addWidget(self.unit_label)

        self.export_seconds_radiobutton = QRadioButton(self.output_card)
        self.export_seconds_radiobutton.setObjectName(u"export_seconds_radiobutton")

        self.output_card_layout.addWidget(self.export_seconds_radiobutton)

        self.export_epochs_radiobutton = QRadioButton(self.output_card)
        self.export_epochs_radiobutton.setObjectName(u"export_epochs_radiobutton")

        self.output_card_layout.addWidget(self.export_epochs_radiobutton)


        self.content_layout.addWidget(self.output_card)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SleepBoutsSettingsView)
        self.choose_file_pushbutton.clicked.connect(SleepBoutsSettingsView.on_choose_ouput_file)

        QMetaObject.connectSlotsByName(SleepBoutsSettingsView)
    # setupUi

    def retranslateUi(self, SleepBoutsSettingsView):
        SleepBoutsSettingsView.setWindowTitle("")
        self.output_title_label.setText(QCoreApplication.translate("SleepBoutsSettingsView", u"Output file", None))
        self.label.setText(QCoreApplication.translate("SleepBoutsSettingsView", u"Filename", None))
        self.output_file_lineedit.setPlaceholderText(QCoreApplication.translate("SleepBoutsSettingsView", u"Select a .tsv file", None))
        self.choose_file_pushbutton.setText(QCoreApplication.translate("SleepBoutsSettingsView", u"Choose file", None))
        self.output_help_label.setText(QCoreApplication.translate("SleepBoutsSettingsView", u"One row per recording. The results are appended at the end of the file if it exists. A file describing the variables (_info) is written next to it when it is created.", None))
        self.unit_label.setText(QCoreApplication.translate("SleepBoutsSettingsView", u"Durations of the sleep bouts", None))
        self.export_seconds_radiobutton.setText(QCoreApplication.translate("SleepBoutsSettingsView", u"Export values in seconds", None))
        self.export_epochs_radiobutton.setText(QCoreApplication.translate("SleepBoutsSettingsView", u"Export values in epochs", None))
    # retranslateUi

