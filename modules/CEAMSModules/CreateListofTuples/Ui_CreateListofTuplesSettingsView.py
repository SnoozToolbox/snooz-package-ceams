# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_CreateListofTuplesSettingsView.ui'
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

class Ui_CreateListofTuplesSettingsView(object):
    def setupUi(self, CreateListofTuplesSettingsView):
        if not CreateListofTuplesSettingsView.objectName():
            CreateListofTuplesSettingsView.setObjectName(u"CreateListofTuplesSettingsView")
        CreateListofTuplesSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        CreateListofTuplesSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(CreateListofTuplesSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.events_horizontalLayout = QHBoxLayout()
        self.events_horizontalLayout.setObjectName(u"events_horizontalLayout")
        self.events_label = QLabel(CreateListofTuplesSettingsView)
        self.events_label.setObjectName(u"events_label")

        self.events_horizontalLayout.addWidget(self.events_label)

        self.events_lineedit = QLineEdit(CreateListofTuplesSettingsView)
        self.events_lineedit.setObjectName(u"events_lineedit")

        self.events_horizontalLayout.addWidget(self.events_lineedit)


        self.verticalLayout.addLayout(self.events_horizontalLayout)

        self.group_horizontalLayout = QHBoxLayout()
        self.group_horizontalLayout.setObjectName(u"group_horizontalLayout")
        self.group_label = QLabel(CreateListofTuplesSettingsView)
        self.group_label.setObjectName(u"group_label")

        self.group_horizontalLayout.addWidget(self.group_label)

        self.group_lineedit = QLineEdit(CreateListofTuplesSettingsView)
        self.group_lineedit.setObjectName(u"group_lineedit")

        self.group_horizontalLayout.addWidget(self.group_lineedit)


        self.verticalLayout.addLayout(self.group_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(CreateListofTuplesSettingsView)

        QMetaObject.connectSlotsByName(CreateListofTuplesSettingsView)
    # setupUi

    def retranslateUi(self, CreateListofTuplesSettingsView):
        CreateListofTuplesSettingsView.setWindowTitle(QCoreApplication.translate("CreateListofTuplesSettingsView", u"Form", None))
        self.events_label.setText(QCoreApplication.translate("CreateListofTuplesSettingsView", u"events", None))
        self.group_label.setText(QCoreApplication.translate("CreateListofTuplesSettingsView", u"group", None))
    # retranslateUi

