# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_OutputFilesStep.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_OutputFilesStep(object):
    def setupUi(self, OutputFilesStep):
        if not OutputFilesStep.objectName():
            OutputFilesStep.setObjectName(u"OutputFilesStep")
        OutputFilesStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(OutputFilesStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(OutputFilesStep)
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

        self.events_info = QFrame(self.content_widget)
        self.events_info.setObjectName(u"events_info")
        self.events_info.setFrameShape(QFrame.Shape.NoFrame)
        self.events_info.setProperty(u"variant", u"info")
        self.events_info_layout = QHBoxLayout(self.events_info)
        self.events_info_layout.setObjectName(u"events_info_layout")
        self.events_info_layout.setContentsMargins(14, 10, 14, 10)
        self.events_info_label = QLabel(self.events_info)
        self.events_info_label.setObjectName(u"events_info_label")
        self.events_info_label.setTextFormat(Qt.TextFormat.RichText)
        self.events_info_label.setWordWrap(True)

        self.events_info_layout.addWidget(self.events_info_label)


        self.content_layout.addWidget(self.events_info)

        self.output_cards_layout = QHBoxLayout()
        self.output_cards_layout.setSpacing(16)
        self.output_cards_layout.setObjectName(u"output_cards_layout")
        self.cohort_card = QFrame(self.content_widget)
        self.cohort_card.setObjectName(u"cohort_card")
        self.cohort_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.cohort_card.setFrameShadow(QFrame.Shadow.Raised)
        self.cohort_card_layout = QVBoxLayout(self.cohort_card)
        self.cohort_card_layout.setSpacing(10)
        self.cohort_card_layout.setObjectName(u"cohort_card_layout")
        self.cohort_card_layout.setContentsMargins(10, 10, 10, 10)
        self.checkBox_cohort_file = QCheckBox(self.cohort_card)
        self.checkBox_cohort_file.setObjectName(u"checkBox_cohort_file")
        font1 = QFont()
        font1.setBold(True)
        self.checkBox_cohort_file.setFont(font1)
        self.checkBox_cohort_file.setChecked(True)

        self.cohort_card_layout.addWidget(self.checkBox_cohort_file)

        self.cohort_file_layout = QHBoxLayout()
        self.cohort_file_layout.setSpacing(8)
        self.cohort_file_layout.setObjectName(u"cohort_file_layout")
        self.cohort_file_label = QLabel(self.cohort_card)
        self.cohort_file_label.setObjectName(u"cohort_file_label")

        self.cohort_file_layout.addWidget(self.cohort_file_label)

        self.cohort_lineedit = QLineEdit(self.cohort_card)
        self.cohort_lineedit.setObjectName(u"cohort_lineedit")
        self.cohort_lineedit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.cohort_file_layout.addWidget(self.cohort_lineedit)

        self.pushButton_cohort = QPushButton(self.cohort_card)
        self.pushButton_cohort.setObjectName(u"pushButton_cohort")

        self.cohort_file_layout.addWidget(self.pushButton_cohort)


        self.cohort_card_layout.addLayout(self.cohort_file_layout)

        self.label_8 = QLabel(self.cohort_card)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_8.setFont(font2)
        self.label_8.setTextFormat(Qt.TextFormat.RichText)
        self.label_8.setWordWrap(True)
        self.label_8.setProperty(u"variant", u"help")

        self.cohort_card_layout.addWidget(self.label_8)

        self.cohort_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.cohort_card_layout.addItem(self.cohort_stretch)


        self.output_cards_layout.addWidget(self.cohort_card)

        self.spindles_card = QFrame(self.content_widget)
        self.spindles_card.setObjectName(u"spindles_card")
        self.spindles_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.spindles_card.setFrameShadow(QFrame.Shadow.Raised)
        self.spindles_card_layout = QVBoxLayout(self.spindles_card)
        self.spindles_card_layout.setSpacing(10)
        self.spindles_card_layout.setObjectName(u"spindles_card_layout")
        self.spindles_card_layout.setContentsMargins(10, 10, 10, 10)
        self.checkBox_spindle_file = QCheckBox(self.spindles_card)
        self.checkBox_spindle_file.setObjectName(u"checkBox_spindle_file")
        self.checkBox_spindle_file.setFont(font1)

        self.spindles_card_layout.addWidget(self.checkBox_spindle_file)

        self.spindles_label = QLabel(self.spindles_card)
        self.spindles_label.setObjectName(u"spindles_label")
        self.spindles_label.setWordWrap(True)
        self.spindles_label.setProperty(u"variant", u"help")

        self.spindles_card_layout.addWidget(self.spindles_label)

        self.label_7 = QLabel(self.spindles_card)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setWordWrap(True)
        self.label_7.setProperty(u"variant", u"help")

        self.spindles_card_layout.addWidget(self.label_7)

        self.spindles_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.spindles_card_layout.addItem(self.spindles_stretch)


        self.output_cards_layout.addWidget(self.spindles_card)

        self.output_cards_layout.setStretch(0, 1)
        self.output_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.output_cards_layout)

        self.about_characteristics_layout = QVBoxLayout()
        self.about_characteristics_layout.setSpacing(6)
        self.about_characteristics_layout.setObjectName(u"about_characteristics_layout")
        self.label_4 = QLabel(self.content_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.about_characteristics_layout.addWidget(self.label_4)

        self.characteristics_layout = QHBoxLayout()
        self.characteristics_layout.setSpacing(16)
        self.characteristics_layout.setObjectName(u"characteristics_layout")
        self.textEdit = QLabel(self.content_widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setTextFormat(Qt.TextFormat.RichText)
        self.textEdit.setWordWrap(True)
        self.textEdit.setProperty(u"variant", u"help")
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.characteristics_layout.addWidget(self.textEdit)

        self.cohort_characteristics_label = QLabel(self.content_widget)
        self.cohort_characteristics_label.setObjectName(u"cohort_characteristics_label")
        self.cohort_characteristics_label.setTextFormat(Qt.TextFormat.RichText)
        self.cohort_characteristics_label.setWordWrap(True)
        self.cohort_characteristics_label.setProperty(u"variant", u"help")
        self.cohort_characteristics_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.characteristics_layout.addWidget(self.cohort_characteristics_label)

        self.characteristics_layout.setStretch(0, 1)
        self.characteristics_layout.setStretch(1, 1)

        self.about_characteristics_layout.addLayout(self.characteristics_layout)

        self.label_5 = QLabel(self.content_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextFormat(Qt.TextFormat.RichText)
        self.label_5.setWordWrap(True)
        self.label_5.setProperty(u"variant", u"help")

        self.about_characteristics_layout.addWidget(self.label_5)


        self.content_layout.addLayout(self.about_characteristics_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(OutputFilesStep)
        self.pushButton_cohort.clicked.connect(OutputFilesStep.browse_cohort_slot)
        self.checkBox_cohort_file.clicked.connect(OutputFilesStep.enable_cohort_slot)
        self.checkBox_spindle_file.clicked.connect(OutputFilesStep.enable_spindle_slot)

        QMetaObject.connectSlotsByName(OutputFilesStep)
    # setupUi

    def retranslateUi(self, OutputFilesStep):
        OutputFilesStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("OutputFilesStep", u"Output Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("OutputFilesStep", u"Choose the characteristics of the spindles to export.", None))
        self.events_info_label.setText(QCoreApplication.translate("OutputFilesStep", u"<b>Spindle events</b><br/>They are added to the accessory file (.tsv, .sts or .ent) as [group, name, start_sec, duration_sec, channels].", None))
        self.checkBox_cohort_file.setText(QCoreApplication.translate("OutputFilesStep", u"Detailed report for the cohort", None))
        self.cohort_file_label.setText(QCoreApplication.translate("OutputFilesStep", u"Filename", None))
        self.cohort_lineedit.setPlaceholderText(QCoreApplication.translate("OutputFilesStep", u"Select a .tsv file", None))
        self.pushButton_cohort.setText(QCoreApplication.translate("OutputFilesStep", u"Choose", None))
        self.label_8.setText(QCoreApplication.translate("OutputFilesStep", u"The spindle details are appended at the end of the cohort report if it exists. The number of hours and cycles reported is set in <b>Hours and Cycles</b>, under Optional settings in the left panel.", None))
        self.checkBox_spindle_file.setText(QCoreApplication.translate("OutputFilesStep", u"Characteristics of each spindle", None))
        self.spindles_label.setText(QCoreApplication.translate("OutputFilesStep", u"One file per recording.", None))
        self.label_7.setText(QCoreApplication.translate("OutputFilesStep", u"Files are saved in a new folder named \"spindles_characteristics\" at the cohort report level. Without cohort report, the file is saved in the same folder as the PSG file.", None))
        self.label_4.setText(QCoreApplication.translate("OutputFilesStep", u"About the spindle characteristics", None))
        self.textEdit.setText(QCoreApplication.translate("OutputFilesStep", u"<b>For each spindle</b><br/>\u2022 duration (s)<br/>\u2022 dominant frequency (Hz), where the spectral energy is maximum<br/>\u2022 average frequency (Hz), counting peaks<br/>\u2022 peak-to-peak amplitude (\u00b5V)<br/>\u2022 duration from the onset to the maximum peak-to-peak amplitude (s)<br/>\u2022 root mean square (RMS) amplitude (\u00b5V)<br/>\u2022 RMS-duration product (\u00b5V\u00b7s)", None))
        self.cohort_characteristics_label.setText(QCoreApplication.translate("OutputFilesStep", u"<b>For the cohort</b><br/>\u2022 spindle count<br/>\u2022 spindle density (spindles per minute)<br/>\u2022 the average of the characteristics of the spindles:<br/>&nbsp;&nbsp;\u2013 total (all selected stages), from the sleep onset<br/>&nbsp;&nbsp;\u2013 per sleep stage: only the time spent in each stage<br/>&nbsp;&nbsp;\u2013 per sleep cycle, from the sleep onset<br/>&nbsp;&nbsp;\u2013 per clock hour, from the sleep onset<br/>&nbsp;&nbsp;\u2013 per hour spent in each stage, from the first epoch of each stage", None))
        self.label_5.setText(QCoreApplication.translate("OutputFilesStep", u"RSAI (RMS spindle activity index) is the <b>sum</b> of the RMS-duration products of all the spindles. The other characteristics are averages.", None))
    # retranslateUi

