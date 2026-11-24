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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
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

        self.folder_card = QFrame(self.content_widget)
        self.folder_card.setObjectName(u"folder_card")
        self.folder_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.folder_card.setFrameShadow(QFrame.Shadow.Raised)
        self.folder_card_layout = QVBoxLayout(self.folder_card)
        self.folder_card_layout.setSpacing(10)
        self.folder_card_layout.setObjectName(u"folder_card_layout")
        self.folder_card_layout.setContentsMargins(10, 10, 10, 10)
        self.folder_title_label = QLabel(self.folder_card)
        self.folder_title_label.setObjectName(u"folder_title_label")
        font1 = QFont()
        font1.setBold(True)
        self.folder_title_label.setFont(font1)

        self.folder_card_layout.addWidget(self.folder_title_label)

        self.output_path_checkBox = QCheckBox(self.folder_card)
        self.output_path_checkBox.setObjectName(u"output_path_checkBox")
        self.output_path_checkBox.setChecked(False)

        self.folder_card_layout.addWidget(self.output_path_checkBox)

        self.folder_help_label = QLabel(self.folder_card)
        self.folder_help_label.setObjectName(u"folder_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.folder_help_label.setFont(font2)
        self.folder_help_label.setWordWrap(True)
        self.folder_help_label.setIndent(26)
        self.folder_help_label.setProperty(u"variant", u"help")

        self.folder_card_layout.addWidget(self.folder_help_label)

        self.path_layout = QHBoxLayout()
        self.path_layout.setSpacing(8)
        self.path_layout.setObjectName(u"path_layout")
        self.path_label = QLabel(self.folder_card)
        self.path_label.setObjectName(u"path_label")

        self.path_layout.addWidget(self.path_label)

        self.path_lineEdit = QLineEdit(self.folder_card)
        self.path_lineEdit.setObjectName(u"path_lineEdit")

        self.path_layout.addWidget(self.path_lineEdit)

        self.choose_pushButton = QPushButton(self.folder_card)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.path_layout.addWidget(self.choose_pushButton)


        self.folder_card_layout.addLayout(self.path_layout)


        self.content_layout.addWidget(self.folder_card)

        self.outputs_card = QFrame(self.content_widget)
        self.outputs_card.setObjectName(u"outputs_card")
        self.outputs_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.outputs_card.setFrameShadow(QFrame.Shadow.Raised)
        self.outputs_card_layout = QVBoxLayout(self.outputs_card)
        self.outputs_card_layout.setSpacing(10)
        self.outputs_card_layout.setObjectName(u"outputs_card_layout")
        self.outputs_card_layout.setContentsMargins(10, 10, 10, 10)
        self.outputs_title_label = QLabel(self.outputs_card)
        self.outputs_title_label.setObjectName(u"outputs_title_label")
        self.outputs_title_label.setFont(font1)

        self.outputs_card_layout.addWidget(self.outputs_title_label)

        self.outputs_help_label = QLabel(self.outputs_card)
        self.outputs_help_label.setObjectName(u"outputs_help_label")
        self.outputs_help_label.setWordWrap(True)
        self.outputs_help_label.setProperty(u"variant", u"help")

        self.outputs_card_layout.addWidget(self.outputs_help_label)

        self.outputs_grid = QGridLayout()
        self.outputs_grid.setObjectName(u"outputs_grid")
        self.outputs_grid.setHorizontalSpacing(24)
        self.outputs_grid.setVerticalSpacing(8)
        self.output_1_name_label = QLabel(self.outputs_card)
        self.output_1_name_label.setObjectName(u"output_1_name_label")
        self.output_1_name_label.setTextFormat(Qt.TextFormat.RichText)
        self.output_1_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.outputs_grid.addWidget(self.output_1_name_label, 0, 0, 1, 1)

        self.output_1_label = QLabel(self.outputs_card)
        self.output_1_label.setObjectName(u"output_1_label")
        self.output_1_label.setTextFormat(Qt.TextFormat.RichText)
        self.output_1_label.setWordWrap(True)
        self.output_1_label.setProperty(u"variant", u"help")
        self.output_1_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.outputs_grid.addWidget(self.output_1_label, 0, 1, 1, 1)

        self.output_line_2 = QFrame(self.outputs_card)
        self.output_line_2.setObjectName(u"output_line_2")
        self.output_line_2.setFrameShape(QFrame.Shape.HLine)
        self.output_line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.outputs_grid.addWidget(self.output_line_2, 1, 0, 1, 2)

        self.output_2_name_label = QLabel(self.outputs_card)
        self.output_2_name_label.setObjectName(u"output_2_name_label")
        self.output_2_name_label.setTextFormat(Qt.TextFormat.RichText)
        self.output_2_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.outputs_grid.addWidget(self.output_2_name_label, 2, 0, 1, 1)

        self.output_2_label = QLabel(self.outputs_card)
        self.output_2_label.setObjectName(u"output_2_label")
        self.output_2_label.setTextFormat(Qt.TextFormat.RichText)
        self.output_2_label.setWordWrap(True)
        self.output_2_label.setProperty(u"variant", u"help")
        self.output_2_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.outputs_grid.addWidget(self.output_2_label, 2, 1, 1, 1)

        self.output_line_3 = QFrame(self.outputs_card)
        self.output_line_3.setObjectName(u"output_line_3")
        self.output_line_3.setFrameShape(QFrame.Shape.HLine)
        self.output_line_3.setFrameShadow(QFrame.Shadow.Plain)

        self.outputs_grid.addWidget(self.output_line_3, 3, 0, 1, 2)

        self.output_3_name_label = QLabel(self.outputs_card)
        self.output_3_name_label.setObjectName(u"output_3_name_label")
        self.output_3_name_label.setTextFormat(Qt.TextFormat.RichText)
        self.output_3_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.outputs_grid.addWidget(self.output_3_name_label, 4, 0, 1, 1)

        self.output_3_label = QLabel(self.outputs_card)
        self.output_3_label.setObjectName(u"output_3_label")
        self.output_3_label.setTextFormat(Qt.TextFormat.RichText)
        self.output_3_label.setWordWrap(True)
        self.output_3_label.setProperty(u"variant", u"help")
        self.output_3_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.outputs_grid.addWidget(self.output_3_label, 4, 1, 1, 1)

        self.output_line_4 = QFrame(self.outputs_card)
        self.output_line_4.setObjectName(u"output_line_4")
        self.output_line_4.setFrameShape(QFrame.Shape.HLine)
        self.output_line_4.setFrameShadow(QFrame.Shadow.Plain)

        self.outputs_grid.addWidget(self.output_line_4, 5, 0, 1, 2)

        self.output_4_name_label = QLabel(self.outputs_card)
        self.output_4_name_label.setObjectName(u"output_4_name_label")
        self.output_4_name_label.setTextFormat(Qt.TextFormat.RichText)
        self.output_4_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.outputs_grid.addWidget(self.output_4_name_label, 6, 0, 1, 1)

        self.output_4_label = QLabel(self.outputs_card)
        self.output_4_label.setObjectName(u"output_4_label")
        self.output_4_label.setTextFormat(Qt.TextFormat.RichText)
        self.output_4_label.setWordWrap(True)
        self.output_4_label.setProperty(u"variant", u"help")
        self.output_4_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.outputs_grid.addWidget(self.output_4_label, 6, 1, 1, 1)

        self.output_line_5 = QFrame(self.outputs_card)
        self.output_line_5.setObjectName(u"output_line_5")
        self.output_line_5.setFrameShape(QFrame.Shape.HLine)
        self.output_line_5.setFrameShadow(QFrame.Shadow.Plain)

        self.outputs_grid.addWidget(self.output_line_5, 7, 0, 1, 2)

        self.output_5_name_label = QLabel(self.outputs_card)
        self.output_5_name_label.setObjectName(u"output_5_name_label")
        self.output_5_name_label.setTextFormat(Qt.TextFormat.RichText)
        self.output_5_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.outputs_grid.addWidget(self.output_5_name_label, 8, 0, 1, 1)

        self.output_5_label = QLabel(self.outputs_card)
        self.output_5_label.setObjectName(u"output_5_label")
        self.output_5_label.setTextFormat(Qt.TextFormat.RichText)
        self.output_5_label.setWordWrap(True)
        self.output_5_label.setProperty(u"variant", u"help")
        self.output_5_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.outputs_grid.addWidget(self.output_5_label, 8, 1, 1, 1)

        self.outputs_grid.setColumnStretch(1, 1)

        self.outputs_card_layout.addLayout(self.outputs_grid)


        self.content_layout.addWidget(self.outputs_card)

        self.about_values_layout = QVBoxLayout()
        self.about_values_layout.setSpacing(6)
        self.about_values_layout.setObjectName(u"about_values_layout")
        self.about_values_title_label = QLabel(self.content_widget)
        self.about_values_title_label.setObjectName(u"about_values_title_label")
        self.about_values_title_label.setFont(font1)

        self.about_values_layout.addWidget(self.about_values_title_label)

        self.about_values_label = QLabel(self.content_widget)
        self.about_values_label.setObjectName(u"about_values_label")
        self.about_values_label.setWordWrap(True)
        self.about_values_label.setProperty(u"variant", u"help")

        self.about_values_layout.addWidget(self.about_values_label)

        self.values_grid = QGridLayout()
        self.values_grid.setObjectName(u"values_grid")
        self.values_grid.setHorizontalSpacing(20)
        self.values_grid.setVerticalSpacing(6)
        self.values_grid_header_0 = QLabel(self.content_widget)
        self.values_grid_header_0.setObjectName(u"values_grid_header_0")
        self.values_grid_header_0.setTextFormat(Qt.TextFormat.RichText)
        self.values_grid_header_0.setWordWrap(True)
        self.values_grid_header_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.values_grid.addWidget(self.values_grid_header_0, 0, 0, 1, 1)

        self.values_grid_header_1 = QLabel(self.content_widget)
        self.values_grid_header_1.setObjectName(u"values_grid_header_1")
        self.values_grid_header_1.setTextFormat(Qt.TextFormat.RichText)
        self.values_grid_header_1.setWordWrap(True)
        self.values_grid_header_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.values_grid.addWidget(self.values_grid_header_1, 0, 1, 1, 1)

        self.values_grid_header_2 = QLabel(self.content_widget)
        self.values_grid_header_2.setObjectName(u"values_grid_header_2")
        self.values_grid_header_2.setTextFormat(Qt.TextFormat.RichText)
        self.values_grid_header_2.setWordWrap(True)
        self.values_grid_header_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.values_grid.addWidget(self.values_grid_header_2, 0, 2, 1, 1)

        self.values_grid_line = QFrame(self.content_widget)
        self.values_grid_line.setObjectName(u"values_grid_line")
        self.values_grid_line.setFrameShape(QFrame.Shape.HLine)
        self.values_grid_line.setFrameShadow(QFrame.Shadow.Plain)

        self.values_grid.addWidget(self.values_grid_line, 1, 0, 1, 3)

        self.values_grid_1_0 = QLabel(self.content_widget)
        self.values_grid_1_0.setObjectName(u"values_grid_1_0")
        self.values_grid_1_0.setWordWrap(True)
        self.values_grid_1_0.setProperty(u"variant", u"help")
        self.values_grid_1_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.values_grid.addWidget(self.values_grid_1_0, 2, 0, 1, 1)

        self.values_grid_1_1 = QLabel(self.content_widget)
        self.values_grid_1_1.setObjectName(u"values_grid_1_1")
        self.values_grid_1_1.setWordWrap(True)
        self.values_grid_1_1.setProperty(u"variant", u"help")
        self.values_grid_1_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.values_grid.addWidget(self.values_grid_1_1, 2, 1, 1, 1)

        self.values_grid_1_2 = QLabel(self.content_widget)
        self.values_grid_1_2.setObjectName(u"values_grid_1_2")
        self.values_grid_1_2.setWordWrap(True)
        self.values_grid_1_2.setProperty(u"variant", u"help")
        self.values_grid_1_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.values_grid.addWidget(self.values_grid_1_2, 2, 2, 1, 1)

        self.values_grid_2_0 = QLabel(self.content_widget)
        self.values_grid_2_0.setObjectName(u"values_grid_2_0")
        self.values_grid_2_0.setWordWrap(True)
        self.values_grid_2_0.setProperty(u"variant", u"help")
        self.values_grid_2_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.values_grid.addWidget(self.values_grid_2_0, 3, 0, 1, 1)

        self.values_grid_2_1 = QLabel(self.content_widget)
        self.values_grid_2_1.setObjectName(u"values_grid_2_1")
        self.values_grid_2_1.setWordWrap(True)
        self.values_grid_2_1.setProperty(u"variant", u"help")
        self.values_grid_2_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.values_grid.addWidget(self.values_grid_2_1, 3, 1, 1, 1)

        self.values_grid_2_2 = QLabel(self.content_widget)
        self.values_grid_2_2.setObjectName(u"values_grid_2_2")
        self.values_grid_2_2.setWordWrap(True)
        self.values_grid_2_2.setProperty(u"variant", u"help")
        self.values_grid_2_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.values_grid.addWidget(self.values_grid_2_2, 3, 2, 1, 1)

        self.values_grid_3_0 = QLabel(self.content_widget)
        self.values_grid_3_0.setObjectName(u"values_grid_3_0")
        self.values_grid_3_0.setWordWrap(True)
        self.values_grid_3_0.setProperty(u"variant", u"help")
        self.values_grid_3_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.values_grid.addWidget(self.values_grid_3_0, 4, 0, 1, 1)

        self.values_grid_3_1 = QLabel(self.content_widget)
        self.values_grid_3_1.setObjectName(u"values_grid_3_1")
        self.values_grid_3_1.setWordWrap(True)
        self.values_grid_3_1.setProperty(u"variant", u"help")
        self.values_grid_3_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.values_grid.addWidget(self.values_grid_3_1, 4, 1, 1, 1)

        self.values_grid_3_2 = QLabel(self.content_widget)
        self.values_grid_3_2.setObjectName(u"values_grid_3_2")
        self.values_grid_3_2.setWordWrap(True)
        self.values_grid_3_2.setProperty(u"variant", u"help")
        self.values_grid_3_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.values_grid.addWidget(self.values_grid_3_2, 4, 2, 1, 1)

        self.values_grid.setColumnStretch(2, 1)

        self.about_values_layout.addLayout(self.values_grid)


        self.content_layout.addLayout(self.about_values_layout)

        self.about_plot_layout = QVBoxLayout()
        self.about_plot_layout.setSpacing(6)
        self.about_plot_layout.setObjectName(u"about_plot_layout")
        self.about_plot_title_label = QLabel(self.content_widget)
        self.about_plot_title_label.setObjectName(u"about_plot_title_label")
        self.about_plot_title_label.setFont(font1)

        self.about_plot_layout.addWidget(self.about_plot_title_label)

        self.about_plot_label = QLabel(self.content_widget)
        self.about_plot_label.setObjectName(u"about_plot_label")
        self.about_plot_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_plot_label.setWordWrap(True)
        self.about_plot_label.setProperty(u"variant", u"help")

        self.about_plot_layout.addWidget(self.about_plot_label)

        self.thresholds_label = QLabel(self.content_widget)
        self.thresholds_label.setObjectName(u"thresholds_label")
        self.thresholds_label.setTextFormat(Qt.TextFormat.RichText)
        self.thresholds_label.setWordWrap(True)
        self.thresholds_label.setProperty(u"variant", u"help")

        self.about_plot_layout.addWidget(self.thresholds_label)

        self.thresholds_grid = QGridLayout()
        self.thresholds_grid.setObjectName(u"thresholds_grid")
        self.thresholds_grid.setHorizontalSpacing(20)
        self.thresholds_grid.setVerticalSpacing(6)
        self.thresholds_grid_header_0 = QLabel(self.content_widget)
        self.thresholds_grid_header_0.setObjectName(u"thresholds_grid_header_0")
        self.thresholds_grid_header_0.setTextFormat(Qt.TextFormat.RichText)
        self.thresholds_grid_header_0.setWordWrap(True)
        self.thresholds_grid_header_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_header_0, 0, 0, 1, 1)

        self.thresholds_grid_header_1 = QLabel(self.content_widget)
        self.thresholds_grid_header_1.setObjectName(u"thresholds_grid_header_1")
        self.thresholds_grid_header_1.setTextFormat(Qt.TextFormat.RichText)
        self.thresholds_grid_header_1.setWordWrap(True)
        self.thresholds_grid_header_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_header_1, 0, 1, 1, 1)

        self.thresholds_grid_header_2 = QLabel(self.content_widget)
        self.thresholds_grid_header_2.setObjectName(u"thresholds_grid_header_2")
        self.thresholds_grid_header_2.setTextFormat(Qt.TextFormat.RichText)
        self.thresholds_grid_header_2.setWordWrap(True)
        self.thresholds_grid_header_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_header_2, 0, 2, 1, 1)

        self.thresholds_grid_header_3 = QLabel(self.content_widget)
        self.thresholds_grid_header_3.setObjectName(u"thresholds_grid_header_3")
        self.thresholds_grid_header_3.setTextFormat(Qt.TextFormat.RichText)
        self.thresholds_grid_header_3.setWordWrap(True)
        self.thresholds_grid_header_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_header_3, 0, 3, 1, 1)

        self.thresholds_grid_header_4 = QLabel(self.content_widget)
        self.thresholds_grid_header_4.setObjectName(u"thresholds_grid_header_4")
        self.thresholds_grid_header_4.setTextFormat(Qt.TextFormat.RichText)
        self.thresholds_grid_header_4.setWordWrap(True)
        self.thresholds_grid_header_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_header_4, 0, 4, 1, 1)

        self.thresholds_grid_line = QFrame(self.content_widget)
        self.thresholds_grid_line.setObjectName(u"thresholds_grid_line")
        self.thresholds_grid_line.setFrameShape(QFrame.Shape.HLine)
        self.thresholds_grid_line.setFrameShadow(QFrame.Shadow.Plain)

        self.thresholds_grid.addWidget(self.thresholds_grid_line, 1, 0, 1, 5)

        self.thresholds_grid_1_0 = QLabel(self.content_widget)
        self.thresholds_grid_1_0.setObjectName(u"thresholds_grid_1_0")
        self.thresholds_grid_1_0.setWordWrap(True)
        self.thresholds_grid_1_0.setProperty(u"variant", u"help")
        self.thresholds_grid_1_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_1_0, 2, 0, 1, 1)

        self.thresholds_grid_1_1 = QLabel(self.content_widget)
        self.thresholds_grid_1_1.setObjectName(u"thresholds_grid_1_1")
        self.thresholds_grid_1_1.setWordWrap(True)
        self.thresholds_grid_1_1.setProperty(u"variant", u"help")
        self.thresholds_grid_1_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_1_1, 2, 1, 1, 1)

        self.thresholds_grid_1_2 = QLabel(self.content_widget)
        self.thresholds_grid_1_2.setObjectName(u"thresholds_grid_1_2")
        self.thresholds_grid_1_2.setWordWrap(True)
        self.thresholds_grid_1_2.setProperty(u"variant", u"help")
        self.thresholds_grid_1_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_1_2, 2, 2, 1, 1)

        self.thresholds_grid_1_3 = QLabel(self.content_widget)
        self.thresholds_grid_1_3.setObjectName(u"thresholds_grid_1_3")
        self.thresholds_grid_1_3.setWordWrap(True)
        self.thresholds_grid_1_3.setProperty(u"variant", u"help")
        self.thresholds_grid_1_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_1_3, 2, 3, 1, 1)

        self.thresholds_grid_1_4 = QLabel(self.content_widget)
        self.thresholds_grid_1_4.setObjectName(u"thresholds_grid_1_4")
        self.thresholds_grid_1_4.setWordWrap(True)
        self.thresholds_grid_1_4.setProperty(u"variant", u"help")
        self.thresholds_grid_1_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_1_4, 2, 4, 1, 1)

        self.thresholds_grid_2_0 = QLabel(self.content_widget)
        self.thresholds_grid_2_0.setObjectName(u"thresholds_grid_2_0")
        self.thresholds_grid_2_0.setWordWrap(True)
        self.thresholds_grid_2_0.setProperty(u"variant", u"help")
        self.thresholds_grid_2_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_2_0, 3, 0, 1, 1)

        self.thresholds_grid_2_1 = QLabel(self.content_widget)
        self.thresholds_grid_2_1.setObjectName(u"thresholds_grid_2_1")
        self.thresholds_grid_2_1.setWordWrap(True)
        self.thresholds_grid_2_1.setProperty(u"variant", u"help")
        self.thresholds_grid_2_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_2_1, 3, 1, 1, 1)

        self.thresholds_grid_2_2 = QLabel(self.content_widget)
        self.thresholds_grid_2_2.setObjectName(u"thresholds_grid_2_2")
        self.thresholds_grid_2_2.setWordWrap(True)
        self.thresholds_grid_2_2.setProperty(u"variant", u"help")
        self.thresholds_grid_2_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_2_2, 3, 2, 1, 1)

        self.thresholds_grid_2_3 = QLabel(self.content_widget)
        self.thresholds_grid_2_3.setObjectName(u"thresholds_grid_2_3")
        self.thresholds_grid_2_3.setWordWrap(True)
        self.thresholds_grid_2_3.setProperty(u"variant", u"help")
        self.thresholds_grid_2_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_2_3, 3, 3, 1, 1)

        self.thresholds_grid_2_4 = QLabel(self.content_widget)
        self.thresholds_grid_2_4.setObjectName(u"thresholds_grid_2_4")
        self.thresholds_grid_2_4.setWordWrap(True)
        self.thresholds_grid_2_4.setProperty(u"variant", u"help")
        self.thresholds_grid_2_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_2_4, 3, 4, 1, 1)

        self.thresholds_grid_3_0 = QLabel(self.content_widget)
        self.thresholds_grid_3_0.setObjectName(u"thresholds_grid_3_0")
        self.thresholds_grid_3_0.setWordWrap(True)
        self.thresholds_grid_3_0.setProperty(u"variant", u"help")
        self.thresholds_grid_3_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_3_0, 4, 0, 1, 1)

        self.thresholds_grid_3_1 = QLabel(self.content_widget)
        self.thresholds_grid_3_1.setObjectName(u"thresholds_grid_3_1")
        self.thresholds_grid_3_1.setWordWrap(True)
        self.thresholds_grid_3_1.setProperty(u"variant", u"help")
        self.thresholds_grid_3_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_3_1, 4, 1, 1, 1)

        self.thresholds_grid_3_2 = QLabel(self.content_widget)
        self.thresholds_grid_3_2.setObjectName(u"thresholds_grid_3_2")
        self.thresholds_grid_3_2.setWordWrap(True)
        self.thresholds_grid_3_2.setProperty(u"variant", u"help")
        self.thresholds_grid_3_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_3_2, 4, 2, 1, 1)

        self.thresholds_grid_3_3 = QLabel(self.content_widget)
        self.thresholds_grid_3_3.setObjectName(u"thresholds_grid_3_3")
        self.thresholds_grid_3_3.setWordWrap(True)
        self.thresholds_grid_3_3.setProperty(u"variant", u"help")
        self.thresholds_grid_3_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_3_3, 4, 3, 1, 1)

        self.thresholds_grid_3_4 = QLabel(self.content_widget)
        self.thresholds_grid_3_4.setObjectName(u"thresholds_grid_3_4")
        self.thresholds_grid_3_4.setWordWrap(True)
        self.thresholds_grid_3_4.setProperty(u"variant", u"help")
        self.thresholds_grid_3_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.thresholds_grid.addWidget(self.thresholds_grid_3_4, 4, 4, 1, 1)

        self.thresholds_grid.setColumnStretch(0, 1)
        self.thresholds_grid.setColumnStretch(1, 1)
        self.thresholds_grid.setColumnStretch(2, 1)
        self.thresholds_grid.setColumnStretch(3, 1)
        self.thresholds_grid.setColumnStretch(4, 1)

        self.about_plot_layout.addLayout(self.thresholds_grid)

        self.thresholds_help_label = QLabel(self.content_widget)
        self.thresholds_help_label.setObjectName(u"thresholds_help_label")
        self.thresholds_help_label.setFont(font2)
        self.thresholds_help_label.setWordWrap(True)
        self.thresholds_help_label.setProperty(u"variant", u"help")

        self.about_plot_layout.addWidget(self.thresholds_help_label)


        self.content_layout.addLayout(self.about_plot_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(OutputFiles)

        QMetaObject.connectSlotsByName(OutputFiles)
    # setupUi

    def retranslateUi(self, OutputFiles):
        OutputFiles.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("OutputFiles", u"Output Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("OutputFiles", u"Select where the output files are saved.", None))
        self.folder_title_label.setText(QCoreApplication.translate("OutputFiles", u"Output folder", None))
        self.output_path_checkBox.setText(QCoreApplication.translate("OutputFiles", u"Save the output files in the folder of each recording", None))
        self.folder_help_label.setText(QCoreApplication.translate("OutputFiles", u"Otherwise, choose a folder.", None))
        self.path_label.setText(QCoreApplication.translate("OutputFiles", u"Folder", None))
        self.choose_pushButton.setText(QCoreApplication.translate("OutputFiles", u"Choose", None))
        self.outputs_title_label.setText(QCoreApplication.translate("OutputFiles", u"Output files", None))
        self.outputs_help_label.setText(QCoreApplication.translate("OutputFiles", u"Up to five files per recording. &lt;Filename&gt; is the name of the recording and &lt;measure&gt; the connectivity measure: wpli, dpli or aec.", None))
        self.output_1_name_label.setText(QCoreApplication.translate("OutputFiles", u"<b>Connectivity matrix</b><br/>TSV", None))
        self.output_1_label.setText(QCoreApplication.translate("OutputFiles", u"<i>&lt;Filename&gt;_&lt;measure&gt;_convalue.tsv</i><br/>The connection strength between each pair of EEG channels: one row and one column per channel.<br/><b>Saved:</b> always.", None))
        self.output_2_name_label.setText(QCoreApplication.translate("OutputFiles", u"<b>Connectivity heatmap</b><br/>PNG", None))
        self.output_2_label.setText(QCoreApplication.translate("OutputFiles", u"<i>&lt;Filename&gt;_&lt;measure&gt;_conheatmap.png</i><br/>The connectivity matrix in colors: the color of each cell shows the connection strength.<br/><b>Saved:</b> always.", None))
        self.output_3_name_label.setText(QCoreApplication.translate("OutputFiles", u"<b>Head connectivity plot</b><br/>PNG", None))
        self.output_3_label.setText(QCoreApplication.translate("OutputFiles", u"<i>&lt;Filename&gt;_&lt;measure&gt;_contopomap.png</i><br/>The connections between the channels on a head-shaped layout (see About the head connectivity plot).<br/><b>Saved:</b> only when at least 4 EEG channels are found in a standard montage.", None))
        self.output_4_name_label.setText(QCoreApplication.translate("OutputFiles", u"<b>Network properties</b><br/>TSV", None))
        self.output_4_label.setText(QCoreApplication.translate("OutputFiles", u"<i>&lt;Filename&gt;_wpli_net_properties_results.tsv</i><br/>One row per window (Window_number), with the columns:<br/>\u2022 charpath: characteristic path length<br/>\u2022 clustering: clustering coefficient<br/>\u2022 GlobalEfficiency, SmallWorldness, Modularity<br/>\u2022 Participation_coefficient: mean participation coefficient<br/>\u2022 MinSpanTreeThreshold: the threshold selected for the window (minimally spanning tree mode)<br/><b>Saved:</b> only with wPLI and at least 32 channels.", None))
        self.output_5_name_label.setText(QCoreApplication.translate("OutputFiles", u"<b>Participation coefficients</b><br/>TSV", None))
        self.output_5_label.setText(QCoreApplication.translate("OutputFiles", u"<i>&lt;Filename&gt;_wpli_participation_coefficient_results.tsv</i><br/>One row per window (Window_number) and one column per channel: the participation coefficient of each channel.<br/><b>Saved:</b> only with wPLI and at least 32 channels.", None))
        self.about_values_title_label.setText(QCoreApplication.translate("OutputFiles", u"About the values", None))
        self.about_values_label.setText(QCoreApplication.translate("OutputFiles", u"The value range of each measure in the connectivity matrix.", None))
        self.values_grid_header_0.setText(QCoreApplication.translate("OutputFiles", u"<b>Measure</b>", None))
        self.values_grid_header_1.setText(QCoreApplication.translate("OutputFiles", u"<b>Range</b>", None))
        self.values_grid_header_2.setText(QCoreApplication.translate("OutputFiles", u"<b>Meaning</b>", None))
        self.values_grid_1_0.setText(QCoreApplication.translate("OutputFiles", u"wPLI", None))
        self.values_grid_1_1.setText(QCoreApplication.translate("OutputFiles", u"0 to 1", None))
        self.values_grid_1_2.setText(QCoreApplication.translate("OutputFiles", u"0: no consistent lagged coupling; 1: strong coupling.", None))
        self.values_grid_2_0.setText(QCoreApplication.translate("OutputFiles", u"dPLI", None))
        self.values_grid_2_1.setText(QCoreApplication.translate("OutputFiles", u"0 to 1", None))
        self.values_grid_2_2.setText(QCoreApplication.translate("OutputFiles", u"0.5: neutral. Above 0.5, channel i tends to lead channel j; below 0.5, it tends to lag.", None))
        self.values_grid_3_0.setText(QCoreApplication.translate("OutputFiles", u"AEC", None))
        self.values_grid_3_1.setText(QCoreApplication.translate("OutputFiles", u"0 to 1", None))
        self.values_grid_3_2.setText(QCoreApplication.translate("OutputFiles", u"0: no amplitude envelope correlation; 1: strong coupling. A leakage correction reduces the spurious connectivity from volume conduction.", None))
        self.about_plot_title_label.setText(QCoreApplication.translate("OutputFiles", u"About the head connectivity plot", None))
        self.about_plot_label.setText(QCoreApplication.translate("OutputFiles", u"\u2022 <b>Montage:</b> chosen automatically from the MNE built-in montages with the channel names. For HydroCel 128/129, the face and neck sensors are removed to keep the head outline clean.<br/>\u2022 <b>Nodes:</b> the channels. Unconnected channels in white, connected channels filled in black, with their labels.<br/>\u2022 <b>Edges:</b> the connections above the display thresholds. Their thickness and opacity scale with the strength: thin and faint for a moderate connection, thick and dark for a strong one.<br/>\u2022 <b>Colors:</b> wPLI and AEC (undirected): one hue, darker is stronger. dPLI (directional): each edge fades from the leader (red) through purple to the lagger (blue); colorbar \"Bias = dPLI \u2212 0.5\".", None))
        self.thresholds_label.setText(QCoreApplication.translate("OutputFiles", u"<b>Default display thresholds</b>", None))
        self.thresholds_grid_header_0.setText(QCoreApplication.translate("OutputFiles", u"<b>Measure</b>", None))
        self.thresholds_grid_header_1.setText(QCoreApplication.translate("OutputFiles", u"<b>Neutral<br/>ignored below</b>", None))
        self.thresholds_grid_header_2.setText(QCoreApplication.translate("OutputFiles", u"<b>Moderate<br/>thin, faint</b>", None))
        self.thresholds_grid_header_3.setText(QCoreApplication.translate("OutputFiles", u"<b>Strong<br/>thick, dark</b>", None))
        self.thresholds_grid_header_4.setText(QCoreApplication.translate("OutputFiles", u"<b>Maximum<br/>color scale</b>", None))
        self.thresholds_grid_1_0.setText(QCoreApplication.translate("OutputFiles", u"wPLI", None))
        self.thresholds_grid_1_1.setText(QCoreApplication.translate("OutputFiles", u"0.05", None))
        self.thresholds_grid_1_2.setText(QCoreApplication.translate("OutputFiles", u"0.10", None))
        self.thresholds_grid_1_3.setText(QCoreApplication.translate("OutputFiles", u"0.20", None))
        self.thresholds_grid_1_4.setText(QCoreApplication.translate("OutputFiles", u"0.40", None))
        self.thresholds_grid_2_0.setText(QCoreApplication.translate("OutputFiles", u"dPLI bias", None))
        self.thresholds_grid_2_1.setText(QCoreApplication.translate("OutputFiles", u"0.01", None))
        self.thresholds_grid_2_2.setText(QCoreApplication.translate("OutputFiles", u"0.02", None))
        self.thresholds_grid_2_3.setText(QCoreApplication.translate("OutputFiles", u"0.08", None))
        self.thresholds_grid_2_4.setText(QCoreApplication.translate("OutputFiles", u"0.25", None))
        self.thresholds_grid_3_0.setText(QCoreApplication.translate("OutputFiles", u"AEC", None))
        self.thresholds_grid_3_1.setText(QCoreApplication.translate("OutputFiles", u"0.10", None))
        self.thresholds_grid_3_2.setText(QCoreApplication.translate("OutputFiles", u"0.20", None))
        self.thresholds_grid_3_3.setText(QCoreApplication.translate("OutputFiles", u"0.35", None))
        self.thresholds_grid_3_4.setText(QCoreApplication.translate("OutputFiles", u"0.60", None))
        self.thresholds_help_label.setText(QCoreApplication.translate("OutputFiles", u"wPLI and AEC on their scale from 0 to 1; dPLI bias = dPLI \u2212 0.5 (its absolute value). Maximum: the strength at which the color and opacity of the edges stop increasing.", None))
    # retranslateUi

