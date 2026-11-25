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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_IntroStep(object):
    def setupUi(self, IntroStep):
        if not IntroStep.objectName():
            IntroStep.setObjectName(u"IntroStep")
        IntroStep.resize(787, 522)
        self.verticalLayout = QVBoxLayout(IntroStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(IntroStep)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.titleLabel.setFont(font)

        self.verticalLayout.addWidget(self.titleLabel)

        self.subtitleLabel = QLabel(IntroStep)
        self.subtitleLabel.setObjectName(u"subtitleLabel")

        self.verticalLayout.addWidget(self.subtitleLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.inputFilesTitle = QLabel(IntroStep)
        self.inputFilesTitle.setObjectName(u"inputFilesTitle")
        self.inputFilesTitle.setMinimumSize(QSize(150, 0))
        font1 = QFont()
        font1.setBold(True)
        self.inputFilesTitle.setFont(font1)

        self.verticalLayout.addWidget(self.inputFilesTitle)

        self.spectralSettingsTitle = QLabel(IntroStep)
        self.spectralSettingsTitle.setObjectName(u"spectralSettingsTitle")
        self.spectralSettingsTitle.setMinimumSize(QSize(150, 0))
        self.spectralSettingsTitle.setFont(font1)

        self.verticalLayout.addWidget(self.spectralSettingsTitle)

        self.outputFileTitle = QLabel(IntroStep)
        self.outputFileTitle.setObjectName(u"outputFileTitle")
        self.outputFileTitle.setMinimumSize(QSize(150, 0))
        self.outputFileTitle.setFont(font1)

        self.verticalLayout.addWidget(self.outputFileTitle)

        self.spectraGroupBox = QGroupBox(IntroStep)
        self.spectraGroupBox.setObjectName(u"spectraGroupBox")
        self.spectraGroupLayout = QVBoxLayout(self.spectraGroupBox)
        self.spectraGroupLayout.setObjectName(u"spectraGroupLayout")
        self.spectraHeading = QLabel(self.spectraGroupBox)
        self.spectraHeading.setObjectName(u"spectraHeading")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.spectraHeading.setFont(font2)

        self.spectraGroupLayout.addWidget(self.spectraHeading)

        self.spectraLayout = QHBoxLayout()
        self.spectraLayout.setSpacing(12)
        self.spectraLayout.setObjectName(u"spectraLayout")
        self.czSpectraLayout = QVBoxLayout()
        self.czSpectraLayout.setObjectName(u"czSpectraLayout")
        self.czSpectraTitle = QLabel(self.spectraGroupBox)
        self.czSpectraTitle.setObjectName(u"czSpectraTitle")
        self.czSpectraTitle.setFont(font1)

        self.czSpectraLayout.addWidget(self.czSpectraTitle)

        self.spectra_CZ_image = QLabel(self.spectraGroupBox)
        self.spectra_CZ_image.setObjectName(u"spectra_CZ_image")
        self.spectra_CZ_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.czSpectraLayout.addWidget(self.spectra_CZ_image)


        self.spectraLayout.addLayout(self.czSpectraLayout)

        self.o1SpectraLayout = QVBoxLayout()
        self.o1SpectraLayout.setObjectName(u"o1SpectraLayout")
        self.o1SpectraTitle = QLabel(self.spectraGroupBox)
        self.o1SpectraTitle.setObjectName(u"o1SpectraTitle")
        self.o1SpectraTitle.setFont(font1)

        self.o1SpectraLayout.addWidget(self.o1SpectraTitle)

        self.spectra_O1_image = QLabel(self.spectraGroupBox)
        self.spectra_O1_image.setObjectName(u"spectra_O1_image")
        self.spectra_O1_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.o1SpectraLayout.addWidget(self.spectra_O1_image)


        self.spectraLayout.addLayout(self.o1SpectraLayout)


        self.spectraGroupLayout.addLayout(self.spectraLayout)


        self.verticalLayout.addWidget(self.spectraGroupBox)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(IntroStep)

        QMetaObject.connectSlotsByName(IntroStep)
    # setupUi

    def retranslateUi(self, IntroStep):
        self.titleLabel.setText(QCoreApplication.translate("IntroStep", u"EEG Spectral Analysis", None))
        self.subtitleLabel.setText(QCoreApplication.translate("IntroStep", u"Use the steps in the left panel to configure the analysis. Power is estimated with the Welch method.", None))
        self.inputFilesTitle.setText(QCoreApplication.translate("IntroStep", u"<html><head/><body><p>1. Input Files<span style=\" font-weight:400;\">: Add PSG files and select EEG channels.</span></p></body></html>", None))
        self.spectralSettingsTitle.setText(QCoreApplication.translate("IntroStep", u"<html><head/><body><p>2. Spectral Settings:<span style=\" font-weight:400;\"> Set the frequency range and analysis windows.</span></p></body></html>", None))
        self.outputFileTitle.setText(QCoreApplication.translate("IntroStep", u"<html><head/><body><p>3. Output File: <span style=\" font-weight:400;\">Choose a TSV report grouped by sleep stage and channel.</span></p></body></html>", None))
        self.spectraGroupBox.setTitle("")
        self.spectraHeading.setText(QCoreApplication.translate("IntroStep", u"Example spectra | N2 vs N3", None))
        self.czSpectraTitle.setText(QCoreApplication.translate("IntroStep", u"Cz-A1", None))
        self.spectra_CZ_image.setText("")
        self.o1SpectraTitle.setText(QCoreApplication.translate("IntroStep", u"O1-A2", None))
        self.spectra_O1_image.setText("")
        pass
    # retranslateUi

