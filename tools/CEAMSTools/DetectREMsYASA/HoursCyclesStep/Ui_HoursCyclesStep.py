# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_HoursCyclesStep.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_HoursCyclesStep(object):
    def setupUi(self, HoursCyclesStep):
        if not HoursCyclesStep.objectName():
            HoursCyclesStep.setObjectName(u"HoursCyclesStep")
        HoursCyclesStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(HoursCyclesStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(HoursCyclesStep)
        self.content_widget.setObjectName(u"content_widget")
        self.content_widget.setMaximumSize(QSize(800, 16777215))
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setSpacing(16)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout = QVBoxLayout()
        self.header_layout.setSpacing(6)
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(self.content_widget)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.header_layout.addWidget(self.title_label)

        self.subtitle_label = QLabel(self.content_widget)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setProperty(u"variant", u"help")

        self.header_layout.addWidget(self.subtitle_label)


        self.content_layout.addLayout(self.header_layout)

        self.limits_row = QHBoxLayout()
        self.limits_row.setSpacing(16)
        self.limits_row.setObjectName(u"limits_row")
        self.limits_card = QFrame(self.content_widget)
        self.limits_card.setObjectName(u"limits_card")
        self.limits_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.limits_card.setFrameShadow(QFrame.Shadow.Raised)
        self.limits_card_layout = QVBoxLayout(self.limits_card)
        self.limits_card_layout.setSpacing(10)
        self.limits_card_layout.setObjectName(u"limits_card_layout")
        self.limits_card_layout.setContentsMargins(10, 10, 10, 10)
        self.limits_grid = QGridLayout()
        self.limits_grid.setObjectName(u"limits_grid")
        self.limits_grid.setHorizontalSpacing(12)
        self.limits_grid.setVerticalSpacing(10)
        self.label_2 = QLabel(self.limits_card)
        self.label_2.setObjectName(u"label_2")

        self.limits_grid.addWidget(self.label_2, 0, 0, 1, 1)

        self.spinBox_cycles = QSpinBox(self.limits_card)
        self.spinBox_cycles.setObjectName(u"spinBox_cycles")
        self.spinBox_cycles.setMinimum(1)
        self.spinBox_cycles.setMaximum(12)
        self.spinBox_cycles.setValue(6)

        self.limits_grid.addWidget(self.spinBox_cycles, 0, 1, 1, 1)

        self.label = QLabel(self.limits_card)
        self.label.setObjectName(u"label")

        self.limits_grid.addWidget(self.label, 1, 0, 1, 1)

        self.spinBox_hours = QSpinBox(self.limits_card)
        self.spinBox_hours.setObjectName(u"spinBox_hours")
        self.spinBox_hours.setEnabled(True)
        self.spinBox_hours.setMinimum(1)
        self.spinBox_hours.setMaximum(48)
        self.spinBox_hours.setValue(8)

        self.limits_grid.addWidget(self.spinBox_hours, 1, 1, 1, 1)

        self.limits_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.limits_grid.addItem(self.limits_grid_spacer, 0, 3, 1, 1)


        self.limits_card_layout.addLayout(self.limits_grid)

        self.limits_help_label = QLabel(self.limits_card)
        self.limits_help_label.setObjectName(u"limits_help_label")
        font1 = QFont()
        font1.setPointSize(10)
        self.limits_help_label.setFont(font1)
        self.limits_help_label.setWordWrap(True)
        self.limits_help_label.setProperty(u"variant", u"help")

        self.limits_card_layout.addWidget(self.limits_help_label)


        self.limits_row.addWidget(self.limits_card)

        self.limits_row_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.limits_row.addItem(self.limits_row_spacer)

        self.limits_row.setStretch(0, 1)
        self.limits_row.setStretch(1, 1)

        self.content_layout.addLayout(self.limits_row)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(HoursCyclesStep)

        QMetaObject.connectSlotsByName(HoursCyclesStep)
    # setupUi

    def retranslateUi(self, HoursCyclesStep):
        HoursCyclesStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("HoursCyclesStep", u"Hours and Cycles", None))
        self.subtitle_label.setText(QCoreApplication.translate("HoursCyclesStep", u"The maximum number of sleep cycles and hours to analyze in the reports (step Output File).", None))
        self.label_2.setText(QCoreApplication.translate("HoursCyclesStep", u"Maximum number of sleep cycles", None))
        self.label.setText(QCoreApplication.translate("HoursCyclesStep", u"Maximum number of hours", None))
        self.limits_help_label.setText(QCoreApplication.translate("HoursCyclesStep", u"The cycles and the hours after these numbers are not reported.", None))
    # retranslateUi

