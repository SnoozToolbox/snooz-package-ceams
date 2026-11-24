# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_InputFiles.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_InputFiles(object):
    def setupUi(self, InputFiles):
        if not InputFiles.objectName():
            InputFiles.setObjectName(u"InputFiles")
        InputFiles.resize(900, 700)
        self.verticalLayout = QVBoxLayout(InputFiles)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.header_layout = QVBoxLayout()
        self.header_layout.setSpacing(6)
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(InputFiles)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.header_layout.addWidget(self.title_label)

        self.subtitle_label = QLabel(InputFiles)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setProperty(u"variant", u"help")

        self.header_layout.addWidget(self.subtitle_label)


        self.verticalLayout.addLayout(self.header_layout)

        self.xml_files_card = QFrame(InputFiles)
        self.xml_files_card.setObjectName(u"xml_files_card")
        self.xml_files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.xml_files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.xml_files_card_layout = QVBoxLayout(self.xml_files_card)
        self.xml_files_card_layout.setSpacing(10)
        self.xml_files_card_layout.setObjectName(u"xml_files_card_layout")
        self.xml_files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.xml_files_title_label = QLabel(self.xml_files_card)
        self.xml_files_title_label.setObjectName(u"xml_files_title_label")
        font1 = QFont()
        font1.setBold(True)
        self.xml_files_title_label.setFont(font1)

        self.xml_files_card_layout.addWidget(self.xml_files_title_label)

        self.tableWidget_files = QTableWidget(self.xml_files_card)
        self.tableWidget_files.setObjectName(u"tableWidget_files")
        self.tableWidget_files.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.xml_files_card_layout.addWidget(self.tableWidget_files)

        self.xml_files_buttons_layout = QHBoxLayout()
        self.xml_files_buttons_layout.setSpacing(8)
        self.xml_files_buttons_layout.setObjectName(u"xml_files_buttons_layout")
        self.output_help_label = QLabel(self.xml_files_card)
        self.output_help_label.setObjectName(u"output_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.output_help_label.setFont(font2)
        self.output_help_label.setWordWrap(True)
        self.output_help_label.setProperty(u"variant", u"help")

        self.xml_files_buttons_layout.addWidget(self.output_help_label)

        self.pushButton_choose = QPushButton(self.xml_files_card)
        self.pushButton_choose.setObjectName(u"pushButton_choose")

        self.xml_files_buttons_layout.addWidget(self.pushButton_choose)

        self.pushButton_clear = QPushButton(self.xml_files_card)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.xml_files_buttons_layout.addWidget(self.pushButton_clear)

        self.xml_files_buttons_layout.setStretch(0, 1)

        self.xml_files_card_layout.addLayout(self.xml_files_buttons_layout)


        self.verticalLayout.addWidget(self.xml_files_card)


        self.retranslateUi(InputFiles)
        self.pushButton_clear.clicked.connect(InputFiles.clear_slot)
        self.pushButton_choose.clicked.connect(InputFiles.choose_slot)

        QMetaObject.connectSlotsByName(InputFiles)
    # setupUi

    def retranslateUi(self, InputFiles):
        InputFiles.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("InputFiles", u"Input Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("InputFiles", u"Add the XML annotation files to convert.", None))
#if QT_CONFIG(tooltip)
        self.xml_files_title_label.setToolTip(QCoreApplication.translate("InputFiles", u"The Compumedics Profusion XML annotation files to convert.", None))
#endif // QT_CONFIG(tooltip)
        self.xml_files_title_label.setText(QCoreApplication.translate("InputFiles", u"XML files", None))
        self.output_help_label.setText(QCoreApplication.translate("InputFiles", u"A .tsv file is written next to each XML file, with the same name.", None))
        self.pushButton_choose.setText(QCoreApplication.translate("InputFiles", u"Choose files", None))
        self.pushButton_clear.setText(QCoreApplication.translate("InputFiles", u"Clear all", None))
    # retranslateUi

