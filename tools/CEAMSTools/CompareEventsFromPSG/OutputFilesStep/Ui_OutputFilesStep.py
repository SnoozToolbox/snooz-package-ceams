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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
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

        self.settings_cards_layout = QHBoxLayout()
        self.settings_cards_layout.setSpacing(16)
        self.settings_cards_layout.setObjectName(u"settings_cards_layout")
        self.stages_card = QFrame(self.content_widget)
        self.stages_card.setObjectName(u"stages_card")
        self.stages_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.stages_card.setFrameShadow(QFrame.Shadow.Raised)
        self.stages_card_layout = QVBoxLayout(self.stages_card)
        self.stages_card_layout.setSpacing(10)
        self.stages_card_layout.setObjectName(u"stages_card_layout")
        self.stages_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_5 = QLabel(self.stages_card)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setBold(True)
        self.label_5.setFont(font1)

        self.stages_card_layout.addWidget(self.label_5)

        self.stages_help_label = QLabel(self.stages_card)
        self.stages_help_label.setObjectName(u"stages_help_label")
        self.stages_help_label.setWordWrap(True)
        self.stages_help_label.setProperty(u"variant", u"help")

        self.stages_card_layout.addWidget(self.stages_help_label)

        self.stages_layout = QHBoxLayout()
        self.stages_layout.setSpacing(18)
        self.stages_layout.setObjectName(u"stages_layout")
        self.checkBox_W = QCheckBox(self.stages_card)
        self.checkBox_W.setObjectName(u"checkBox_W")

        self.stages_layout.addWidget(self.checkBox_W)

        self.checkBox_1 = QCheckBox(self.stages_card)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setChecked(False)

        self.stages_layout.addWidget(self.checkBox_1)

        self.checkBox_2 = QCheckBox(self.stages_card)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.stages_layout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.stages_card)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)

        self.stages_layout.addWidget(self.checkBox_3)

        self.checkBox_R = QCheckBox(self.stages_card)
        self.checkBox_R.setObjectName(u"checkBox_R")

        self.stages_layout.addWidget(self.checkBox_R)

        self.checkBox_4 = QCheckBox(self.stages_card)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(False)

        self.stages_layout.addWidget(self.checkBox_4)

        self.stages_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.stages_layout.addItem(self.stages_spacer)


        self.stages_card_layout.addLayout(self.stages_layout)

        self.stages_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.stages_card_layout.addItem(self.stages_stretch)


        self.settings_cards_layout.addWidget(self.stages_card)

        self.evaluation_card = QFrame(self.content_widget)
        self.evaluation_card.setObjectName(u"evaluation_card")
        self.evaluation_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.evaluation_card.setFrameShadow(QFrame.Shadow.Raised)
        self.evaluation_card_layout = QVBoxLayout(self.evaluation_card)
        self.evaluation_card_layout.setSpacing(10)
        self.evaluation_card_layout.setObjectName(u"evaluation_card_layout")
        self.evaluation_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.evaluation_card)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.evaluation_card_layout.addWidget(self.label)

        self.jaccard_grid = QGridLayout()
        self.jaccard_grid.setObjectName(u"jaccard_grid")
        self.jaccard_grid.setHorizontalSpacing(12)
        self.jaccard_grid.setVerticalSpacing(10)
        self.label_2 = QLabel(self.evaluation_card)
        self.label_2.setObjectName(u"label_2")

        self.jaccard_grid.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_jaccord = QLineEdit(self.evaluation_card)
        self.lineEdit_jaccord.setObjectName(u"lineEdit_jaccord")

        self.jaccard_grid.addWidget(self.lineEdit_jaccord, 0, 1, 1, 1)

        self.jaccard_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.jaccard_grid.addItem(self.jaccard_grid_spacer, 0, 3, 1, 1)


        self.evaluation_card_layout.addLayout(self.jaccard_grid)

        self.textEdit = QLabel(self.evaluation_card)
        self.textEdit.setObjectName(u"textEdit")
        font2 = QFont()
        font2.setPointSize(10)
        self.textEdit.setFont(font2)
        self.textEdit.setWordWrap(True)
        self.textEdit.setProperty(u"variant", u"help")

        self.evaluation_card_layout.addWidget(self.textEdit)

        self.evaluation_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.evaluation_card_layout.addItem(self.evaluation_stretch)


        self.settings_cards_layout.addWidget(self.evaluation_card)

        self.settings_cards_layout.setStretch(0, 1)
        self.settings_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.settings_cards_layout)

        self.output_card = QFrame(self.content_widget)
        self.output_card.setObjectName(u"output_card")
        self.output_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.output_card.setFrameShadow(QFrame.Shadow.Raised)
        self.output_card_layout = QVBoxLayout(self.output_card)
        self.output_card_layout.setSpacing(10)
        self.output_card_layout.setObjectName(u"output_card_layout")
        self.output_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_3 = QLabel(self.output_card)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.output_card_layout.addWidget(self.label_3)

        self.suffix_grid = QGridLayout()
        self.suffix_grid.setObjectName(u"suffix_grid")
        self.suffix_grid.setHorizontalSpacing(12)
        self.suffix_grid.setVerticalSpacing(10)
        self.label_4 = QLabel(self.output_card)
        self.label_4.setObjectName(u"label_4")

        self.suffix_grid.addWidget(self.label_4, 0, 0, 1, 1)

        self.lineEdit_suffix = QLineEdit(self.output_card)
        self.lineEdit_suffix.setObjectName(u"lineEdit_suffix")

        self.suffix_grid.addWidget(self.lineEdit_suffix, 0, 1, 1, 1)

        self.suffix_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.suffix_grid.addItem(self.suffix_grid_spacer, 0, 3, 1, 1)


        self.output_card_layout.addLayout(self.suffix_grid)

        self.textEdit_2 = QLabel(self.output_card)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setFont(font2)
        self.textEdit_2.setWordWrap(True)
        self.textEdit_2.setProperty(u"variant", u"help")

        self.output_card_layout.addWidget(self.textEdit_2)


        self.content_layout.addWidget(self.output_card)

        self.extra_card = QFrame(self.content_widget)
        self.extra_card.setObjectName(u"extra_card")
        self.extra_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.extra_card.setFrameShadow(QFrame.Shadow.Raised)
        self.extra_card_layout = QVBoxLayout(self.extra_card)
        self.extra_card_layout.setSpacing(10)
        self.extra_card_layout.setObjectName(u"extra_card_layout")
        self.extra_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_title = QLabel(self.extra_card)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setFont(font1)

        self.extra_card_layout.addWidget(self.label_title)

        self.extra_layout = QVBoxLayout()
        self.extra_layout.setSpacing(8)
        self.extra_layout.setObjectName(u"extra_layout")
        self.extra_layout_1_layout = QVBoxLayout()
        self.extra_layout_1_layout.setSpacing(2)
        self.extra_layout_1_layout.setObjectName(u"extra_layout_1_layout")
        self.checkBox_TP_exp = QCheckBox(self.extra_card)
        self.checkBox_TP_exp.setObjectName(u"checkBox_TP_exp")

        self.extra_layout_1_layout.addWidget(self.checkBox_TP_exp)

        self.label_6 = QLabel(self.extra_card)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setWordWrap(True)
        self.label_6.setIndent(26)
        self.label_6.setProperty(u"variant", u"help")

        self.extra_layout_1_layout.addWidget(self.label_6)


        self.extra_layout.addLayout(self.extra_layout_1_layout)

        self.extra_layout_line_1 = QFrame(self.extra_card)
        self.extra_layout_line_1.setObjectName(u"extra_layout_line_1")
        self.extra_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.extra_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.extra_layout.addWidget(self.extra_layout_line_1)

        self.extra_layout_2_layout = QVBoxLayout()
        self.extra_layout_2_layout.setSpacing(2)
        self.extra_layout_2_layout.setObjectName(u"extra_layout_2_layout")
        self.checkBox_FPFN_exp = QCheckBox(self.extra_card)
        self.checkBox_FPFN_exp.setObjectName(u"checkBox_FPFN_exp")

        self.extra_layout_2_layout.addWidget(self.checkBox_FPFN_exp)

        self.label_7 = QLabel(self.extra_card)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setWordWrap(True)
        self.label_7.setIndent(26)
        self.label_7.setProperty(u"variant", u"help")

        self.extra_layout_2_layout.addWidget(self.label_7)


        self.extra_layout.addLayout(self.extra_layout_2_layout)


        self.extra_card_layout.addLayout(self.extra_layout)


        self.content_layout.addWidget(self.extra_card)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(OutputFilesStep)

        QMetaObject.connectSlotsByName(OutputFilesStep)
    # setupUi

    def retranslateUi(self, OutputFilesStep):
        OutputFilesStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("OutputFilesStep", u"Output File", None))
        self.subtitle_label.setText(QCoreApplication.translate("OutputFilesStep", u"Define the output parameters: the sleep stages in which the events are compared, the threshold of the evaluation and the output files.", None))
        self.label_5.setText(QCoreApplication.translate("OutputFilesStep", u"Sleep stages", None))
        self.stages_help_label.setText(QCoreApplication.translate("OutputFilesStep", u"The events are compared in the selected stages (e.g. N2 for sleep spindles).", None))
        self.checkBox_W.setText(QCoreApplication.translate("OutputFilesStep", u"Wake", None))
        self.checkBox_1.setText(QCoreApplication.translate("OutputFilesStep", u"N1", None))
        self.checkBox_2.setText(QCoreApplication.translate("OutputFilesStep", u"N2", None))
        self.checkBox_3.setText(QCoreApplication.translate("OutputFilesStep", u"N3", None))
        self.checkBox_R.setText(QCoreApplication.translate("OutputFilesStep", u"R", None))
        self.checkBox_4.setText(QCoreApplication.translate("OutputFilesStep", u"Stage 4", None))
        self.label.setText(QCoreApplication.translate("OutputFilesStep", u"Performance evaluation", None))
        self.label_2.setText(QCoreApplication.translate("OutputFilesStep", u"Jaccard index threshold", None))
        self.textEdit.setText(QCoreApplication.translate("OutputFilesStep", u"A detection is a true positive when its Jaccard index with an expert event, (intersection) / (union), exceeds this threshold. Only one detection can match an event: the one with the highest Jaccard index.", None))
        self.label_3.setText(QCoreApplication.translate("OutputFilesStep", u"Output file", None))
        self.label_4.setText(QCoreApplication.translate("OutputFilesStep", u"Suffix", None))
        self.lineEdit_suffix.setPlaceholderText(QCoreApplication.translate("OutputFilesStep", u"_perf", None))
        self.textEdit_2.setText(QCoreApplication.translate("OutputFilesStep", u"Written in the folder of the PSG file, named as the PSG file with this suffix and the extension .tsv. One file per PSG file, with the performance in the samples and the events domains: one column per channel, one row per metric.", None))
        self.label_title.setText(QCoreApplication.translate("OutputFilesStep", u"Additional output files", None))
        self.checkBox_TP_exp.setText(QCoreApplication.translate("OutputFilesStep", u"Export the true positive (TP) events", None))
        self.label_6.setText(QCoreApplication.translate("OutputFilesStep", u"The detected events that match the expert scoring. The file is named with the suffix TP.", None))
        self.checkBox_FPFN_exp.setText(QCoreApplication.translate("OutputFilesStep", u"Export the false negative (FN) and false positive (FP) events", None))
        self.label_7.setText(QCoreApplication.translate("OutputFilesStep", u"The expert events missed and the false detections. The file is named with the suffix FNFP.", None))
    # retranslateUi

