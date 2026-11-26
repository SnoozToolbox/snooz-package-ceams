# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_TextFileAssociation.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_TextFileAssociation(object):
    def setupUi(self, TextFileAssociation):
        if not TextFileAssociation.objectName():
            TextFileAssociation.setObjectName(u"TextFileAssociation")
        TextFileAssociation.resize(900, 700)
        self.verticalLayout = QVBoxLayout(TextFileAssociation)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(TextFileAssociation)
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

        self.name_card = QFrame(self.content_widget)
        self.name_card.setObjectName(u"name_card")
        self.name_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.name_card.setFrameShadow(QFrame.Shadow.Raised)
        self.name_card_layout = QVBoxLayout(self.name_card)
        self.name_card_layout.setSpacing(10)
        self.name_card_layout.setObjectName(u"name_card_layout")
        self.name_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_16 = QLabel(self.name_card)
        self.label_16.setObjectName(u"label_16")
        font1 = QFont()
        font1.setBold(True)
        self.label_16.setFont(font1)

        self.name_card_layout.addWidget(self.label_16)

        self.label_17 = QLabel(self.name_card)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setWordWrap(True)
        self.label_17.setProperty(u"variant", u"help")

        self.name_card_layout.addWidget(self.label_17)

        self.name_grid = QGridLayout()
        self.name_grid.setObjectName(u"name_grid")
        self.name_grid.setHorizontalSpacing(12)
        self.name_grid.setVerticalSpacing(10)
        self.label_18 = QLabel(self.name_card)
        self.label_18.setObjectName(u"label_18")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QSize(50, 0))
        self.label_18.setMaximumSize(QSize(60, 16777215))

        self.name_grid.addWidget(self.label_18, 0, 0, 1, 1)

        self.lineEdit_prefix = QLineEdit(self.name_card)
        self.lineEdit_prefix.setObjectName(u"lineEdit_prefix")

        self.name_grid.addWidget(self.lineEdit_prefix, 0, 1, 1, 1)

        self.label_19 = QLabel(self.name_card)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(60, 16777215))

        self.name_grid.addWidget(self.label_19, 1, 0, 1, 1)

        self.lineEdit_suffix = QLineEdit(self.name_card)
        self.lineEdit_suffix.setObjectName(u"lineEdit_suffix")

        self.name_grid.addWidget(self.lineEdit_suffix, 1, 1, 1, 1)

        self.label = QLabel(self.name_card)
        self.label.setObjectName(u"label")

        self.name_grid.addWidget(self.label, 2, 0, 1, 1)

        self.lineEdit_ext = QLineEdit(self.name_card)
        self.lineEdit_ext.setObjectName(u"lineEdit_ext")

        self.name_grid.addWidget(self.lineEdit_ext, 2, 1, 1, 1)

        self.extension_unit_label = QLabel(self.name_card)
        self.extension_unit_label.setObjectName(u"extension_unit_label")
        self.extension_unit_label.setProperty(u"variant", u"help")

        self.name_grid.addWidget(self.extension_unit_label, 2, 2, 1, 1)

        self.name_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.name_grid.addItem(self.name_grid_spacer, 0, 3, 1, 1)


        self.name_card_layout.addLayout(self.name_grid)

        self.checkBox_case_sensitive = QCheckBox(self.name_card)
        self.checkBox_case_sensitive.setObjectName(u"checkBox_case_sensitive")
        self.checkBox_case_sensitive.setEnabled(False)
        self.checkBox_case_sensitive.setChecked(True)

        self.name_card_layout.addWidget(self.checkBox_case_sensitive)

        self.textEdit = QLabel(self.name_card)
        self.textEdit.setObjectName(u"textEdit")
        font2 = QFont()
        font2.setPointSize(10)
        self.textEdit.setFont(font2)
        self.textEdit.setWordWrap(True)
        self.textEdit.setProperty(u"variant", u"help")

        self.name_card_layout.addWidget(self.textEdit)


        self.content_layout.addWidget(self.name_card)

        self.label_2 = QFrame(self.content_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFrameShape(QFrame.Shape.NoFrame)
        self.label_2.setProperty(u"variant", u"warning")
        self.label_2_layout = QHBoxLayout(self.label_2)
        self.label_2_layout.setObjectName(u"label_2_layout")
        self.label_2_layout.setContentsMargins(14, 10, 14, 10)
        self.label_2_label = QLabel(self.label_2)
        self.label_2_label.setObjectName(u"label_2_label")
        self.label_2_label.setTextFormat(Qt.TextFormat.RichText)
        self.label_2_label.setWordWrap(True)

        self.label_2_layout.addWidget(self.label_2_label)


        self.content_layout.addWidget(self.label_2)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TextFileAssociation)

        QMetaObject.connectSlotsByName(TextFileAssociation)
    # setupUi

    def retranslateUi(self, TextFileAssociation):
        TextFileAssociation.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("TextFileAssociation", u"Link PSG and Text file", None))
        self.subtitle_label.setText(QCoreApplication.translate("TextFileAssociation", u"Set how Snooz finds the text file of each PSG file by name.", None))
        self.label_16.setText(QCoreApplication.translate("TextFileAssociation", u"Text file names", None))
        self.label_17.setText(QCoreApplication.translate("TextFileAssociation", u"The name of the text file of a PSG file is the prefix, then the PSG file name, then the suffix, then the extension. Snooz reads the text file in the folder of the PSG file.", None))
        self.label_18.setText(QCoreApplication.translate("TextFileAssociation", u"Prefix", None))
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip(QCoreApplication.translate("TextFileAssociation", u"Optionally, define the prefix to insert before the PSG filename to identify the stages filename.", None))
#endif // QT_CONFIG(tooltip)
        self.label_19.setText(QCoreApplication.translate("TextFileAssociation", u"Suffix", None))
#if QT_CONFIG(tooltip)
        self.label_19.setToolTip(QCoreApplication.translate("TextFileAssociation", u"Optionally, define the suffix to append to the PSG filename to identify the stages filename.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("TextFileAssociation", u"Extension", None))
        self.lineEdit_ext.setText(QCoreApplication.translate("TextFileAssociation", u"tsv", None))
        self.extension_unit_label.setText(QCoreApplication.translate("TextFileAssociation", u"tsv, txt or csv", None))
#if QT_CONFIG(tooltip)
        self.checkBox_case_sensitive.setToolTip(QCoreApplication.translate("TextFileAssociation", u"Uncheck if the sleep stage filename has a different case than the EDF filename.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_case_sensitive.setText(QCoreApplication.translate("TextFileAssociation", u"Filenames are case sensitive", None))
        self.textEdit.setText(QCoreApplication.translate("TextFileAssociation", u"For example, with the prefix annot_, the suffix _expert1 and the extension tsv, the text file of subject1.edf is annot_subject1_expert1.tsv.", None))
        self.label_2_label.setText(QCoreApplication.translate("TextFileAssociation", u"<b>The text file must not have the name of the PSG file</b><br/>Otherwise Snooz reads it as the accessory file of the PSG file. To prevent processing errors, add a prefix or a suffix to the name of the text file.", None))
    # retranslateUi

