# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Outputfiles.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Outputfiles(object):
    def setupUi(self, Outputfiles):
        if not Outputfiles.objectName():
            Outputfiles.setObjectName(u"Outputfiles")
        Outputfiles.resize(900, 700)
        self.verticalLayout = QVBoxLayout(Outputfiles)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(Outputfiles)
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

        self.report_card = QFrame(self.content_widget)
        self.report_card.setObjectName(u"report_card")
        self.report_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.report_card.setFrameShadow(QFrame.Shadow.Raised)
        self.report_card_layout = QVBoxLayout(self.report_card)
        self.report_card_layout.setSpacing(10)
        self.report_card_layout.setObjectName(u"report_card_layout")
        self.report_card_layout.setContentsMargins(10, 10, 10, 10)
        self.report_title_label = QLabel(self.report_card)
        self.report_title_label.setObjectName(u"report_title_label")
        font1 = QFont()
        font1.setBold(True)
        self.report_title_label.setFont(font1)

        self.report_card_layout.addWidget(self.report_title_label)

        self.filename_layout = QHBoxLayout()
        self.filename_layout.setSpacing(8)
        self.filename_layout.setObjectName(u"filename_layout")
        self.filename_label = QLabel(self.report_card)
        self.filename_label.setObjectName(u"filename_label")

        self.filename_layout.addWidget(self.filename_label)

        self.filename_lineEdit = QLineEdit(self.report_card)
        self.filename_lineEdit.setObjectName(u"filename_lineEdit")

        self.filename_layout.addWidget(self.filename_lineEdit)

        self.choose_pushButton = QPushButton(self.report_card)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.filename_layout.addWidget(self.choose_pushButton)


        self.report_card_layout.addLayout(self.filename_layout)

        self.report_label = QLabel(self.report_card)
        self.report_label.setObjectName(u"report_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.report_label.setFont(font2)
        self.report_label.setWordWrap(True)
        self.report_label.setProperty(u"variant", u"help")

        self.report_card_layout.addWidget(self.report_label)


        self.content_layout.addWidget(self.report_card)

        self.append_warning = QFrame(self.content_widget)
        self.append_warning.setObjectName(u"append_warning")
        self.append_warning.setFrameShape(QFrame.Shape.NoFrame)
        self.append_warning.setProperty(u"variant", u"warning")
        self.append_warning_layout = QHBoxLayout(self.append_warning)
        self.append_warning_layout.setObjectName(u"append_warning_layout")
        self.append_warning_layout.setContentsMargins(14, 10, 14, 10)
        self.append_warning_label = QLabel(self.append_warning)
        self.append_warning_label.setObjectName(u"append_warning_label")
        self.append_warning_label.setTextFormat(Qt.TextFormat.RichText)
        self.append_warning_label.setWordWrap(True)

        self.append_warning_layout.addWidget(self.append_warning_label)


        self.content_layout.addWidget(self.append_warning)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Outputfiles)

        QMetaObject.connectSlotsByName(Outputfiles)
    # setupUi

    def retranslateUi(self, Outputfiles):
        Outputfiles.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("Outputfiles", u"Output File", None))
        self.subtitle_label.setText(QCoreApplication.translate("Outputfiles", u"Choose the file of the report, written for all the selected recordings.", None))
        self.report_title_label.setText(QCoreApplication.translate("Outputfiles", u"Spectral power report", None))
        self.filename_label.setText(QCoreApplication.translate("Outputfiles", u"Filename", None))
        self.filename_lineEdit.setPlaceholderText(QCoreApplication.translate("Outputfiles", u"Choose a .tsv file", None))
        self.choose_pushButton.setText(QCoreApplication.translate("Outputfiles", u"Browse...", None))
        self.report_label.setText(QCoreApplication.translate("Outputfiles", u"A .tsv file (tab separated values). The results are grouped by channel and sleep stage, without hourly or cycle breakdowns.", None))
        self.append_warning_label.setText(QCoreApplication.translate("Outputfiles", u"<b>The data are appended</b><br/>New results are appended if the file already exists.", None))
    # retranslateUi

