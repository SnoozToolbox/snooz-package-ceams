# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SleepStageSelStep.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_SleepStageSelStep(object):
    def setupUi(self, SleepStageSelStep):
        if not SleepStageSelStep.objectName():
            SleepStageSelStep.setObjectName(u"SleepStageSelStep")
        SleepStageSelStep.resize(1068, 590)
        SleepStageSelStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_2 = QVBoxLayout(SleepStageSelStep)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(SleepStageSelStep)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(SleepStageSelStep)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_1 = QCheckBox(SleepStageSelStep)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_1, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(SleepStageSelStep)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 2)

        self.checkBox_3 = QCheckBox(SleepStageSelStep)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_3, 0, 3, 1, 1)

        self.checkBox_5 = QCheckBox(SleepStageSelStep)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_5, 0, 4, 1, 1)

        self.checkBox_9 = QCheckBox(SleepStageSelStep)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout.addWidget(self.checkBox_9, 1, 0, 1, 2)

        self.checkBox_0 = QCheckBox(SleepStageSelStep)
        self.checkBox_0.setObjectName(u"checkBox_0")

        self.gridLayout.addWidget(self.checkBox_0, 1, 2, 1, 2)


        self.horizontalLayout_4.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 417, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.retranslateUi(SleepStageSelStep)

        QMetaObject.connectSlotsByName(SleepStageSelStep)
    # setupUi

    def retranslateUi(self, SleepStageSelStep):
        SleepStageSelStep.setWindowTitle("")
        self.label_7.setText(QCoreApplication.translate("SleepStageSelStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep Stage Selection</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("SleepStageSelStep", u"Artifact detection is performed on the entire recording.\n"
"However, you can select specific sleep stages to potentially establish a cleaner baseline\n"
"for the set of algorithms that use a 3-component Gaussian Mixture Model (GMM).", None))
        self.checkBox_1.setText(QCoreApplication.translate("SleepStageSelStep", u"N1", None))
        self.checkBox_2.setText(QCoreApplication.translate("SleepStageSelStep", u"N2", None))
        self.checkBox_3.setText(QCoreApplication.translate("SleepStageSelStep", u"N3", None))
        self.checkBox_5.setText(QCoreApplication.translate("SleepStageSelStep", u"R", None))
        self.checkBox_9.setText(QCoreApplication.translate("SleepStageSelStep", u"Unscored", None))
        self.checkBox_0.setText(QCoreApplication.translate("SleepStageSelStep", u"Awake", None))
    # retranslateUi

