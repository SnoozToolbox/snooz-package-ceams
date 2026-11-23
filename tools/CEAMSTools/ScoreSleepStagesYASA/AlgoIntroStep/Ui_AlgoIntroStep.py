# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AlgoIntroStep.ui'
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

class Ui_AlgoIntroStep(object):
    def setupUi(self, AlgoIntroStep):
        if not AlgoIntroStep.objectName():
            AlgoIntroStep.setObjectName(u"AlgoIntroStep")
        AlgoIntroStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(AlgoIntroStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(AlgoIntroStep)
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

        self.steps_grid.setColumnStretch(3, 1)

        self.steps_card_layout.addLayout(self.steps_grid)


        self.steps_section_layout.addWidget(self.steps_card)


        self.content_layout.addLayout(self.steps_section_layout)

        self.channels_section_layout = QVBoxLayout()
        self.channels_section_layout.setSpacing(8)
        self.channels_section_layout.setObjectName(u"channels_section_layout")
        self.channels_title_label = QLabel(self.content_widget)
        self.channels_title_label.setObjectName(u"channels_title_label")
        self.channels_title_label.setFont(font1)

        self.channels_section_layout.addWidget(self.channels_title_label)

        self.channels_card = QFrame(self.content_widget)
        self.channels_card.setObjectName(u"channels_card")
        self.channels_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.channels_card.setFrameShadow(QFrame.Shadow.Raised)
        self.channels_card_layout = QVBoxLayout(self.channels_card)
        self.channels_card_layout.setSpacing(10)
        self.channels_card_layout.setObjectName(u"channels_card_layout")
        self.channels_card_layout.setContentsMargins(10, 10, 10, 10)
        self.channels_label = QLabel(self.channels_card)
        self.channels_label.setObjectName(u"channels_label")
        self.channels_label.setWordWrap(True)
        self.channels_label.setProperty(u"variant", u"help")

        self.channels_card_layout.addWidget(self.channels_label)

        self.channels_line = QFrame(self.channels_card)
        self.channels_line.setObjectName(u"channels_line")
        self.channels_line.setFrameShape(QFrame.Shape.HLine)
        self.channels_line.setFrameShadow(QFrame.Shadow.Plain)

        self.channels_card_layout.addWidget(self.channels_line)

        self.channels_note_label = QLabel(self.channels_card)
        self.channels_note_label.setObjectName(u"channels_note_label")
        self.channels_note_label.setFont(font2)
        self.channels_note_label.setWordWrap(True)
        self.channels_note_label.setProperty(u"variant", u"help")

        self.channels_card_layout.addWidget(self.channels_note_label)

        self.discontinuous_note_label = QLabel(self.channels_card)
        self.discontinuous_note_label.setObjectName(u"discontinuous_note_label")
        self.discontinuous_note_label.setFont(font2)
        self.discontinuous_note_label.setWordWrap(True)
        self.discontinuous_note_label.setProperty(u"variant", u"help")

        self.channels_card_layout.addWidget(self.discontinuous_note_label)


        self.channels_section_layout.addWidget(self.channels_card)


        self.content_layout.addLayout(self.channels_section_layout)

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
        self.methods_label.setOpenExternalLinks(True)
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


        self.retranslateUi(AlgoIntroStep)
        self.methods_show_button.clicked.connect(self.methods_widget.show)
        self.methods_show_button.clicked.connect(self.methods_hide_button.show)
        self.methods_show_button.clicked.connect(self.methods_show_button.hide)
        self.methods_hide_button.clicked.connect(self.methods_widget.hide)
        self.methods_hide_button.clicked.connect(self.methods_show_button.show)
        self.methods_hide_button.clicked.connect(self.methods_hide_button.hide)

        QMetaObject.connectSlotsByName(AlgoIntroStep)
    # setupUi

    def retranslateUi(self, AlgoIntroStep):
        AlgoIntroStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("AlgoIntroStep", u"Score Sleep Stages with YASA", None))
        self.subtitle_label.setText(QCoreApplication.translate("AlgoIntroStep", u"Classifies the sleep stages of your polysomnography (PSG) files in 30-second epochs with YASA [1], and saves them in the accessory file.", None))
        self.steps_title_label.setText(QCoreApplication.translate("AlgoIntroStep", u"What you will do", None))
        self.step_1_number_label.setText(QCoreApplication.translate("AlgoIntroStep", u"1", None))
        self.step_1_name_label.setText(QCoreApplication.translate("AlgoIntroStep", u"Input Files", None))
        self.step_1_label.setText(QCoreApplication.translate("AlgoIntroStep", u"Add the PSG files, define the montage, then select the channels and give each one its alias (EEG, EOG or EMG).", None))
        self.step_2_number_label.setText(QCoreApplication.translate("AlgoIntroStep", u"2", None))
        self.step_2_name_label.setText(QCoreApplication.translate("AlgoIntroStep", u"Export Scoring", None))
        self.step_2_label.setText(QCoreApplication.translate("AlgoIntroStep", u"Define the group of the predicted sleep stages in the accessory file. Optionally, compare them with the expert scoring of the files.", None))
        self.channels_title_label.setText(QCoreApplication.translate("AlgoIntroStep", u"Channels", None))
        self.channels_label.setText(QCoreApplication.translate("AlgoIntroStep", u"The sleep stages can be scored from a single EEG channel, preferably a central one (C3, C4). One EOG and one EMG channel can improve the accuracy. You can select up to four EEG channels: for each epoch, the most confident classification is kept.", None))
        self.channels_note_label.setText(QCoreApplication.translate("AlgoIntroStep", u"In the internal analysis of Snooz, central channels combined with one frontal and one occipital channel typically perform marginally better.", None))
        self.discontinuous_note_label.setText(QCoreApplication.translate("AlgoIntroStep", u"Discontinuous files need at least one EEG channel with one EOG or EMG channel.", None))
        self.files_title_label.setText(QCoreApplication.translate("AlgoIntroStep", u"Accepted files", None))
        self.file_1_name_label.setText(QCoreApplication.translate("AlgoIntroStep", u"EDF", None))
        self.file_1_label.setText(QCoreApplication.translate("AlgoIntroStep", u"The .edf and .tsv files have the same filename and are in the same directory.", None))
        self.file_2_name_label.setText(QCoreApplication.translate("AlgoIntroStep", u"Stellate", None))
        self.file_2_label.setText(QCoreApplication.translate("AlgoIntroStep", u"The .sig and .sts files have the same filename and are in the same directory.", None))
        self.file_3_name_label.setText(QCoreApplication.translate("AlgoIntroStep", u"NATUS", None))
        self.file_3_label.setText(QCoreApplication.translate("AlgoIntroStep", u"The entire NATUS subject folder is required <i>(for CEAMS users)</i>.", None))
        self.methods_show_button.setText(QCoreApplication.translate("AlgoIntroStep", u"\u203a Methods and references", None))
        self.methods_hide_button.setText(QCoreApplication.translate("AlgoIntroStep", u"\u2304 Methods and references", None))
        self.methods_note_label.setText(QCoreApplication.translate("AlgoIntroStep", u"The details of each setting are shown in its own step.", None))
        self.methods_label.setText(QCoreApplication.translate("AlgoIntroStep", u"<b>YASA sleep staging [1]:</b> an open-source algorithm trained on more than 30,000 hours of PSG data from diverse populations.<br/>\u2022 <b>Data processing:</b> a central EEG channel, with the EOG and EMG channels, downsampled to 100 Hz and band-pass filtered between 0.4 and 30 Hz.<br/>\u2022 <b>Feature extraction:</b> time and frequency domain features of the EEG, and optionally of the EOG and EMG, for each 30-second epoch.<br/>\u2022 <b>Smoothing and normalization:</b> the features are smoothed across epochs to include the context, then z-scored over each night.<br/>\u2022 <b>Classification:</b> LightGBM, a tree-based gradient-boosting classifier.<br/>\u2022 <b>Performance evaluation:</b> standardized guidelines, including the accuracy, Cohen's kappa, the Matthews correlation coefficient, confusion matrices and F1-scores.<br/><br/>Documentation of YASA: <a href=\"https://raphaelvallat.com/yasa/\">raphaelvallat.com/yasa</a>.", None))
        self.references_label.setText(QCoreApplication.translate("AlgoIntroStep", u"[1] Vallat, R., &amp; Walker, M. P. (2021). An open-source, high-performance tool for automated sleep staging. <i>eLife</i>, <i>10</i>, Article e70092. <a href=\"https://doi.org/10.7554/eLife.70092\">https://doi.org/10.7554/eLife.70092</a>", None))
    # retranslateUi

