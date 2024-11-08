# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signals_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SignalsWidget(object):
    def setupUi(self, SignalsWidget):
        if not SignalsWidget.objectName():
            SignalsWidget.setObjectName(u"SignalsWidget")
        SignalsWidget.resize(1250, 584)
        self.verticalLayout = QVBoxLayout(SignalsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.signals_graphicsView = QGraphicsView(SignalsWidget)
        self.signals_graphicsView.setObjectName(u"signals_graphicsView")

        self.verticalLayout.addWidget(self.signals_graphicsView)

        self.timeline_horizontalScrollBar = QScrollBar(SignalsWidget)
        self.timeline_horizontalScrollBar.setObjectName(u"timeline_horizontalScrollBar")
        self.timeline_horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.timeline_horizontalScrollBar)


        self.retranslateUi(SignalsWidget)
        self.timeline_horizontalScrollBar.valueChanged.connect(SignalsWidget.on_timeline_scroll)

        QMetaObject.connectSlotsByName(SignalsWidget)
    # setupUi

    def retranslateUi(self, SignalsWidget):
        SignalsWidget.setWindowTitle(QCoreApplication.translate("SignalsWidget", u"Form", None))
    # retranslateUi

