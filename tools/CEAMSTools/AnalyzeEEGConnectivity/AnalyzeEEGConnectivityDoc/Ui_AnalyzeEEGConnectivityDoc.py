# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AnalyzeEEGConnectivityDoc.ui'
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

class Ui_AnalyzeEEGConnectivityDoc(object):
    def setupUi(self, AnalyzeEEGConnectivityDoc):
        if not AnalyzeEEGConnectivityDoc.objectName():
            AnalyzeEEGConnectivityDoc.setObjectName(u"AnalyzeEEGConnectivityDoc")
        AnalyzeEEGConnectivityDoc.resize(900, 700)
        self.verticalLayout = QVBoxLayout(AnalyzeEEGConnectivityDoc)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(AnalyzeEEGConnectivityDoc)
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

        self.before_info = QFrame(self.content_widget)
        self.before_info.setObjectName(u"before_info")
        self.before_info.setFrameShape(QFrame.Shape.NoFrame)
        self.before_info.setProperty(u"variant", u"info")
        self.before_info_layout = QHBoxLayout(self.before_info)
        self.before_info_layout.setObjectName(u"before_info_layout")
        self.before_info_layout.setContentsMargins(14, 10, 14, 10)
        self.before_info_label = QLabel(self.before_info)
        self.before_info_label.setObjectName(u"before_info_label")
        self.before_info_label.setTextFormat(Qt.TextFormat.RichText)
        self.before_info_label.setWordWrap(True)

        self.before_info_layout.addWidget(self.before_info_label)


        self.content_layout.addWidget(self.before_info)

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

        self.step_line_5 = QFrame(self.steps_card)
        self.step_line_5.setObjectName(u"step_line_5")
        self.step_line_5.setFrameShape(QFrame.Shape.HLine)
        self.step_line_5.setFrameShadow(QFrame.Shadow.Plain)

        self.steps_grid.addWidget(self.step_line_5, 7, 0, 1, 4)

        self.step_5_number_label = QLabel(self.steps_card)
        self.step_5_number_label.setObjectName(u"step_5_number_label")
        self.step_5_number_label.setFont(font2)
        self.step_5_number_label.setProperty(u"variant", u"step_number")
        self.step_5_number_label.setMinimumSize(QSize(24, 24))
        self.step_5_number_label.setMaximumSize(QSize(24, 24))
        self.step_5_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.steps_grid.addWidget(self.step_5_number_label, 8, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.step_5_name_label = QLabel(self.steps_card)
        self.step_5_name_label.setObjectName(u"step_5_name_label")
        self.step_5_name_label.setFont(font3)
        self.step_5_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_5_name_label, 8, 1, 1, 1)

        self.step_5_label = QLabel(self.steps_card)
        self.step_5_label.setObjectName(u"step_5_label")
        self.step_5_label.setWordWrap(True)
        self.step_5_label.setProperty(u"variant", u"help")
        self.step_5_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_5_label, 8, 3, 1, 1)

        self.step_line_6 = QFrame(self.steps_card)
        self.step_line_6.setObjectName(u"step_line_6")
        self.step_line_6.setFrameShape(QFrame.Shape.HLine)
        self.step_line_6.setFrameShadow(QFrame.Shadow.Plain)

        self.steps_grid.addWidget(self.step_line_6, 9, 0, 1, 4)

        self.step_6_number_label = QLabel(self.steps_card)
        self.step_6_number_label.setObjectName(u"step_6_number_label")
        self.step_6_number_label.setFont(font2)
        self.step_6_number_label.setProperty(u"variant", u"step_number")
        self.step_6_number_label.setMinimumSize(QSize(24, 24))
        self.step_6_number_label.setMaximumSize(QSize(24, 24))
        self.step_6_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.steps_grid.addWidget(self.step_6_number_label, 10, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.step_6_name_label = QLabel(self.steps_card)
        self.step_6_name_label.setObjectName(u"step_6_name_label")
        self.step_6_name_label.setFont(font3)
        self.step_6_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_6_name_label, 10, 1, 1, 1)

        self.step_6_label = QLabel(self.steps_card)
        self.step_6_label.setObjectName(u"step_6_label")
        self.step_6_label.setWordWrap(True)
        self.step_6_label.setProperty(u"variant", u"help")
        self.step_6_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_6_label, 10, 3, 1, 1)

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


        self.retranslateUi(AnalyzeEEGConnectivityDoc)
        self.methods_show_button.clicked.connect(self.methods_widget.show)
        self.methods_show_button.clicked.connect(self.methods_hide_button.show)
        self.methods_show_button.clicked.connect(self.methods_show_button.hide)
        self.methods_hide_button.clicked.connect(self.methods_widget.hide)
        self.methods_hide_button.clicked.connect(self.methods_show_button.show)
        self.methods_hide_button.clicked.connect(self.methods_hide_button.hide)

        QMetaObject.connectSlotsByName(AnalyzeEEGConnectivityDoc)
    # setupUi

    def retranslateUi(self, AnalyzeEEGConnectivityDoc):
        AnalyzeEEGConnectivityDoc.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"Analyze EEG Functional Connectivity", None))
        self.subtitle_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"Computes the functional connectivity between the EEG channels of your polysomnography (PSG) files with the weighted phase lag index (wPLI), the directed phase lag index (dPLI) or the amplitude envelope correlation (AEC), and the network properties of the wPLI connectivity.", None))
        self.before_info_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"<b>Before you start</b><br/>Mark the non-brain channels, the noisy channels and the noisy epochs with the app \"Inspect EEG channels\". The connectivity is computed on brain EEG channels only: the channels marked with the group <i>art_inspector</i> and the name <i>art_channel</i> or <i>non_brain</i> are excluded automatically. At least 2 brain EEG channels are required.", None))
        self.steps_title_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"What you will do", None))
        self.step_1_number_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"1", None))
        self.step_1_name_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"Input Files", None))
        self.step_1_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"Add the PSG files, then define the montage and the channels of each file.", None))
        self.step_2_number_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"2", None))
        self.step_2_name_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"Events Exclusion", None))
        self.step_2_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"Select the events to exclude from the analysis, such as artefacts already detected and saved in the accessory file.", None))
        self.step_3_number_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"3", None))
        self.step_3_name_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"Filter Settings", None))
        self.step_3_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"Choose the frequency band (full band, delta, theta, alpha, beta or a custom band) and the part of the recording to analyse: chosen sleep stages, the whole recording or a segment of it (unscored), or chosen annotations.", None))
        self.step_4_number_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"4", None))
        self.step_4_name_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"Annotation Selection", None))
        self.step_4_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"Only when the analysis is performed on specific annotations.", None))
        self.step_5_number_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"5", None))
        self.step_5_name_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"Connectivity Settings", None))
        self.step_5_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"wPLI, dPLI or AEC, the epoch length and overlap, the statistical testing (number of surrogates and p-value) and the threshold of the network properties.", None))
        self.step_6_number_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"6", None))
        self.step_6_name_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"Output Files", None))
        self.step_6_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"Choose where the output files are saved: in the folder of each recording or in a folder you choose.", None))
        self.files_title_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"Accepted files", None))
        self.file_1_name_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"EDF", None))
        self.file_1_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"The .edf and .tsv files have the same filename and are in the same directory.", None))
        self.file_2_name_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"Stellate", None))
        self.file_2_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"The .sig and .sts files have the same filename and are in the same directory.", None))
        self.file_3_name_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"NATUS", None))
        self.file_3_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"The entire NATUS subject folder is required <i>(for CEAMS users)</i>.", None))
        self.methods_show_button.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"\u203a Methods and references", None))
        self.methods_hide_button.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"\u2304 Methods and references", None))
        self.methods_note_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"The details of each setting are shown in its own step.", None))
        self.methods_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"<b>Weighted phase lag index (wPLI) [1]:</b> quantifies the strength of the non-zero phase-lagged connectivity between EEG channels, emphasizing the stronger, more consistent interactions while minimizing the influence of noise and common sources.<br/><br/><b>Directed phase lag index (dPLI) [2]:</b> a measure of directional functional connectivity, based on the consistency of the phase lead-lag relationship between EEG channels, insensitive to volume conduction.<br/><br/><b>Amplitude envelope correlation (AEC) [3]:</b> quantifies the functional connectivity by the correlation between the amplitude envelopes of the EEG signals. To reduce the spurious connectivity due to signal leakage (volume conduction), the signals are orthogonalized before the envelope extraction.<br/><br/><b>Statistical testing [4]:</b> for wPLI and dPLI only, the connections that could appear by chance are removed by comparing each connection with time-shifted surrogates.<br/><br/><b>Network properties [5]:</b> graph-theoretical metrics of "
                        "the wPLI connectivity matrix only: characteristic path length, clustering coefficient, global efficiency, small-worldness, modularity and participation coefficient, each normalized against a random null-model network. They require wPLI and at least 32 brain EEG channels; otherwise they are skipped.", None))
        self.references_label.setText(QCoreApplication.translate("AnalyzeEEGConnectivityDoc", u"[1] Vinck, M., Oostenveld, R., van Wingerden, M., Battaglia, F., &amp; Pennartz, C. M. A. (2011). An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. <i>NeuroImage</i>, <i>55</i>(4), 1548\u20131565. <a href=\"https://doi.org/10.1016/j.neuroimage.2011.01.055\">https://doi.org/10.1016/j.neuroimage.2011.01.055</a><br/>[2] Stam, C. J., &amp; van Straaten, E. C. W. (2012). Go with the flow: Use of a directed phase lag index (dPLI) to characterize patterns of phase relations in a large-scale model of brain dynamics. <i>NeuroImage</i>, <i>62</i>(3), 1415\u20131428. <a href=\"https://doi.org/10.1016/j.neuroimage.2012.05.050\">https://doi.org/10.1016/j.neuroimage.2012.05.050</a><br/>[3] Hipp, J. F., Hawellek, D. J., Corbetta, M., Siegel, M., &amp; Engel, A. K. (2012). Large-scale cortical correlation structure of spontaneous oscillatory activity. <i>Nature Neuroscience</i>, <i>15</i>(6), 884\u2013890. <a href=\"https://doi.org/10.103"
                        "8/nn.3101\">https://doi.org/10.1038/nn.3101</a><br/>[4] Duclos, C., Maschke, C., Mahdid, Y., Nadin, D., Rokos, A., Arbour, C., Badawy, M., L\u00e9tourneau, J., Owen, A. M., Plourde, G., &amp; Blain-Moraes, S. (2022). Brain responses to propofol in advance of recovery from coma and disorders of consciousness: A preliminary study. <i>American Journal of Respiratory and Critical Care Medicine</i>, <i>205</i>(2), 171\u2013182. <a href=\"https://doi.org/10.1164/rccm.202105-1223OC\">https://doi.org/10.1164/rccm.202105-1223OC</a><br/>[5] Rubinov, M., &amp; Sporns, O. (2010). Complex network measures of brain connectivity: Uses and interpretations. <i>NeuroImage</i>, <i>52</i>(3), 1059\u20131069. <a href=\"https://doi.org/10.1016/j.neuroimage.2009.10.003\">https://doi.org/10.1016/j.neuroimage.2009.10.003</a>", None))
    # retranslateUi

