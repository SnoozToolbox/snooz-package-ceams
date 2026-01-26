# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_RandBSettingsView.ui'
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

class Ui_RandBSettingsView(object):
    def setupUi(self, RandBSettingsView):
        if not RandBSettingsView.objectName():
            RandBSettingsView.setObjectName(u"RandBSettingsView")
        RandBSettingsView.resize(704, 328)
        self.verticalLayout = QVBoxLayout(RandBSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signals_horizontalLayout = QHBoxLayout()
        self.signals_horizontalLayout.setObjectName(u"signals_horizontalLayout")

        self.verticalLayout.addLayout(self.signals_horizontalLayout)

        self.win_len_sec_horizontalLayout = QHBoxLayout()
        self.win_len_sec_horizontalLayout.setObjectName(u"win_len_sec_horizontalLayout")
        self.win_len_sec_label = QLabel(RandBSettingsView)
        self.win_len_sec_label.setObjectName(u"win_len_sec_label")

        self.win_len_sec_horizontalLayout.addWidget(self.win_len_sec_label)

        self.win_len_sec_lineedit = QLineEdit(RandBSettingsView)
        self.win_len_sec_lineedit.setObjectName(u"win_len_sec_lineedit")

        self.win_len_sec_horizontalLayout.addWidget(self.win_len_sec_lineedit)


        self.verticalLayout.addLayout(self.win_len_sec_horizontalLayout)

        self.win_step_sec_horizontalLayout = QHBoxLayout()
        self.win_step_sec_horizontalLayout.setObjectName(u"win_step_sec_horizontalLayout")
        self.win_step_sec_label = QLabel(RandBSettingsView)
        self.win_step_sec_label.setObjectName(u"win_step_sec_label")

        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_label)

        self.win_step_sec_lineedit = QLineEdit(RandBSettingsView)
        self.win_step_sec_lineedit.setObjectName(u"win_step_sec_lineedit")

        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_lineedit)


        self.verticalLayout.addLayout(self.win_step_sec_horizontalLayout)

        self.window_name_horizontalLayout = QHBoxLayout()
        self.window_name_horizontalLayout.setObjectName(u"window_name_horizontalLayout")
        self.window_name_label = QLabel(RandBSettingsView)
        self.window_name_label.setObjectName(u"window_name_label")

        self.window_name_horizontalLayout.addWidget(self.window_name_label)

        self.window_name_lineedit = QLineEdit(RandBSettingsView)
        self.window_name_lineedit.setObjectName(u"window_name_lineedit")

        self.window_name_horizontalLayout.addWidget(self.window_name_lineedit)


        self.verticalLayout.addLayout(self.window_name_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(RandBSettingsView)

        QMetaObject.connectSlotsByName(RandBSettingsView)
    # setupUi

    def retranslateUi(self, RandBSettingsView):
        RandBSettingsView.setWindowTitle(QCoreApplication.translate("RandBSettingsView", u"Form", None))
        self.win_len_sec_label.setText(QCoreApplication.translate("RandBSettingsView", u"win_len_sec", None))
        self.win_step_sec_label.setText(QCoreApplication.translate("RandBSettingsView", u"win_step_sec", None))
        self.window_name_label.setText(QCoreApplication.translate("RandBSettingsView", u"window_name", None))
    # retranslateUi

