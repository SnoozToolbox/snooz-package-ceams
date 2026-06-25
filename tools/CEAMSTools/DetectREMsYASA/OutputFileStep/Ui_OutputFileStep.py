# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_OutputFileStep.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_OutputFileStep(object):
    def setupUi(self, OutputFileStep):
        if not OutputFileStep.objectName():
            OutputFileStep.setObjectName(u"OutputFileStep")
        OutputFileStep.resize(741, 590)
        OutputFileStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(OutputFileStep)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(OutputFileStep)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 3, 1, 1)

        self.label_2 = QLabel(OutputFileStep)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)

        self.lineEdit_CohortFilename = QLineEdit(OutputFileStep)
        self.lineEdit_CohortFilename.setObjectName(u"lineEdit_CohortFilename")

        self.gridLayout.addWidget(self.lineEdit_CohortFilename, 4, 3, 1, 1)

        self.pushButton_CohortFilename = QPushButton(OutputFileStep)
        self.pushButton_CohortFilename.setObjectName(u"pushButton_CohortFilename")

        self.gridLayout.addWidget(self.pushButton_CohortFilename, 4, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 2, 1, 1)

        self.label = QLabel(OutputFileStep)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 2, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(OutputFileStep)

        QMetaObject.connectSlotsByName(OutputFileStep)
    # setupUi

    def retranslateUi(self, OutputFileStep):
        OutputFileStep.setWindowTitle("")
        self.label_3.setText(QCoreApplication.translate("OutputFileStep", u"<html><head/><body><p>Select a file name to save the report file:</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("OutputFileStep", u"<html><head/><body><p>REMs characteristics:</p><p>- REMs count<br/>- Duration of the REMs in second<br/>- Amplitude of the REMs (Difference between the peak and trough of the [LOC - ROC])<br/>- Density of the REMs in cycles and hours<br/>- Variablity of the densities</p><p>The report consists of the average of the mentioned characteristics in:</p><p>- total (all selected stages)<br/>- per sleep cycle<br/>- per clock hour<br/>- per hour spent in each stage</p></body></html>", None))
        self.pushButton_CohortFilename.setText(QCoreApplication.translate("OutputFileStep", u"Browse", None))
        self.label.setText(QCoreApplication.translate("OutputFileStep", u"<html><head/><body><p><span style=\" font-weight:700;\">REMs Cohort Report</span></p></body></html>", None))
    # retranslateUi

