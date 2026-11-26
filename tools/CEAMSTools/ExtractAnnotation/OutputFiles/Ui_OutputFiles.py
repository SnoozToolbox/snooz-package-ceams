# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_OutputFiles.ui'
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

class Ui_OutputFiles(object):
    def setupUi(self, OutputFiles):
        if not OutputFiles.objectName():
            OutputFiles.setObjectName(u"OutputFiles")
        OutputFiles.resize(900, 700)
        self.verticalLayout = QVBoxLayout(OutputFiles)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(OutputFiles)
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

        self.output_card = QFrame(self.content_widget)
        self.output_card.setObjectName(u"output_card")
        self.output_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.output_card.setFrameShadow(QFrame.Shadow.Raised)
        self.output_card_layout = QVBoxLayout(self.output_card)
        self.output_card_layout.setSpacing(10)
        self.output_card_layout.setObjectName(u"output_card_layout")
        self.output_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.output_card)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)

        self.output_card_layout.addWidget(self.label)

        self.label_6 = QLabel(self.output_card)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)
        self.label_6.setProperty(u"variant", u"help")

        self.output_card_layout.addWidget(self.label_6)

        self.suffix_grid = QGridLayout()
        self.suffix_grid.setObjectName(u"suffix_grid")
        self.suffix_grid.setHorizontalSpacing(12)
        self.suffix_grid.setVerticalSpacing(10)
        self.label_2 = QLabel(self.output_card)
        self.label_2.setObjectName(u"label_2")

        self.suffix_grid.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_suffix = QLineEdit(self.output_card)
        self.lineEdit_suffix.setObjectName(u"lineEdit_suffix")

        self.suffix_grid.addWidget(self.lineEdit_suffix, 0, 1, 1, 1)

        self.suffix_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.suffix_grid.addItem(self.suffix_grid_spacer, 0, 3, 1, 1)


        self.output_card_layout.addLayout(self.suffix_grid)

        self.checkBox_time = QCheckBox(self.output_card)
        self.checkBox_time.setObjectName(u"checkBox_time")
        self.checkBox_time.setChecked(True)

        self.output_card_layout.addWidget(self.checkBox_time)


        self.content_layout.addWidget(self.output_card)

        self.label_8 = QFrame(self.content_widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFrameShape(QFrame.Shape.NoFrame)
        self.label_8.setProperty(u"variant", u"warning")
        self.label_8_layout = QHBoxLayout(self.label_8)
        self.label_8_layout.setObjectName(u"label_8_layout")
        self.label_8_layout.setContentsMargins(14, 10, 14, 10)
        self.label_8_label = QLabel(self.label_8)
        self.label_8_label.setObjectName(u"label_8_label")
        self.label_8_label.setTextFormat(Qt.TextFormat.RichText)
        self.label_8_label.setWordWrap(True)

        self.label_8_layout.addWidget(self.label_8_label)


        self.content_layout.addWidget(self.label_8)

        self.about_output_layout = QVBoxLayout()
        self.about_output_layout.setSpacing(6)
        self.about_output_layout.setObjectName(u"about_output_layout")
        self.about_output_title_label = QLabel(self.content_widget)
        self.about_output_title_label.setObjectName(u"about_output_title_label")
        self.about_output_title_label.setFont(font1)

        self.about_output_layout.addWidget(self.about_output_title_label)

        self.about_output_label = QLabel(self.content_widget)
        self.about_output_label.setObjectName(u"about_output_label")
        self.about_output_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_output_label.setWordWrap(True)
        self.about_output_label.setProperty(u"variant", u"help")

        self.about_output_layout.addWidget(self.about_output_label)


        self.content_layout.addLayout(self.about_output_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(OutputFiles)

        QMetaObject.connectSlotsByName(OutputFiles)
    # setupUi

    def retranslateUi(self, OutputFiles):
        OutputFiles.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("OutputFiles", u"Output Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("OutputFiles", u"Choose the name of the output files and their content.", None))
        self.label.setText(QCoreApplication.translate("OutputFiles", u"Output file", None))
        self.label_6.setText(QCoreApplication.translate("OutputFiles", u"The output file is written in the folder of the PSG file. Its name is the PSG file name, then the suffix and the extension .tsv.", None))
        self.label_2.setText(QCoreApplication.translate("OutputFiles", u"Suffix", None))
        self.lineEdit_suffix.setPlaceholderText(QCoreApplication.translate("OutputFiles", u"_annot", None))
        self.checkBox_time.setText(QCoreApplication.translate("OutputFiles", u"Add the time elapsed (HH:MM:SS) since the start of the recording", None))
        self.label_8_label.setText(QCoreApplication.translate("OutputFiles", u"<b>Existing files are replaced</b><br/>The output file is written in the folder of the PSG file, named after it with the suffix. A file with that name is replaced. Without a suffix, the output file of an EDF recording is its Snooz accessory file (.tsv), which is replaced by the extracted annotations.", None))
        self.about_output_title_label.setText(QCoreApplication.translate("OutputFiles", u"About the output file", None))
        self.about_output_label.setText(QCoreApplication.translate("OutputFiles", u"The output file has these columns.<br/>\u2022 group is the category of the annotation, for example artifact. Annotations with different names can be in the same group.<br/>\u2022 name is the text label of the annotation, for example art_snooz.<br/>\u2022 start_sec is the onset of the annotation in seconds, for example 300.<br/>\u2022 duration_sec is the duration of the annotation in seconds, for example 30.<br/>\u2022 channels is the list of channels of the annotation, for example ['LOC', 'ROC'].<br/>\u2022 time elapsed (HH:MM:SS) is optional. It is the time elapsed since the start of the PSG recording.", None))
    # retranslateUi

