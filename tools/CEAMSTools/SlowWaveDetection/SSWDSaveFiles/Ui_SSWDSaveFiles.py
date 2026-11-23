# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SSWDSaveFiles.ui'
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

class Ui_SSWDSaveFiles(object):
    def setupUi(self, SSWDSaveFiles):
        if not SSWDSaveFiles.objectName():
            SSWDSaveFiles.setObjectName(u"SSWDSaveFiles")
        SSWDSaveFiles.resize(900, 700)
        self.verticalLayout = QVBoxLayout(SSWDSaveFiles)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(SSWDSaveFiles)
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
        self.checkBox_save_cohort = QCheckBox(self.cohort_card)
        self.checkBox_save_cohort.setObjectName(u"checkBox_save_cohort")
        font1 = QFont()
        font1.setBold(True)
        self.checkBox_save_cohort.setFont(font1)

        self.cohort_card_layout.addWidget(self.checkBox_save_cohort)

        self.cohort_file_layout = QHBoxLayout()
        self.cohort_file_layout.setSpacing(8)
        self.cohort_file_layout.setObjectName(u"cohort_file_layout")
        self.cohort_file_label = QLabel(self.cohort_card)
        self.cohort_file_label.setObjectName(u"cohort_file_label")

        self.cohort_file_layout.addWidget(self.cohort_file_label)

        self.lineEdit_cohort_report = QLineEdit(self.cohort_card)
        self.lineEdit_cohort_report.setObjectName(u"lineEdit_cohort_report")
        self.lineEdit_cohort_report.setEnabled(False)

        self.cohort_file_layout.addWidget(self.lineEdit_cohort_report)

        self.pushButto_browse = QPushButton(self.cohort_card)
        self.pushButto_browse.setObjectName(u"pushButto_browse")
        self.pushButto_browse.setEnabled(False)

        self.cohort_file_layout.addWidget(self.pushButto_browse)


        self.cohort_card_layout.addLayout(self.cohort_file_layout)

        self.label_2 = QLabel(self.cohort_card)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_2.setFont(font2)
        self.label_2.setTextFormat(Qt.TextFormat.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setProperty(u"variant", u"help")

        self.cohort_card_layout.addWidget(self.label_2)

        self.cohort_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.cohort_card_layout.addItem(self.cohort_stretch)


        self.output_cards_layout.addWidget(self.cohort_card)

        self.waves_card = QFrame(self.content_widget)
        self.waves_card.setObjectName(u"waves_card")
        self.waves_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.waves_card.setFrameShadow(QFrame.Shadow.Raised)
        self.waves_card_layout = QVBoxLayout(self.waves_card)
        self.waves_card_layout.setSpacing(10)
        self.waves_card_layout.setObjectName(u"waves_card_layout")
        self.waves_card_layout.setContentsMargins(10, 10, 10, 10)
        self.checkBox_export_sw = QCheckBox(self.waves_card)
        self.checkBox_export_sw.setObjectName(u"checkBox_export_sw")
        self.checkBox_export_sw.setFont(font1)

        self.waves_card_layout.addWidget(self.checkBox_export_sw)

        self.waves_label = QLabel(self.waves_card)
        self.waves_label.setObjectName(u"waves_label")
        self.waves_label.setWordWrap(True)
        self.waves_label.setProperty(u"variant", u"help")

        self.waves_card_layout.addWidget(self.waves_label)

        self.waves_help_label = QLabel(self.waves_card)
        self.waves_help_label.setObjectName(u"waves_help_label")
        self.waves_help_label.setFont(font2)
        self.waves_help_label.setWordWrap(True)
        self.waves_help_label.setProperty(u"variant", u"help")

        self.waves_card_layout.addWidget(self.waves_help_label)

        self.waves_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.waves_card_layout.addItem(self.waves_stretch)


        self.output_cards_layout.addWidget(self.waves_card)

        self.output_cards_layout.setStretch(0, 1)
        self.output_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.output_cards_layout)

        self.textEdit_3 = QFrame(self.content_widget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_3.setProperty(u"variant", u"info")
        self.textEdit_3_layout = QHBoxLayout(self.textEdit_3)
        self.textEdit_3_layout.setObjectName(u"textEdit_3_layout")
        self.textEdit_3_layout.setContentsMargins(14, 10, 14, 10)
        self.textEdit_3_label = QLabel(self.textEdit_3)
        self.textEdit_3_label.setObjectName(u"textEdit_3_label")
        self.textEdit_3_label.setTextFormat(Qt.TextFormat.RichText)
        self.textEdit_3_label.setWordWrap(True)

        self.textEdit_3_layout.addWidget(self.textEdit_3_label)


        self.content_layout.addWidget(self.textEdit_3)

        self.about_characteristics_layout = QVBoxLayout()
        self.about_characteristics_layout.setSpacing(6)
        self.about_characteristics_layout.setObjectName(u"about_characteristics_layout")
        self.label_title_2 = QLabel(self.content_widget)
        self.label_title_2.setObjectName(u"label_title_2")
        self.label_title_2.setFont(font1)

        self.about_characteristics_layout.addWidget(self.label_title_2)

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

        self.phase_card = QFrame(self.content_widget)
        self.phase_card.setObjectName(u"phase_card")
        self.phase_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.phase_card.setFrameShadow(QFrame.Shadow.Raised)
        self.phase_card_layout = QVBoxLayout(self.phase_card)
        self.phase_card_layout.setSpacing(10)
        self.phase_card_layout.setObjectName(u"phase_card_layout")
        self.phase_card_layout.setContentsMargins(10, 10, 10, 10)
        self.phase_image = QLabel(self.phase_card)
        self.phase_image.setObjectName(u"phase_image")

        self.phase_card_layout.addWidget(self.phase_image)

        self.phase_caption_label = QLabel(self.phase_card)
        self.phase_caption_label.setObjectName(u"phase_caption_label")
        self.phase_caption_label.setFont(font2)
        self.phase_caption_label.setWordWrap(True)
        self.phase_caption_label.setProperty(u"variant", u"help")

        self.phase_card_layout.addWidget(self.phase_caption_label)


        self.characteristics_layout.addWidget(self.phase_card)

        self.characteristics_layout.setStretch(0, 1)
        self.characteristics_layout.setStretch(1, 1)

        self.about_characteristics_layout.addLayout(self.characteristics_layout)

        self.textEdit_2 = QLabel(self.content_widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setTextFormat(Qt.TextFormat.RichText)
        self.textEdit_2.setWordWrap(True)
        self.textEdit_2.setProperty(u"variant", u"help")
        self.textEdit_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.about_characteristics_layout.addWidget(self.textEdit_2)

        self.references_layout = QVBoxLayout()
        self.references_layout.setSpacing(8)
        self.references_layout.setObjectName(u"references_layout")
        self.references_layout.setContentsMargins(0, 6, 0, 0)
        self.references_line = QFrame(self.content_widget)
        self.references_line.setObjectName(u"references_line")
        self.references_line.setFrameShape(QFrame.Shape.HLine)
        self.references_line.setFrameShadow(QFrame.Shadow.Plain)

        self.references_layout.addWidget(self.references_line)

        self.references_label = QLabel(self.content_widget)
        self.references_label.setObjectName(u"references_label")
        self.references_label.setFont(font2)
        self.references_label.setTextFormat(Qt.TextFormat.RichText)
        self.references_label.setWordWrap(True)
        self.references_label.setOpenExternalLinks(True)
        self.references_label.setProperty(u"variant", u"help")

        self.references_layout.addWidget(self.references_label)


        self.about_characteristics_layout.addLayout(self.references_layout)


        self.content_layout.addLayout(self.about_characteristics_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SSWDSaveFiles)
        self.checkBox_export_sw.clicked.connect(SSWDSaveFiles.check_export_sw_file_slot)
        self.pushButto_browse.clicked.connect(SSWDSaveFiles.browse_cohort_slot)
        self.checkBox_save_cohort.clicked.connect(SSWDSaveFiles.check_save_cohort_slot)

        QMetaObject.connectSlotsByName(SSWDSaveFiles)
    # setupUi

    def retranslateUi(self, SSWDSaveFiles):
        SSWDSaveFiles.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("SSWDSaveFiles", u"Output Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("SSWDSaveFiles", u"Choose the characteristics of the slow waves to export.", None))
        self.events_info_label.setText(QCoreApplication.translate("SSWDSaveFiles", u"<b>Slow wave events</b><br/>They are added to the accessory file (.tsv, .sts or .ent) of each PSG recording as [group, name, start_sec, duration_sec, channels].", None))
        self.checkBox_save_cohort.setText(QCoreApplication.translate("SSWDSaveFiles", u"Detailed report for the cohort", None))
        self.cohort_file_label.setText(QCoreApplication.translate("SSWDSaveFiles", u"Filename", None))
        self.lineEdit_cohort_report.setPlaceholderText(QCoreApplication.translate("SSWDSaveFiles", u"Select a .tsv file", None))
        self.pushButto_browse.setText(QCoreApplication.translate("SSWDSaveFiles", u"Choose", None))
        self.label_2.setText(QCoreApplication.translate("SSWDSaveFiles", u"The slow wave details are appended at the end of the cohort report if it exists. The number of hours and cycles reported is set in <b>Hours and Cycles</b>, under Optional settings in the left panel.", None))
        self.checkBox_export_sw.setText(QCoreApplication.translate("SSWDSaveFiles", u"Characteristics of each slow wave", None))
        self.waves_label.setText(QCoreApplication.translate("SSWDSaveFiles", u"One file per recording.", None))
        self.waves_help_label.setText(QCoreApplication.translate("SSWDSaveFiles", u"Files are saved in a new folder named \"slow_wave_characteristics\" at the cohort report level. Without cohort report, the file is saved in the same folder as the PSG file.", None))
        self.textEdit_3_label.setText(QCoreApplication.translate("SSWDSaveFiles", u"<b>Sleep stages</b><br/>When both files are exported, the sleep stages selected for the detection are also saved, one file per recording, in a new folder named \"slow_wave_sleep_stages\" at the cohort report level (recordings with sleep stages only). They are used to compute the slow wave density per division of the night. The tool Classify Slow Waves needs the three outputs.", None))
        self.label_title_2.setText(QCoreApplication.translate("SSWDSaveFiles", u"About the slow wave characteristics", None))
        self.textEdit.setText(QCoreApplication.translate("SSWDSaveFiles", u"<b>For each slow wave</b><br/>\u2022 duration (s): T<br/>\u2022 frequency (Hz): 1/T<br/>\u2022 peak-to-peak amplitude (\u00b5V): H to D<br/>\u2022 negative peak amplitude (\u00b5V): H<br/>\u2022 duration of the negative half-wave (s)<br/>\u2022 time from the onset to the negative peak (s)<br/>\u2022 duration of the positive half-wave (s)<br/>\u2022 time from the onset to the positive peak (s)<br/>\u2022 slope to the negative peak (\u00b5V/s), from the zero crossing<br/>\u2022 slope from the positive peak (\u00b5V/s), to the zero crossing<br/>\u2022 transition slope (\u00b5V/s), from H to D<br/>\u2022 transition frequency (Hz): 1/(2\u03c4)", None))
        self.phase_image.setText("")
        self.phase_caption_label.setText(QCoreApplication.translate("SSWDSaveFiles", u"Phase of a slow wave [1]: the transition from H to D is highlighted.", None))
        self.textEdit_2.setText(QCoreApplication.translate("SSWDSaveFiles", u"<b>For the cohort</b><br/>\u2022 slow wave count<br/>\u2022 slow wave density (slow waves per minute)<br/>\u2022 the average of the characteristics of the slow waves:<br/>&nbsp;&nbsp;\u2013 total (all selected stages), from the sleep onset<br/>&nbsp;&nbsp;\u2013 per sleep stage: only the time spent in each stage<br/>&nbsp;&nbsp;\u2013 per sleep cycle, from the sleep onset<br/>&nbsp;&nbsp;\u2013 per clock hour, from the sleep onset<br/>&nbsp;&nbsp;\u2013 per hour spent in each stage, from the first epoch of each stage", None))
        self.references_label.setText(QCoreApplication.translate("SSWDSaveFiles", u"[1] Bouchard, M., Lina, J.-M., Gaudreault, P.-O., Lafreni\u00e8re, A., Dub\u00e9, J., Gosselin, N., &amp; Carrier, J. (2021). Sleeping at the switch. <i>eLife</i>, <i>10</i>, Article e64337. <a href=\"https://doi.org/10.7554/eLife.64337\">https://doi.org/10.7554/eLife.64337</a>", None))
    # retranslateUi

