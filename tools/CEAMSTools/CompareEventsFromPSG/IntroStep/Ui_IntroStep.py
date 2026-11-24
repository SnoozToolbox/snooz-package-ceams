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

        self.step_line_4 = QFrame(self.steps_card)
        self.step_line_4.setObjectName(u"step_line_4")
        self.step_line_4.setFrameShape(QFrame.Shape.HLine)
        self.step_line_4.setFrameShadow(QFrame.Shadow.Plain)

        self.steps_grid.addWidget(self.step_line_4, 5, 0, 1, 4)

        self.step_4_number_label = QLabel(self.steps_card)
        self.step_4_number_label.setObjectName(u"step_4_number_label")
        self.step_4_number_label.setFont(font2)
        self.step_4_number_label.setProperty(u"variant", u"step_number")
        self.step_4_number_label.setMinimumSize(QSize(24, 24))
        self.step_4_number_label.setMaximumSize(QSize(24, 24))
        self.step_4_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.steps_grid.addWidget(self.step_4_number_label, 6, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.step_4_name_label = QLabel(self.steps_card)
        self.step_4_name_label.setObjectName(u"step_4_name_label")
        self.step_4_name_label.setFont(font3)
        self.step_4_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_4_name_label, 6, 1, 1, 1)

        self.step_4_label = QLabel(self.steps_card)
        self.step_4_label.setObjectName(u"step_4_label")
        self.step_4_label.setWordWrap(True)
        self.step_4_label.setProperty(u"variant", u"help")
        self.step_4_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_4_label, 6, 3, 1, 1)

        self.steps_grid.setColumnStretch(3, 1)

        self.steps_card_layout.addLayout(self.steps_grid)


        self.steps_section_layout.addWidget(self.steps_card)


        self.content_layout.addLayout(self.steps_section_layout)

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
        self.title_label.setText(QCoreApplication.translate("IntroStep", u"Evaluate Detected Events", None))
        self.subtitle_label.setText(QCoreApplication.translate("IntroStep", u"Compares two sets of events, such as detections and expert annotations, to evaluate the performance of a detector. Also evaluates the concordance between the scorings of two experts.", None))
        self.steps_title_label.setText(QCoreApplication.translate("IntroStep", u"What you will do", None))
        self.step_1_number_label.setText(QCoreApplication.translate("IntroStep", u"1", None))
        self.step_1_name_label.setText(QCoreApplication.translate("IntroStep", u"PSG Input Files", None))
        self.step_1_label.setText(QCoreApplication.translate("IntroStep", u"Add the PSG files. They must be scored in sleep stages.", None))
        self.step_2_number_label.setText(QCoreApplication.translate("IntroStep", u"2", None))
        self.step_2_name_label.setText(QCoreApplication.translate("IntroStep", u"Expert annotation", None))
        self.step_2_label.setText(QCoreApplication.translate("IntroStep", u"Select, for each PSG file, the expert events used as the gold standard.", None))
        self.step_3_number_label.setText(QCoreApplication.translate("IntroStep", u"3", None))
        self.step_3_name_label.setText(QCoreApplication.translate("IntroStep", u"Detector annotation", None))
        self.step_3_label.setText(QCoreApplication.translate("IntroStep", u"Select, for each PSG file, the detections to compare with the expert events.", None))
        self.step_4_number_label.setText(QCoreApplication.translate("IntroStep", u"4", None))
        self.step_4_name_label.setText(QCoreApplication.translate("IntroStep", u"Output File", None))
        self.step_4_label.setText(QCoreApplication.translate("IntroStep", u"Choose the sleep stages in which the events are compared, the Jaccard index threshold and the suffix of the output file. Optionally, export the true positive events, and the false negative and false positive events.", None))
        self.files_title_label.setText(QCoreApplication.translate("IntroStep", u"Accepted files", None))
        self.file_1_name_label.setText(QCoreApplication.translate("IntroStep", u"EDF", None))
        self.file_1_label.setText(QCoreApplication.translate("IntroStep", u"The .edf and .tsv files have the same filename and are in the same directory.", None))
        self.file_2_name_label.setText(QCoreApplication.translate("IntroStep", u"Stellate", None))
        self.file_2_label.setText(QCoreApplication.translate("IntroStep", u"The .sig and .sts files have the same filename and are in the same directory.", None))
        self.file_3_name_label.setText(QCoreApplication.translate("IntroStep", u"NATUS", None))
        self.file_3_label.setText(QCoreApplication.translate("IntroStep", u"The entire NATUS subject folder is required <i>(for CEAMS users)</i>.", None))
        self.methods_show_button.setText(QCoreApplication.translate("IntroStep", u"\u203a Methods", None))
        self.methods_hide_button.setText(QCoreApplication.translate("IntroStep", u"\u2304 Methods", None))
        self.methods_note_label.setText(QCoreApplication.translate("IntroStep", u"The details of each setting are shown in its own step.", None))
        self.methods_label.setText(QCoreApplication.translate("IntroStep", u"<b>Variables:</b> <i>e</i> is an event of the expert and <i>d</i> a detection. True positive (TP): a correct detection (<i>e</i> and <i>d</i> are the same). False positive (FP): an incorrect detection (<i>d</i> does not match any <i>e</i>). False negative (FN): an event missed (<i>e</i> not detected).<br/><br/><b>Metrics:</b> precision = TP / (TP + FP), the fraction of the detections that are correct. Recall = TP / (TP + FN), the fraction of the events found. F1 score = 2 \u00d7 (precision \u00d7 recall) / (precision + recall). Kappa = 2 (TP \u00d7 TN \u2212 FN \u00d7 FP) / ((TP + FP)(FP + TN) + (TP + FN)(FN + TN)), in the samples domain only: a conservative agreement, because the expected agreement is removed from the score.<br/><br/><b>Samples domain:</b> the events <i>e</i> and <i>d</i> are sampled at 100 Hz, so TP, TN, FP and FN are numbers of samples (TP-samples = 500: 500 samples of the expert events are correctly detected). The evaluation is conservative (strict), but many shorter <i>d</i> can match a l"
                        "onger <i>e</i> without significant penalty: not suited for event density.<br/><br/><b>Events domain:</b> with the Jaccard index, (intersection of <i>e</i> and <i>d</i>) / (union of <i>e</i> and <i>d</i>). A <i>d</i> is a TP when its Jaccard index exceeds the threshold, and only one <i>d</i> can match an <i>e</i>: the one with the highest Jaccard index. Suited for event density, but the threshold must be defined.", None))
    # retranslateUi

