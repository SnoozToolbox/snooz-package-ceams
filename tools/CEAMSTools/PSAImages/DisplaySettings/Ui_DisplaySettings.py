# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DisplaySettings.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_DisplaySettings(object):
    def setupUi(self, DisplaySettings):
        if not DisplaySettings.objectName():
            DisplaySettings.setObjectName(u"DisplaySettings")
        DisplaySettings.resize(900, 700)
        self.verticalLayout = QVBoxLayout(DisplaySettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(DisplaySettings)
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

        self.group_level_card = QFrame(self.content_widget)
        self.group_level_card.setObjectName(u"group_level_card")
        self.group_level_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.group_level_card.setFrameShadow(QFrame.Shadow.Raised)
        self.group_level_card_layout = QVBoxLayout(self.group_level_card)
        self.group_level_card_layout.setSpacing(10)
        self.group_level_card_layout.setObjectName(u"group_level_card_layout")
        self.group_level_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.group_level_card)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)

        self.group_level_card_layout.addWidget(self.label)

        self.group_avg_layout = QVBoxLayout()
        self.group_avg_layout.setSpacing(6)
        self.group_avg_layout.setObjectName(u"group_avg_layout")
        self.label_8 = QLabel(self.group_level_card)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setTextFormat(Qt.TextFormat.RichText)
        self.label_8.setWordWrap(True)
        self.label_8.setProperty(u"variant", u"help")

        self.group_avg_layout.addWidget(self.label_8)

        self.checkBox_group_avg_auto = QCheckBox(self.group_level_card)
        self.checkBox_group_avg_auto.setObjectName(u"checkBox_group_avg_auto")
        self.checkBox_group_avg_auto.setMinimumSize(QSize(60, 0))
        self.checkBox_group_avg_auto.setMaximumSize(QSize(60, 16777215))
        self.checkBox_group_avg_auto.setChecked(True)

        self.group_avg_layout.addWidget(self.checkBox_group_avg_auto)

        self.group_avg_grid = QGridLayout()
        self.group_avg_grid.setObjectName(u"group_avg_grid")
        self.group_avg_grid.setHorizontalSpacing(12)
        self.group_avg_grid.setVerticalSpacing(4)
        self.label_10 = QLabel(self.group_level_card)
        self.label_10.setObjectName(u"label_10")

        self.group_avg_grid.addWidget(self.label_10, 0, 0, 1, 1)

        self.comboBox_group_avg_chan1 = QComboBox(self.group_level_card)
        self.comboBox_group_avg_chan1.addItem("")
        self.comboBox_group_avg_chan1.addItem("")
        self.comboBox_group_avg_chan1.addItem("")
        self.comboBox_group_avg_chan1.addItem("")
        self.comboBox_group_avg_chan1.addItem("")
        self.comboBox_group_avg_chan1.addItem("")
        self.comboBox_group_avg_chan1.addItem("")
        self.comboBox_group_avg_chan1.addItem("")
        self.comboBox_group_avg_chan1.addItem("")
        self.comboBox_group_avg_chan1.addItem("")
        self.comboBox_group_avg_chan1.setObjectName(u"comboBox_group_avg_chan1")
        self.comboBox_group_avg_chan1.setEnabled(False)

        self.group_avg_grid.addWidget(self.comboBox_group_avg_chan1, 1, 0, 1, 1)

        self.label_11 = QLabel(self.group_level_card)
        self.label_11.setObjectName(u"label_11")

        self.group_avg_grid.addWidget(self.label_11, 0, 1, 1, 1)

        self.comboBox_group_avg_chan2 = QComboBox(self.group_level_card)
        self.comboBox_group_avg_chan2.addItem("")
        self.comboBox_group_avg_chan2.addItem("")
        self.comboBox_group_avg_chan2.addItem("")
        self.comboBox_group_avg_chan2.addItem("")
        self.comboBox_group_avg_chan2.addItem("")
        self.comboBox_group_avg_chan2.addItem("")
        self.comboBox_group_avg_chan2.addItem("")
        self.comboBox_group_avg_chan2.addItem("")
        self.comboBox_group_avg_chan2.addItem("")
        self.comboBox_group_avg_chan2.addItem("")
        self.comboBox_group_avg_chan2.setObjectName(u"comboBox_group_avg_chan2")
        self.comboBox_group_avg_chan2.setEnabled(False)

        self.group_avg_grid.addWidget(self.comboBox_group_avg_chan2, 1, 1, 1, 1)

        self.label_12 = QLabel(self.group_level_card)
        self.label_12.setObjectName(u"label_12")

        self.group_avg_grid.addWidget(self.label_12, 0, 2, 1, 1)

        self.comboBox_group_avg_chan3 = QComboBox(self.group_level_card)
        self.comboBox_group_avg_chan3.addItem("")
        self.comboBox_group_avg_chan3.addItem("")
        self.comboBox_group_avg_chan3.addItem("")
        self.comboBox_group_avg_chan3.addItem("")
        self.comboBox_group_avg_chan3.addItem("")
        self.comboBox_group_avg_chan3.addItem("")
        self.comboBox_group_avg_chan3.addItem("")
        self.comboBox_group_avg_chan3.addItem("")
        self.comboBox_group_avg_chan3.addItem("")
        self.comboBox_group_avg_chan3.addItem("")
        self.comboBox_group_avg_chan3.setObjectName(u"comboBox_group_avg_chan3")
        self.comboBox_group_avg_chan3.setEnabled(False)

        self.group_avg_grid.addWidget(self.comboBox_group_avg_chan3, 1, 2, 1, 1)

        self.label_13 = QLabel(self.group_level_card)
        self.label_13.setObjectName(u"label_13")

        self.group_avg_grid.addWidget(self.label_13, 0, 3, 1, 1)

        self.comboBox_group_avg_chan4 = QComboBox(self.group_level_card)
        self.comboBox_group_avg_chan4.addItem("")
        self.comboBox_group_avg_chan4.addItem("")
        self.comboBox_group_avg_chan4.addItem("")
        self.comboBox_group_avg_chan4.addItem("")
        self.comboBox_group_avg_chan4.addItem("")
        self.comboBox_group_avg_chan4.addItem("")
        self.comboBox_group_avg_chan4.addItem("")
        self.comboBox_group_avg_chan4.addItem("")
        self.comboBox_group_avg_chan4.addItem("")
        self.comboBox_group_avg_chan4.addItem("")
        self.comboBox_group_avg_chan4.setObjectName(u"comboBox_group_avg_chan4")
        self.comboBox_group_avg_chan4.setEnabled(False)

        self.group_avg_grid.addWidget(self.comboBox_group_avg_chan4, 1, 3, 1, 1)

        self.group_avg_grid.setColumnStretch(0, 1)
        self.group_avg_grid.setColumnStretch(1, 1)
        self.group_avg_grid.setColumnStretch(2, 1)
        self.group_avg_grid.setColumnStretch(3, 1)

        self.group_avg_layout.addLayout(self.group_avg_grid)

        self.label_15 = QLabel(self.group_level_card)
        self.label_15.setObjectName(u"label_15")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_15.setFont(font2)
        self.label_15.setWordWrap(True)
        self.label_15.setProperty(u"variant", u"help")

        self.group_avg_layout.addWidget(self.label_15)


        self.group_level_card_layout.addLayout(self.group_avg_layout)

        self.group_level_line = QFrame(self.group_level_card)
        self.group_level_line.setObjectName(u"group_level_line")
        self.group_level_line.setFrameShape(QFrame.Shape.HLine)
        self.group_level_line.setFrameShadow(QFrame.Shadow.Plain)

        self.group_level_card_layout.addWidget(self.group_level_line)

        self.group_sel_layout = QVBoxLayout()
        self.group_sel_layout.setSpacing(6)
        self.group_sel_layout.setObjectName(u"group_sel_layout")
        self.label_2 = QLabel(self.group_level_card)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.TextFormat.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setProperty(u"variant", u"help")

        self.group_sel_layout.addWidget(self.label_2)

        self.checkBox_group_sel_auto = QCheckBox(self.group_level_card)
        self.checkBox_group_sel_auto.setObjectName(u"checkBox_group_sel_auto")
        self.checkBox_group_sel_auto.setMinimumSize(QSize(60, 0))
        self.checkBox_group_sel_auto.setMaximumSize(QSize(60, 16777215))
        self.checkBox_group_sel_auto.setChecked(True)

        self.group_sel_layout.addWidget(self.checkBox_group_sel_auto)

        self.group_sel_grid = QGridLayout()
        self.group_sel_grid.setObjectName(u"group_sel_grid")
        self.group_sel_grid.setHorizontalSpacing(12)
        self.group_sel_grid.setVerticalSpacing(4)
        self.label_4 = QLabel(self.group_level_card)
        self.label_4.setObjectName(u"label_4")

        self.group_sel_grid.addWidget(self.label_4, 0, 0, 1, 1)

        self.comboBox_group_sel_cat1 = QComboBox(self.group_level_card)
        self.comboBox_group_sel_cat1.addItem("")
        self.comboBox_group_sel_cat1.addItem("")
        self.comboBox_group_sel_cat1.addItem("")
        self.comboBox_group_sel_cat1.addItem("")
        self.comboBox_group_sel_cat1.addItem("")
        self.comboBox_group_sel_cat1.addItem("")
        self.comboBox_group_sel_cat1.addItem("")
        self.comboBox_group_sel_cat1.addItem("")
        self.comboBox_group_sel_cat1.addItem("")
        self.comboBox_group_sel_cat1.addItem("")
        self.comboBox_group_sel_cat1.setObjectName(u"comboBox_group_sel_cat1")
        self.comboBox_group_sel_cat1.setEnabled(False)

        self.group_sel_grid.addWidget(self.comboBox_group_sel_cat1, 1, 0, 1, 1)

        self.label_5 = QLabel(self.group_level_card)
        self.label_5.setObjectName(u"label_5")

        self.group_sel_grid.addWidget(self.label_5, 0, 1, 1, 1)

        self.comboBox_group_sel_cat2 = QComboBox(self.group_level_card)
        self.comboBox_group_sel_cat2.addItem("")
        self.comboBox_group_sel_cat2.addItem("")
        self.comboBox_group_sel_cat2.addItem("")
        self.comboBox_group_sel_cat2.addItem("")
        self.comboBox_group_sel_cat2.addItem("")
        self.comboBox_group_sel_cat2.addItem("")
        self.comboBox_group_sel_cat2.addItem("")
        self.comboBox_group_sel_cat2.addItem("")
        self.comboBox_group_sel_cat2.addItem("")
        self.comboBox_group_sel_cat2.addItem("")
        self.comboBox_group_sel_cat2.setObjectName(u"comboBox_group_sel_cat2")
        self.comboBox_group_sel_cat2.setEnabled(False)

        self.group_sel_grid.addWidget(self.comboBox_group_sel_cat2, 1, 1, 1, 1)

        self.label_6 = QLabel(self.group_level_card)
        self.label_6.setObjectName(u"label_6")

        self.group_sel_grid.addWidget(self.label_6, 0, 2, 1, 1)

        self.comboBox_group_sel_cat3 = QComboBox(self.group_level_card)
        self.comboBox_group_sel_cat3.addItem("")
        self.comboBox_group_sel_cat3.addItem("")
        self.comboBox_group_sel_cat3.addItem("")
        self.comboBox_group_sel_cat3.addItem("")
        self.comboBox_group_sel_cat3.addItem("")
        self.comboBox_group_sel_cat3.addItem("")
        self.comboBox_group_sel_cat3.addItem("")
        self.comboBox_group_sel_cat3.addItem("")
        self.comboBox_group_sel_cat3.addItem("")
        self.comboBox_group_sel_cat3.addItem("")
        self.comboBox_group_sel_cat3.setObjectName(u"comboBox_group_sel_cat3")
        self.comboBox_group_sel_cat3.setEnabled(False)

        self.group_sel_grid.addWidget(self.comboBox_group_sel_cat3, 1, 2, 1, 1)

        self.label_7 = QLabel(self.group_level_card)
        self.label_7.setObjectName(u"label_7")

        self.group_sel_grid.addWidget(self.label_7, 0, 3, 1, 1)

        self.comboBox_group_sel_cat4 = QComboBox(self.group_level_card)
        self.comboBox_group_sel_cat4.addItem("")
        self.comboBox_group_sel_cat4.addItem("")
        self.comboBox_group_sel_cat4.addItem("")
        self.comboBox_group_sel_cat4.addItem("")
        self.comboBox_group_sel_cat4.addItem("")
        self.comboBox_group_sel_cat4.addItem("")
        self.comboBox_group_sel_cat4.addItem("")
        self.comboBox_group_sel_cat4.addItem("")
        self.comboBox_group_sel_cat4.addItem("")
        self.comboBox_group_sel_cat4.addItem("")
        self.comboBox_group_sel_cat4.setObjectName(u"comboBox_group_sel_cat4")
        self.comboBox_group_sel_cat4.setEnabled(False)

        self.group_sel_grid.addWidget(self.comboBox_group_sel_cat4, 1, 3, 1, 1)

        self.group_sel_grid.setColumnStretch(0, 1)
        self.group_sel_grid.setColumnStretch(1, 1)
        self.group_sel_grid.setColumnStretch(2, 1)
        self.group_sel_grid.setColumnStretch(3, 1)

        self.group_sel_layout.addLayout(self.group_sel_grid)


        self.group_level_card_layout.addLayout(self.group_sel_layout)


        self.content_layout.addWidget(self.group_level_card)

        self.cohort_level_card = QFrame(self.content_widget)
        self.cohort_level_card.setObjectName(u"cohort_level_card")
        self.cohort_level_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.cohort_level_card.setFrameShadow(QFrame.Shadow.Raised)
        self.cohort_level_card_layout = QVBoxLayout(self.cohort_level_card)
        self.cohort_level_card_layout.setSpacing(10)
        self.cohort_level_card_layout.setObjectName(u"cohort_level_card_layout")
        self.cohort_level_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_14 = QLabel(self.cohort_level_card)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.cohort_level_card_layout.addWidget(self.label_14)

        self.label_17 = QLabel(self.cohort_level_card)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setWordWrap(True)
        self.label_17.setProperty(u"variant", u"help")

        self.cohort_level_card_layout.addWidget(self.label_17)

        self.checkBox_cohort_auto = QCheckBox(self.cohort_level_card)
        self.checkBox_cohort_auto.setObjectName(u"checkBox_cohort_auto")
        self.checkBox_cohort_auto.setMinimumSize(QSize(60, 0))
        self.checkBox_cohort_auto.setMaximumSize(QSize(60, 16777215))
        self.checkBox_cohort_auto.setChecked(True)

        self.cohort_level_card_layout.addWidget(self.checkBox_cohort_auto)

        self.cohort_grid = QGridLayout()
        self.cohort_grid.setObjectName(u"cohort_grid")
        self.cohort_grid.setHorizontalSpacing(12)
        self.cohort_grid.setVerticalSpacing(4)
        self.label_18 = QLabel(self.cohort_level_card)
        self.label_18.setObjectName(u"label_18")

        self.cohort_grid.addWidget(self.label_18, 0, 0, 1, 1)

        self.comboBox_cohort_group1 = QComboBox(self.cohort_level_card)
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.addItem("")
        self.comboBox_cohort_group1.setObjectName(u"comboBox_cohort_group1")
        self.comboBox_cohort_group1.setEnabled(False)

        self.cohort_grid.addWidget(self.comboBox_cohort_group1, 1, 0, 1, 1)

        self.label_21 = QLabel(self.cohort_level_card)
        self.label_21.setObjectName(u"label_21")

        self.cohort_grid.addWidget(self.label_21, 0, 1, 1, 1)

        self.comboBox_cohort_group2 = QComboBox(self.cohort_level_card)
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.addItem("")
        self.comboBox_cohort_group2.setObjectName(u"comboBox_cohort_group2")
        self.comboBox_cohort_group2.setEnabled(False)

        self.cohort_grid.addWidget(self.comboBox_cohort_group2, 1, 1, 1, 1)

        self.label_19 = QLabel(self.cohort_level_card)
        self.label_19.setObjectName(u"label_19")

        self.cohort_grid.addWidget(self.label_19, 0, 2, 1, 1)

        self.comboBox_cohort_group3 = QComboBox(self.cohort_level_card)
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.addItem("")
        self.comboBox_cohort_group3.setObjectName(u"comboBox_cohort_group3")
        self.comboBox_cohort_group3.setEnabled(False)

        self.cohort_grid.addWidget(self.comboBox_cohort_group3, 1, 2, 1, 1)

        self.label_20 = QLabel(self.cohort_level_card)
        self.label_20.setObjectName(u"label_20")

        self.cohort_grid.addWidget(self.label_20, 0, 3, 1, 1)

        self.comboBox_cohort_group4 = QComboBox(self.cohort_level_card)
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.addItem("")
        self.comboBox_cohort_group4.setObjectName(u"comboBox_cohort_group4")
        self.comboBox_cohort_group4.setEnabled(False)

        self.cohort_grid.addWidget(self.comboBox_cohort_group4, 1, 3, 1, 1)

        self.cohort_grid.setColumnStretch(0, 1)
        self.cohort_grid.setColumnStretch(1, 1)
        self.cohort_grid.setColumnStretch(2, 1)
        self.cohort_grid.setColumnStretch(3, 1)

        self.cohort_level_card_layout.addLayout(self.cohort_grid)

        self.label_22 = QLabel(self.cohort_level_card)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)
        self.label_22.setWordWrap(True)
        self.label_22.setProperty(u"variant", u"help")

        self.cohort_level_card_layout.addWidget(self.label_22)


        self.content_layout.addWidget(self.cohort_level_card)

        self.about_colors_layout = QVBoxLayout()
        self.about_colors_layout.setSpacing(6)
        self.about_colors_layout.setObjectName(u"about_colors_layout")
        self.about_colors_title_label = QLabel(self.content_widget)
        self.about_colors_title_label.setObjectName(u"about_colors_title_label")
        self.about_colors_title_label.setFont(font1)

        self.about_colors_layout.addWidget(self.about_colors_title_label)

        self.about_colors_label = QLabel(self.content_widget)
        self.about_colors_label.setObjectName(u"about_colors_label")
        self.about_colors_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_colors_label.setWordWrap(True)
        self.about_colors_label.setProperty(u"variant", u"help")

        self.about_colors_layout.addWidget(self.about_colors_label)


        self.content_layout.addLayout(self.about_colors_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(DisplaySettings)
        self.checkBox_cohort_auto.clicked.connect(DisplaySettings.update_colors_slot)
        self.checkBox_group_avg_auto.clicked.connect(DisplaySettings.update_colors_slot)
        self.checkBox_group_sel_auto.clicked.connect(DisplaySettings.update_colors_slot)
        self.comboBox_cohort_group1.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_cohort_group2.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_cohort_group3.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_cohort_group4.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_group_avg_chan1.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_group_avg_chan2.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_group_avg_chan3.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_group_avg_chan4.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_group_sel_cat1.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_group_sel_cat2.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_group_sel_cat3.currentIndexChanged.connect(DisplaySettings.update_colors_slot)
        self.comboBox_group_sel_cat4.currentIndexChanged.connect(DisplaySettings.update_colors_slot)

        QMetaObject.connectSlotsByName(DisplaySettings)
    # setupUi

    def retranslateUi(self, DisplaySettings):
        DisplaySettings.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("DisplaySettings", u"Colors", None))
        self.subtitle_label.setText(QCoreApplication.translate("DisplaySettings", u"Define the first four colors used in the pictures.", None))
        self.label.setText(QCoreApplication.translate("DisplaySettings", u"Pictures at the group level", None))
        self.label_8.setText(QCoreApplication.translate("DisplaySettings", u"<b>One picture per group</b>, available when displaying the mean signal curve. The colors differentiate the channels.", None))
        self.checkBox_group_avg_auto.setText(QCoreApplication.translate("DisplaySettings", u"Auto", None))
        self.label_10.setText(QCoreApplication.translate("DisplaySettings", u"Channel #1", None))
        self.comboBox_group_avg_chan1.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_group_avg_chan1.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_group_avg_chan1.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_group_avg_chan1.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_group_avg_chan1.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_group_avg_chan1.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_group_avg_chan1.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_group_avg_chan1.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_group_avg_chan1.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_group_avg_chan1.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.label_11.setText(QCoreApplication.translate("DisplaySettings", u"Channel #2", None))
        self.comboBox_group_avg_chan2.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_group_avg_chan2.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_group_avg_chan2.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_group_avg_chan2.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_group_avg_chan2.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_group_avg_chan2.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_group_avg_chan2.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_group_avg_chan2.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_group_avg_chan2.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_group_avg_chan2.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_group_avg_chan2.setCurrentText(QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.label_12.setText(QCoreApplication.translate("DisplaySettings", u"Channel #3", None))
        self.comboBox_group_avg_chan3.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_group_avg_chan3.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_group_avg_chan3.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_group_avg_chan3.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_group_avg_chan3.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_group_avg_chan3.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_group_avg_chan3.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_group_avg_chan3.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_group_avg_chan3.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_group_avg_chan3.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_group_avg_chan3.setCurrentText(QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.label_13.setText(QCoreApplication.translate("DisplaySettings", u"Channel #4", None))
        self.comboBox_group_avg_chan4.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_group_avg_chan4.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_group_avg_chan4.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_group_avg_chan4.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_group_avg_chan4.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_group_avg_chan4.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_group_avg_chan4.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_group_avg_chan4.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_group_avg_chan4.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_group_avg_chan4.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_group_avg_chan4.setCurrentText(QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.label_15.setText(QCoreApplication.translate("DisplaySettings", u"When several channels are displayed, the sleep stages are distinguished by the line style. The colors of the groups, below, are used when a single channel is displayed.", None))
        self.label_2.setText(QCoreApplication.translate("DisplaySettings", u"<b>One picture per channel</b>, available when displaying all the signal curves. The colors differentiate the groups.", None))
        self.checkBox_group_sel_auto.setText(QCoreApplication.translate("DisplaySettings", u"Auto", None))
        self.label_4.setText(QCoreApplication.translate("DisplaySettings", u"Group #1", None))
        self.comboBox_group_sel_cat1.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_group_sel_cat1.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_group_sel_cat1.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_group_sel_cat1.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_group_sel_cat1.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_group_sel_cat1.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_group_sel_cat1.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_group_sel_cat1.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_group_sel_cat1.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_group_sel_cat1.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.label_5.setText(QCoreApplication.translate("DisplaySettings", u"Group #2", None))
        self.comboBox_group_sel_cat2.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_group_sel_cat2.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_group_sel_cat2.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_group_sel_cat2.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_group_sel_cat2.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_group_sel_cat2.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_group_sel_cat2.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_group_sel_cat2.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_group_sel_cat2.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_group_sel_cat2.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_group_sel_cat2.setCurrentText(QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.label_6.setText(QCoreApplication.translate("DisplaySettings", u"Group #3", None))
        self.comboBox_group_sel_cat3.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_group_sel_cat3.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_group_sel_cat3.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_group_sel_cat3.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_group_sel_cat3.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_group_sel_cat3.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_group_sel_cat3.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_group_sel_cat3.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_group_sel_cat3.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_group_sel_cat3.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_group_sel_cat3.setCurrentText(QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.label_7.setText(QCoreApplication.translate("DisplaySettings", u"Group #4", None))
        self.comboBox_group_sel_cat4.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_group_sel_cat4.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_group_sel_cat4.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_group_sel_cat4.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_group_sel_cat4.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_group_sel_cat4.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_group_sel_cat4.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_group_sel_cat4.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_group_sel_cat4.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_group_sel_cat4.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_group_sel_cat4.setCurrentText(QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.label_14.setText(QCoreApplication.translate("DisplaySettings", u"Pictures at the cohort level", None))
        self.label_17.setText(QCoreApplication.translate("DisplaySettings", u"The colors differentiate the cohort groups.", None))
        self.checkBox_cohort_auto.setText(QCoreApplication.translate("DisplaySettings", u"Auto", None))
        self.label_18.setText(QCoreApplication.translate("DisplaySettings", u"Group #1", None))
        self.comboBox_cohort_group1.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_cohort_group1.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_cohort_group1.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_cohort_group1.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_cohort_group1.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_cohort_group1.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_cohort_group1.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_cohort_group1.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_cohort_group1.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_cohort_group1.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.label_21.setText(QCoreApplication.translate("DisplaySettings", u"Group #2", None))
        self.comboBox_cohort_group2.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_cohort_group2.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_cohort_group2.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_cohort_group2.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_cohort_group2.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_cohort_group2.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_cohort_group2.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_cohort_group2.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_cohort_group2.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_cohort_group2.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_cohort_group2.setCurrentText(QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.label_19.setText(QCoreApplication.translate("DisplaySettings", u"Group #3", None))
        self.comboBox_cohort_group3.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_cohort_group3.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_cohort_group3.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_cohort_group3.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_cohort_group3.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_cohort_group3.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_cohort_group3.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_cohort_group3.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_cohort_group3.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_cohort_group3.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_cohort_group3.setCurrentText(QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.label_20.setText(QCoreApplication.translate("DisplaySettings", u"Group #4", None))
        self.comboBox_cohort_group4.setItemText(0, QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.comboBox_cohort_group4.setItemText(1, QCoreApplication.translate("DisplaySettings", u"red", None))
        self.comboBox_cohort_group4.setItemText(2, QCoreApplication.translate("DisplaySettings", u"green", None))
        self.comboBox_cohort_group4.setItemText(3, QCoreApplication.translate("DisplaySettings", u"orange", None))
        self.comboBox_cohort_group4.setItemText(4, QCoreApplication.translate("DisplaySettings", u"purple", None))
        self.comboBox_cohort_group4.setItemText(5, QCoreApplication.translate("DisplaySettings", u"brown", None))
        self.comboBox_cohort_group4.setItemText(6, QCoreApplication.translate("DisplaySettings", u"pink", None))
        self.comboBox_cohort_group4.setItemText(7, QCoreApplication.translate("DisplaySettings", u"gray", None))
        self.comboBox_cohort_group4.setItemText(8, QCoreApplication.translate("DisplaySettings", u"olive", None))
        self.comboBox_cohort_group4.setItemText(9, QCoreApplication.translate("DisplaySettings", u"cyan", None))

        self.comboBox_cohort_group4.setCurrentText(QCoreApplication.translate("DisplaySettings", u"blue", None))
        self.label_22.setText(QCoreApplication.translate("DisplaySettings", u"The sleep stages are differentiated by the line style.", None))
        self.about_colors_title_label.setText(QCoreApplication.translate("DisplaySettings", u"About the colors", None))
        self.about_colors_label.setText(QCoreApplication.translate("DisplaySettings", u"\u2022 This page defines the first four colors out of the ten used in the pictures. The condition groups and the channels are not limited to four, since ten colors are available.<br/>\u2022 With \"Auto\", the colors are blue, red, green, purple, orange, brown, pink, gray, olive and cyan, in this order. Uncheck \"Auto\" to choose the first four.", None))
    # retranslateUi

