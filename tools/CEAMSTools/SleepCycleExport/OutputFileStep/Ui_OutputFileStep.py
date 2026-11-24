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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_OutputFileStep(object):
    def setupUi(self, OutputFileStep):
        if not OutputFileStep.objectName():
            OutputFileStep.setObjectName(u"OutputFileStep")
        OutputFileStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(OutputFileStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(OutputFileStep)
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
        self.label_6 = QLabel(self.cohort_card)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setBold(True)
        self.label_6.setFont(font1)

        self.cohort_card_layout.addWidget(self.label_6)

        self.label_2 = QLabel(self.cohort_card)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)
        self.label_2.setProperty(u"variant", u"help")

        self.cohort_card_layout.addWidget(self.label_2)

        self.cohort_file_layout = QHBoxLayout()
        self.cohort_file_layout.setSpacing(8)
        self.cohort_file_layout.setObjectName(u"cohort_file_layout")
        self.label = QLabel(self.cohort_card)
        self.label.setObjectName(u"label")

        self.cohort_file_layout.addWidget(self.label)

        self.tsv_file_lineEdit = QLineEdit(self.cohort_card)
        self.tsv_file_lineEdit.setObjectName(u"tsv_file_lineEdit")

        self.cohort_file_layout.addWidget(self.tsv_file_lineEdit)

        self.choose_pushButton = QPushButton(self.cohort_card)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.cohort_file_layout.addWidget(self.choose_pushButton)


        self.cohort_card_layout.addLayout(self.cohort_file_layout)

        self.label_5 = QLabel(self.cohort_card)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_5.setFont(font2)
        self.label_5.setWordWrap(True)
        self.label_5.setProperty(u"variant", u"help")

        self.cohort_card_layout.addWidget(self.label_5)

        self.cohort_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.cohort_card_layout.addItem(self.cohort_stretch)


        self.output_cards_layout.addWidget(self.cohort_card)

        self.hypnogram_card = QFrame(self.content_widget)
        self.hypnogram_card.setObjectName(u"hypnogram_card")
        self.hypnogram_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.hypnogram_card.setFrameShadow(QFrame.Shadow.Raised)
        self.hypnogram_card_layout = QVBoxLayout(self.hypnogram_card)
        self.hypnogram_card_layout.setSpacing(10)
        self.hypnogram_card_layout.setObjectName(u"hypnogram_card_layout")
        self.hypnogram_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_7 = QLabel(self.hypnogram_card)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.hypnogram_card_layout.addWidget(self.label_7)

        self.label_3 = QLabel(self.hypnogram_card)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)
        self.label_3.setProperty(u"variant", u"help")

        self.hypnogram_card_layout.addWidget(self.label_3)

        self.suffix_layout = QHBoxLayout()
        self.suffix_layout.setSpacing(8)
        self.suffix_layout.setObjectName(u"suffix_layout")
        self.label_4 = QLabel(self.hypnogram_card)
        self.label_4.setObjectName(u"label_4")

        self.suffix_layout.addWidget(self.label_4)

        self.Hyp_suffix_lineEdit = QLineEdit(self.hypnogram_card)
        self.Hyp_suffix_lineEdit.setObjectName(u"Hyp_suffix_lineEdit")

        self.suffix_layout.addWidget(self.Hyp_suffix_lineEdit)


        self.hypnogram_card_layout.addLayout(self.suffix_layout)

        self.label_9 = QLabel(self.hypnogram_card)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setWordWrap(True)
        self.label_9.setProperty(u"variant", u"help")

        self.hypnogram_card_layout.addWidget(self.label_9)

        self.hypnogram_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.hypnogram_card_layout.addItem(self.hypnogram_stretch)


        self.output_cards_layout.addWidget(self.hypnogram_card)

        self.output_cards_layout.setStretch(0, 1)
        self.output_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.output_cards_layout)

        self.each_card = QFrame(self.content_widget)
        self.each_card.setObjectName(u"each_card")
        self.each_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.each_card.setFrameShadow(QFrame.Shadow.Raised)
        self.each_card_layout = QVBoxLayout(self.each_card)
        self.each_card_layout.setSpacing(10)
        self.each_card_layout.setObjectName(u"each_card_layout")
        self.each_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_15 = QLabel(self.each_card)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.each_card_layout.addWidget(self.label_15)

        self.each_help_label = QLabel(self.each_card)
        self.each_help_label.setObjectName(u"each_help_label")
        self.each_help_label.setWordWrap(True)
        self.each_help_label.setProperty(u"variant", u"help")

        self.each_card_layout.addWidget(self.each_help_label)

        self.each_layout = QVBoxLayout()
        self.each_layout.setSpacing(8)
        self.each_layout.setObjectName(u"each_layout")
        self.each_layout_1_layout = QVBoxLayout()
        self.each_layout_1_layout.setSpacing(2)
        self.each_layout_1_layout.setObjectName(u"each_layout_1_layout")
        self.label_11 = QLabel(self.each_card)
        self.label_11.setObjectName(u"label_11")

        self.each_layout_1_layout.addWidget(self.label_11)

        self.label_13 = QLabel(self.each_card)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setWordWrap(True)
        self.label_13.setProperty(u"variant", u"help")

        self.each_layout_1_layout.addWidget(self.label_13)


        self.each_layout.addLayout(self.each_layout_1_layout)

        self.each_layout_line_1 = QFrame(self.each_card)
        self.each_layout_line_1.setObjectName(u"each_layout_line_1")
        self.each_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.each_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.each_layout.addWidget(self.each_layout_line_1)

        self.each_layout_2_layout = QVBoxLayout()
        self.each_layout_2_layout.setSpacing(2)
        self.each_layout_2_layout.setObjectName(u"each_layout_2_layout")
        self.label_8 = QLabel(self.each_card)
        self.label_8.setObjectName(u"label_8")

        self.each_layout_2_layout.addWidget(self.label_8)

        self.label_10 = QLabel(self.each_card)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setWordWrap(True)
        self.label_10.setProperty(u"variant", u"help")

        self.each_layout_2_layout.addWidget(self.label_10)


        self.each_layout.addLayout(self.each_layout_2_layout)


        self.each_card_layout.addLayout(self.each_layout)


        self.content_layout.addWidget(self.each_card)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(OutputFileStep)
        self.choose_pushButton.clicked.connect(OutputFileStep.choose_slot1)

        QMetaObject.connectSlotsByName(OutputFileStep)
    # setupUi

    def retranslateUi(self, OutputFileStep):
        OutputFileStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("OutputFileStep", u"Output Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("OutputFileStep", u"Define where the files are saved: the sleep cycles of the cohort and the hypnogram of each recording.", None))
        self.label_6.setText(QCoreApplication.translate("OutputFileStep", u"Cohort report (.tsv)", None))
        self.label_2.setText(QCoreApplication.translate("OutputFileStep", u"Lists the start time and duration (s) of each NREM and REM period across all recordings.", None))
        self.label.setText(QCoreApplication.translate("OutputFileStep", u"Filename", None))
        self.tsv_file_lineEdit.setPlaceholderText(QCoreApplication.translate("OutputFileStep", u"Select a .tsv file", None))
        self.tsv_file_lineEdit.setText("")
        self.choose_pushButton.setText(QCoreApplication.translate("OutputFileStep", u"Choose", None))
        self.label_5.setText(QCoreApplication.translate("OutputFileStep", u"The cycles are appended at the end of the file if it exists.", None))
        self.label_7.setText(QCoreApplication.translate("OutputFileStep", u"Hypnogram images (.pdf)", None))
        self.label_3.setText(QCoreApplication.translate("OutputFileStep", u"One image per recording, with its sleep cycles.", None))
        self.label_4.setText(QCoreApplication.translate("OutputFileStep", u"Suffix", None))
        self.Hyp_suffix_lineEdit.setPlaceholderText(QCoreApplication.translate("OutputFileStep", u"Example: _hyp", None))
        self.label_9.setText(QCoreApplication.translate("OutputFileStep", u"Saved in the folder of the cohort report, named after the report and the recording, then the suffix (for example: cycles_learn-nsrr01_hyp.pdf). Without an extension, .pdf is added. PNG is also supported.", None))
        self.label_15.setText(QCoreApplication.translate("OutputFileStep", u"Saved next to each PSG file", None))
        self.each_help_label.setText(QCoreApplication.translate("OutputFileStep", u"Named after the PSG file, with a suffix.", None))
        self.label_11.setText(QCoreApplication.translate("OutputFileStep", u"Sleep stages and periods (.tsv)", None))
        self.label_13.setText(QCoreApplication.translate("OutputFileStep", u"The sleep stages and the NREM and REM periods of the recording. Suffix: \"_stage_cycle.tsv\".", None))
        self.label_8.setText(QCoreApplication.translate("OutputFileStep", u"Log file (.txt)", None))
        self.label_10.setText(QCoreApplication.translate("OutputFileStep", u"The warnings encountered during the sleep cycle delimitation, such as a REM period fusion or a sleep onset in REM period (SOREMP). Suffix: \"_Cycle_WARNING.txt\". Written only when there are warnings.", None))
    # retranslateUi

