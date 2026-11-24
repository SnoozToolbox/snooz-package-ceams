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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
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

        self.cohort_card = QFrame(self.content_widget)
        self.cohort_card.setObjectName(u"cohort_card")
        self.cohort_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.cohort_card.setFrameShadow(QFrame.Shadow.Raised)
        self.cohort_card_layout = QVBoxLayout(self.cohort_card)
        self.cohort_card_layout.setSpacing(10)
        self.cohort_card_layout.setObjectName(u"cohort_card_layout")
        self.cohort_card_layout.setContentsMargins(10, 10, 10, 10)
        self.cohort_title_label = QLabel(self.cohort_card)
        self.cohort_title_label.setObjectName(u"cohort_title_label")
        font1 = QFont()
        font1.setBold(True)
        self.cohort_title_label.setFont(font1)

        self.cohort_card_layout.addWidget(self.cohort_title_label)

        self.filename_layout = QHBoxLayout()
        self.filename_layout.setSpacing(8)
        self.filename_layout.setObjectName(u"filename_layout")
        self.filename_label = QLabel(self.cohort_card)
        self.filename_label.setObjectName(u"filename_label")

        self.filename_layout.addWidget(self.filename_label)

        self.lineEdit_filename = QLineEdit(self.cohort_card)
        self.lineEdit_filename.setObjectName(u"lineEdit_filename")
        self.lineEdit_filename.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_filename.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.filename_layout.addWidget(self.lineEdit_filename)

        self.pushButton_browse = QPushButton(self.cohort_card)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.filename_layout.addWidget(self.pushButton_browse)


        self.cohort_card_layout.addLayout(self.filename_layout)

        self.label_4 = QLabel(self.cohort_card)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_4.setFont(font2)
        self.label_4.setTextFormat(Qt.TextFormat.RichText)
        self.label_4.setWordWrap(True)
        self.label_4.setProperty(u"variant", u"help")

        self.cohort_card_layout.addWidget(self.label_4)


        self.content_layout.addWidget(self.cohort_card)

        self.append_warning = QFrame(self.content_widget)
        self.append_warning.setObjectName(u"append_warning")
        self.append_warning.setFrameShape(QFrame.Shape.NoFrame)
        self.append_warning.setProperty(u"variant", u"warning")
        self.append_warning_layout = QHBoxLayout(self.append_warning)
        self.append_warning_layout.setObjectName(u"append_warning_layout")
        self.append_warning_layout.setContentsMargins(14, 10, 14, 10)
        self.append_warning_label = QLabel(self.append_warning)
        self.append_warning_label.setObjectName(u"append_warning_label")
        self.append_warning_label.setTextFormat(Qt.TextFormat.RichText)
        self.append_warning_label.setWordWrap(True)

        self.append_warning_layout.addWidget(self.append_warning_label)


        self.content_layout.addWidget(self.append_warning)

        self.optional_card = QFrame(self.content_widget)
        self.optional_card.setObjectName(u"optional_card")
        self.optional_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.optional_card.setFrameShadow(QFrame.Shadow.Raised)
        self.optional_card_layout = QVBoxLayout(self.optional_card)
        self.optional_card_layout.setSpacing(10)
        self.optional_card_layout.setObjectName(u"optional_card_layout")
        self.optional_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.optional_card)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.optional_card_layout.addWidget(self.label)

        self.events_layout = QVBoxLayout()
        self.events_layout.setSpacing(8)
        self.events_layout.setObjectName(u"events_layout")
        self.events_layout_1_layout = QVBoxLayout()
        self.events_layout_1_layout.setSpacing(2)
        self.events_layout_1_layout.setObjectName(u"events_layout_1_layout")
        self.checkBox_writeEvts = QCheckBox(self.optional_card)
        self.checkBox_writeEvts.setObjectName(u"checkBox_writeEvts")

        self.events_layout_1_layout.addWidget(self.checkBox_writeEvts)

        self.label_5 = QLabel(self.optional_card)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setTextFormat(Qt.TextFormat.RichText)
        self.label_5.setWordWrap(True)
        self.label_5.setIndent(26)
        self.label_5.setProperty(u"variant", u"help")

        self.events_layout_1_layout.addWidget(self.label_5)


        self.events_layout.addLayout(self.events_layout_1_layout)


        self.optional_card_layout.addLayout(self.events_layout)

        self.optional_line = QFrame(self.optional_card)
        self.optional_line.setObjectName(u"optional_line")
        self.optional_line.setFrameShape(QFrame.Shape.HLine)
        self.optional_line.setFrameShadow(QFrame.Shadow.Plain)

        self.optional_card_layout.addWidget(self.optional_line)

        self.label_2 = QLabel(self.optional_card)
        self.label_2.setObjectName(u"label_2")

        self.optional_card_layout.addWidget(self.label_2)

        self.picture_folder_layout = QHBoxLayout()
        self.picture_folder_layout.setSpacing(8)
        self.picture_folder_layout.setObjectName(u"picture_folder_layout")
        self.lineEdit_picturename = QLineEdit(self.optional_card)
        self.lineEdit_picturename.setObjectName(u"lineEdit_picturename")
        self.lineEdit_picturename.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_picturename.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.picture_folder_layout.addWidget(self.lineEdit_picturename)

        self.pushButton_browse_pic = QPushButton(self.optional_card)
        self.pushButton_browse_pic.setObjectName(u"pushButton_browse_pic")

        self.picture_folder_layout.addWidget(self.pushButton_browse_pic)


        self.optional_card_layout.addLayout(self.picture_folder_layout)

        self.label_3 = QLabel(self.optional_card)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setWordWrap(True)
        self.label_3.setProperty(u"variant", u"help")

        self.optional_card_layout.addWidget(self.label_3)


        self.content_layout.addWidget(self.optional_card)

        self.about_report_layout = QVBoxLayout()
        self.about_report_layout.setSpacing(6)
        self.about_report_layout.setObjectName(u"about_report_layout")
        self.about_report_title_label = QLabel(self.content_widget)
        self.about_report_title_label.setObjectName(u"about_report_title_label")
        self.about_report_title_label.setFont(font1)

        self.about_report_layout.addWidget(self.about_report_title_label)

        self.about_report_label = QLabel(self.content_widget)
        self.about_report_label.setObjectName(u"about_report_label")
        self.about_report_label.setWordWrap(True)
        self.about_report_label.setProperty(u"variant", u"help")

        self.about_report_layout.addWidget(self.about_report_label)

        self.variables_layout = QHBoxLayout()
        self.variables_layout.setSpacing(16)
        self.variables_layout.setObjectName(u"variables_layout")
        self.saturation_label = QLabel(self.content_widget)
        self.saturation_label.setObjectName(u"saturation_label")
        self.saturation_label.setTextFormat(Qt.TextFormat.RichText)
        self.saturation_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.saturation_label.setWordWrap(True)
        self.saturation_label.setProperty(u"variant", u"help")

        self.variables_layout.addWidget(self.saturation_label)

        self.desaturation_label = QLabel(self.content_widget)
        self.desaturation_label.setObjectName(u"desaturation_label")
        self.desaturation_label.setTextFormat(Qt.TextFormat.RichText)
        self.desaturation_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.desaturation_label.setWordWrap(True)
        self.desaturation_label.setProperty(u"variant", u"help")

        self.variables_layout.addWidget(self.desaturation_label)

        self.recovery_label = QLabel(self.content_widget)
        self.recovery_label.setObjectName(u"recovery_label")
        self.recovery_label.setTextFormat(Qt.TextFormat.RichText)
        self.recovery_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.recovery_label.setWordWrap(True)
        self.recovery_label.setProperty(u"variant", u"help")

        self.variables_layout.addWidget(self.recovery_label)

        self.variables_layout.setStretch(0, 1)
        self.variables_layout.setStretch(1, 1)
        self.variables_layout.setStretch(2, 1)

        self.about_report_layout.addLayout(self.variables_layout)

        self.about_report_end_label = QLabel(self.content_widget)
        self.about_report_end_label.setObjectName(u"about_report_end_label")
        self.about_report_end_label.setWordWrap(True)
        self.about_report_end_label.setProperty(u"variant", u"help")

        self.about_report_layout.addWidget(self.about_report_end_label)


        self.content_layout.addLayout(self.about_report_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(OutputFiles)
        self.pushButton_browse.clicked.connect(OutputFiles.browse_slot)
        self.pushButton_browse_pic.clicked.connect(OutputFiles.browse_pic_slot)
        self.checkBox_writeEvts.clicked.connect(OutputFiles.write_checkbox_slot)

        QMetaObject.connectSlotsByName(OutputFiles)
    # setupUi

    def retranslateUi(self, OutputFiles):
        OutputFiles.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("OutputFiles", u"Output Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("OutputFiles", u"Choose the file of the report for the cohort and the optional outputs of each recording.", None))
        self.cohort_title_label.setText(QCoreApplication.translate("OutputFiles", u"Cohort oxygen saturation report", None))
        self.filename_label.setText(QCoreApplication.translate("OutputFiles", u"Filename", None))
        self.lineEdit_filename.setText("")
        self.lineEdit_filename.setPlaceholderText(QCoreApplication.translate("OutputFiles", u"Select a .tsv file", None))
        self.pushButton_browse.setText(QCoreApplication.translate("OutputFiles", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("OutputFiles", u"A .tsv file: one line per recording. The number of sleep cycles reported is set in <b>Hours and Cycles</b>, under Optional settings in the left panel.", None))
        self.append_warning_label.setText(QCoreApplication.translate("OutputFiles", u"<b>The data are appended</b><br/>New recordings are added at the end of the report, so the file is modified each time the tool is run.", None))
        self.label.setText(QCoreApplication.translate("OutputFiles", u"Optional outputs", None))
        self.checkBox_writeEvts.setText(QCoreApplication.translate("OutputFiles", u"Write the detected events in the accessory file", None))
        self.label_5.setText(QCoreApplication.translate("OutputFiles", u"Desaturations: group <b>SpO2</b>, name <b>desat_SpO2</b>. Recoveries: group <b>SpO2</b>, name <b>recovery_SpO2</b>. Artefacts detected: group <b>SpO2</b>, name <b>art_SpO2</b>.", None))
        self.label_2.setText(QCoreApplication.translate("OutputFiles", u"Folder of the files of each recording", None))
        self.lineEdit_picturename.setText("")
        self.lineEdit_picturename.setPlaceholderText(QCoreApplication.translate("OutputFiles", u"Select a folder", None))
        self.pushButton_browse_pic.setText(QCoreApplication.translate("OutputFiles", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("OutputFiles", u"Optional: the files are written only when a folder is chosen. For each recording, the characteristics of the events and the graph of the oxygen saturation; their filenames are the PSG filename followed by _oxygen_saturation_events and _oxygen_saturation_graph.", None))
        self.about_report_title_label.setText(QCoreApplication.translate("OutputFiles", u"About the report", None))
        self.about_report_label.setText(QCoreApplication.translate("OutputFiles", u"The oxygen saturation is analyzed during the sleep period, from the first epoch scored as sleep (N1, N2, N3 or R) to the final awakening (including the last epoch scored as sleep). Automatic artefact detection is applied to the oximeter channel: the artefacts longer than 5 s are excluded from the analysis, the shorter ones are interpolated. The report has three categories of variables:", None))
        self.saturation_label.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:700;\">Oxygen saturation</span><br/>\u2022 minimum, maximum, mean and variability (standard deviation)<br/>\u2022 percentage of time below 96% to 60%<br/>Metrics are computed for the entire sleep period, and stratified by sleep thirds and halves, the sleep cycles and the sleep stages (W, N1, N2, N3, REM, NREM, N2\u2013N3 and total sleep).</p></body></html>", None))
        self.desaturation_label.setText(QCoreApplication.translate("OutputFiles", u"<b>Oxygen desaturations</b><br/>\u2022 number of events<br/>\u2022 index (ODI, events per hour)<br/>\u2022 severity: sum of the areas of the events (%\u00b7s) over the sleep period<br/>\u2022 percentage of sleep time in desaturation<br/>\u2022 average and median duration (s), area (%\u00b7s), slope (%/s) and drop (%)", None))
        self.recovery_label.setText(QCoreApplication.translate("OutputFiles", u"<b>Oxygen recoveries</b><br/>\u2022 number of events<br/>\u2022 index (events per hour)<br/>\u2022 severity: sum of the areas of the events (%\u00b7s) over the sleep period<br/>\u2022 percentage of sleep time in recovery<br/>\u2022 average and median duration (s), area (%\u00b7s), slope (%/s) and amplitude (%)", None))
        self.about_report_end_label.setText(QCoreApplication.translate("OutputFiles", u"The total severity is the sum of the areas of the desaturations and the recoveries (%\u00b7s) over the valid sleep period (s). The characteristics of each event (file of each recording) are its start time (s), duration (s), slope (%/s), depth (%) and area (%\u00b7s). The graph shows the saturation signal of the whole recording, with the invalid sections highlighted.", None))
    # retranslateUi

