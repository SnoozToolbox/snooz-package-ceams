# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file ''
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

class Ui_DictionaryResultsView(object):
    def setupUi(self, DictionaryResultsView):
        if not DictionaryResultsView.objectName():
            DictionaryResultsView.setObjectName(u"DictionaryResultsView")
        DictionaryResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(DictionaryResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(DictionaryResultsView)

        QMetaObject.connectSlotsByName(DictionaryResultsView)
    # setupUi

    def retranslateUi(self, DictionaryResultsView):
        DictionaryResultsView.setWindowTitle(QCoreApplication.translate("DictionaryResultsView", u"Form", None))
    # retranslateUi

