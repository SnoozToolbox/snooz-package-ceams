# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EditPathsInSnoozWorkspaceSettingStep.ui'
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

class Ui_EditPathsInSnoozWorkspaceSettingStep(object):
    def setupUi(self, EditPathsInSnoozWorkspaceSettingStep):
        if not EditPathsInSnoozWorkspaceSettingStep.objectName():
            EditPathsInSnoozWorkspaceSettingStep.setObjectName(u"EditPathsInSnoozWorkspaceSettingStep")
        EditPathsInSnoozWorkspaceSettingStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(EditPathsInSnoozWorkspaceSettingStep)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_box_layout = QVBoxLayout()
        self.header_box_layout.setObjectName(u"header_box_layout")
        self.header_box_layout.setContentsMargins(19, 12, 19, 0)
        self.header_layout = QVBoxLayout()
        self.header_layout.setSpacing(6)
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(EditPathsInSnoozWorkspaceSettingStep)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.header_layout.addWidget(self.title_label)

        self.subtitle_label = QLabel(EditPathsInSnoozWorkspaceSettingStep)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setProperty(u"variant", u"help")

        self.header_layout.addWidget(self.subtitle_label)


        self.header_box_layout.addLayout(self.header_layout)


        self.verticalLayout.addLayout(self.header_box_layout)


        self.retranslateUi(EditPathsInSnoozWorkspaceSettingStep)

        QMetaObject.connectSlotsByName(EditPathsInSnoozWorkspaceSettingStep)
    # setupUi

    def retranslateUi(self, EditPathsInSnoozWorkspaceSettingStep):
        EditPathsInSnoozWorkspaceSettingStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("EditPathsInSnoozWorkspaceSettingStep", u"Edit Paths", None))
        self.subtitle_label.setText(QCoreApplication.translate("EditPathsInSnoozWorkspaceSettingStep", u"Add the Snooz workspaces, edit their paths, then choose the suffix and the folder of the new workspaces.", None))
    # retranslateUi

