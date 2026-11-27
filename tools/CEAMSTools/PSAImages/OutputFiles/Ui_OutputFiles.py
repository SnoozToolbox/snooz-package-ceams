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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

from CEAMSTools.PSAImages.OutputFiles.DecimalSpinBox import DecimalSpinBox
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

        self.pictures_card = QFrame(self.content_widget)
        self.pictures_card.setObjectName(u"pictures_card")
        self.pictures_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.pictures_card.setFrameShadow(QFrame.Shadow.Raised)
        self.pictures_card_layout = QVBoxLayout(self.pictures_card)
        self.pictures_card_layout.setSpacing(10)
        self.pictures_card_layout.setObjectName(u"pictures_card_layout")
        self.pictures_card_layout.setContentsMargins(10, 10, 10, 10)
        self.pictures_title_label = QLabel(self.pictures_card)
        self.pictures_title_label.setObjectName(u"pictures_title_label")
        font1 = QFont()
        font1.setBold(True)
        self.pictures_title_label.setFont(font1)

        self.pictures_card_layout.addWidget(self.pictures_title_label)

        self.level_options = QVBoxLayout()
        self.level_options.setSpacing(8)
        self.level_options.setObjectName(u"level_options")
        self.level_options_1_layout = QVBoxLayout()
        self.level_options_1_layout.setSpacing(2)
        self.level_options_1_layout.setObjectName(u"level_options_1_layout")
        self.radioButton_report_level = QRadioButton(self.pictures_card)
        self.buttonGroup_level = QButtonGroup(OutputFiles)
        self.buttonGroup_level.setObjectName(u"buttonGroup_level")
        self.buttonGroup_level.addButton(self.radioButton_report_level)
        self.radioButton_report_level.setObjectName(u"radioButton_report_level")
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(False)
        self.radioButton_report_level.setFont(font2)

        self.level_options_1_layout.addWidget(self.radioButton_report_level)

        self.group_level_layout = QVBoxLayout()
        self.group_level_layout.setSpacing(2)
        self.group_level_layout.setObjectName(u"group_level_layout")
        self.group_level_help_label = QLabel(self.pictures_card)
        self.group_level_help_label.setObjectName(u"group_level_help_label")
        font3 = QFont()
        font3.setPointSize(10)
        self.group_level_help_label.setFont(font3)
        self.group_level_help_label.setWordWrap(True)
        self.group_level_help_label.setIndent(26)
        self.group_level_help_label.setProperty(u"variant", u"help")

        self.group_level_layout.addWidget(self.group_level_help_label)

        self.group_options_layout = QVBoxLayout()
        self.group_options_layout.setSpacing(4)
        self.group_options_layout.setObjectName(u"group_options_layout")
        self.group_options_layout.setContentsMargins(26, 4, 0, 0)
        self.checkBox_group_avg = QCheckBox(self.pictures_card)
        self.checkBox_group_avg.setObjectName(u"checkBox_group_avg")
        self.checkBox_group_avg.setFont(font2)

        self.group_options_layout.addWidget(self.checkBox_group_avg)

        self.label_9 = QLabel(self.pictures_card)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setWordWrap(True)
        self.label_9.setIndent(26)
        self.label_9.setProperty(u"variant", u"help")

        self.group_options_layout.addWidget(self.label_9)

        self.checkBox_group_sel = QCheckBox(self.pictures_card)
        self.checkBox_group_sel.setObjectName(u"checkBox_group_sel")
        self.checkBox_group_sel.setEnabled(True)
        self.checkBox_group_sel.setFont(font2)

        self.group_options_layout.addWidget(self.checkBox_group_sel)

        self.label_3 = QLabel(self.pictures_card)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setWordWrap(True)
        self.label_3.setIndent(26)
        self.label_3.setProperty(u"variant", u"help")

        self.group_options_layout.addWidget(self.label_3)


        self.group_level_layout.addLayout(self.group_options_layout)


        self.level_options_1_layout.addLayout(self.group_level_layout)


        self.level_options.addLayout(self.level_options_1_layout)

        self.level_options_line_1 = QFrame(self.pictures_card)
        self.level_options_line_1.setObjectName(u"level_options_line_1")
        self.level_options_line_1.setFrameShape(QFrame.Shape.HLine)
        self.level_options_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.level_options.addWidget(self.level_options_line_1)

        self.level_options_2_layout = QVBoxLayout()
        self.level_options_2_layout.setSpacing(2)
        self.level_options_2_layout.setObjectName(u"level_options_2_layout")
        self.radioButton_cohort_level = QRadioButton(self.pictures_card)
        self.buttonGroup_level.addButton(self.radioButton_cohort_level)
        self.radioButton_cohort_level.setObjectName(u"radioButton_cohort_level")
        self.radioButton_cohort_level.setFont(font2)

        self.level_options_2_layout.addWidget(self.radioButton_cohort_level)

        self.cohort_level_layout = QVBoxLayout()
        self.cohort_level_layout.setSpacing(2)
        self.cohort_level_layout.setObjectName(u"cohort_level_layout")
        self.cohort_level_help_label = QLabel(self.pictures_card)
        self.cohort_level_help_label.setObjectName(u"cohort_level_help_label")
        self.cohort_level_help_label.setFont(font3)
        self.cohort_level_help_label.setWordWrap(True)
        self.cohort_level_help_label.setIndent(26)
        self.cohort_level_help_label.setProperty(u"variant", u"help")

        self.cohort_level_layout.addWidget(self.cohort_level_help_label)

        self.cohort_options_layout = QVBoxLayout()
        self.cohort_options_layout.setSpacing(4)
        self.cohort_options_layout.setObjectName(u"cohort_options_layout")
        self.cohort_options_layout.setContentsMargins(26, 4, 0, 0)
        self.checkBox_cohort_avg = QCheckBox(self.pictures_card)
        self.checkBox_cohort_avg.setObjectName(u"checkBox_cohort_avg")
        self.checkBox_cohort_avg.setChecked(False)

        self.cohort_options_layout.addWidget(self.checkBox_cohort_avg)

        self.label_19 = QLabel(self.pictures_card)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)
        self.label_19.setWordWrap(True)
        self.label_19.setIndent(26)
        self.label_19.setProperty(u"variant", u"help")

        self.cohort_options_layout.addWidget(self.label_19)

        self.checkBox_cohort_sel = QCheckBox(self.pictures_card)
        self.checkBox_cohort_sel.setObjectName(u"checkBox_cohort_sel")
        self.checkBox_cohort_sel.setEnabled(True)

        self.cohort_options_layout.addWidget(self.checkBox_cohort_sel)

        self.label_20 = QLabel(self.pictures_card)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)
        self.label_20.setWordWrap(True)
        self.label_20.setIndent(26)
        self.label_20.setProperty(u"variant", u"help")

        self.cohort_options_layout.addWidget(self.label_20)


        self.cohort_level_layout.addLayout(self.cohort_options_layout)


        self.level_options_2_layout.addLayout(self.cohort_level_layout)


        self.level_options.addLayout(self.level_options_2_layout)


        self.pictures_card_layout.addLayout(self.level_options)


        self.content_layout.addWidget(self.pictures_card)

        self.stages_card = QFrame(self.content_widget)
        self.stages_card.setObjectName(u"stages_card")
        self.stages_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.stages_card.setFrameShadow(QFrame.Shadow.Raised)
        self.stages_card_layout = QVBoxLayout(self.stages_card)
        self.stages_card_layout.setSpacing(10)
        self.stages_card_layout.setObjectName(u"stages_card_layout")
        self.stages_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_8 = QLabel(self.stages_card)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.stages_card_layout.addWidget(self.label_8)

        self.textEdit = QLabel(self.stages_card)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setWordWrap(True)
        self.textEdit.setProperty(u"variant", u"help")

        self.stages_card_layout.addWidget(self.textEdit)

        self.stages_layout = QHBoxLayout()
        self.stages_layout.setSpacing(16)
        self.stages_layout.setObjectName(u"stages_layout")
        self.checkBox_Wake = QCheckBox(self.stages_card)
        self.checkBox_Wake.setObjectName(u"checkBox_Wake")

        self.stages_layout.addWidget(self.checkBox_Wake)

        self.checkBox_N1 = QCheckBox(self.stages_card)
        self.checkBox_N1.setObjectName(u"checkBox_N1")

        self.stages_layout.addWidget(self.checkBox_N1)

        self.checkBox_N2 = QCheckBox(self.stages_card)
        self.checkBox_N2.setObjectName(u"checkBox_N2")

        self.stages_layout.addWidget(self.checkBox_N2)

        self.checkBox_N3 = QCheckBox(self.stages_card)
        self.checkBox_N3.setObjectName(u"checkBox_N3")

        self.stages_layout.addWidget(self.checkBox_N3)

        self.checkBox_N2N3 = QCheckBox(self.stages_card)
        self.checkBox_N2N3.setObjectName(u"checkBox_N2N3")

        self.stages_layout.addWidget(self.checkBox_N2N3)

        self.checkBox_NREM = QCheckBox(self.stages_card)
        self.checkBox_NREM.setObjectName(u"checkBox_NREM")

        self.stages_layout.addWidget(self.checkBox_NREM)

        self.checkBox_REM = QCheckBox(self.stages_card)
        self.checkBox_REM.setObjectName(u"checkBox_REM")

        self.stages_layout.addWidget(self.checkBox_REM)

        self.checkBox_Unscored = QCheckBox(self.stages_card)
        self.checkBox_Unscored.setObjectName(u"checkBox_Unscored")

        self.stages_layout.addWidget(self.checkBox_Unscored)

        self.checkBox_All = QCheckBox(self.stages_card)
        self.checkBox_All.setObjectName(u"checkBox_All")

        self.stages_layout.addWidget(self.checkBox_All)

        self.stages_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.stages_layout.addItem(self.stages_spacer)


        self.stages_card_layout.addLayout(self.stages_layout)


        self.content_layout.addWidget(self.stages_card)

        self.section_card = QFrame(self.content_widget)
        self.section_card.setObjectName(u"section_card")
        self.section_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.section_card.setFrameShadow(QFrame.Shadow.Raised)
        self.section_card_layout = QVBoxLayout(self.section_card)
        self.section_card_layout.setSpacing(10)
        self.section_card_layout.setObjectName(u"section_card_layout")
        self.section_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_6 = QLabel(self.section_card)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.section_card_layout.addWidget(self.label_6)

        self.section_grid = QGridLayout()
        self.section_grid.setObjectName(u"section_grid")
        self.section_grid.setHorizontalSpacing(16)
        self.section_grid.setVerticalSpacing(8)
        self.radioButton_total = QRadioButton(self.section_card)
        self.buttonGroup_section = QButtonGroup(OutputFiles)
        self.buttonGroup_section.setObjectName(u"buttonGroup_section")
        self.buttonGroup_section.addButton(self.radioButton_total)
        self.radioButton_total.setObjectName(u"radioButton_total")
        self.radioButton_total.setChecked(True)

        self.section_grid.addWidget(self.radioButton_total, 0, 0, 1, 1)

        self.radioButton_sleep_cycle = QRadioButton(self.section_card)
        self.buttonGroup_section.addButton(self.radioButton_sleep_cycle)
        self.radioButton_sleep_cycle.setObjectName(u"radioButton_sleep_cycle")

        self.section_grid.addWidget(self.radioButton_sleep_cycle, 1, 0, 1, 1)

        self.label_17 = QLabel(self.section_card)
        self.label_17.setObjectName(u"label_17")

        self.section_grid.addWidget(self.label_17, 1, 1, 1, 1)

        self.spinBox_sleep_cycle = QSpinBox(self.section_card)
        self.spinBox_sleep_cycle.setObjectName(u"spinBox_sleep_cycle")

        self.section_grid.addWidget(self.spinBox_sleep_cycle, 1, 2, 1, 1)

        self.radioButton_clock_hour = QRadioButton(self.section_card)
        self.buttonGroup_section.addButton(self.radioButton_clock_hour)
        self.radioButton_clock_hour.setObjectName(u"radioButton_clock_hour")

        self.section_grid.addWidget(self.radioButton_clock_hour, 2, 0, 1, 1)

        self.label_7 = QLabel(self.section_card)
        self.label_7.setObjectName(u"label_7")

        self.section_grid.addWidget(self.label_7, 2, 1, 1, 1)

        self.spinBox_clock_hour = QSpinBox(self.section_card)
        self.spinBox_clock_hour.setObjectName(u"spinBox_clock_hour")

        self.section_grid.addWidget(self.spinBox_clock_hour, 2, 2, 1, 1)

        self.radioButton_stage_hour = QRadioButton(self.section_card)
        self.buttonGroup_section.addButton(self.radioButton_stage_hour)
        self.radioButton_stage_hour.setObjectName(u"radioButton_stage_hour")

        self.section_grid.addWidget(self.radioButton_stage_hour, 3, 0, 1, 1)

        self.label_18 = QLabel(self.section_card)
        self.label_18.setObjectName(u"label_18")

        self.section_grid.addWidget(self.label_18, 3, 1, 1, 1)

        self.spinBox_stage_hour = QSpinBox(self.section_card)
        self.spinBox_stage_hour.setObjectName(u"spinBox_stage_hour")

        self.section_grid.addWidget(self.spinBox_stage_hour, 3, 2, 1, 1)

        self.section_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.section_grid.addItem(self.section_spacer, 0, 3, 1, 1)

        self.section_grid.setColumnStretch(3, 1)

        self.section_card_layout.addLayout(self.section_grid)


        self.content_layout.addWidget(self.section_card)

        self.display_card = QFrame(self.content_widget)
        self.display_card.setObjectName(u"display_card")
        self.display_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.display_card.setFrameShadow(QFrame.Shadow.Raised)
        self.display_card_layout = QVBoxLayout(self.display_card)
        self.display_card_layout.setSpacing(10)
        self.display_card_layout.setObjectName(u"display_card_layout")
        self.display_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.display_card)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.display_card_layout.addWidget(self.label)

        self.display_options = QVBoxLayout()
        self.display_options.setSpacing(8)
        self.display_options.setObjectName(u"display_options")
        self.display_options_1_layout = QVBoxLayout()
        self.display_options_1_layout.setSpacing(2)
        self.display_options_1_layout.setObjectName(u"display_options_1_layout")
        self.radioButton_all = QRadioButton(self.display_card)
        self.buttonGroup_display = QButtonGroup(OutputFiles)
        self.buttonGroup_display.setObjectName(u"buttonGroup_display")
        self.buttonGroup_display.addButton(self.radioButton_all)
        self.radioButton_all.setObjectName(u"radioButton_all")

        self.display_options_1_layout.addWidget(self.radioButton_all)

        self.display_all_help_label = QLabel(self.display_card)
        self.display_all_help_label.setObjectName(u"display_all_help_label")
        self.display_all_help_label.setFont(font3)
        self.display_all_help_label.setWordWrap(True)
        self.display_all_help_label.setIndent(26)
        self.display_all_help_label.setProperty(u"variant", u"help")

        self.display_options_1_layout.addWidget(self.display_all_help_label)


        self.display_options.addLayout(self.display_options_1_layout)

        self.display_options_line_1 = QFrame(self.display_card)
        self.display_options_line_1.setObjectName(u"display_options_line_1")
        self.display_options_line_1.setFrameShape(QFrame.Shape.HLine)
        self.display_options_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.display_options.addWidget(self.display_options_line_1)

        self.display_options_2_layout = QVBoxLayout()
        self.display_options_2_layout.setSpacing(2)
        self.display_options_2_layout.setObjectName(u"display_options_2_layout")
        self.radioButton_mean = QRadioButton(self.display_card)
        self.buttonGroup_display.addButton(self.radioButton_mean)
        self.radioButton_mean.setObjectName(u"radioButton_mean")

        self.display_options_2_layout.addWidget(self.radioButton_mean)

        self.display_mean_help_label = QLabel(self.display_card)
        self.display_mean_help_label.setObjectName(u"display_mean_help_label")
        self.display_mean_help_label.setFont(font3)
        self.display_mean_help_label.setWordWrap(True)
        self.display_mean_help_label.setIndent(26)
        self.display_mean_help_label.setProperty(u"variant", u"help")

        self.display_options_2_layout.addWidget(self.display_mean_help_label)


        self.display_options.addLayout(self.display_options_2_layout)

        self.display_options_line_2 = QFrame(self.display_card)
        self.display_options_line_2.setObjectName(u"display_options_line_2")
        self.display_options_line_2.setFrameShape(QFrame.Shape.HLine)
        self.display_options_line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.display_options.addWidget(self.display_options_line_2)

        self.display_options_3_layout = QVBoxLayout()
        self.display_options_3_layout.setSpacing(2)
        self.display_options_3_layout.setObjectName(u"display_options_3_layout")
        self.radioButton_meanstd = QRadioButton(self.display_card)
        self.buttonGroup_display.addButton(self.radioButton_meanstd)
        self.radioButton_meanstd.setObjectName(u"radioButton_meanstd")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_meanstd.sizePolicy().hasHeightForWidth())
        self.radioButton_meanstd.setSizePolicy(sizePolicy)
        self.radioButton_meanstd.setMinimumSize(QSize(0, 0))
        self.radioButton_meanstd.setChecked(True)

        self.display_options_3_layout.addWidget(self.radioButton_meanstd)

        self.display_meanstd_help_label = QLabel(self.display_card)
        self.display_meanstd_help_label.setObjectName(u"display_meanstd_help_label")
        self.display_meanstd_help_label.setFont(font3)
        self.display_meanstd_help_label.setWordWrap(True)
        self.display_meanstd_help_label.setIndent(26)
        self.display_meanstd_help_label.setProperty(u"variant", u"help")

        self.display_options_3_layout.addWidget(self.display_meanstd_help_label)


        self.display_options.addLayout(self.display_options_3_layout)


        self.display_card_layout.addLayout(self.display_options)

        self.display_line_1 = QFrame(self.display_card)
        self.display_line_1.setObjectName(u"display_line_1")
        self.display_line_1.setFrameShape(QFrame.Shape.HLine)
        self.display_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.display_card_layout.addWidget(self.display_line_1)

        self.scales_layout = QHBoxLayout()
        self.scales_layout.setSpacing(24)
        self.scales_layout.setObjectName(u"scales_layout")
        self.checkBox_log_y = QCheckBox(self.display_card)
        self.checkBox_log_y.setObjectName(u"checkBox_log_y")

        self.scales_layout.addWidget(self.checkBox_log_y)

        self.checkBox_log_x = QCheckBox(self.display_card)
        self.checkBox_log_x.setObjectName(u"checkBox_log_x")

        self.scales_layout.addWidget(self.checkBox_log_x)

        self.checkBox_legend = QCheckBox(self.display_card)
        self.checkBox_legend.setObjectName(u"checkBox_legend")
        self.checkBox_legend.setChecked(False)

        self.scales_layout.addWidget(self.checkBox_legend)

        self.scales_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.scales_layout.addItem(self.scales_spacer)


        self.display_card_layout.addLayout(self.scales_layout)

        self.axis_layout = QVBoxLayout()
        self.axis_layout.setSpacing(6)
        self.axis_layout.setObjectName(u"axis_layout")
        self.checkBox_force_axis = QCheckBox(self.display_card)
        self.checkBox_force_axis.setObjectName(u"checkBox_force_axis")

        self.axis_layout.addWidget(self.checkBox_force_axis)

        self.limits_layout = QHBoxLayout()
        self.limits_layout.setSpacing(8)
        self.limits_layout.setObjectName(u"limits_layout")
        self.limits_layout.setContentsMargins(26, 0, 0, 0)
        self.label_25 = QLabel(self.display_card)
        self.label_25.setObjectName(u"label_25")

        self.limits_layout.addWidget(self.label_25)

        self.doubleSpinBox_xmin = DecimalSpinBox(self.display_card)
        self.doubleSpinBox_xmin.setObjectName(u"doubleSpinBox_xmin")
        self.doubleSpinBox_xmin.setEnabled(False)
        self.doubleSpinBox_xmin.setMinimum(-100.000000000000000)
        self.doubleSpinBox_xmin.setMaximum(10000.000000000000000)
        self.doubleSpinBox_xmin.setSingleStep(0.500000000000000)

        self.limits_layout.addWidget(self.doubleSpinBox_xmin)

        self.label_26 = QLabel(self.display_card)
        self.label_26.setObjectName(u"label_26")

        self.limits_layout.addWidget(self.label_26)

        self.doubleSpinBox_xmax = DecimalSpinBox(self.display_card)
        self.doubleSpinBox_xmax.setObjectName(u"doubleSpinBox_xmax")
        self.doubleSpinBox_xmax.setEnabled(False)
        self.doubleSpinBox_xmax.setMinimum(0.000000000000000)
        self.doubleSpinBox_xmax.setMaximum(100000.000000000000000)
        self.doubleSpinBox_xmax.setSingleStep(0.500000000000000)

        self.limits_layout.addWidget(self.doubleSpinBox_xmax)

        self.label_27 = QLabel(self.display_card)
        self.label_27.setObjectName(u"label_27")

        self.limits_layout.addWidget(self.label_27)

        self.doubleSpinBox_ymin = DecimalSpinBox(self.display_card)
        self.doubleSpinBox_ymin.setObjectName(u"doubleSpinBox_ymin")
        self.doubleSpinBox_ymin.setEnabled(False)
        self.doubleSpinBox_ymin.setDecimals(5)
        self.doubleSpinBox_ymin.setMinimum(-10.000000000000000)
        self.doubleSpinBox_ymin.setMaximum(1000.000000000000000)
        self.doubleSpinBox_ymin.setSingleStep(50.000000000000000)

        self.limits_layout.addWidget(self.doubleSpinBox_ymin)

        self.label_28 = QLabel(self.display_card)
        self.label_28.setObjectName(u"label_28")

        self.limits_layout.addWidget(self.label_28)

        self.doubleSpinBox_ymax = DecimalSpinBox(self.display_card)
        self.doubleSpinBox_ymax.setObjectName(u"doubleSpinBox_ymax")
        self.doubleSpinBox_ymax.setEnabled(False)
        self.doubleSpinBox_ymax.setMinimum(0.000000000000000)
        self.doubleSpinBox_ymax.setMaximum(100000000000000000000.000000000000000)
        self.doubleSpinBox_ymax.setSingleStep(50.000000000000000)

        self.limits_layout.addWidget(self.doubleSpinBox_ymax)

        self.limits_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.limits_layout.addItem(self.limits_spacer)


        self.axis_layout.addLayout(self.limits_layout)


        self.display_card_layout.addLayout(self.axis_layout)

        self.display_line_2 = QFrame(self.display_card)
        self.display_line_2.setObjectName(u"display_line_2")
        self.display_line_2.setFrameShape(QFrame.Shape.HLine)
        self.display_line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.display_card_layout.addWidget(self.display_line_2)

        self.figure_grid = QGridLayout()
        self.figure_grid.setObjectName(u"figure_grid")
        self.figure_grid.setHorizontalSpacing(12)
        self.figure_grid.setVerticalSpacing(8)
        self.label_13 = QLabel(self.display_card)
        self.label_13.setObjectName(u"label_13")

        self.figure_grid.addWidget(self.label_13, 0, 0, 1, 1)

        self.fontComboBox = QComboBox(self.display_card)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setEditable(False)

        self.figure_grid.addWidget(self.fontComboBox, 0, 1, 1, 1)

        self.label_FontSize = QLabel(self.display_card)
        self.label_FontSize.setObjectName(u"label_FontSize")

        self.figure_grid.addWidget(self.label_FontSize, 0, 2, 1, 1)

        self.spinBox_fontsize = QSpinBox(self.display_card)
        self.spinBox_fontsize.setObjectName(u"spinBox_fontsize")
        self.spinBox_fontsize.setValue(12)

        self.figure_grid.addWidget(self.spinBox_fontsize, 0, 3, 1, 1)

        self.label_14 = QLabel(self.display_card)
        self.label_14.setObjectName(u"label_14")

        self.figure_grid.addWidget(self.label_14, 1, 0, 1, 1)

        self.figure_size_layout = QHBoxLayout()
        self.figure_size_layout.setSpacing(8)
        self.figure_size_layout.setObjectName(u"figure_size_layout")
        self.label_16 = QLabel(self.display_card)
        self.label_16.setObjectName(u"label_16")

        self.figure_size_layout.addWidget(self.label_16)

        self.spinBox_figwidth = QSpinBox(self.display_card)
        self.spinBox_figwidth.setObjectName(u"spinBox_figwidth")
        self.spinBox_figwidth.setMinimum(1)
        self.spinBox_figwidth.setValue(8)

        self.figure_size_layout.addWidget(self.spinBox_figwidth)

        self.label_15 = QLabel(self.display_card)
        self.label_15.setObjectName(u"label_15")

        self.figure_size_layout.addWidget(self.label_15)

        self.spinBox_figheight = QSpinBox(self.display_card)
        self.spinBox_figheight.setObjectName(u"spinBox_figheight")
        self.spinBox_figheight.setMinimum(1)
        self.spinBox_figheight.setValue(6)

        self.figure_size_layout.addWidget(self.spinBox_figheight)

        self.figure_size_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.figure_size_layout.addItem(self.figure_size_spacer)


        self.figure_grid.addLayout(self.figure_size_layout, 1, 1, 1, 1)

        self.figure_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.figure_grid.addItem(self.figure_spacer, 0, 4, 1, 1)

        self.figure_grid.setColumnStretch(4, 1)

        self.display_card_layout.addLayout(self.figure_grid)


        self.content_layout.addWidget(self.display_card)

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

        self.output_layout = QHBoxLayout()
        self.output_layout.setSpacing(8)
        self.output_layout.setObjectName(u"output_layout")
        self.lineEdit_output = QLineEdit(self.output_card)
        self.lineEdit_output.setObjectName(u"lineEdit_output")
        self.lineEdit_output.setMinimumSize(QSize(0, 0))
        self.lineEdit_output.setMaximumSize(QSize(900, 16777215))

        self.output_layout.addWidget(self.lineEdit_output)

        self.pushButton_choose = QPushButton(self.output_card)
        self.pushButton_choose.setObjectName(u"pushButton_choose")
        self.pushButton_choose.setMinimumSize(QSize(80, 0))
        self.pushButton_choose.setMaximumSize(QSize(50, 16777215))

        self.output_layout.addWidget(self.pushButton_choose)


        self.output_card_layout.addLayout(self.output_layout)

        self.label_5 = QLabel(self.output_card)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setWordWrap(True)
        self.label_5.setProperty(u"variant", u"help")

        self.output_card_layout.addWidget(self.label_5)


        self.content_layout.addWidget(self.output_card)

        self.about_pictures_layout = QVBoxLayout()
        self.about_pictures_layout.setSpacing(6)
        self.about_pictures_layout.setObjectName(u"about_pictures_layout")
        self.about_pictures_title_label = QLabel(self.content_widget)
        self.about_pictures_title_label.setObjectName(u"about_pictures_title_label")
        self.about_pictures_title_label.setFont(font1)

        self.about_pictures_layout.addWidget(self.about_pictures_title_label)

        self.about_pictures_label = QLabel(self.content_widget)
        self.about_pictures_label.setObjectName(u"about_pictures_label")
        self.about_pictures_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_pictures_label.setWordWrap(True)
        self.about_pictures_label.setProperty(u"variant", u"help")

        self.about_pictures_layout.addWidget(self.about_pictures_label)


        self.content_layout.addLayout(self.about_pictures_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(OutputFiles)
        self.pushButton_choose.clicked.connect(OutputFiles.choose_slot)
        self.checkBox_cohort_avg.clicked.connect(OutputFiles.out_options_slot)
        self.checkBox_cohort_sel.clicked.connect(OutputFiles.out_options_slot)
        self.checkBox_group_avg.clicked.connect(OutputFiles.out_options_slot)
        self.checkBox_group_sel.clicked.connect(OutputFiles.out_options_slot)

        QMetaObject.connectSlotsByName(OutputFiles)
    # setupUi

    def retranslateUi(self, OutputFiles):
        OutputFiles.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("OutputFiles", u"Output Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("OutputFiles", u"Define the pictures to generate and the folder to save them in.", None))
        self.pictures_title_label.setText(QCoreApplication.translate("OutputFiles", u"Pictures to generate", None))
        self.radioButton_report_level.setText(QCoreApplication.translate("OutputFiles", u"Group level", None))
        self.group_level_help_label.setText(QCoreApplication.translate("OutputFiles", u"Generates pictures for each individual group.", None))
        self.checkBox_group_avg.setText(QCoreApplication.translate("OutputFiles", u"One picture per group", None))
#if QT_CONFIG(tooltip)
        self.checkBox_group_avg.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("OutputFiles", u"All the selected channels or ROIs are illustrated on the same picture. With \"MEAN\", the picture shows the average of all the subjects in the group.", None))
        self.checkBox_group_sel.setText(QCoreApplication.translate("OutputFiles", u"One picture per channel or ROI per group", None))
#if QT_CONFIG(tooltip)
        self.checkBox_group_sel.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("OutputFiles", u"All the subjects in a group are illustrated on the same picture. With \"MEAN\", the picture shows the average of all the subjects in the group, for each selected channel.", None))
        self.radioButton_cohort_level.setText(QCoreApplication.translate("OutputFiles", u"Cohort level", None))
        self.cohort_level_help_label.setText(QCoreApplication.translate("OutputFiles", u"Generates pictures for the cohort.", None))
        self.checkBox_cohort_avg.setText(QCoreApplication.translate("OutputFiles", u"One picture per cohort", None))
        self.label_19.setText(QCoreApplication.translate("OutputFiles", u"Each curve is the EEG spectral power averaged across the selected channels or ROIs, for a group of subjects.", None))
        self.checkBox_cohort_sel.setText(QCoreApplication.translate("OutputFiles", u"One picture per channel or ROI", None))
        self.label_20.setText(QCoreApplication.translate("OutputFiles", u"Each curve is the EEG spectral power of a selected channel or ROI, for a group of subjects.", None))
        self.label_8.setText(QCoreApplication.translate("OutputFiles", u"Sleep stage selection", None))
        self.textEdit.setText(QCoreApplication.translate("OutputFiles", u"Each selected stage is plotted separately. Select N2N3 or NREM to plot the corresponding combined data from the report, with or without the individual stages.", None))
        self.checkBox_Wake.setText(QCoreApplication.translate("OutputFiles", u"Wake", None))
        self.checkBox_N1.setText(QCoreApplication.translate("OutputFiles", u"N1", None))
        self.checkBox_N2.setText(QCoreApplication.translate("OutputFiles", u"N2", None))
        self.checkBox_N3.setText(QCoreApplication.translate("OutputFiles", u"N3", None))
        self.checkBox_N2N3.setText(QCoreApplication.translate("OutputFiles", u"N2N3", None))
        self.checkBox_NREM.setText(QCoreApplication.translate("OutputFiles", u"NREM", None))
        self.checkBox_REM.setText(QCoreApplication.translate("OutputFiles", u"R", None))
        self.checkBox_Unscored.setText(QCoreApplication.translate("OutputFiles", u"Unscored", None))
        self.checkBox_All.setText(QCoreApplication.translate("OutputFiles", u"All", None))
        self.label_6.setText(QCoreApplication.translate("OutputFiles", u"Section to display", None))
        self.radioButton_total.setText(QCoreApplication.translate("OutputFiles", u"Total", None))
        self.radioButton_sleep_cycle.setText(QCoreApplication.translate("OutputFiles", u"Sleep cycle", None))
        self.label_17.setText(QCoreApplication.translate("OutputFiles", u"Desired cycle", None))
        self.radioButton_clock_hour.setText(QCoreApplication.translate("OutputFiles", u"Clock hour", None))
        self.label_7.setText(QCoreApplication.translate("OutputFiles", u"Desired hour", None))
        self.radioButton_stage_hour.setText(QCoreApplication.translate("OutputFiles", u"Stage hour", None))
        self.label_18.setText(QCoreApplication.translate("OutputFiles", u"Desired hour", None))
        self.label.setText(QCoreApplication.translate("OutputFiles", u"Display options", None))
        self.radioButton_all.setText(QCoreApplication.translate("OutputFiles", u"All the curves", None))
        self.display_all_help_label.setText(QCoreApplication.translate("OutputFiles", u"Displays all the EEG spectral power curves on the picture.", None))
        self.radioButton_mean.setText(QCoreApplication.translate("OutputFiles", u"MEAN", None))
        self.display_mean_help_label.setText(QCoreApplication.translate("OutputFiles", u"Displays only the mean EEG spectral power curve.", None))
        self.radioButton_meanstd.setText(QCoreApplication.translate("OutputFiles", u"MEAN + STD", None))
        self.display_meanstd_help_label.setText(QCoreApplication.translate("OutputFiles", u"Displays the mean EEG spectral power curve in a bold line and its standard deviation in a shaded area.", None))
        self.checkBox_log_y.setText(QCoreApplication.translate("OutputFiles", u"Logarithmic scale for the Y axis", None))
        self.checkBox_log_x.setText(QCoreApplication.translate("OutputFiles", u"Logarithmic scale for the X axis", None))
        self.checkBox_legend.setText(QCoreApplication.translate("OutputFiles", u"Show legend", None))
        self.checkBox_force_axis.setText(QCoreApplication.translate("OutputFiles", u"Force axis limits", None))
#if QT_CONFIG(tooltip)
        self.checkBox_force_axis.setToolTip(QCoreApplication.translate("OutputFiles", u"Enable this option for consistent axes across all pictures and define the axes limits. Otherwise, the axes are automatically determined based on the data.", None))
#endif // QT_CONFIG(tooltip)
        self.label_25.setText(QCoreApplication.translate("OutputFiles", u"x-min", None))
        self.label_26.setText(QCoreApplication.translate("OutputFiles", u"x-max", None))
        self.label_27.setText(QCoreApplication.translate("OutputFiles", u"y-min", None))
        self.label_28.setText(QCoreApplication.translate("OutputFiles", u"y-max", None))
        self.label_13.setText(QCoreApplication.translate("OutputFiles", u"Font", None))
        self.label_FontSize.setText(QCoreApplication.translate("OutputFiles", u"Font size", None))
        self.label_14.setText(QCoreApplication.translate("OutputFiles", u"Figure size (inch)", None))
        self.label_16.setText(QCoreApplication.translate("OutputFiles", u"Width", None))
        self.label_15.setText(QCoreApplication.translate("OutputFiles", u"Height", None))
        self.label_4.setText(QCoreApplication.translate("OutputFiles", u"Output folder", None))
        self.lineEdit_output.setPlaceholderText(QCoreApplication.translate("OutputFiles", u"Select the folder where the pictures will be saved", None))
        self.pushButton_choose.setText(QCoreApplication.translate("OutputFiles", u"Choose", None))
        self.label_5.setText(QCoreApplication.translate("OutputFiles", u"The pictures are .pdf files named with the report file name and the channel or ROI label. Existing pictures with the same names are replaced.", None))
        self.about_pictures_title_label.setText(QCoreApplication.translate("OutputFiles", u"About the pictures", None))
        self.about_pictures_label.setText(QCoreApplication.translate("OutputFiles", u"<b>Group level and cohort level</b><br/>\u2022 At the group level, each report file is a group. Its pictures show the subjects of the report.<br/>\u2022 At the cohort level, the report files with the same group label in step 2, \"Group Definition\", are put together. The colors differentiate the groups.<br/>\u2022 On every picture, the sleep stages are differentiated by the line style.<br/>\u2022 You can generate one picture for each channel or ROI, or put them all on a single picture.<br/><br/><b>Sleep stages and section</b><br/>\u2022 Select the preferred sleep stages and the section to display, \"Total\", a sleep cycle, a clock hour or a stage hour.<br/>\u2022 \"All\" plots the power of all the stages together.<br/>\u2022 Some reports are computed on annotations instead of sleep stages (step \"Section Selection\" of \"Analyze EEG Spectral Power\"). For these reports, the annotations are plotted in place of the sleep stages, and the sleep stage selection is not used.<br/>\u2022 A run cannot mix reports compu"
                        "ted per sleep stage and reports computed on annotations. Mixing them stops the run with an error.<br/>\u2022 The section must be in the reports. Check the distributions you need in the step \"Output Files\" of \"Analyze EEG Spectral Power\".<br/><br/><b>Picture names</b><br/>\u2022 At the group level, a picture is named with the report file name, the channel or ROI label, the section and the stages, then _mean or _mean_std with \"MEAN\" or \"MEAN + STD\". For example, learn-nsrr01_PSA_report_EEG_psa_Total_All_mean_std.pdf.<br/>\u2022 \"One picture per group\" adds avg, for example learn-nsrr01_PSA_report_avg_psa_Total_All_mean_std.pdf for several channels.<br/>\u2022 At the cohort level, a picture is named cohort_psa, then the display option and the section, and the channel or ROI label for one picture per channel. For example, cohort_psa_mean_std_Total.pdf and cohort_psa_mean_std_Total_EEG.pdf.", None))
    # retranslateUi

