# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_RnBSettingsView.ui'
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

class Ui_RnBSettingsView(object):
    def setupUi(self, RnBSettingsView):
        if not RnBSettingsView.objectName():
            RnBSettingsView.setObjectName(u"RnBSettingsView")
        RnBSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        RnBSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(RnBSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signals_horizontalLayout = QHBoxLayout()
        self.signals_horizontalLayout.setObjectName(u"signals_horizontalLayout")
        self.signals_label = QLabel(RnBSettingsView)
        self.signals_label.setObjectName(u"signals_label")

        self.signals_horizontalLayout.addWidget(self.signals_label)

        self.signals_lineedit = QLineEdit(RnBSettingsView)
        self.signals_lineedit.setObjectName(u"signals_lineedit")

        self.signals_horizontalLayout.addWidget(self.signals_lineedit)


        self.verticalLayout.addLayout(self.signals_horizontalLayout)

        self.win_len_sec_horizontalLayout = QHBoxLayout()
        self.win_len_sec_horizontalLayout.setObjectName(u"win_len_sec_horizontalLayout")
        self.win_len_sec_label = QLabel(RnBSettingsView)
        self.win_len_sec_label.setObjectName(u"win_len_sec_label")

        self.win_len_sec_horizontalLayout.addWidget(self.win_len_sec_label)

        self.win_len_sec_lineedit = QLineEdit(RnBSettingsView)
        self.win_len_sec_lineedit.setObjectName(u"win_len_sec_lineedit")

        self.win_len_sec_horizontalLayout.addWidget(self.win_len_sec_lineedit)


        self.verticalLayout.addLayout(self.win_len_sec_horizontalLayout)

        self.win_step_sec_horizontalLayout = QHBoxLayout()
        self.win_step_sec_horizontalLayout.setObjectName(u"win_step_sec_horizontalLayout")
        self.win_step_sec_label = QLabel(RnBSettingsView)
        self.win_step_sec_label.setObjectName(u"win_step_sec_label")

        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_label)

        self.win_step_sec_lineedit = QLineEdit(RnBSettingsView)
        self.win_step_sec_lineedit.setObjectName(u"win_step_sec_lineedit")

        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_lineedit)


        self.verticalLayout.addLayout(self.win_step_sec_horizontalLayout)

        self.alpha_param_horizontalLayout = QHBoxLayout()
        self.alpha_param_horizontalLayout.setObjectName(u"alpha_param_horizontalLayout")
        self.alpha_param_label = QLabel(RnBSettingsView)
        self.alpha_param_label.setObjectName(u"alpha_param_label")

        self.alpha_param_horizontalLayout.addWidget(self.alpha_param_label)

        self.alpha_param_lineedit = QLineEdit(RnBSettingsView)
        self.alpha_param_lineedit.setObjectName(u"alpha_param_lineedit")

        self.alpha_param_horizontalLayout.addWidget(self.alpha_param_lineedit)


        self.verticalLayout.addLayout(self.alpha_param_horizontalLayout)

        self.decomp_level_horizontalLayout = QHBoxLayout()
        self.decomp_level_horizontalLayout.setObjectName(u"decomp_level_horizontalLayout")
        self.decomp_level_label = QLabel(RnBSettingsView)
        self.decomp_level_label.setObjectName(u"decomp_level_label")

        self.decomp_level_horizontalLayout.addWidget(self.decomp_level_label)

        self.decomp_level_lineedit = QLineEdit(RnBSettingsView)
        self.decomp_level_lineedit.setObjectName(u"decomp_level_lineedit")

        self.decomp_level_horizontalLayout.addWidget(self.decomp_level_lineedit)


        self.verticalLayout.addLayout(self.decomp_level_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(RnBSettingsView)

        QMetaObject.connectSlotsByName(RnBSettingsView)
    # setupUi

    def retranslateUi(self, RnBSettingsView):
        RnBSettingsView.setWindowTitle(QCoreApplication.translate("RnBSettingsView", u"Form", None))
        self.signals_label.setText(QCoreApplication.translate("RnBSettingsView", u"signals", None))
        self.win_len_sec_label.setText(QCoreApplication.translate("RnBSettingsView", u"win_len_sec", None))
        self.win_step_sec_label.setText(QCoreApplication.translate("RnBSettingsView", u"win_step_sec", None))
        self.alpha_param_label.setText(QCoreApplication.translate("RnBSettingsView", u"alpha_param", None))
        self.decomp_level_label.setText(QCoreApplication.translate("RnBSettingsView", u"decomp_level", None))
    # retranslateUi

