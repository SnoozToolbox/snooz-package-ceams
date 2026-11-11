# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_LempZivComplexitySettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_LempZivComplexitySettingsView(object):
    def setupUi(self, LempZivComplexitySettingsView):
        if not LempZivComplexitySettingsView.objectName():
            LempZivComplexitySettingsView.setObjectName(u"LempZivComplexitySettingsView")
        LempZivComplexitySettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        LempZivComplexitySettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(LempZivComplexitySettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.epochs_horizontalLayout = QHBoxLayout()
        self.epochs_horizontalLayout.setObjectName(u"epochs_horizontalLayout")
        self.epochs_label = QLabel(LempZivComplexitySettingsView)
        self.epochs_label.setObjectName(u"epochs_label")

        self.epochs_horizontalLayout.addWidget(self.epochs_label)

        self.epochs_lineedit = QLineEdit(LempZivComplexitySettingsView)
        self.epochs_lineedit.setObjectName(u"epochs_lineedit")

        self.epochs_horizontalLayout.addWidget(self.epochs_lineedit)


        self.verticalLayout.addLayout(self.epochs_horizontalLayout)

        self.events_horizontalLayout = QHBoxLayout()
        self.events_horizontalLayout.setObjectName(u"events_horizontalLayout")
        self.events_label = QLabel(LempZivComplexitySettingsView)
        self.events_label.setObjectName(u"events_label")

        self.events_horizontalLayout.addWidget(self.events_label)

        self.events_lineedit = QLineEdit(LempZivComplexitySettingsView)
        self.events_lineedit.setObjectName(u"events_lineedit")

        self.events_horizontalLayout.addWidget(self.events_lineedit)


        self.verticalLayout.addLayout(self.events_horizontalLayout)

        self.mode_horizontalLayout = QHBoxLayout()
        self.mode_horizontalLayout.setObjectName(u"mode_horizontalLayout")
        self.mode_label = QLabel(LempZivComplexitySettingsView)
        self.mode_label.setObjectName(u"mode_label")

        self.mode_horizontalLayout.addWidget(self.mode_label)

        self.mode_lineedit = QLineEdit(LempZivComplexitySettingsView)
        self.mode_lineedit.setObjectName(u"mode_lineedit")

        self.mode_horizontalLayout.addWidget(self.mode_lineedit)


        self.verticalLayout.addLayout(self.mode_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(LempZivComplexitySettingsView)

        QMetaObject.connectSlotsByName(LempZivComplexitySettingsView)
    # setupUi

    def retranslateUi(self, LempZivComplexitySettingsView):
        LempZivComplexitySettingsView.setWindowTitle(QCoreApplication.translate("LempZivComplexitySettingsView", u"Form", None))
        self.epochs_label.setText(QCoreApplication.translate("LempZivComplexitySettingsView", u"epochs", None))
        self.events_label.setText(QCoreApplication.translate("LempZivComplexitySettingsView", u"events", None))
        self.mode_label.setText(QCoreApplication.translate("LempZivComplexitySettingsView", u"mode", None))
    # retranslateUi

