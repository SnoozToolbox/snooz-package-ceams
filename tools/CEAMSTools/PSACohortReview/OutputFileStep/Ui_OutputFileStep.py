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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
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

        self.reports_card = QFrame(self.content_widget)
        self.reports_card.setObjectName(u"reports_card")
        self.reports_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.reports_card.setFrameShadow(QFrame.Shadow.Raised)
        self.reports_card_layout = QVBoxLayout(self.reports_card)
        self.reports_card_layout.setSpacing(10)
        self.reports_card_layout.setObjectName(u"reports_card_layout")
        self.reports_card_layout.setContentsMargins(10, 10, 10, 10)
        self.reports_title_label = QLabel(self.reports_card)
        self.reports_title_label.setObjectName(u"reports_title_label")
        font1 = QFont()
        font1.setBold(True)
        self.reports_title_label.setFont(font1)

        self.reports_card_layout.addWidget(self.reports_title_label)

        self.reports_help_label = QLabel(self.reports_card)
        self.reports_help_label.setObjectName(u"reports_help_label")
        self.reports_help_label.setWordWrap(True)
        self.reports_help_label.setProperty(u"variant", u"help")

        self.reports_card_layout.addWidget(self.reports_help_label)

        self.reports_layout = QVBoxLayout()
        self.reports_layout.setSpacing(8)
        self.reports_layout.setObjectName(u"reports_layout")
        self.reports_layout_1_layout = QVBoxLayout()
        self.reports_layout_1_layout.setSpacing(2)
        self.reports_layout_1_layout.setObjectName(u"reports_layout_1_layout")
        self.export_raw_checkBox = QCheckBox(self.reports_card)
        self.export_raw_checkBox.setObjectName(u"export_raw_checkBox")
        self.export_raw_checkBox.setMaximumSize(QSize(16777215, 16777215))

        self.reports_layout_1_layout.addWidget(self.export_raw_checkBox)

        self.label_3 = QLabel(self.reports_card)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_3.setFont(font2)
        self.label_3.setWordWrap(True)
        self.label_3.setIndent(26)
        self.label_3.setProperty(u"variant", u"help")

        self.reports_layout_1_layout.addWidget(self.label_3)


        self.reports_layout.addLayout(self.reports_layout_1_layout)

        self.reports_layout_line_1 = QFrame(self.reports_card)
        self.reports_layout_line_1.setObjectName(u"reports_layout_line_1")
        self.reports_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.reports_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.reports_layout.addWidget(self.reports_layout_line_1)

        self.reports_layout_2_layout = QVBoxLayout()
        self.reports_layout_2_layout.setSpacing(2)
        self.reports_layout_2_layout.setObjectName(u"reports_layout_2_layout")
        self.export_transpose_checkBox = QCheckBox(self.reports_card)
        self.export_transpose_checkBox.setObjectName(u"export_transpose_checkBox")
        self.export_transpose_checkBox.setMaximumSize(QSize(16777215, 16777215))
        self.export_transpose_checkBox.setChecked(True)

        self.reports_layout_2_layout.addWidget(self.export_transpose_checkBox)

        self.transposed_layout = QVBoxLayout()
        self.transposed_layout.setSpacing(6)
        self.transposed_layout.setObjectName(u"transposed_layout")
        self.label_8 = QLabel(self.reports_card)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setWordWrap(True)
        self.label_8.setIndent(26)
        self.label_8.setProperty(u"variant", u"help")

        self.transposed_layout.addWidget(self.label_8)

        self.activity_layout = QHBoxLayout()
        self.activity_layout.setSpacing(12)
        self.activity_layout.setObjectName(u"activity_layout")
        self.activity_layout.setContentsMargins(26, 0, 0, 0)
        self.label = QLabel(self.reports_card)
        self.label.setObjectName(u"label")

        self.activity_layout.addWidget(self.label)

        self.activity_comboBox = QComboBox(self.reports_card)
        self.activity_comboBox.setObjectName(u"activity_comboBox")
        self.activity_comboBox.setMaximumSize(QSize(16777215, 16777215))

        self.activity_layout.addWidget(self.activity_comboBox)

        self.activity_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.activity_layout.addItem(self.activity_spacer)

        self.activity_layout.setStretch(2, 1)

        self.transposed_layout.addLayout(self.activity_layout)

        self.activity_help_label = QLabel(self.reports_card)
        self.activity_help_label.setObjectName(u"activity_help_label")
        self.activity_help_label.setFont(font2)
        self.activity_help_label.setWordWrap(True)
        self.activity_help_label.setIndent(26)
        self.activity_help_label.setProperty(u"variant", u"help")

        self.transposed_layout.addWidget(self.activity_help_label)


        self.reports_layout_2_layout.addLayout(self.transposed_layout)


        self.reports_layout.addLayout(self.reports_layout_2_layout)


        self.reports_card_layout.addLayout(self.reports_layout)


        self.content_layout.addWidget(self.reports_card)

        self.output_card = QFrame(self.content_widget)
        self.output_card.setObjectName(u"output_card")
        self.output_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.output_card.setFrameShadow(QFrame.Shadow.Raised)
        self.output_card_layout = QVBoxLayout(self.output_card)
        self.output_card_layout.setSpacing(10)
        self.output_card_layout.setObjectName(u"output_card_layout")
        self.output_card_layout.setContentsMargins(10, 10, 10, 10)
        self.output_title_label = QLabel(self.output_card)
        self.output_title_label.setObjectName(u"output_title_label")
        self.output_title_label.setFont(font1)

        self.output_card_layout.addWidget(self.output_title_label)

        self.filename_layout = QHBoxLayout()
        self.filename_layout.setSpacing(8)
        self.filename_layout.setObjectName(u"filename_layout")
        self.filename_label = QLabel(self.output_card)
        self.filename_label.setObjectName(u"filename_label")

        self.filename_layout.addWidget(self.filename_label)

        self.filename_lineEdit = QLineEdit(self.output_card)
        self.filename_lineEdit.setObjectName(u"filename_lineEdit")
        self.filename_lineEdit.setMaximumSize(QSize(16777215, 16777215))

        self.filename_layout.addWidget(self.filename_lineEdit)

        self.choose_pushButton = QPushButton(self.output_card)
        self.choose_pushButton.setObjectName(u"choose_pushButton")
        self.choose_pushButton.setMaximumSize(QSize(150, 16777215))

        self.filename_layout.addWidget(self.choose_pushButton)


        self.output_card_layout.addLayout(self.filename_layout)

        self.label_2 = QLabel(self.output_card)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setWordWrap(True)
        self.label_2.setProperty(u"variant", u"help")

        self.output_card_layout.addWidget(self.label_2)


        self.content_layout.addWidget(self.output_card)

        self.overwrite_warning = QFrame(self.content_widget)
        self.overwrite_warning.setObjectName(u"overwrite_warning")
        self.overwrite_warning.setFrameShape(QFrame.Shape.NoFrame)
        self.overwrite_warning.setProperty(u"variant", u"warning")
        self.overwrite_warning_layout = QHBoxLayout(self.overwrite_warning)
        self.overwrite_warning_layout.setObjectName(u"overwrite_warning_layout")
        self.overwrite_warning_layout.setContentsMargins(14, 10, 14, 10)
        self.overwrite_warning_label = QLabel(self.overwrite_warning)
        self.overwrite_warning_label.setObjectName(u"overwrite_warning_label")
        self.overwrite_warning_label.setTextFormat(Qt.TextFormat.RichText)
        self.overwrite_warning_label.setWordWrap(True)

        self.overwrite_warning_layout.addWidget(self.overwrite_warning_label)


        self.content_layout.addWidget(self.overwrite_warning)

        self.about_activity_layout = QVBoxLayout()
        self.about_activity_layout.setSpacing(6)
        self.about_activity_layout.setObjectName(u"about_activity_layout")
        self.about_activity_title_label = QLabel(self.content_widget)
        self.about_activity_title_label.setObjectName(u"about_activity_title_label")
        self.about_activity_title_label.setFont(font1)

        self.about_activity_layout.addWidget(self.about_activity_title_label)

        self.about_activity_label = QLabel(self.content_widget)
        self.about_activity_label.setObjectName(u"about_activity_label")
        self.about_activity_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_activity_label.setWordWrap(True)
        self.about_activity_label.setProperty(u"variant", u"help")

        self.about_activity_layout.addWidget(self.about_activity_label)


        self.content_layout.addLayout(self.about_activity_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(OutputFileStep)
        self.choose_pushButton.clicked.connect(OutputFileStep.choose_button_slot)
        self.export_transpose_checkBox.clicked.connect(OutputFileStep.export_transposed_checkbox_slot)

        QMetaObject.connectSlotsByName(OutputFileStep)
    # setupUi

    def retranslateUi(self, OutputFileStep):
        OutputFileStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("OutputFileStep", u"Output File", None))
        self.subtitle_label.setText(QCoreApplication.translate("OutputFileStep", u"Choose the reports to export and the file to write them in.", None))
        self.reports_title_label.setText(QCoreApplication.translate("OutputFileStep", u"Reports to export", None))
        self.reports_help_label.setText(QCoreApplication.translate("OutputFileStep", u"Check the reports to generate, the clean report, the transposed report or both.", None))
#if QT_CONFIG(tooltip)
        self.export_raw_checkBox.setToolTip(QCoreApplication.translate("OutputFileStep", u"Check to export the spectral power of the selected channels only, in the same format as the input report.", None))
#endif // QT_CONFIG(tooltip)
        self.export_raw_checkBox.setText(QCoreApplication.translate("OutputFileStep", u"Export the clean EEG spectral report", None))
        self.label_3.setText(QCoreApplication.translate("OutputFileStep", u"Cleans the EEG spectral power report. The clean report keeps only the selected channels, with their edited labels, in the same format as the input reports.", None))
#if QT_CONFIG(tooltip)
        self.export_transpose_checkBox.setToolTip(QCoreApplication.translate("OutputFileStep", u"Check to export the transposed report. It has one subject per row, with the selected channels (ROIs included) and the frequency bands as additional columns.", None))
#endif // QT_CONFIG(tooltip)
        self.export_transpose_checkBox.setText(QCoreApplication.translate("OutputFileStep", u"Export the transposed EEG spectral report", None))
        self.label_8.setText(QCoreApplication.translate("OutputFileStep", u"Transposes the EEG spectral power report to have one subject per row.", None))
        self.label.setText(QCoreApplication.translate("OutputFileStep", u"Activity variables", None))
        self.activity_help_label.setText(QCoreApplication.translate("OutputFileStep", u"Choose the activity variables to export. Only those found in the reports are listed.", None))
        self.output_title_label.setText(QCoreApplication.translate("OutputFileStep", u"Output file", None))
        self.filename_label.setText(QCoreApplication.translate("OutputFileStep", u"Filename", None))
        self.filename_lineEdit.setPlaceholderText(QCoreApplication.translate("OutputFileStep", u"Choose a file to save the reports", None))
        self.filename_lineEdit.setInputMask("")
        self.filename_lineEdit.setText("")
        self.choose_pushButton.setText(QCoreApplication.translate("OutputFileStep", u"Choose", None))
        self.label_2.setText(QCoreApplication.translate("OutputFileStep", u"The suffix _clean or _transposed is added to the filename, and the files are .tsv (tab separated values) files. For example, cohort.tsv gives cohort_clean.tsv and cohort_transposed.tsv.", None))
        self.overwrite_warning_label.setText(QCoreApplication.translate("OutputFileStep", u"<b>Existing files are overwritten</b><br/>The output files are replaced if they already exist.", None))
        self.about_activity_title_label.setText(QCoreApplication.translate("OutputFileStep", u"About the activity variables", None))
        self.about_activity_label.setText(QCoreApplication.translate("OutputFileStep", u"<b>Power per frequency band and sleep stage</b><br/>\u2022 \"Total\" exports the average over the whole recording.<br/>\u2022 \"Distribution per clock hour\" exports the average for each real clock hour (hours 1 to 9 by default).<br/>\u2022 \"Distribution per hour spent in each sleep stage\" exports the average for each hour spent in each sleep stage, once the stage reaches an hour (hours 1 to 9 by default).<br/>\u2022 \"Distribution per sleep cycle\" exports the average for each sleep cycle (cycles 1 to 6 by default).<br/>\u2022 The maximum number of hours and sleep cycles, and the starting point (the first sleep stage or the sleep onset), are defined when you run \"Analyze EEG Spectral Power\".<br/><br/><b>Power per frequency band and annotation</b><br/>\u2022 For a report of the analysis per annotation, the averages are given for each selected annotation.<br/>\u2022 \"Distribution per hour spent in each sleep stage\" is not available for these reports.<br/><br/><b>Variable names</b><br/>\u2022 The clean rep"
                        "ort has the same variable names as the input reports.<br/>\u2022 In the transposed report, the channel label and the frequency band are added to the variable name as a suffix, with abs for the absolute power or rel for the relative power.<br/>\u2022 For example, for the channel EEG F3-RC and the band 1 to 4 Hz, total_act becomes total_act_abs_EEG F3-RC_1_4 for the absolute power, and total_act_rel_EEG F3-RC_1_4 for the relative power.", None))
    # retranslateUi

