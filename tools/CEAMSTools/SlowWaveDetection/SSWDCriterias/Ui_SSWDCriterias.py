# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SSWDCriterias.ui'
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
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)
import themes_rc

class Ui_SSWDCriterias(object):
    def setupUi(self, SSWDCriterias):
        if not SSWDCriterias.objectName():
            SSWDCriterias.setObjectName(u"SSWDCriterias")
        SSWDCriterias.resize(900, 700)
        self.verticalLayout = QVBoxLayout(SSWDCriterias)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(SSWDCriterias)
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

        self.settings_cards_layout = QHBoxLayout()
        self.settings_cards_layout.setSpacing(16)
        self.settings_cards_layout.setObjectName(u"settings_cards_layout")
        self.events_card = QFrame(self.content_widget)
        self.events_card.setObjectName(u"events_card")
        self.events_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.events_card.setFrameShadow(QFrame.Shadow.Raised)
        self.events_card_layout = QVBoxLayout(self.events_card)
        self.events_card_layout.setSpacing(10)
        self.events_card_layout.setObjectName(u"events_card_layout")
        self.events_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_16 = QLabel(self.events_card)
        self.label_16.setObjectName(u"label_16")
        font1 = QFont()
        font1.setBold(True)
        self.label_16.setFont(font1)

        self.events_card_layout.addWidget(self.label_16)

        self.events_grid = QGridLayout()
        self.events_grid.setObjectName(u"events_grid")
        self.events_grid.setHorizontalSpacing(12)
        self.events_grid.setVerticalSpacing(10)
        self.label_3 = QLabel(self.events_card)
        self.label_3.setObjectName(u"label_3")

        self.events_grid.addWidget(self.label_3, 0, 0, 1, 1)

        self.group_lineedit = QLineEdit(self.events_card)
        self.group_lineedit.setObjectName(u"group_lineedit")

        self.events_grid.addWidget(self.group_lineedit, 0, 1, 1, 1)

        self.label = QLabel(self.events_card)
        self.label.setObjectName(u"label")

        self.events_grid.addWidget(self.label, 1, 0, 1, 1)

        self.event_name_lineedit = QLineEdit(self.events_card)
        self.event_name_lineedit.setObjectName(u"event_name_lineedit")
        self.event_name_lineedit.setEnabled(True)

        self.events_grid.addWidget(self.event_name_lineedit, 1, 1, 1, 1)

        self.events_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.events_grid.addItem(self.events_grid_spacer, 0, 3, 1, 1)


        self.events_card_layout.addLayout(self.events_grid)

        self.label_18 = QLabel(self.events_card)
        self.label_18.setObjectName(u"label_18")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_18.setFont(font2)
        self.label_18.setWordWrap(True)
        self.label_18.setProperty(u"variant", u"help")

        self.events_card_layout.addWidget(self.label_18)

        self.events_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.events_card_layout.addItem(self.events_stretch)


        self.settings_cards_layout.addWidget(self.events_card)

        self.scope_card = QFrame(self.content_widget)
        self.scope_card.setObjectName(u"scope_card")
        self.scope_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.scope_card.setFrameShadow(QFrame.Shadow.Raised)
        self.scope_card_layout = QVBoxLayout(self.scope_card)
        self.scope_card_layout.setSpacing(10)
        self.scope_card_layout.setObjectName(u"scope_card_layout")
        self.scope_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_19 = QLabel(self.scope_card)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.scope_card_layout.addWidget(self.label_19)

        self.scope_layout = QVBoxLayout()
        self.scope_layout.setSpacing(8)
        self.scope_layout.setObjectName(u"scope_layout")
        self.scope_layout_1_layout = QVBoxLayout()
        self.scope_layout_1_layout.setSpacing(2)
        self.scope_layout_1_layout.setObjectName(u"scope_layout_1_layout")
        self.radioButton_sleep_stages = QRadioButton(self.scope_card)
        self.buttonGroup_stage_mode = QButtonGroup(SSWDCriterias)
        self.buttonGroup_stage_mode.setObjectName(u"buttonGroup_stage_mode")
        self.buttonGroup_stage_mode.addButton(self.radioButton_sleep_stages)
        self.radioButton_sleep_stages.setObjectName(u"radioButton_sleep_stages")
        self.radioButton_sleep_stages.setChecked(True)

        self.scope_layout_1_layout.addWidget(self.radioButton_sleep_stages)

        self.sleep_stages_layout = QVBoxLayout()
        self.sleep_stages_layout.setSpacing(8)
        self.sleep_stages_layout.setObjectName(u"sleep_stages_layout")
        self.sleep_stages_layout.setContentsMargins(0, 4, 0, 0)
        self.stages_layout = QHBoxLayout()
        self.stages_layout.setSpacing(22)
        self.stages_layout.setObjectName(u"stages_layout")
        self.stages_layout.setContentsMargins(26, 0, 0, 0)
        self.checkBox_n1 = QCheckBox(self.scope_card)
        self.checkBox_n1.setObjectName(u"checkBox_n1")

        self.stages_layout.addWidget(self.checkBox_n1)

        self.checkBox_n2 = QCheckBox(self.scope_card)
        self.checkBox_n2.setObjectName(u"checkBox_n2")
        self.checkBox_n2.setChecked(True)

        self.stages_layout.addWidget(self.checkBox_n2)

        self.checkBox_n3 = QCheckBox(self.scope_card)
        self.checkBox_n3.setObjectName(u"checkBox_n3")
        self.checkBox_n3.setChecked(True)

        self.stages_layout.addWidget(self.checkBox_n3)

        self.checkBox_r = QCheckBox(self.scope_card)
        self.checkBox_r.setObjectName(u"checkBox_r")

        self.stages_layout.addWidget(self.checkBox_r)

        self.stages_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.stages_layout.addItem(self.stages_spacer)


        self.sleep_stages_layout.addLayout(self.stages_layout)

        self.remp_layout = QHBoxLayout()
        self.remp_layout.setSpacing(16)
        self.remp_layout.setObjectName(u"remp_layout")
        self.remp_layout.setContentsMargins(26, 0, 0, 0)
        self.label_21 = QLabel(self.scope_card)
        self.label_21.setObjectName(u"label_21")

        self.remp_layout.addWidget(self.label_21)

        self.radioButton_excl_remp = QRadioButton(self.scope_card)
        self.radioButton_excl_remp.setObjectName(u"radioButton_excl_remp")

        self.remp_layout.addWidget(self.radioButton_excl_remp)

        self.radioButton_incl_remp = QRadioButton(self.scope_card)
        self.radioButton_incl_remp.setObjectName(u"radioButton_incl_remp")
        self.radioButton_incl_remp.setChecked(True)

        self.remp_layout.addWidget(self.radioButton_incl_remp)

        self.remp_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.remp_layout.addItem(self.remp_spacer)


        self.sleep_stages_layout.addLayout(self.remp_layout)


        self.scope_layout_1_layout.addLayout(self.sleep_stages_layout)


        self.scope_layout.addLayout(self.scope_layout_1_layout)

        self.scope_layout_line_1 = QFrame(self.scope_card)
        self.scope_layout_line_1.setObjectName(u"scope_layout_line_1")
        self.scope_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.scope_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.scope_layout.addWidget(self.scope_layout_line_1)

        self.scope_layout_2_layout = QVBoxLayout()
        self.scope_layout_2_layout.setSpacing(2)
        self.scope_layout_2_layout.setObjectName(u"scope_layout_2_layout")
        self.radioButton_unscored_mode = QRadioButton(self.scope_card)
        self.buttonGroup_stage_mode.addButton(self.radioButton_unscored_mode)
        self.radioButton_unscored_mode.setObjectName(u"radioButton_unscored_mode")

        self.scope_layout_2_layout.addWidget(self.radioButton_unscored_mode)

        self.unscored_help_label = QLabel(self.scope_card)
        self.unscored_help_label.setObjectName(u"unscored_help_label")
        self.unscored_help_label.setFont(font2)
        self.unscored_help_label.setWordWrap(True)
        self.unscored_help_label.setIndent(26)
        self.unscored_help_label.setProperty(u"variant", u"help")

        self.scope_layout_2_layout.addWidget(self.unscored_help_label)


        self.scope_layout.addLayout(self.scope_layout_2_layout)


        self.scope_card_layout.addLayout(self.scope_layout)

        self.scope_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.scope_card_layout.addItem(self.scope_stretch)


        self.settings_cards_layout.addWidget(self.scope_card)

        self.settings_cards_layout.setStretch(0, 1)
        self.settings_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.settings_cards_layout)

        self.criteria_card = QFrame(self.content_widget)
        self.criteria_card.setObjectName(u"criteria_card")
        self.criteria_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.criteria_card.setFrameShadow(QFrame.Shadow.Raised)
        self.criteria_card_layout = QVBoxLayout(self.criteria_card)
        self.criteria_card_layout.setSpacing(10)
        self.criteria_card_layout.setObjectName(u"criteria_card_layout")
        self.criteria_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_5 = QLabel(self.criteria_card)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.criteria_card_layout.addWidget(self.label_5)

        self.preset_layout = QVBoxLayout()
        self.preset_layout.setSpacing(8)
        self.preset_layout.setObjectName(u"preset_layout")
        self.preset_layout_1_layout = QVBoxLayout()
        self.preset_layout_1_layout.setSpacing(2)
        self.preset_layout_1_layout.setObjectName(u"preset_layout_1_layout")
        self.carrier_radioButton = QRadioButton(self.criteria_card)
        self.buttonGroup_2 = QButtonGroup(SSWDCriterias)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.carrier_radioButton)
        self.carrier_radioButton.setObjectName(u"carrier_radioButton")
        self.carrier_radioButton.setChecked(True)

        self.preset_layout_1_layout.addWidget(self.carrier_radioButton)

        self.carrier_help_label = QLabel(self.criteria_card)
        self.carrier_help_label.setObjectName(u"carrier_help_label")
        self.carrier_help_label.setFont(font2)
        self.carrier_help_label.setWordWrap(True)
        self.carrier_help_label.setIndent(26)
        self.carrier_help_label.setProperty(u"variant", u"help")

        self.preset_layout_1_layout.addWidget(self.carrier_help_label)


        self.preset_layout.addLayout(self.preset_layout_1_layout)

        self.preset_layout_line_1 = QFrame(self.criteria_card)
        self.preset_layout_line_1.setObjectName(u"preset_layout_line_1")
        self.preset_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.preset_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.preset_layout.addWidget(self.preset_layout_line_1)

        self.preset_layout_2_layout = QVBoxLayout()
        self.preset_layout_2_layout.setSpacing(2)
        self.preset_layout_2_layout.setObjectName(u"preset_layout_2_layout")
        self.personalized_radioButton = QRadioButton(self.criteria_card)
        self.buttonGroup_2.addButton(self.personalized_radioButton)
        self.personalized_radioButton.setObjectName(u"personalized_radioButton")

        self.preset_layout_2_layout.addWidget(self.personalized_radioButton)

        self.personalized_help_label = QLabel(self.criteria_card)
        self.personalized_help_label.setObjectName(u"personalized_help_label")
        self.personalized_help_label.setFont(font2)
        self.personalized_help_label.setWordWrap(True)
        self.personalized_help_label.setIndent(26)
        self.personalized_help_label.setProperty(u"variant", u"help")

        self.preset_layout_2_layout.addWidget(self.personalized_help_label)


        self.preset_layout.addLayout(self.preset_layout_2_layout)


        self.criteria_card_layout.addLayout(self.preset_layout)

        self.line = QFrame(self.criteria_card)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Plain)

        self.criteria_card_layout.addWidget(self.line)

        self.criteria_grid = QGridLayout()
        self.criteria_grid.setObjectName(u"criteria_grid")
        self.criteria_grid.setHorizontalSpacing(12)
        self.criteria_grid.setVerticalSpacing(10)
        self.label_9 = QLabel(self.criteria_card)
        self.label_9.setObjectName(u"label_9")

        self.criteria_grid.addWidget(self.label_9, 0, 0, 1, 1)

        self.doubleSpinBox_f_min = QDoubleSpinBox(self.criteria_card)
        self.doubleSpinBox_f_min.setObjectName(u"doubleSpinBox_f_min")
        self.doubleSpinBox_f_min.setMaximumSize(QSize(110, 16777215))
        self.doubleSpinBox_f_min.setEnabled(False)

        self.criteria_grid.addWidget(self.doubleSpinBox_f_min, 0, 1, 1, 1)

        self.label_11 = QLabel(self.criteria_card)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.label_11, 0, 2, 1, 1)

        self.doubleSpinBox_f_max = QDoubleSpinBox(self.criteria_card)
        self.doubleSpinBox_f_max.setObjectName(u"doubleSpinBox_f_max")
        self.doubleSpinBox_f_max.setMaximumSize(QSize(110, 16777215))
        self.doubleSpinBox_f_max.setEnabled(False)

        self.criteria_grid.addWidget(self.doubleSpinBox_f_max, 0, 3, 1, 1)

        self.f_unit_label = QLabel(self.criteria_card)
        self.f_unit_label.setObjectName(u"f_unit_label")
        self.f_unit_label.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.f_unit_label, 0, 4, 1, 1)

        self.label_2 = QLabel(self.criteria_card)
        self.label_2.setObjectName(u"label_2")

        self.criteria_grid.addWidget(self.label_2, 1, 0, 1, 1)

        self.doubleSpinBox_PaP_amp = QDoubleSpinBox(self.criteria_card)
        self.doubleSpinBox_PaP_amp.setObjectName(u"doubleSpinBox_PaP_amp")
        self.doubleSpinBox_PaP_amp.setMaximumSize(QSize(110, 16777215))
        self.doubleSpinBox_PaP_amp.setEnabled(False)
        self.doubleSpinBox_PaP_amp.setMaximum(200.000000000000000)

        self.criteria_grid.addWidget(self.doubleSpinBox_PaP_amp, 1, 1, 1, 1)

        self.pap_unit_label = QLabel(self.criteria_card)
        self.pap_unit_label.setObjectName(u"pap_unit_label")
        self.pap_unit_label.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.pap_unit_label, 1, 2, 1, 1)

        self.label_4 = QLabel(self.criteria_card)
        self.label_4.setObjectName(u"label_4")

        self.criteria_grid.addWidget(self.label_4, 2, 0, 1, 1)

        self.doubleSpinBox_neg_amp = QDoubleSpinBox(self.criteria_card)
        self.doubleSpinBox_neg_amp.setObjectName(u"doubleSpinBox_neg_amp")
        self.doubleSpinBox_neg_amp.setMaximumSize(QSize(110, 16777215))
        self.doubleSpinBox_neg_amp.setEnabled(False)
        self.doubleSpinBox_neg_amp.setMaximum(200.000000000000000)

        self.criteria_grid.addWidget(self.doubleSpinBox_neg_amp, 2, 1, 1, 1)

        self.neg_unit_label = QLabel(self.criteria_card)
        self.neg_unit_label.setObjectName(u"neg_unit_label")
        self.neg_unit_label.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.neg_unit_label, 2, 2, 1, 1)

        self.label_6 = QLabel(self.criteria_card)
        self.label_6.setObjectName(u"label_6")

        self.criteria_grid.addWidget(self.label_6, 3, 0, 1, 1)

        self.spinBox_min_neg = QSpinBox(self.criteria_card)
        self.spinBox_min_neg.setObjectName(u"spinBox_min_neg")
        self.spinBox_min_neg.setMaximumSize(QSize(110, 16777215))
        self.spinBox_min_neg.setEnabled(False)
        self.spinBox_min_neg.setMaximum(3000)

        self.criteria_grid.addWidget(self.spinBox_min_neg, 3, 1, 1, 1)

        self.label_13 = QLabel(self.criteria_card)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.label_13, 3, 2, 1, 1)

        self.spinBox_max_neg = QSpinBox(self.criteria_card)
        self.spinBox_max_neg.setObjectName(u"spinBox_max_neg")
        self.spinBox_max_neg.setMaximumSize(QSize(110, 16777215))
        self.spinBox_max_neg.setEnabled(False)
        self.spinBox_max_neg.setMaximum(3000)

        self.criteria_grid.addWidget(self.spinBox_max_neg, 3, 3, 1, 1)

        self.neg_ms_unit_label = QLabel(self.criteria_card)
        self.neg_ms_unit_label.setObjectName(u"neg_ms_unit_label")
        self.neg_ms_unit_label.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.neg_ms_unit_label, 3, 4, 1, 1)

        self.label_7 = QLabel(self.criteria_card)
        self.label_7.setObjectName(u"label_7")

        self.criteria_grid.addWidget(self.label_7, 4, 0, 1, 1)

        self.spinBox_min_pos = QSpinBox(self.criteria_card)
        self.spinBox_min_pos.setObjectName(u"spinBox_min_pos")
        self.spinBox_min_pos.setMaximumSize(QSize(110, 16777215))
        self.spinBox_min_pos.setEnabled(False)
        self.spinBox_min_pos.setMaximum(3000)

        self.criteria_grid.addWidget(self.spinBox_min_pos, 4, 1, 1, 1)

        self.label_15 = QLabel(self.criteria_card)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.label_15, 4, 2, 1, 1)

        self.spinBox_max_pos = QSpinBox(self.criteria_card)
        self.spinBox_max_pos.setObjectName(u"spinBox_max_pos")
        self.spinBox_max_pos.setMaximumSize(QSize(110, 16777215))
        self.spinBox_max_pos.setEnabled(False)
        self.spinBox_max_pos.setMaximum(3000)

        self.criteria_grid.addWidget(self.spinBox_max_pos, 4, 3, 1, 1)

        self.pos_ms_unit_label = QLabel(self.criteria_card)
        self.pos_ms_unit_label.setObjectName(u"pos_ms_unit_label")
        self.pos_ms_unit_label.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.pos_ms_unit_label, 4, 4, 1, 1)

        self.criteria_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.criteria_grid.addItem(self.criteria_grid_spacer, 0, 5, 1, 1)


        self.criteria_card_layout.addLayout(self.criteria_grid)

        self.criteria_help_label = QLabel(self.criteria_card)
        self.criteria_help_label.setObjectName(u"criteria_help_label")
        self.criteria_help_label.setFont(font2)
        self.criteria_help_label.setWordWrap(True)
        self.criteria_help_label.setProperty(u"variant", u"help")

        self.criteria_card_layout.addWidget(self.criteria_help_label)

        self.age_sex_line = QFrame(self.criteria_card)
        self.age_sex_line.setObjectName(u"age_sex_line")
        self.age_sex_line.setFrameShape(QFrame.Shape.HLine)
        self.age_sex_line.setFrameShadow(QFrame.Shadow.Plain)

        self.criteria_card_layout.addWidget(self.age_sex_line)

        self.age_sex_grid = QGridLayout()
        self.age_sex_grid.setObjectName(u"age_sex_grid")
        self.age_sex_grid.setHorizontalSpacing(12)
        self.age_sex_grid.setVerticalSpacing(10)
        self.checkBox_age = QCheckBox(self.criteria_card)
        self.checkBox_age.setObjectName(u"checkBox_age")
        self.checkBox_age.setEnabled(False)
        self.checkBox_age.setTristate(False)

        self.age_sex_grid.addWidget(self.checkBox_age, 0, 0, 1, 1)

        self.spinBox_years = QSpinBox(self.criteria_card)
        self.spinBox_years.setObjectName(u"spinBox_years")
        self.spinBox_years.setMaximumSize(QSize(110, 16777215))
        self.spinBox_years.setEnabled(False)
        self.spinBox_years.setMaximum(122)

        self.age_sex_grid.addWidget(self.spinBox_years, 0, 1, 1, 1)

        self.label_years = QLabel(self.criteria_card)
        self.label_years.setObjectName(u"label_years")
        self.label_years.setEnabled(False)

        self.age_sex_grid.addWidget(self.label_years, 0, 2, 1, 1)

        self.spinBox_months = QSpinBox(self.criteria_card)
        self.spinBox_months.setObjectName(u"spinBox_months")
        self.spinBox_months.setMaximumSize(QSize(110, 16777215))
        self.spinBox_months.setEnabled(False)
        self.spinBox_months.setMaximum(11)

        self.age_sex_grid.addWidget(self.spinBox_months, 0, 3, 1, 1)

        self.label_months = QLabel(self.criteria_card)
        self.label_months.setObjectName(u"label_months")
        self.label_months.setEnabled(False)

        self.age_sex_grid.addWidget(self.label_months, 0, 4, 1, 1)

        self.checkBox_sex = QCheckBox(self.criteria_card)
        self.checkBox_sex.setObjectName(u"checkBox_sex")
        self.checkBox_sex.setEnabled(False)

        self.age_sex_grid.addWidget(self.checkBox_sex, 1, 0, 1, 1)

        self.comboBox_sex = QComboBox(self.criteria_card)
        self.comboBox_sex.addItem("")
        self.comboBox_sex.addItem("")
        self.comboBox_sex.setObjectName(u"comboBox_sex")
        self.comboBox_sex.setEnabled(False)

        self.age_sex_grid.addWidget(self.comboBox_sex, 1, 1, 1, 3)

        self.age_sex_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.age_sex_grid.addItem(self.age_sex_grid_spacer, 0, 5, 1, 1)


        self.criteria_card_layout.addLayout(self.age_sex_grid)

        self.age_sex_help_label = QLabel(self.criteria_card)
        self.age_sex_help_label.setObjectName(u"age_sex_help_label")
        self.age_sex_help_label.setFont(font2)
        self.age_sex_help_label.setWordWrap(True)
        self.age_sex_help_label.setProperty(u"variant", u"help")

        self.criteria_card_layout.addWidget(self.age_sex_help_label)


        self.content_layout.addWidget(self.criteria_card)

        self.about_wave_layout = QVBoxLayout()
        self.about_wave_layout.setSpacing(6)
        self.about_wave_layout.setObjectName(u"about_wave_layout")
        self.about_wave_title_label = QLabel(self.content_widget)
        self.about_wave_title_label.setObjectName(u"about_wave_title_label")
        self.about_wave_title_label.setFont(font1)

        self.about_wave_layout.addWidget(self.about_wave_title_label)

        self.about_wave_row = QHBoxLayout()
        self.about_wave_row.setSpacing(16)
        self.about_wave_row.setObjectName(u"about_wave_row")
        self.phase_card = QFrame(self.content_widget)
        self.phase_card.setObjectName(u"phase_card")
        self.phase_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.phase_card.setFrameShadow(QFrame.Shadow.Raised)
        self.phase_card_layout = QVBoxLayout(self.phase_card)
        self.phase_card_layout.setSpacing(10)
        self.phase_card_layout.setObjectName(u"phase_card_layout")
        self.phase_card_layout.setContentsMargins(10, 10, 10, 10)
        self.phase_image = QLabel(self.phase_card)
        self.phase_image.setObjectName(u"phase_image")

        self.phase_card_layout.addWidget(self.phase_image)

        self.phase_caption_label = QLabel(self.phase_card)
        self.phase_caption_label.setObjectName(u"phase_caption_label")
        self.phase_caption_label.setFont(font2)
        self.phase_caption_label.setWordWrap(True)
        self.phase_caption_label.setProperty(u"variant", u"help")

        self.phase_card_layout.addWidget(self.phase_caption_label)


        self.about_wave_row.addWidget(self.phase_card)

        self.about_wave_label = QLabel(self.content_widget)
        self.about_wave_label.setObjectName(u"about_wave_label")
        self.about_wave_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_wave_label.setWordWrap(True)
        self.about_wave_label.setProperty(u"variant", u"help")
        self.about_wave_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.about_wave_row.addWidget(self.about_wave_label)

        self.about_wave_row.setStretch(0, 1)
        self.about_wave_row.setStretch(1, 1)

        self.about_wave_layout.addLayout(self.about_wave_row)

        self.references_layout = QVBoxLayout()
        self.references_layout.setSpacing(8)
        self.references_layout.setObjectName(u"references_layout")
        self.references_layout.setContentsMargins(0, 6, 0, 0)
        self.references_line = QFrame(self.content_widget)
        self.references_line.setObjectName(u"references_line")
        self.references_line.setFrameShape(QFrame.Shape.HLine)
        self.references_line.setFrameShadow(QFrame.Shadow.Plain)

        self.references_layout.addWidget(self.references_line)

        self.references_label = QLabel(self.content_widget)
        self.references_label.setObjectName(u"references_label")
        self.references_label.setFont(font2)
        self.references_label.setTextFormat(Qt.TextFormat.RichText)
        self.references_label.setWordWrap(True)
        self.references_label.setOpenExternalLinks(True)
        self.references_label.setProperty(u"variant", u"help")

        self.references_layout.addWidget(self.references_label)


        self.about_wave_layout.addLayout(self.references_layout)


        self.content_layout.addLayout(self.about_wave_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SSWDCriterias)
        self.buttonGroup_stage_mode.buttonClicked.connect(SSWDCriterias.on_stage_mode_changed)
        self.buttonGroup_2.buttonClicked.connect(SSWDCriterias.on_input_format_changed)
        self.checkBox_age.clicked.connect(SSWDCriterias.on_input_format_changed)
        self.checkBox_sex.clicked.connect(SSWDCriterias.on_input_format_changed)

        QMetaObject.connectSlotsByName(SSWDCriterias)
    # setupUi

    def retranslateUi(self, SSWDCriterias):
        SSWDCriterias.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("SSWDCriterias", u"Detection Criteria", None))
        self.subtitle_label.setText(QCoreApplication.translate("SSWDCriterias", u"Define the slow wave events, the criteria of the detector and the part of the recording in which slow waves are detected.", None))
        self.label_16.setText(QCoreApplication.translate("SSWDCriterias", u"Slow wave events", None))
        self.label_3.setText(QCoreApplication.translate("SSWDCriterias", u"Group", None))
        self.label.setText(QCoreApplication.translate("SSWDCriterias", u"Name", None))
        self.label_18.setText(QCoreApplication.translate("SSWDCriterias", u"The detected slow waves are added to the accessory file with this group and name.", None))
        self.label_19.setText(QCoreApplication.translate("SSWDCriterias", u"Recording scope", None))
        self.radioButton_sleep_stages.setText(QCoreApplication.translate("SSWDCriterias", u"Sleep stages", None))
        self.checkBox_n1.setText(QCoreApplication.translate("SSWDCriterias", u"N1", None))
        self.checkBox_n2.setText(QCoreApplication.translate("SSWDCriterias", u"N2", None))
        self.checkBox_n3.setText(QCoreApplication.translate("SSWDCriterias", u"N3", None))
        self.checkBox_r.setText(QCoreApplication.translate("SSWDCriterias", u"R", None))
        self.label_21.setText(QCoreApplication.translate("SSWDCriterias", u"Exclude REM periods", None))
        self.radioButton_excl_remp.setText(QCoreApplication.translate("SSWDCriterias", u"Yes", None))
        self.radioButton_incl_remp.setText(QCoreApplication.translate("SSWDCriterias", u"No", None))
        self.radioButton_unscored_mode.setText(QCoreApplication.translate("SSWDCriterias", u"Unscored", None))
        self.unscored_help_label.setText(QCoreApplication.translate("SSWDCriterias", u"The whole recording, when it has no sleep stages.", None))
        self.label_5.setText(QCoreApplication.translate("SSWDCriterias", u"Slow wave criteria", None))
        self.carrier_radioButton.setText(QCoreApplication.translate("SSWDCriterias", u"Carrier", None))
        self.carrier_help_label.setText(QCoreApplication.translate("SSWDCriterias", u"The default criteria, not editable.", None))
        self.personalized_radioButton.setText(QCoreApplication.translate("SSWDCriterias", u"Personalized settings", None))
        self.personalized_help_label.setText(QCoreApplication.translate("SSWDCriterias", u"Edit the criteria below.", None))
        self.label_9.setText(QCoreApplication.translate("SSWDCriterias", u"Band-pass filter", None))
        self.label_11.setText(QCoreApplication.translate("SSWDCriterias", u"to", None))
        self.f_unit_label.setText(QCoreApplication.translate("SSWDCriterias", u"Hz", None))
        self.label_2.setText(QCoreApplication.translate("SSWDCriterias", u"Peak-to-peak amplitude (H to D)", None))
        self.pap_unit_label.setText(QCoreApplication.translate("SSWDCriterias", u"\u00b5V", None))
        self.label_4.setText(QCoreApplication.translate("SSWDCriterias", u"Negative amplitude (H)", None))
        self.neg_unit_label.setText(QCoreApplication.translate("SSWDCriterias", u"\u00b5V", None))
        self.label_6.setText(QCoreApplication.translate("SSWDCriterias", u"Duration of the negative part", None))
        self.label_13.setText(QCoreApplication.translate("SSWDCriterias", u"to", None))
        self.neg_ms_unit_label.setText(QCoreApplication.translate("SSWDCriterias", u"ms", None))
        self.label_7.setText(QCoreApplication.translate("SSWDCriterias", u"Duration of the positive part", None))
        self.label_15.setText(QCoreApplication.translate("SSWDCriterias", u"to", None))
        self.pos_ms_unit_label.setText(QCoreApplication.translate("SSWDCriterias", u"ms", None))
        self.criteria_help_label.setText(QCoreApplication.translate("SSWDCriterias", u"A wave is a slow wave when its amplitudes are above these values and the durations of its parts are within these ranges. The filter is applied before the detection.", None))
#if QT_CONFIG(whatsthis)
        self.checkBox_age.setWhatsThis(QCoreApplication.translate("SSWDCriterias", u"Modify parameters automatically according to patients age", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBox_age.setText(QCoreApplication.translate("SSWDCriterias", u"Age", None))
        self.label_years.setText(QCoreApplication.translate("SSWDCriterias", u"years", None))
        self.label_months.setText(QCoreApplication.translate("SSWDCriterias", u"months", None))
#if QT_CONFIG(whatsthis)
        self.checkBox_sex.setWhatsThis(QCoreApplication.translate("SSWDCriterias", u"<html><head/><body><p>Modify parameters according to patients sex</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBox_sex.setText(QCoreApplication.translate("SSWDCriterias", u"Sex", None))
        self.comboBox_sex.setItemText(0, QCoreApplication.translate("SSWDCriterias", u"Female", None))
        self.comboBox_sex.setItemText(1, QCoreApplication.translate("SSWDCriterias", u"Male", None))

        self.age_sex_help_label.setText(QCoreApplication.translate("SSWDCriterias", u"Not available yet: the criteria do not change with the age or the sex.", None))
        self.about_wave_title_label.setText(QCoreApplication.translate("SSWDCriterias", u"About the slow wave", None))
        self.phase_image.setText("")
        self.phase_caption_label.setText(QCoreApplication.translate("SSWDCriterias", u"Phase of a slow wave [1]: the transition from H to D is highlighted.", None))
        self.about_wave_label.setText(QCoreApplication.translate("SSWDCriterias", u"A slow wave goes from a zero crossing of the filtered EEG (positive to negative) to the next one [1].<br/>\u2022 <b>H</b>: negative peak (hyperpolarization)<br/>\u2022 <b>D</b>: positive peak (depolarization)<br/>\u2022 <b>T</b>: duration of the wave; 1/T is its frequency<br/>\u2022 <b>\u03c4</b>: time from H to D; 1/(2\u03c4) is the transition frequency", None))
        self.references_label.setText(QCoreApplication.translate("SSWDCriterias", u"[1] Bouchard, M., Lina, J.-M., Gaudreault, P.-O., Lafreni\u00e8re, A., Dub\u00e9, J., Gosselin, N., &amp; Carrier, J. (2021). Sleeping at the switch. <i>eLife</i>, <i>10</i>, Article e64337. <a href=\"https://doi.org/10.7554/eLife.64337\">https://doi.org/10.7554/eLife.64337</a>", None))
    # retranslateUi

