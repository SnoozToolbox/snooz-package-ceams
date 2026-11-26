# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ArtIntroStepPL.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_ArtIntroStepPL(object):
    def setupUi(self, ArtIntroStepPL):
        if not ArtIntroStepPL.objectName():
            ArtIntroStepPL.setObjectName(u"ArtIntroStepPL")
        ArtIntroStepPL.resize(900, 700)
        self.verticalLayout = QVBoxLayout(ArtIntroStepPL)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(ArtIntroStepPL)
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

        self.artifacts_section_layout = QVBoxLayout()
        self.artifacts_section_layout.setSpacing(8)
        self.artifacts_section_layout.setObjectName(u"artifacts_section_layout")
        self.label = QLabel(self.content_widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.artifacts_section_layout.addWidget(self.label)

        self.artifacts_card = QFrame(self.content_widget)
        self.artifacts_card.setObjectName(u"artifacts_card")
        self.artifacts_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.artifacts_card.setFrameShadow(QFrame.Shadow.Raised)
        self.artifacts_card_layout = QVBoxLayout(self.artifacts_card)
        self.artifacts_card_layout.setSpacing(10)
        self.artifacts_card_layout.setObjectName(u"artifacts_card_layout")
        self.artifacts_card_layout.setContentsMargins(10, 10, 10, 10)
        self.artifacts_grid = QGridLayout()
        self.artifacts_grid.setObjectName(u"artifacts_grid")
        self.artifacts_grid.setHorizontalSpacing(24)
        self.artifacts_grid.setVerticalSpacing(10)
        self.artifact_1_label = QLabel(self.artifacts_card)
        self.artifact_1_label.setObjectName(u"artifact_1_label")
        self.artifact_1_label.setTextFormat(Qt.TextFormat.RichText)
        self.artifact_1_label.setWordWrap(True)
        self.artifact_1_label.setProperty(u"variant", u"help")
        self.artifact_1_label.setMinimumSize(QSize(250, 0))
        self.artifact_1_label.setMaximumSize(QSize(250, 16777215))

        self.artifacts_grid.addWidget(self.artifact_1_label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.label_6 = QLabel(self.artifacts_card)
        self.label_6.setObjectName(u"label_6")

        self.artifacts_grid.addWidget(self.label_6, 0, 1, 1, 1)

        self.artifact_line_2 = QFrame(self.artifacts_card)
        self.artifact_line_2.setObjectName(u"artifact_line_2")
        self.artifact_line_2.setFrameShape(QFrame.Shape.HLine)
        self.artifact_line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.artifacts_grid.addWidget(self.artifact_line_2, 1, 0, 1, 2)

        self.artifact_2_label = QLabel(self.artifacts_card)
        self.artifact_2_label.setObjectName(u"artifact_2_label")
        self.artifact_2_label.setTextFormat(Qt.TextFormat.RichText)
        self.artifact_2_label.setWordWrap(True)
        self.artifact_2_label.setProperty(u"variant", u"help")
        self.artifact_2_label.setMinimumSize(QSize(250, 0))
        self.artifact_2_label.setMaximumSize(QSize(250, 16777215))

        self.artifacts_grid.addWidget(self.artifact_2_label, 2, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.label_8 = QLabel(self.artifacts_card)
        self.label_8.setObjectName(u"label_8")

        self.artifacts_grid.addWidget(self.label_8, 2, 1, 1, 1)

        self.artifact_line_3 = QFrame(self.artifacts_card)
        self.artifact_line_3.setObjectName(u"artifact_line_3")
        self.artifact_line_3.setFrameShape(QFrame.Shape.HLine)
        self.artifact_line_3.setFrameShadow(QFrame.Shadow.Plain)

        self.artifacts_grid.addWidget(self.artifact_line_3, 3, 0, 1, 2)

        self.artifact_3_label = QLabel(self.artifacts_card)
        self.artifact_3_label.setObjectName(u"artifact_3_label")
        self.artifact_3_label.setTextFormat(Qt.TextFormat.RichText)
        self.artifact_3_label.setWordWrap(True)
        self.artifact_3_label.setProperty(u"variant", u"help")
        self.artifact_3_label.setMinimumSize(QSize(250, 0))
        self.artifact_3_label.setMaximumSize(QSize(250, 16777215))

        self.artifacts_grid.addWidget(self.artifact_3_label, 4, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.label_5 = QLabel(self.artifacts_card)
        self.label_5.setObjectName(u"label_5")

        self.artifacts_grid.addWidget(self.label_5, 4, 1, 1, 1)

        self.artifact_line_4 = QFrame(self.artifacts_card)
        self.artifact_line_4.setObjectName(u"artifact_line_4")
        self.artifact_line_4.setFrameShape(QFrame.Shape.HLine)
        self.artifact_line_4.setFrameShadow(QFrame.Shadow.Plain)

        self.artifacts_grid.addWidget(self.artifact_line_4, 5, 0, 1, 2)

        self.artifact_4_label = QLabel(self.artifacts_card)
        self.artifact_4_label.setObjectName(u"artifact_4_label")
        self.artifact_4_label.setTextFormat(Qt.TextFormat.RichText)
        self.artifact_4_label.setWordWrap(True)
        self.artifact_4_label.setProperty(u"variant", u"help")
        self.artifact_4_label.setMinimumSize(QSize(250, 0))
        self.artifact_4_label.setMaximumSize(QSize(250, 16777215))

        self.artifacts_grid.addWidget(self.artifact_4_label, 6, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.label_9 = QLabel(self.artifacts_card)
        self.label_9.setObjectName(u"label_9")

        self.artifacts_grid.addWidget(self.label_9, 6, 1, 1, 1)

        self.artifact_line_5 = QFrame(self.artifacts_card)
        self.artifact_line_5.setObjectName(u"artifact_line_5")
        self.artifact_line_5.setFrameShape(QFrame.Shape.HLine)
        self.artifact_line_5.setFrameShadow(QFrame.Shadow.Plain)

        self.artifacts_grid.addWidget(self.artifact_line_5, 7, 0, 1, 2)

        self.artifact_5_label = QLabel(self.artifacts_card)
        self.artifact_5_label.setObjectName(u"artifact_5_label")
        self.artifact_5_label.setTextFormat(Qt.TextFormat.RichText)
        self.artifact_5_label.setWordWrap(True)
        self.artifact_5_label.setProperty(u"variant", u"help")
        self.artifact_5_label.setMinimumSize(QSize(250, 0))
        self.artifact_5_label.setMaximumSize(QSize(250, 16777215))

        self.artifacts_grid.addWidget(self.artifact_5_label, 8, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.label_10 = QLabel(self.artifacts_card)
        self.label_10.setObjectName(u"label_10")

        self.artifacts_grid.addWidget(self.label_10, 8, 1, 1, 1)

        self.artifact_line_6 = QFrame(self.artifacts_card)
        self.artifact_line_6.setObjectName(u"artifact_line_6")
        self.artifact_line_6.setFrameShape(QFrame.Shape.HLine)
        self.artifact_line_6.setFrameShadow(QFrame.Shadow.Plain)

        self.artifacts_grid.addWidget(self.artifact_line_6, 9, 0, 1, 2)

        self.artifact_6_label = QLabel(self.artifacts_card)
        self.artifact_6_label.setObjectName(u"artifact_6_label")
        self.artifact_6_label.setTextFormat(Qt.TextFormat.RichText)
        self.artifact_6_label.setWordWrap(True)
        self.artifact_6_label.setProperty(u"variant", u"help")
        self.artifact_6_label.setMinimumSize(QSize(250, 0))
        self.artifact_6_label.setMaximumSize(QSize(250, 16777215))

        self.artifacts_grid.addWidget(self.artifact_6_label, 10, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.label_11 = QLabel(self.artifacts_card)
        self.label_11.setObjectName(u"label_11")

        self.artifacts_grid.addWidget(self.label_11, 10, 1, 1, 1)

        self.artifacts_grid.setColumnStretch(1, 1)

        self.artifacts_card_layout.addLayout(self.artifacts_grid)

        self.artifacts_caption_label = QLabel(self.artifacts_card)
        self.artifacts_caption_label.setObjectName(u"artifacts_caption_label")
        self.artifacts_caption_label.setFont(font2)
        self.artifacts_caption_label.setWordWrap(True)
        self.artifacts_caption_label.setProperty(u"variant", u"help")

        self.artifacts_card_layout.addWidget(self.artifacts_caption_label)


        self.artifacts_section_layout.addWidget(self.artifacts_card)


        self.content_layout.addLayout(self.artifacts_section_layout)

        self.about_detection_layout = QVBoxLayout()
        self.about_detection_layout.setSpacing(6)
        self.about_detection_layout.setObjectName(u"about_detection_layout")
        self.about_detection_title_label = QLabel(self.content_widget)
        self.about_detection_title_label.setObjectName(u"about_detection_title_label")
        self.about_detection_title_label.setFont(font3)

        self.about_detection_layout.addWidget(self.about_detection_title_label)

        self.about_detection_label = QLabel(self.content_widget)
        self.about_detection_label.setObjectName(u"about_detection_label")
        self.about_detection_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_detection_label.setWordWrap(True)
        self.about_detection_label.setProperty(u"variant", u"help")

        self.about_detection_layout.addWidget(self.about_detection_label)


        self.content_layout.addLayout(self.about_detection_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ArtIntroStepPL)

        QMetaObject.connectSlotsByName(ArtIntroStepPL)
    # setupUi

    def retranslateUi(self, ArtIntroStepPL):
        ArtIntroStepPL.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Detect EEG Artifacts", None))
        self.subtitle_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Detects the artifacts of the EEG channels of your polysomnography (PSG) files with six detectors, and adds them as events to the accessory file.", None))
        self.steps_title_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"What you will do", None))
        self.step_1_number_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"1", None))
        self.step_1_name_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Input Files", None))
        self.step_1_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Add the PSG files and select their channels. In \"Alias\", add the EEG channels to \"EEG\" and an EMG channel to \"EMG\". The EMG only helps the muscle artifact detector. Without an EMG channel, write NA in \"EMG\".", None))
        self.step_2_number_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"2", None))
        self.step_2_name_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Filter EEG signals", None))
        self.step_2_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Choose the bandpass filter and the power line notch filter applied before the detection.", None))
        self.step_3_number_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"3", None))
        self.step_3_name_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Non valid events", None))
        self.step_3_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Select the events already excluded from the analysis, such as bad channels or bad epochs.", None))
        self.step_4_number_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"4", None))
        self.step_4_name_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Stage Selection", None))
        self.step_4_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Select the sleep stages in which artifacts are detected, and a set of default thresholds.", None))
        self.step_5_number_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"5", None))
        self.step_5_name_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Detectors Settings", None))
        self.step_5_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Check the detectors to run and choose the group and name of the artifact events. Each detector has its own page with its thresholds.", None))
        self.files_title_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Accepted files", None))
        self.file_1_name_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"EDF", None))
        self.file_1_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"The .edf and .tsv files have the same filename and are in the same directory.", None))
        self.file_2_name_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Stellate", None))
        self.file_2_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"The .sig and .sts files have the same filename and are in the same directory.", None))
        self.file_3_name_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"NATUS", None))
        self.file_3_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"The entire NATUS subject folder is required <i>(for CEAMS users)</i>.", None))
        self.label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Artifacts detected", None))
        self.artifact_1_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"<b>Flatline</b><br/>Segments of low power, where the signal is nearly flat.", None))
        self.artifact_2_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"<b>High frequency burst</b><br/>Short bursts of power above 25\u00a0Hz.", None))
        self.artifact_3_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"<b>Persistent noise</b><br/>Lasting noise above 25\u00a0Hz.", None))
        self.artifact_4_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"<b>Power line contamination</b><br/>Power at 50 or 60\u00a0Hz.", None))
        self.artifact_5_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"<b>Baseline variation</b><br/>Power below 0.4\u00a0Hz, from breathing or sweat.", None))
        self.artifact_6_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"<b>Muscle artifact</b><br/>Bursts of activity between 20.25 and 32\u00a0Hz.", None))
        self.artifacts_caption_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"Simulated EEG. Each detector is described in its own page.", None))
        self.about_detection_title_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"About the detection", None))
        self.about_detection_label.setText(QCoreApplication.translate("ArtIntroStepPL", u"<b>How the detectors work</b><br/>\u2022 Each detector computes the spectral power of the EEG on sliding windows (Welch's method).<br/>\u2022 It flags the windows whose power exceeds its thresholds.<br/>\u2022 Several thresholds depend on the power distribution of the selected stages.<br/><br/><b>The artifact events</b><br/>\u2022 The artifacts are added as events to the accessory file of each PSG file (.tsv, .sts or .ent). Snooz creates the .tsv file of an EDF file when it is absent.<br/>\u2022 The events with the same group and name are replaced.<br/>\u2022 The name of each event ends with @@ and its channel, as in EDFbrowser, for example art_snooz_set1_NREM@@C3.<br/><br/>The documentation of the tool (\"Read more!\" below) describes each detector and its settings.", None))
    # retranslateUi

