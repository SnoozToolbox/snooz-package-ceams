# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Outputfiles.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Outputfiles(object):
    def setupUi(self, Outputfiles):
        if not Outputfiles.objectName():
            Outputfiles.setObjectName(u"Outputfiles")
        self.verticalLayout = QVBoxLayout(Outputfiles)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.report_label = QLabel(Outputfiles)
        self.report_label.setObjectName(u"report_label")
        self.report_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.report_label)

        self.filenameLayout = QHBoxLayout()
        self.filenameLayout.setObjectName(u"filenameLayout")
        self.filename_label = QLabel(Outputfiles)
        self.filename_label.setObjectName(u"filename_label")

        self.filenameLayout.addWidget(self.filename_label)

        self.filename_lineEdit = QLineEdit(Outputfiles)
        self.filename_lineEdit.setObjectName(u"filename_lineEdit")

        self.filenameLayout.addWidget(self.filename_lineEdit)

        self.choose_pushButton = QPushButton(Outputfiles)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.filenameLayout.addWidget(self.choose_pushButton)


        self.verticalLayout.addLayout(self.filenameLayout)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

#if QT_CONFIG(shortcut)
        self.filename_label.setBuddy(self.filename_lineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Outputfiles)

        QMetaObject.connectSlotsByName(Outputfiles)
    # setupUi

    def retranslateUi(self, Outputfiles):
        self.report_label.setText(QCoreApplication.translate("Outputfiles", u"Snooz writes one TSV report for all selected recordings. Results are grouped by channel and sleep stage, without hourly or cycle breakdowns. New results are appended if the file already exists.", None))
        self.filename_label.setText(QCoreApplication.translate("Outputfiles", u"Output file", None))
        self.filename_lineEdit.setPlaceholderText(QCoreApplication.translate("Outputfiles", u"Choose a .tsv file", None))
        self.choose_pushButton.setText(QCoreApplication.translate("Outputfiles", u"Browse...", None))
        pass
    # retranslateUi

