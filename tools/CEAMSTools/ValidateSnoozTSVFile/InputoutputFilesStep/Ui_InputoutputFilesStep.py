# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_InputoutputFilesStep.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_InputoutputFilesStep(object):
    def setupUi(self, InputoutputFilesStep):
        if not InputoutputFilesStep.objectName():
            InputoutputFilesStep.setObjectName(u"InputoutputFilesStep")
        InputoutputFilesStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(InputoutputFilesStep)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.header_layout = QVBoxLayout()
        self.header_layout.setSpacing(6)
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(InputoutputFilesStep)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.header_layout.addWidget(self.title_label)

        self.subtitle_label = QLabel(InputoutputFilesStep)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setProperty(u"variant", u"help")

        self.header_layout.addWidget(self.subtitle_label)


        self.verticalLayout.addLayout(self.header_layout)

        self.tsv_files_card = QFrame(InputoutputFilesStep)
        self.tsv_files_card.setObjectName(u"tsv_files_card")
        self.tsv_files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.tsv_files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.tsv_files_card_layout = QVBoxLayout(self.tsv_files_card)
        self.tsv_files_card_layout.setSpacing(10)
        self.tsv_files_card_layout.setObjectName(u"tsv_files_card_layout")
        self.tsv_files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.tsv_files_title_label = QLabel(self.tsv_files_card)
        self.tsv_files_title_label.setObjectName(u"tsv_files_title_label")
        font1 = QFont()
        font1.setBold(True)
        self.tsv_files_title_label.setFont(font1)

        self.tsv_files_card_layout.addWidget(self.tsv_files_title_label)

        self.listWidget = QListWidget(self.tsv_files_card)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.listWidget.setLineWidth(0)

        self.tsv_files_card_layout.addWidget(self.listWidget)

        self.tsv_files_buttons_layout = QHBoxLayout()
        self.tsv_files_buttons_layout.setSpacing(8)
        self.tsv_files_buttons_layout.setObjectName(u"tsv_files_buttons_layout")
        self.tsv_files_buttons_layout_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.tsv_files_buttons_layout.addItem(self.tsv_files_buttons_layout_spacer)

        self.pushButton = QPushButton(self.tsv_files_card)
        self.pushButton.setObjectName(u"pushButton")

        self.tsv_files_buttons_layout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.tsv_files_card)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.tsv_files_buttons_layout.addWidget(self.pushButton_2)

        self.tsv_files_buttons_layout.setStretch(0, 1)

        self.tsv_files_card_layout.addLayout(self.tsv_files_buttons_layout)


        self.verticalLayout.addWidget(self.tsv_files_card)

        self.reports_card = QFrame(InputoutputFilesStep)
        self.reports_card.setObjectName(u"reports_card")
        self.reports_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.reports_card.setFrameShadow(QFrame.Shadow.Raised)
        self.reports_card_layout = QVBoxLayout(self.reports_card)
        self.reports_card_layout.setSpacing(10)
        self.reports_card_layout.setObjectName(u"reports_card_layout")
        self.reports_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.reports_card)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.reports_card_layout.addWidget(self.label)

        self.reports_help_label = QLabel(self.reports_card)
        self.reports_help_label.setObjectName(u"reports_help_label")
        self.reports_help_label.setWordWrap(True)
        self.reports_help_label.setProperty(u"variant", u"help")

        self.reports_card_layout.addWidget(self.reports_help_label)

        self.reports_layout = QHBoxLayout()
        self.reports_layout.setSpacing(8)
        self.reports_layout.setObjectName(u"reports_layout")
        self.lineEdit = QLineEdit(self.reports_card)
        self.lineEdit.setObjectName(u"lineEdit")

        self.reports_layout.addWidget(self.lineEdit)

        self.pushButton_3 = QPushButton(self.reports_card)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.reports_layout.addWidget(self.pushButton_3)


        self.reports_card_layout.addLayout(self.reports_layout)


        self.verticalLayout.addWidget(self.reports_card)


        self.retranslateUi(InputoutputFilesStep)

        QMetaObject.connectSlotsByName(InputoutputFilesStep)
    # setupUi

    def retranslateUi(self, InputoutputFilesStep):
        InputoutputFilesStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("InputoutputFilesStep", u"Input/Output Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("InputoutputFilesStep", u"Add the annotation files to validate, then choose the folder of the validation reports.", None))
#if QT_CONFIG(tooltip)
        self.tsv_files_title_label.setToolTip(QCoreApplication.translate("InputoutputFilesStep", u"The Snooz annotation files (.tsv) to validate.", None))
#endif // QT_CONFIG(tooltip)
        self.tsv_files_title_label.setText(QCoreApplication.translate("InputoutputFilesStep", u"Annotation files", None))
        self.pushButton.setText(QCoreApplication.translate("InputoutputFilesStep", u"Add files", None))
        self.pushButton_2.setText(QCoreApplication.translate("InputoutputFilesStep", u"Clear all", None))
        self.label.setText(QCoreApplication.translate("InputoutputFilesStep", u"Reports folder", None))
        self.reports_help_label.setText(QCoreApplication.translate("InputoutputFilesStep", u"One validation report per annotation file: &lt;name&gt;_validation_log.txt.", None))
        self.pushButton_3.setText(QCoreApplication.translate("InputoutputFilesStep", u"Choose", None))
    # retranslateUi

