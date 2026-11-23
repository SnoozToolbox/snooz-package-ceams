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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_InputFiles(object):
    def setupUi(self, InputFiles):
        if not InputFiles.objectName():
            InputFiles.setObjectName(u"InputFiles")
        InputFiles.resize(900, 700)
        self.verticalLayout = QVBoxLayout(InputFiles)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 12, 10, 12)
        self.header_row = QVBoxLayout()
        self.header_row.setObjectName(u"header_row")
        self.header_row.setContentsMargins(9, 0, 9, 0)
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


        self.header_row.addLayout(self.header_layout)


        self.verticalLayout.addLayout(self.header_row)


        self.retranslateUi(InputFiles)

        QMetaObject.connectSlotsByName(InputFiles)
    # setupUi

    def retranslateUi(self, InputFiles):
        InputFiles.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("InputFiles", u"Input Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("InputFiles", u"Add the detailed events cohort reports, then select the channels and the regions of interest of the cohort.", None))
    # retranslateUi

