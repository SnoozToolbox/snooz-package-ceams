# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ExportResultsStep.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_ExportResultsStep(object):
    def setupUi(self, ExportResultsStep):
        if not ExportResultsStep.objectName():
            ExportResultsStep.setObjectName(u"ExportResultsStep")
        ExportResultsStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(ExportResultsStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(ExportResultsStep)
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

        self.scoring_card = QFrame(self.content_widget)
        self.scoring_card.setObjectName(u"scoring_card")
        self.scoring_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.scoring_card.setFrameShadow(QFrame.Shadow.Raised)
        self.scoring_card_layout = QVBoxLayout(self.scoring_card)
        self.scoring_card_layout.setSpacing(10)
        self.scoring_card_layout.setObjectName(u"scoring_card_layout")
        self.scoring_card_layout.setContentsMargins(10, 10, 10, 10)
        self.checkBox = QCheckBox(self.scoring_card)
        self.checkBox.setObjectName(u"checkBox")
        font1 = QFont()
        font1.setBold(True)
        self.checkBox.setFont(font1)
        self.checkBox.setChecked(True)

        self.scoring_card_layout.addWidget(self.checkBox)

        self.label_3 = QLabel(self.scoring_card)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_3.setFont(font2)
        self.label_3.setWordWrap(True)
        self.label_3.setIndent(26)
        self.label_3.setProperty(u"variant", u"help")

        self.scoring_card_layout.addWidget(self.label_3)

        self.group_grid = QGridLayout()
        self.group_grid.setObjectName(u"group_grid")
        self.group_grid.setHorizontalSpacing(12)
        self.group_grid.setVerticalSpacing(10)
        self.label_2 = QLabel(self.scoring_card)
        self.label_2.setObjectName(u"label_2")

        self.group_grid.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.scoring_card)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(500, 16777215))

        self.group_grid.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.group_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.group_grid.addItem(self.group_grid_spacer, 0, 3, 1, 1)


        self.scoring_card_layout.addLayout(self.group_grid)

        self.group_help_label = QLabel(self.scoring_card)
        self.group_help_label.setObjectName(u"group_help_label")
        self.group_help_label.setFont(font2)
        self.group_help_label.setWordWrap(True)
        self.group_help_label.setProperty(u"variant", u"help")

        self.scoring_card_layout.addWidget(self.group_help_label)

        self.scoring_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.scoring_card_layout.addItem(self.scoring_stretch)


        self.content_layout.addWidget(self.scoring_card)

        self.compare_card = QFrame(self.content_widget)
        self.compare_card.setObjectName(u"compare_card")
        self.compare_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.compare_card.setFrameShadow(QFrame.Shadow.Raised)
        self.compare_card_layout = QVBoxLayout(self.compare_card)
        self.compare_card_layout.setSpacing(10)
        self.compare_card_layout.setObjectName(u"compare_card_layout")
        self.compare_card_layout.setContentsMargins(10, 10, 10, 10)
        self.checkBox_2 = QCheckBox(self.compare_card)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font1)

        self.compare_card_layout.addWidget(self.checkBox_2)

        self.frame_9 = QFrame(self.compare_card)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9_layout = QVBoxLayout(self.frame_9)
        self.frame_9_layout.setSpacing(6)
        self.frame_9_layout.setObjectName(u"frame_9_layout")
        self.frame_9_layout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)
        self.label_4.setProperty(u"variant", u"help")

        self.frame_9_layout.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setTextFormat(Qt.TextFormat.RichText)
        self.label_5.setWordWrap(True)
        self.label_5.setProperty(u"variant", u"help")

        self.frame_9_layout.addWidget(self.label_5)


        self.compare_card_layout.addWidget(self.frame_9)

        self.frame_6 = QFrame(self.compare_card)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6_layout = QVBoxLayout(self.frame_6)
        self.frame_6_layout.setSpacing(8)
        self.frame_6_layout.setObjectName(u"frame_6_layout")
        self.frame_6_layout.setContentsMargins(0, 0, 0, 0)
        self.folder_layout = QHBoxLayout()
        self.folder_layout.setSpacing(8)
        self.folder_layout.setObjectName(u"folder_layout")
        self.folder_label = QLabel(self.frame_6)
        self.folder_label.setObjectName(u"folder_label")

        self.folder_layout.addWidget(self.folder_label)

        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")

        self.folder_layout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(500, 16777215))

        self.folder_layout.addWidget(self.pushButton)


        self.frame_6_layout.addLayout(self.folder_layout)


        self.compare_card_layout.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.compare_card)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8_layout = QVBoxLayout(self.frame_8)
        self.frame_8_layout.setSpacing(8)
        self.frame_8_layout.setObjectName(u"frame_8_layout")
        self.frame_8_layout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setWordWrap(True)
        self.label_6.setProperty(u"variant", u"help")

        self.frame_8_layout.addWidget(self.label_6)


        self.compare_card_layout.addWidget(self.frame_8)

        self.compare_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.compare_card_layout.addItem(self.compare_stretch)


        self.content_layout.addWidget(self.compare_card)

        self.stage_group_warning = QFrame(self.content_widget)
        self.stage_group_warning.setObjectName(u"stage_group_warning")
        self.stage_group_warning.setFrameShape(QFrame.Shape.NoFrame)
        self.stage_group_warning.setProperty(u"variant", u"warning")
        self.stage_group_warning_layout = QHBoxLayout(self.stage_group_warning)
        self.stage_group_warning_layout.setObjectName(u"stage_group_warning_layout")
        self.stage_group_warning_layout.setContentsMargins(14, 10, 14, 10)
        self.stage_group_warning_label = QLabel(self.stage_group_warning)
        self.stage_group_warning_label.setObjectName(u"stage_group_warning_label")
        self.stage_group_warning_label.setTextFormat(Qt.TextFormat.RichText)
        self.stage_group_warning_label.setWordWrap(True)

        self.stage_group_warning_layout.addWidget(self.stage_group_warning_label)


        self.content_layout.addWidget(self.stage_group_warning)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ExportResultsStep)

        QMetaObject.connectSlotsByName(ExportResultsStep)
    # setupUi

    def retranslateUi(self, ExportResultsStep):
        ExportResultsStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("ExportResultsStep", u"Export Scoring", None))
        self.subtitle_label.setText(QCoreApplication.translate("ExportResultsStep", u"Define where the predicted sleep stages are saved. Optionally, compare them with the expert scoring.", None))
        self.checkBox.setText(QCoreApplication.translate("ExportResultsStep", u"Automatic scoring", None))
        self.label_3.setText(QCoreApplication.translate("ExportResultsStep", u"Always on: the predicted sleep stages are added to the accessory file, and a hypnodensity plot (PDF) of each recording is saved next to its PSG file.", None))
        self.label_2.setText(QCoreApplication.translate("ExportResultsStep", u"Group", None))
        self.lineEdit_2.setText(QCoreApplication.translate("ExportResultsStep", u"stage", None))
        self.group_help_label.setText(QCoreApplication.translate("ExportResultsStep", u"The group of the predicted sleep stages in the accessory file (default: stage).", None))
        self.checkBox_2.setText(QCoreApplication.translate("ExportResultsStep", u"Compare with the expert scoring", None))
        self.label_4.setText(QCoreApplication.translate("ExportResultsStep", u"The expert sleep stages must be in the accessory file (such as the .tsv file of an EDF file) before running this tool.", None))
        self.label_5.setText(QCoreApplication.translate("ExportResultsStep", u"Expert sleep stages: group <b>stage</b>, names 0 (W), 1 (N1), 2 (N2), 3 (N3), 5 (R) and 9 (unscored).", None))
        self.folder_label.setText(QCoreApplication.translate("ExportResultsStep", u"Folder", None))
        self.pushButton.setText(QCoreApplication.translate("ExportResultsStep", u"Choose", None))
        self.label_6.setText(QCoreApplication.translate("ExportResultsStep", u"Saved in this folder: for each recording, a PDF with the expert and predicted hypnograms, the confusion matrix, the accuracy, the average confidence and Cohen's kappa, and the hypnodensity plot; for the cohort, the accuracy, average confidence and kappa of each recording in YASA_sleep_staging_metrics_cohort_report.tsv.", None))
        self.stage_group_warning_label.setText(QCoreApplication.translate("ExportResultsStep", u"<b>Group of the sleep stages</b><br/>The other tools of Snooz find the sleep stages in the group <b>stage</b>: with another group, they may not find the predicted sleep stages. With <b>stage</b>, the predicted sleep stages replace the sleep stages of the accessory file.", None))
    # retranslateUi

