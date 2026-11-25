# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_IntroStep.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_IntroStep(object):
    def setupUi(self, IntroStep):
        if not IntroStep.objectName():
            IntroStep.setObjectName(u"IntroStep")
        IntroStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(IntroStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(IntroStep)
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

        self.steps_section_layout = QVBoxLayout()
        self.steps_section_layout.setSpacing(8)
        self.steps_section_layout.setObjectName(u"steps_section_layout")
        self.steps_title_label = QLabel(self.content_widget)
        self.steps_title_label.setObjectName(u"steps_title_label")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.steps_title_label.setFont(font1)

        self.steps_section_layout.addWidget(self.steps_title_label)

        self.steps_card = QFrame(self.content_widget)
        self.steps_card.setObjectName(u"steps_card")
        self.steps_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.steps_card.setFrameShadow(QFrame.Shadow.Raised)
        self.steps_card_layout = QVBoxLayout(self.steps_card)
        self.steps_card_layout.setSpacing(10)
        self.steps_card_layout.setObjectName(u"steps_card_layout")
        self.steps_card_layout.setContentsMargins(10, 10, 10, 10)
        self.steps_grid = QGridLayout()
        self.steps_grid.setObjectName(u"steps_grid")
        self.steps_grid.setHorizontalSpacing(12)
        self.steps_grid.setVerticalSpacing(10)
        self.step_1_number_label = QLabel(self.steps_card)
        self.step_1_number_label.setObjectName(u"step_1_number_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.step_1_number_label.setFont(font2)
        self.step_1_number_label.setProperty(u"variant", u"step_number")
        self.step_1_number_label.setMinimumSize(QSize(24, 24))
        self.step_1_number_label.setMaximumSize(QSize(24, 24))
        self.step_1_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.steps_grid.addWidget(self.step_1_number_label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.step_1_name_label = QLabel(self.steps_card)
        self.step_1_name_label.setObjectName(u"step_1_name_label")
        font3 = QFont()
        font3.setBold(True)
        self.step_1_name_label.setFont(font3)
        self.step_1_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_1_name_label, 0, 1, 1, 1)

        self.steps_gap = QSpacerItem(16, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.steps_grid.addItem(self.steps_gap, 0, 2, 1, 1)

        self.step_1_label = QLabel(self.steps_card)
        self.step_1_label.setObjectName(u"step_1_label")
        self.step_1_label.setWordWrap(True)
        self.step_1_label.setProperty(u"variant", u"help")
        self.step_1_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_1_label, 0, 3, 1, 1)

        self.step_line_2 = QFrame(self.steps_card)
        self.step_line_2.setObjectName(u"step_line_2")
        self.step_line_2.setFrameShape(QFrame.Shape.HLine)
        self.step_line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.steps_grid.addWidget(self.step_line_2, 1, 0, 1, 4)

        self.step_2_number_label = QLabel(self.steps_card)
        self.step_2_number_label.setObjectName(u"step_2_number_label")
        self.step_2_number_label.setFont(font2)
        self.step_2_number_label.setProperty(u"variant", u"step_number")
        self.step_2_number_label.setMinimumSize(QSize(24, 24))
        self.step_2_number_label.setMaximumSize(QSize(24, 24))
        self.step_2_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.steps_grid.addWidget(self.step_2_number_label, 2, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.step_2_name_label = QLabel(self.steps_card)
        self.step_2_name_label.setObjectName(u"step_2_name_label")
        self.step_2_name_label.setFont(font3)
        self.step_2_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_2_name_label, 2, 1, 1, 1)

        self.step_2_label = QLabel(self.steps_card)
        self.step_2_label.setObjectName(u"step_2_label")
        self.step_2_label.setWordWrap(True)
        self.step_2_label.setProperty(u"variant", u"help")
        self.step_2_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_2_label, 2, 3, 1, 1)

        self.step_line_3 = QFrame(self.steps_card)
        self.step_line_3.setObjectName(u"step_line_3")
        self.step_line_3.setFrameShape(QFrame.Shape.HLine)
        self.step_line_3.setFrameShadow(QFrame.Shadow.Plain)

        self.steps_grid.addWidget(self.step_line_3, 3, 0, 1, 4)

        self.step_3_number_label = QLabel(self.steps_card)
        self.step_3_number_label.setObjectName(u"step_3_number_label")
        self.step_3_number_label.setFont(font2)
        self.step_3_number_label.setProperty(u"variant", u"step_number")
        self.step_3_number_label.setMinimumSize(QSize(24, 24))
        self.step_3_number_label.setMaximumSize(QSize(24, 24))
        self.step_3_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.steps_grid.addWidget(self.step_3_number_label, 4, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.step_3_name_label = QLabel(self.steps_card)
        self.step_3_name_label.setObjectName(u"step_3_name_label")
        self.step_3_name_label.setFont(font3)
        self.step_3_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_3_name_label, 4, 1, 1, 1)

        self.step_3_label = QLabel(self.steps_card)
        self.step_3_label.setObjectName(u"step_3_label")
        self.step_3_label.setWordWrap(True)
        self.step_3_label.setProperty(u"variant", u"help")
        self.step_3_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_3_label, 4, 3, 1, 1)

        self.steps_grid.setColumnStretch(3, 1)

        self.steps_card_layout.addLayout(self.steps_grid)


        self.steps_section_layout.addWidget(self.steps_card)


        self.content_layout.addLayout(self.steps_section_layout)

        self.spectra_section_layout = QVBoxLayout()
        self.spectra_section_layout.setSpacing(8)
        self.spectra_section_layout.setObjectName(u"spectra_section_layout")
        self.spectra_title_label = QLabel(self.content_widget)
        self.spectra_title_label.setObjectName(u"spectra_title_label")
        self.spectra_title_label.setFont(font1)

        self.spectra_section_layout.addWidget(self.spectra_title_label)

        self.spectra_card = QFrame(self.content_widget)
        self.spectra_card.setObjectName(u"spectra_card")
        self.spectra_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.spectra_card.setFrameShadow(QFrame.Shadow.Raised)
        self.spectra_card_layout = QVBoxLayout(self.spectra_card)
        self.spectra_card_layout.setSpacing(10)
        self.spectra_card_layout.setObjectName(u"spectra_card_layout")
        self.spectra_card_layout.setContentsMargins(10, 10, 10, 10)
        self.spectra_image = QLabel(self.spectra_card)
        self.spectra_image.setObjectName(u"spectra_image")

        self.spectra_card_layout.addWidget(self.spectra_image)

        self.spectra_caption_label = QLabel(self.spectra_card)
        self.spectra_caption_label.setObjectName(u"spectra_caption_label")
        self.spectra_caption_label.setFont(font2)
        self.spectra_caption_label.setWordWrap(True)
        self.spectra_caption_label.setProperty(u"variant", u"help")

        self.spectra_card_layout.addWidget(self.spectra_caption_label)


        self.spectra_section_layout.addWidget(self.spectra_card)


        self.content_layout.addLayout(self.spectra_section_layout)

        self.recordings_section_layout = QVBoxLayout()
        self.recordings_section_layout.setSpacing(8)
        self.recordings_section_layout.setObjectName(u"recordings_section_layout")
        self.recordings_title_label = QLabel(self.content_widget)
        self.recordings_title_label.setObjectName(u"recordings_title_label")
        self.recordings_title_label.setFont(font1)

        self.recordings_section_layout.addWidget(self.recordings_title_label)

        self.recordings_card = QFrame(self.content_widget)
        self.recordings_card.setObjectName(u"recordings_card")
        self.recordings_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.recordings_card.setFrameShadow(QFrame.Shadow.Raised)
        self.recordings_card_layout = QVBoxLayout(self.recordings_card)
        self.recordings_card_layout.setSpacing(10)
        self.recordings_card_layout.setObjectName(u"recordings_card_layout")
        self.recordings_card_layout.setContentsMargins(10, 10, 10, 10)
        self.stages_label = QLabel(self.recordings_card)
        self.stages_label.setObjectName(u"stages_label")
        self.stages_label.setWordWrap(True)
        self.stages_label.setProperty(u"variant", u"help")

        self.recordings_card_layout.addWidget(self.stages_label)

        self.recordings_line = QFrame(self.recordings_card)
        self.recordings_line.setObjectName(u"recordings_line")
        self.recordings_line.setFrameShape(QFrame.Shape.HLine)
        self.recordings_line.setFrameShadow(QFrame.Shadow.Plain)

        self.recordings_card_layout.addWidget(self.recordings_line)

        self.sample_rate_label = QLabel(self.recordings_card)
        self.sample_rate_label.setObjectName(u"sample_rate_label")
        self.sample_rate_label.setWordWrap(True)
        self.sample_rate_label.setProperty(u"variant", u"help")

        self.recordings_card_layout.addWidget(self.sample_rate_label)


        self.recordings_section_layout.addWidget(self.recordings_card)


        self.content_layout.addLayout(self.recordings_section_layout)

        self.files_section_layout = QVBoxLayout()
        self.files_section_layout.setSpacing(8)
        self.files_section_layout.setObjectName(u"files_section_layout")
        self.files_title_label = QLabel(self.content_widget)
        self.files_title_label.setObjectName(u"files_title_label")
        self.files_title_label.setFont(font1)

        self.files_section_layout.addWidget(self.files_title_label)

        self.files_card = QFrame(self.content_widget)
        self.files_card.setObjectName(u"files_card")
        self.files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.files_card_layout = QVBoxLayout(self.files_card)
        self.files_card_layout.setSpacing(10)
        self.files_card_layout.setObjectName(u"files_card_layout")
        self.files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.files_grid = QGridLayout()
        self.files_grid.setObjectName(u"files_grid")
        self.files_grid.setHorizontalSpacing(32)
        self.files_grid.setVerticalSpacing(6)
        self.file_1_name_label = QLabel(self.files_card)
        self.file_1_name_label.setObjectName(u"file_1_name_label")
        self.file_1_name_label.setFont(font3)

        self.files_grid.addWidget(self.file_1_name_label, 0, 0, 1, 1)

        self.file_1_label = QLabel(self.files_card)
        self.file_1_label.setObjectName(u"file_1_label")
        self.file_1_label.setWordWrap(True)

        self.files_grid.addWidget(self.file_1_label, 0, 1, 1, 1)

        self.file_2_name_label = QLabel(self.files_card)
        self.file_2_name_label.setObjectName(u"file_2_name_label")
        self.file_2_name_label.setFont(font3)

        self.files_grid.addWidget(self.file_2_name_label, 1, 0, 1, 1)

        self.file_2_label = QLabel(self.files_card)
        self.file_2_label.setObjectName(u"file_2_label")
        self.file_2_label.setWordWrap(True)

        self.files_grid.addWidget(self.file_2_label, 1, 1, 1, 1)

        self.file_3_name_label = QLabel(self.files_card)
        self.file_3_name_label.setObjectName(u"file_3_name_label")
        self.file_3_name_label.setFont(font3)

        self.files_grid.addWidget(self.file_3_name_label, 2, 0, 1, 1)

        self.file_3_label = QLabel(self.files_card)
        self.file_3_label.setObjectName(u"file_3_label")
        self.file_3_label.setTextFormat(Qt.TextFormat.RichText)
        self.file_3_label.setWordWrap(True)

        self.files_grid.addWidget(self.file_3_label, 2, 1, 1, 1)

        self.files_grid.setColumnStretch(1, 1)

        self.files_card_layout.addLayout(self.files_grid)


        self.files_section_layout.addWidget(self.files_card)


        self.content_layout.addLayout(self.files_section_layout)

        self.methods_section_layout = QVBoxLayout()
        self.methods_section_layout.setSpacing(2)
        self.methods_section_layout.setObjectName(u"methods_section_layout")
        self.methods_buttons_layout = QHBoxLayout()
        self.methods_buttons_layout.setSpacing(0)
        self.methods_buttons_layout.setObjectName(u"methods_buttons_layout")
        self.methods_show_button = QPushButton(self.content_widget)
        self.methods_show_button.setObjectName(u"methods_show_button")
        self.methods_show_button.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.methods_show_button.setFlat(True)
        self.methods_show_button.setProperty(u"variant", u"link")

        self.methods_buttons_layout.addWidget(self.methods_show_button)

        self.methods_hide_button = QPushButton(self.content_widget)
        self.methods_hide_button.setObjectName(u"methods_hide_button")
        self.methods_hide_button.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.methods_hide_button.setVisible(False)
        self.methods_hide_button.setFlat(True)
        self.methods_hide_button.setProperty(u"variant", u"link")

        self.methods_buttons_layout.addWidget(self.methods_hide_button)

        self.methods_buttons_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.methods_buttons_layout.addItem(self.methods_buttons_spacer)


        self.methods_section_layout.addLayout(self.methods_buttons_layout)

        self.methods_note_label = QLabel(self.content_widget)
        self.methods_note_label.setObjectName(u"methods_note_label")
        self.methods_note_label.setFont(font2)
        self.methods_note_label.setWordWrap(True)
        self.methods_note_label.setProperty(u"variant", u"help")

        self.methods_section_layout.addWidget(self.methods_note_label)

        self.methods_widget = QWidget(self.content_widget)
        self.methods_widget.setObjectName(u"methods_widget")
        self.methods_widget.setVisible(False)
        self.methods_layout = QVBoxLayout(self.methods_widget)
        self.methods_layout.setSpacing(10)
        self.methods_layout.setObjectName(u"methods_layout")
        self.methods_layout.setContentsMargins(0, 6, 0, 0)
        self.methods_label = QLabel(self.methods_widget)
        self.methods_label.setObjectName(u"methods_label")
        self.methods_label.setTextFormat(Qt.TextFormat.RichText)
        self.methods_label.setWordWrap(True)
        self.methods_label.setProperty(u"variant", u"help")

        self.methods_layout.addWidget(self.methods_label)

        self.references_layout = QVBoxLayout()
        self.references_layout.setSpacing(8)
        self.references_layout.setObjectName(u"references_layout")
        self.references_layout.setContentsMargins(0, 6, 0, 0)
        self.references_line = QFrame(self.methods_widget)
        self.references_line.setObjectName(u"references_line")
        self.references_line.setFrameShape(QFrame.Shape.HLine)
        self.references_line.setFrameShadow(QFrame.Shadow.Plain)

        self.references_layout.addWidget(self.references_line)

        self.references_label = QLabel(self.methods_widget)
        self.references_label.setObjectName(u"references_label")
        self.references_label.setFont(font2)
        self.references_label.setTextFormat(Qt.TextFormat.RichText)
        self.references_label.setWordWrap(True)
        self.references_label.setOpenExternalLinks(True)
        self.references_label.setProperty(u"variant", u"help")

        self.references_layout.addWidget(self.references_label)


        self.methods_layout.addLayout(self.references_layout)


        self.methods_section_layout.addWidget(self.methods_widget)


        self.content_layout.addLayout(self.methods_section_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(IntroStep)
        self.methods_show_button.clicked.connect(self.methods_widget.show)
        self.methods_show_button.clicked.connect(self.methods_hide_button.show)
        self.methods_show_button.clicked.connect(self.methods_show_button.hide)
        self.methods_hide_button.clicked.connect(self.methods_widget.hide)
        self.methods_hide_button.clicked.connect(self.methods_show_button.show)
        self.methods_hide_button.clicked.connect(self.methods_hide_button.hide)

        QMetaObject.connectSlotsByName(IntroStep)
    # setupUi

    def retranslateUi(self, IntroStep):
        IntroStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("IntroStep", u"EEG Spectral Power Analysis", None))
        self.subtitle_label.setText(QCoreApplication.translate("IntroStep", u"Estimates the EEG spectral power of your polysomnography (PSG) files with the Welch method, per sleep stage and channel, over the whole recording.", None))
        self.steps_title_label.setText(QCoreApplication.translate("IntroStep", u"What you will do", None))
        self.step_1_number_label.setText(QCoreApplication.translate("IntroStep", u"1", None))
        self.step_1_name_label.setText(QCoreApplication.translate("IntroStep", u"Input Files", None))
        self.step_1_label.setText(QCoreApplication.translate("IntroStep", u"Add the PSG files, then select the montage and the EEG channels of each file.", None))
        self.step_2_number_label.setText(QCoreApplication.translate("IntroStep", u"2", None))
        self.step_2_name_label.setText(QCoreApplication.translate("IntroStep", u"Spectral Settings", None))
        self.step_2_label.setText(QCoreApplication.translate("IntroStep", u"Set the frequency range and the FFT windows.", None))
        self.step_3_number_label.setText(QCoreApplication.translate("IntroStep", u"3", None))
        self.step_3_name_label.setText(QCoreApplication.translate("IntroStep", u"Output File", None))
        self.step_3_label.setText(QCoreApplication.translate("IntroStep", u"Choose the report file: one report for all the recordings, grouped by channel and sleep stage.", None))
        self.spectra_title_label.setText(QCoreApplication.translate("IntroStep", u"Example spectra", None))
        self.spectra_image.setText("")
        self.spectra_caption_label.setText(QCoreApplication.translate("IntroStep", u"Spectral power of an example recording in N2 and N3, in 1 Hz bands.", None))
        self.recordings_title_label.setText(QCoreApplication.translate("IntroStep", u"Recordings", None))
        self.stages_label.setText(QCoreApplication.translate("IntroStep", u"The recordings must be scored: the power is reported per sleep stage.", None))
        self.sample_rate_label.setText(QCoreApplication.translate("IntroStep", u"The EEG channels must be sampled above 124 Hz (125 Hz or more): they are filtered between 0.3 and 62 Hz before the analysis.", None))
        self.files_title_label.setText(QCoreApplication.translate("IntroStep", u"Accepted files", None))
        self.file_1_name_label.setText(QCoreApplication.translate("IntroStep", u"EDF", None))
        self.file_1_label.setText(QCoreApplication.translate("IntroStep", u"The .edf and .tsv files have the same filename and are in the same directory.", None))
        self.file_2_name_label.setText(QCoreApplication.translate("IntroStep", u"Stellate", None))
        self.file_2_label.setText(QCoreApplication.translate("IntroStep", u"The .sig and .sts files have the same filename and are in the same directory.", None))
        self.file_3_name_label.setText(QCoreApplication.translate("IntroStep", u"NATUS", None))
        self.file_3_label.setText(QCoreApplication.translate("IntroStep", u"The entire NATUS subject folder is required <i>(for CEAMS users)</i>.", None))
        self.methods_show_button.setText(QCoreApplication.translate("IntroStep", u"\u203a Methods and references", None))
        self.methods_hide_button.setText(QCoreApplication.translate("IntroStep", u"\u2304 Methods and references", None))
        self.methods_note_label.setText(QCoreApplication.translate("IntroStep", u"The details of each setting are shown in its own step.", None))
        self.methods_label.setText(QCoreApplication.translate("IntroStep", u"<b>Filter:</b> the selected channels are filtered between 0.3 and 62 Hz (Butterworth band-pass, order 6, zero phase) before the analysis.<br/><br/><b>Spectrum (Welch [1]):</b> the signal is divided into windows (Hann window) and a Fast Fourier Transform (FFT) is applied to each window. The periodograms of the windows are averaged per sleep stage and over the whole recording. The frequency bin resolution is 1 / window length (s): 0.2 Hz with 5 s windows. The power of the bins is summed in each 1 Hz band, from the first to the last frequency.", None))
        self.references_label.setText(QCoreApplication.translate("IntroStep", u"[1] Welch, P. D. (1967). The use of fast Fourier transform for the estimation of power spectra: A method based on time averaging over short, modified periodograms. <i>IEEE Transactions on Audio and Electroacoustics</i>, <i>15</i>(2), 70\u201373. <a href=\"https://doi.org/10.1109/TAU.1967.1161901\">https://doi.org/10.1109/TAU.1967.1161901</a>", None))
    # retranslateUi

