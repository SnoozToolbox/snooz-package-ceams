# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_RandBResultsView.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
import themes_rc

class Ui_RandBResultsView(object):
    def setupUi(self, RandBResultsView):
        if not RandBResultsView.objectName():
            RandBResultsView.setObjectName(u"RandBResultsView")
        RandBResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(RandBResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(RandBResultsView)

        QMetaObject.connectSlotsByName(RandBResultsView)
    # setupUi

    def retranslateUi(self, RandBResultsView):
        RandBResultsView.setWindowTitle(QCoreApplication.translate("RandBResultsView", u"Form", None))
    # retranslateUi

