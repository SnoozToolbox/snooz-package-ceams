# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_IntroStep.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_IntroStep(object):
    def setupUi(self, IntroStep):
        if not IntroStep.objectName():
            IntroStep.setObjectName(u"IntroStep")
        IntroStep.resize(787, 522)
        self.verticalLayout = QVBoxLayout(IntroStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(IntroStep)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spectra_CZ_image = QLabel(IntroStep)
        self.spectra_CZ_image.setObjectName(u"spectra_CZ_image")

        self.horizontalLayout.addWidget(self.spectra_CZ_image)

        self.spectra_O1_image = QLabel(IntroStep)
        self.spectra_O1_image.setObjectName(u"spectra_O1_image")

        self.horizontalLayout.addWidget(self.spectra_O1_image)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(IntroStep)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(IntroStep)

        QMetaObject.connectSlotsByName(IntroStep)
    # setupUi

    def retranslateUi(self, IntroStep):
        self.label_2.setText(QCoreApplication.translate("IntroStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Estimate EEG spectral power with the Welch method.</span></p><p>1. Add PSG files and select the EEG channels.</p><p>2. Set the frequency range and analysis windows, or keep the defaults.</p><p>3. Choose a TSV file for the whole-recording report by sleep stage and channel.</p></body></html>", None))
        self.spectra_CZ_image.setText(QCoreApplication.translate("IntroStep", u"spectra_CZ_image", None))
        self.spectra_O1_image.setText(QCoreApplication.translate("IntroStep", u"spectra_O1_image", None))
        self.label.setText(QCoreApplication.translate("IntroStep", u"A fixed 0.3\u201362 Hz band-pass filter is applied. Use channels sampled above 124 Hz (e.g., 125 Hz).", None))
        pass
    # retranslateUi

