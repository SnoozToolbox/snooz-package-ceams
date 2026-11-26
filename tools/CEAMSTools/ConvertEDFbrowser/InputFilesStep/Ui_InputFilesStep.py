# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_InputFilesStep.ui'
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

class Ui_InputFilesStep(object):
    def setupUi(self, InputFilesStep):
        if not InputFilesStep.objectName():
            InputFilesStep.setObjectName(u"InputFilesStep")
        InputFilesStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(InputFilesStep)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_box_layout = QVBoxLayout()
        self.header_box_layout.setObjectName(u"header_box_layout")
        self.header_box_layout.setContentsMargins(19, 12, 19, 0)
        self.header_layout = QVBoxLayout()
        self.header_layout.setSpacing(6)
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(InputFilesStep)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.header_layout.addWidget(self.title_label)

        self.subtitle_label = QLabel(InputFilesStep)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setProperty(u"variant", u"help")

        self.header_layout.addWidget(self.subtitle_label)


        self.header_box_layout.addLayout(self.header_layout)


        self.verticalLayout.addLayout(self.header_box_layout)


        self.retranslateUi(InputFilesStep)

        QMetaObject.connectSlotsByName(InputFilesStep)
    # setupUi

    def retranslateUi(self, InputFilesStep):
        InputFilesStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("InputFilesStep", u"Input Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("InputFilesStep", u"Add the EDFbrowser annotation files to convert. The default columns fit EDFbrowser files, with the onset in column 1, the duration in column 2 and the name in column 3, without group or channel column.", None))
    # retranslateUi

