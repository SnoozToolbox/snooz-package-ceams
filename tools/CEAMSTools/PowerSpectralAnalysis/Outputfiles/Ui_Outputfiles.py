# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Outputfiles.ui'
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

class Ui_Outputfiles(object):
    def setupUi(self, Outputfiles):
        if not Outputfiles.objectName():
            Outputfiles.setObjectName(u"Outputfiles")
        Outputfiles.resize(900, 700)
        self.verticalLayout = QVBoxLayout(Outputfiles)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(Outputfiles)
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

        self.distribution_card = QFrame(self.content_widget)
        self.distribution_card.setObjectName(u"distribution_card")
        self.distribution_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.distribution_card.setFrameShadow(QFrame.Shadow.Raised)
        self.distribution_card_layout = QVBoxLayout(self.distribution_card)
        self.distribution_card_layout.setSpacing(10)
        self.distribution_card_layout.setObjectName(u"distribution_card_layout")
        self.distribution_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.distribution_card)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)

        self.distribution_card_layout.addWidget(self.label)

        self.distribution_help_label = QLabel(self.distribution_card)
        self.distribution_help_label.setObjectName(u"distribution_help_label")
        self.distribution_help_label.setWordWrap(True)
        self.distribution_help_label.setProperty(u"variant", u"help")

        self.distribution_card_layout.addWidget(self.distribution_help_label)

        self.distribution_layout = QVBoxLayout()
        self.distribution_layout.setSpacing(8)
        self.distribution_layout.setObjectName(u"distribution_layout")
        self.distribution_layout_1_layout = QVBoxLayout()
        self.distribution_layout_1_layout.setSpacing(2)
        self.distribution_layout_1_layout.setObjectName(u"distribution_layout_1_layout")
        self.total_checkBox = QCheckBox(self.distribution_card)
        self.total_checkBox.setObjectName(u"total_checkBox")
        self.total_checkBox.setEnabled(False)
        self.total_checkBox.setMinimumSize(QSize(238, 0))
        self.total_checkBox.setMaximumSize(QSize(238, 16777215))
        self.total_checkBox.setChecked(True)

        self.distribution_layout_1_layout.addWidget(self.total_checkBox)

        self.total_help_label = QLabel(self.distribution_card)
        self.total_help_label.setObjectName(u"total_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.total_help_label.setFont(font2)
        self.total_help_label.setWordWrap(True)
        self.total_help_label.setIndent(26)
        self.total_help_label.setProperty(u"variant", u"help")

        self.distribution_layout_1_layout.addWidget(self.total_help_label)


        self.distribution_layout.addLayout(self.distribution_layout_1_layout)

        self.distribution_layout_line_1 = QFrame(self.distribution_card)
        self.distribution_layout_line_1.setObjectName(u"distribution_layout_line_1")
        self.distribution_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.distribution_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.distribution_layout.addWidget(self.distribution_layout_line_1)

        self.distribution_layout_2_layout = QVBoxLayout()
        self.distribution_layout_2_layout.setSpacing(2)
        self.distribution_layout_2_layout.setObjectName(u"distribution_layout_2_layout")
        self.hour_checkBox = QCheckBox(self.distribution_card)
        self.hour_checkBox.setObjectName(u"hour_checkBox")
        self.hour_checkBox.setMinimumSize(QSize(238, 0))
        self.hour_checkBox.setMaximumSize(QSize(238, 16777215))
        self.hour_checkBox.setChecked(True)

        self.distribution_layout_2_layout.addWidget(self.hour_checkBox)

        self.hour_help_label = QLabel(self.distribution_card)
        self.hour_help_label.setObjectName(u"hour_help_label")
        self.hour_help_label.setFont(font2)
        self.hour_help_label.setWordWrap(True)
        self.hour_help_label.setIndent(26)
        self.hour_help_label.setProperty(u"variant", u"help")

        self.distribution_layout_2_layout.addWidget(self.hour_help_label)


        self.distribution_layout.addLayout(self.distribution_layout_2_layout)

        self.distribution_layout_line_2 = QFrame(self.distribution_card)
        self.distribution_layout_line_2.setObjectName(u"distribution_layout_line_2")
        self.distribution_layout_line_2.setFrameShape(QFrame.Shape.HLine)
        self.distribution_layout_line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.distribution_layout.addWidget(self.distribution_layout_line_2)

        self.distribution_layout_3_layout = QVBoxLayout()
        self.distribution_layout_3_layout.setSpacing(2)
        self.distribution_layout_3_layout.setObjectName(u"distribution_layout_3_layout")
        self.cycle_checkBox = QCheckBox(self.distribution_card)
        self.cycle_checkBox.setObjectName(u"cycle_checkBox")
        self.cycle_checkBox.setMinimumSize(QSize(238, 0))
        self.cycle_checkBox.setMaximumSize(QSize(238, 16777215))
        self.cycle_checkBox.setChecked(True)

        self.distribution_layout_3_layout.addWidget(self.cycle_checkBox)

        self.cycle_help_label = QLabel(self.distribution_card)
        self.cycle_help_label.setObjectName(u"cycle_help_label")
        self.cycle_help_label.setFont(font2)
        self.cycle_help_label.setWordWrap(True)
        self.cycle_help_label.setIndent(26)
        self.cycle_help_label.setProperty(u"variant", u"help")

        self.distribution_layout_3_layout.addWidget(self.cycle_help_label)


        self.distribution_layout.addLayout(self.distribution_layout_3_layout)


        self.distribution_card_layout.addLayout(self.distribution_layout)

        self.limits_help_label = QLabel(self.distribution_card)
        self.limits_help_label.setObjectName(u"limits_help_label")
        self.limits_help_label.setFont(font2)
        self.limits_help_label.setWordWrap(True)
        self.limits_help_label.setProperty(u"variant", u"help")

        self.distribution_card_layout.addWidget(self.limits_help_label)


        self.content_layout.addWidget(self.distribution_card)

        self.output_card = QFrame(self.content_widget)
        self.output_card.setObjectName(u"output_card")
        self.output_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.output_card.setFrameShadow(QFrame.Shadow.Raised)
        self.output_card_layout = QVBoxLayout(self.output_card)
        self.output_card_layout.setSpacing(10)
        self.output_card_layout.setObjectName(u"output_card_layout")
        self.output_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_4 = QLabel(self.output_card)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.output_card_layout.addWidget(self.label_4)

        self.filename_layout = QHBoxLayout()
        self.filename_layout.setSpacing(8)
        self.filename_layout.setObjectName(u"filename_layout")
        self.label_3 = QLabel(self.output_card)
        self.label_3.setObjectName(u"label_3")

        self.filename_layout.addWidget(self.label_3)

        self.filename_lineEdit = QLineEdit(self.output_card)
        self.filename_lineEdit.setObjectName(u"filename_lineEdit")
        self.filename_lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.filename_layout.addWidget(self.filename_lineEdit)

        self.choose_pushButton = QPushButton(self.output_card)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.filename_layout.addWidget(self.choose_pushButton)


        self.output_card_layout.addLayout(self.filename_layout)

        self.filename_help_label = QLabel(self.output_card)
        self.filename_help_label.setObjectName(u"filename_help_label")
        self.filename_help_label.setFont(font2)
        self.filename_help_label.setWordWrap(True)
        self.filename_help_label.setProperty(u"variant", u"help")

        self.output_card_layout.addWidget(self.filename_help_label)


        self.content_layout.addWidget(self.output_card)

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

        self.about_averages_layout = QVBoxLayout()
        self.about_averages_layout.setSpacing(6)
        self.about_averages_layout.setObjectName(u"about_averages_layout")
        self.about_averages_title_label = QLabel(self.content_widget)
        self.about_averages_title_label.setObjectName(u"about_averages_title_label")
        self.about_averages_title_label.setFont(font1)

        self.about_averages_layout.addWidget(self.about_averages_title_label)

        self.about_averages_label = QLabel(self.content_widget)
        self.about_averages_label.setObjectName(u"about_averages_label")
        self.about_averages_label.setWordWrap(True)
        self.about_averages_label.setProperty(u"variant", u"help")

        self.about_averages_layout.addWidget(self.about_averages_label)


        self.content_layout.addLayout(self.about_averages_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Outputfiles)
        self.choose_pushButton.clicked.connect(Outputfiles.choose_button_slot)

        QMetaObject.connectSlotsByName(Outputfiles)
    # setupUi

    def retranslateUi(self, Outputfiles):
        Outputfiles.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("Outputfiles", u"Output Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("Outputfiles", u"Choose the distributions of the spectral power to export and the file to write them in.", None))
        self.label.setText(QCoreApplication.translate("Outputfiles", u"Spectral power distribution to export", None))
        self.distribution_help_label.setText(QCoreApplication.translate("Outputfiles", u"Computed on the sections chosen in step 4: per sleep stage or on the selected annotations.", None))
#if QT_CONFIG(tooltip)
        self.total_checkBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.total_checkBox.setText(QCoreApplication.translate("Outputfiles", u"Total", None))
        self.total_help_label.setText(QCoreApplication.translate("Outputfiles", u"Average power over the whole recording.", None))
#if QT_CONFIG(tooltip)
        self.hour_checkBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.hour_checkBox.setText(QCoreApplication.translate("Outputfiles", u"Distribution per hour", None))
        self.hour_help_label.setText(QCoreApplication.translate("Outputfiles", u"Average power for each clock hour and each stage hour, from hour 1. Empty when the hour has no data.", None))
#if QT_CONFIG(tooltip)
        self.cycle_checkBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.cycle_checkBox.setText(QCoreApplication.translate("Outputfiles", u"Distribution per sleep cycle", None))
        self.cycle_help_label.setText(QCoreApplication.translate("Outputfiles", u"Average power for each sleep cycle, from cycle 1. Empty when the cycle does not exist.", None))
        self.limits_help_label.setText(QCoreApplication.translate("Outputfiles", u"The number of hours and cycles reported is set in \"Hours and Cycles\", under \"Optional settings\" in the left panel.", None))
        self.label_4.setText(QCoreApplication.translate("Outputfiles", u"Output file", None))
        self.label_3.setText(QCoreApplication.translate("Outputfiles", u"Filename", None))
        self.filename_lineEdit.setInputMask("")
        self.filename_lineEdit.setText("")
        self.filename_lineEdit.setPlaceholderText(QCoreApplication.translate("Outputfiles", u"Select the file to save the cohort EEG spectral report.", None))
        self.choose_pushButton.setText(QCoreApplication.translate("Outputfiles", u"Choose", None))
        self.filename_help_label.setText(QCoreApplication.translate("Outputfiles", u"A .tsv file (tab separated values): one line per subject, channel and frequency band.", None))
        self.append_warning_label.setText(QCoreApplication.translate("Outputfiles", u"<b>The data are appended</b><br/>Spectral data are appended to the output file, so the file is modified each time the tool is run.", None))
        self.about_averages_title_label.setText(QCoreApplication.translate("Outputfiles", u"About the averages", None))
        self.about_averages_label.setText(QCoreApplication.translate("Outputfiles", u"The averages include only the valid FFT windows: the clean windows of the selected stages or periods. When \"Analyse power in sleep cycles only\" is checked in step 4, the analysis starts at the sleep onset and the gaps between the cycles are not analysed. Otherwise the whole recording is analysed, even before the sleep onset and after the last asleep epoch.", None))
    # retranslateUi

