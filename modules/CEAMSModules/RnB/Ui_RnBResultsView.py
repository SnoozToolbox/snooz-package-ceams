# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_RnBResultsView.ui'
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
import themes_rc

class Ui_RnBResultsView(object):
    def setupUi(self, RnBResultsView):
        if not RnBResultsView.objectName():
            RnBResultsView.setObjectName(u"RnBResultsView")
        RnBResultsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        RnBResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(RnBResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(RnBResultsView)

        QMetaObject.connectSlotsByName(RnBResultsView)
    # setupUi

    def retranslateUi(self, RnBResultsView):
        RnBResultsView.setWindowTitle(QCoreApplication.translate("RnBResultsView", u"Form", None))
    # retranslateUi

