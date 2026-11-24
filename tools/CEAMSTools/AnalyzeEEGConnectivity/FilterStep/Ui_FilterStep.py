# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_FilterStep.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_FilterStep(object):
    def setupUi(self, FilterStep):
        if not FilterStep.objectName():
            FilterStep.setObjectName(u"FilterStep")
        FilterStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(FilterStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(FilterStep)
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

        self.band_card = QFrame(self.content_widget)
        self.band_card.setObjectName(u"band_card")
        self.band_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.band_card.setFrameShadow(QFrame.Shadow.Raised)
        self.band_card_layout = QVBoxLayout(self.band_card)
        self.band_card_layout.setSpacing(10)
        self.band_card_layout.setObjectName(u"band_card_layout")
        self.band_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_4 = QLabel(self.band_card)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setBold(True)
        self.label_4.setFont(font1)

        self.band_card_layout.addWidget(self.label_4)

        self.label = QLabel(self.band_card)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)
        self.label.setProperty(u"variant", u"help")

        self.band_card_layout.addWidget(self.label)

        self.bands_layout = QVBoxLayout()
        self.bands_layout.setSpacing(8)
        self.bands_layout.setObjectName(u"bands_layout")
        self.fullband_radioButton = QRadioButton(self.band_card)
        self.buttonGroup_freq = QButtonGroup(FilterStep)
        self.buttonGroup_freq.setObjectName(u"buttonGroup_freq")
        self.buttonGroup_freq.addButton(self.fullband_radioButton)
        self.fullband_radioButton.setObjectName(u"fullband_radioButton")
        self.fullband_radioButton.setChecked(True)

        self.bands_layout.addWidget(self.fullband_radioButton)

        self.standard_bands_layout = QHBoxLayout()
        self.standard_bands_layout.setSpacing(24)
        self.standard_bands_layout.setObjectName(u"standard_bands_layout")
        self.delta_radioButton = QRadioButton(self.band_card)
        self.buttonGroup_freq.addButton(self.delta_radioButton)
        self.delta_radioButton.setObjectName(u"delta_radioButton")

        self.standard_bands_layout.addWidget(self.delta_radioButton)

        self.theta_radioButton = QRadioButton(self.band_card)
        self.buttonGroup_freq.addButton(self.theta_radioButton)
        self.theta_radioButton.setObjectName(u"theta_radioButton")

        self.standard_bands_layout.addWidget(self.theta_radioButton)

        self.alpha_radioButton = QRadioButton(self.band_card)
        self.buttonGroup_freq.addButton(self.alpha_radioButton)
        self.alpha_radioButton.setObjectName(u"alpha_radioButton")

        self.standard_bands_layout.addWidget(self.alpha_radioButton)

        self.beta_radioButton = QRadioButton(self.band_card)
        self.buttonGroup_freq.addButton(self.beta_radioButton)
        self.beta_radioButton.setObjectName(u"beta_radioButton")

        self.standard_bands_layout.addWidget(self.beta_radioButton)

        self.standard_bands_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.standard_bands_layout.addItem(self.standard_bands_spacer)


        self.bands_layout.addLayout(self.standard_bands_layout)

        self.custom_radioButton = QRadioButton(self.band_card)
        self.buttonGroup_freq.addButton(self.custom_radioButton)
        self.custom_radioButton.setObjectName(u"custom_radioButton")

        self.bands_layout.addWidget(self.custom_radioButton)

        self.custom_band_layout = QHBoxLayout()
        self.custom_band_layout.setSpacing(8)
        self.custom_band_layout.setObjectName(u"custom_band_layout")
        self.custom_band_layout.setContentsMargins(26, 0, 0, 0)
        self.low_cutoff_label = QLabel(self.band_card)
        self.low_cutoff_label.setObjectName(u"low_cutoff_label")
        self.low_cutoff_label.setEnabled(False)

        self.custom_band_layout.addWidget(self.low_cutoff_label)

        self.lowcutoff_doubleSpinBox = QDoubleSpinBox(self.band_card)
        self.lowcutoff_doubleSpinBox.setObjectName(u"lowcutoff_doubleSpinBox")
        self.lowcutoff_doubleSpinBox.setMaximumSize(QSize(110, 16777215))
        self.lowcutoff_doubleSpinBox.setEnabled(False)
        self.lowcutoff_doubleSpinBox.setMinimum(0.100000000000000)
        self.lowcutoff_doubleSpinBox.setMaximum(40.000000000000000)

        self.custom_band_layout.addWidget(self.lowcutoff_doubleSpinBox)

        self.low_cutoff_unit_label = QLabel(self.band_card)
        self.low_cutoff_unit_label.setObjectName(u"low_cutoff_unit_label")
        self.low_cutoff_unit_label.setProperty(u"variant", u"help")

        self.custom_band_layout.addWidget(self.low_cutoff_unit_label)

        self.custom_band_gap = QSpacerItem(16, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.custom_band_layout.addItem(self.custom_band_gap)

        self.high_cutoff_label = QLabel(self.band_card)
        self.high_cutoff_label.setObjectName(u"high_cutoff_label")
        self.high_cutoff_label.setEnabled(False)

        self.custom_band_layout.addWidget(self.high_cutoff_label)

        self.highcutoff_doubleSpinBox = QDoubleSpinBox(self.band_card)
        self.highcutoff_doubleSpinBox.setObjectName(u"highcutoff_doubleSpinBox")
        self.highcutoff_doubleSpinBox.setMaximumSize(QSize(110, 16777215))
        self.highcutoff_doubleSpinBox.setEnabled(False)

        self.custom_band_layout.addWidget(self.highcutoff_doubleSpinBox)

        self.high_cutoff_unit_label = QLabel(self.band_card)
        self.high_cutoff_unit_label.setObjectName(u"high_cutoff_unit_label")
        self.high_cutoff_unit_label.setProperty(u"variant", u"help")

        self.custom_band_layout.addWidget(self.high_cutoff_unit_label)

        self.custom_band_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.custom_band_layout.addItem(self.custom_band_spacer)


        self.bands_layout.addLayout(self.custom_band_layout)


        self.band_card_layout.addLayout(self.bands_layout)

        self.band_help_label = QLabel(self.band_card)
        self.band_help_label.setObjectName(u"band_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.band_help_label.setFont(font2)
        self.band_help_label.setWordWrap(True)
        self.band_help_label.setProperty(u"variant", u"help")

        self.band_card_layout.addWidget(self.band_help_label)


        self.content_layout.addWidget(self.band_card)

        self.scope_card = QFrame(self.content_widget)
        self.scope_card.setObjectName(u"scope_card")
        self.scope_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.scope_card.setFrameShadow(QFrame.Shadow.Raised)
        self.scope_card_layout = QVBoxLayout(self.scope_card)
        self.scope_card_layout.setSpacing(10)
        self.scope_card_layout.setObjectName(u"scope_card_layout")
        self.scope_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_3 = QLabel(self.scope_card)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.scope_card_layout.addWidget(self.label_3)

        self.scopes_label = QLabel(self.scope_card)
        self.scopes_label.setObjectName(u"scopes_label")
        self.scopes_label.setWordWrap(True)
        self.scopes_label.setProperty(u"variant", u"help")

        self.scope_card_layout.addWidget(self.scopes_label)

        self.scope_layout = QVBoxLayout()
        self.scope_layout.setSpacing(8)
        self.scope_layout.setObjectName(u"scope_layout")
        self.scope_layout_1_layout = QVBoxLayout()
        self.scope_layout_1_layout.setSpacing(2)
        self.scope_layout_1_layout.setObjectName(u"scope_layout_1_layout")
        self.sleep_stages_radioButton = QRadioButton(self.scope_card)
        self.buttonGroup_scope = QButtonGroup(FilterStep)
        self.buttonGroup_scope.setObjectName(u"buttonGroup_scope")
        self.buttonGroup_scope.addButton(self.sleep_stages_radioButton)
        self.sleep_stages_radioButton.setObjectName(u"sleep_stages_radioButton")
        self.sleep_stages_radioButton.setChecked(True)

        self.scope_layout_1_layout.addWidget(self.sleep_stages_radioButton)

        self.sleep_stages_layout = QVBoxLayout()
        self.sleep_stages_layout.setSpacing(6)
        self.sleep_stages_layout.setObjectName(u"sleep_stages_layout")
        self.sleep_stages_help_label = QLabel(self.scope_card)
        self.sleep_stages_help_label.setObjectName(u"sleep_stages_help_label")
        self.sleep_stages_help_label.setFont(font2)
        self.sleep_stages_help_label.setWordWrap(True)
        self.sleep_stages_help_label.setIndent(26)
        self.sleep_stages_help_label.setProperty(u"variant", u"help")

        self.sleep_stages_layout.addWidget(self.sleep_stages_help_label)

        self.stages_layout = QHBoxLayout()
        self.stages_layout.setSpacing(22)
        self.stages_layout.setObjectName(u"stages_layout")
        self.stages_layout.setContentsMargins(26, 0, 0, 0)
        self.n1_checkBox = QCheckBox(self.scope_card)
        self.n1_checkBox.setObjectName(u"n1_checkBox")

        self.stages_layout.addWidget(self.n1_checkBox)

        self.n2_checkBox = QCheckBox(self.scope_card)
        self.n2_checkBox.setObjectName(u"n2_checkBox")

        self.stages_layout.addWidget(self.n2_checkBox)

        self.n3_checkBox = QCheckBox(self.scope_card)
        self.n3_checkBox.setObjectName(u"n3_checkBox")
        self.n3_checkBox.setChecked(True)

        self.stages_layout.addWidget(self.n3_checkBox)

        self.rem_checkBox = QCheckBox(self.scope_card)
        self.rem_checkBox.setObjectName(u"rem_checkBox")

        self.stages_layout.addWidget(self.rem_checkBox)

        self.stages_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.stages_layout.addItem(self.stages_spacer)


        self.sleep_stages_layout.addLayout(self.stages_layout)


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
        self.unscored_radioButton = QRadioButton(self.scope_card)
        self.buttonGroup_scope.addButton(self.unscored_radioButton)
        self.unscored_radioButton.setObjectName(u"unscored_radioButton")
        self.unscored_radioButton.setChecked(False)

        self.scope_layout_2_layout.addWidget(self.unscored_radioButton)

        self.unscored_layout = QVBoxLayout()
        self.unscored_layout.setSpacing(6)
        self.unscored_layout.setObjectName(u"unscored_layout")
        self.unscored_help_label = QLabel(self.scope_card)
        self.unscored_help_label.setObjectName(u"unscored_help_label")
        self.unscored_help_label.setFont(font2)
        self.unscored_help_label.setWordWrap(True)
        self.unscored_help_label.setIndent(26)
        self.unscored_help_label.setProperty(u"variant", u"help")

        self.unscored_layout.addWidget(self.unscored_help_label)

        self.trim_layout = QHBoxLayout()
        self.trim_layout.setSpacing(8)
        self.trim_layout.setObjectName(u"trim_layout")
        self.trim_layout.setContentsMargins(26, 0, 0, 0)
        self.trim_checkBox = QCheckBox(self.scope_card)
        self.trim_checkBox.setObjectName(u"trim_checkBox")
        self.trim_checkBox.setEnabled(False)

        self.trim_layout.addWidget(self.trim_checkBox)

        self.trim_gap = QSpacerItem(16, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.trim_layout.addItem(self.trim_gap)

        self.start_time_label = QLabel(self.scope_card)
        self.start_time_label.setObjectName(u"start_time_label")
        self.start_time_label.setEnabled(False)

        self.trim_layout.addWidget(self.start_time_label)

        self.start_time_doubleSpinBox = QDoubleSpinBox(self.scope_card)
        self.start_time_doubleSpinBox.setObjectName(u"start_time_doubleSpinBox")
        self.start_time_doubleSpinBox.setMaximumSize(QSize(110, 16777215))
        self.start_time_doubleSpinBox.setEnabled(False)
        self.start_time_doubleSpinBox.setMaximum(1000000.000000000000000)
        self.start_time_doubleSpinBox.setSingleStep(10.000000000000000)

        self.trim_layout.addWidget(self.start_time_doubleSpinBox)

        self.start_time_unit_label = QLabel(self.scope_card)
        self.start_time_unit_label.setObjectName(u"start_time_unit_label")
        self.start_time_unit_label.setProperty(u"variant", u"help")

        self.trim_layout.addWidget(self.start_time_unit_label)

        self.trim_gap_2 = QSpacerItem(16, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.trim_layout.addItem(self.trim_gap_2)

        self.duration_time_label = QLabel(self.scope_card)
        self.duration_time_label.setObjectName(u"duration_time_label")
        self.duration_time_label.setEnabled(False)

        self.trim_layout.addWidget(self.duration_time_label)

        self.duration_time_doubleSpinBox = QDoubleSpinBox(self.scope_card)
        self.duration_time_doubleSpinBox.setObjectName(u"duration_time_doubleSpinBox")
        self.duration_time_doubleSpinBox.setMaximumSize(QSize(110, 16777215))
        self.duration_time_doubleSpinBox.setEnabled(False)
        self.duration_time_doubleSpinBox.setMaximum(1000000.000000000000000)
        self.duration_time_doubleSpinBox.setSingleStep(10.000000000000000)
        self.duration_time_doubleSpinBox.setValue(300.000000000000000)

        self.trim_layout.addWidget(self.duration_time_doubleSpinBox)

        self.duration_time_unit_label = QLabel(self.scope_card)
        self.duration_time_unit_label.setObjectName(u"duration_time_unit_label")
        self.duration_time_unit_label.setProperty(u"variant", u"help")

        self.trim_layout.addWidget(self.duration_time_unit_label)

        self.trim_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.trim_layout.addItem(self.trim_spacer)


        self.unscored_layout.addLayout(self.trim_layout)


        self.scope_layout_2_layout.addLayout(self.unscored_layout)


        self.scope_layout.addLayout(self.scope_layout_2_layout)

        self.scope_layout_line_2 = QFrame(self.scope_card)
        self.scope_layout_line_2.setObjectName(u"scope_layout_line_2")
        self.scope_layout_line_2.setFrameShape(QFrame.Shape.HLine)
        self.scope_layout_line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.scope_layout.addWidget(self.scope_layout_line_2)

        self.scope_layout_3_layout = QVBoxLayout()
        self.scope_layout_3_layout.setSpacing(2)
        self.scope_layout_3_layout.setObjectName(u"scope_layout_3_layout")
        self.specific_annotations_radioButton = QRadioButton(self.scope_card)
        self.buttonGroup_scope.addButton(self.specific_annotations_radioButton)
        self.specific_annotations_radioButton.setObjectName(u"specific_annotations_radioButton")

        self.scope_layout_3_layout.addWidget(self.specific_annotations_radioButton)

        self.annotations_help_label = QLabel(self.scope_card)
        self.annotations_help_label.setObjectName(u"annotations_help_label")
        self.annotations_help_label.setFont(font2)
        self.annotations_help_label.setWordWrap(True)
        self.annotations_help_label.setIndent(26)
        self.annotations_help_label.setProperty(u"variant", u"help")

        self.scope_layout_3_layout.addWidget(self.annotations_help_label)


        self.scope_layout.addLayout(self.scope_layout_3_layout)


        self.scope_card_layout.addLayout(self.scope_layout)


        self.content_layout.addWidget(self.scope_card)

        self.about_filter_layout = QVBoxLayout()
        self.about_filter_layout.setSpacing(6)
        self.about_filter_layout.setObjectName(u"about_filter_layout")
        self.about_filter_title_label = QLabel(self.content_widget)
        self.about_filter_title_label.setObjectName(u"about_filter_title_label")
        self.about_filter_title_label.setFont(font1)

        self.about_filter_layout.addWidget(self.about_filter_title_label)

        self.about_filter_label = QLabel(self.content_widget)
        self.about_filter_label.setObjectName(u"about_filter_label")
        self.about_filter_label.setWordWrap(True)
        self.about_filter_label.setProperty(u"variant", u"help")

        self.about_filter_layout.addWidget(self.about_filter_label)


        self.content_layout.addLayout(self.about_filter_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(FilterStep)

        QMetaObject.connectSlotsByName(FilterStep)
    # setupUi

    def retranslateUi(self, FilterStep):
        FilterStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("FilterStep", u"Filter Settings", None))
        self.subtitle_label.setText(QCoreApplication.translate("FilterStep", u"Choose the frequency band that best matches your research objectives and the part of the recording to analyse.", None))
        self.label_4.setText(QCoreApplication.translate("FilterStep", u"Frequency band", None))
        self.label.setText(QCoreApplication.translate("FilterStep", u"The EEG signal is filtered into the band you choose, to focus the analysis on specific brain oscillations.", None))
        self.fullband_radioButton.setText(QCoreApplication.translate("FilterStep", u"Full frequency band (0.16\u201330 Hz)", None))
        self.delta_radioButton.setText(QCoreApplication.translate("FilterStep", u"Delta (0.16\u20134 Hz)", None))
        self.theta_radioButton.setText(QCoreApplication.translate("FilterStep", u"Theta (4\u20138 Hz)", None))
        self.alpha_radioButton.setText(QCoreApplication.translate("FilterStep", u"Alpha (8\u201313 Hz)", None))
        self.beta_radioButton.setText(QCoreApplication.translate("FilterStep", u"Beta (13\u201330 Hz)", None))
        self.custom_radioButton.setText(QCoreApplication.translate("FilterStep", u"Custom frequency band", None))
        self.low_cutoff_label.setText(QCoreApplication.translate("FilterStep", u"Low cutoff", None))
        self.low_cutoff_unit_label.setText(QCoreApplication.translate("FilterStep", u"Hz", None))
        self.high_cutoff_label.setText(QCoreApplication.translate("FilterStep", u"High cutoff", None))
        self.high_cutoff_unit_label.setText(QCoreApplication.translate("FilterStep", u"Hz", None))
        self.band_help_label.setText(QCoreApplication.translate("FilterStep", u"IIR bandpass, order 6", None))
        self.label_3.setText(QCoreApplication.translate("FilterStep", u"Recording scope", None))
        self.scopes_label.setText(QCoreApplication.translate("FilterStep", u"Choose the part of the recording to analyse.", None))
        self.sleep_stages_radioButton.setText(QCoreApplication.translate("FilterStep", u"Sleep stages", None))
        self.sleep_stages_help_label.setText(QCoreApplication.translate("FilterStep", u"The selected sleep stages.", None))
        self.n1_checkBox.setText(QCoreApplication.translate("FilterStep", u"N1", None))
        self.n2_checkBox.setText(QCoreApplication.translate("FilterStep", u"N2", None))
        self.n3_checkBox.setText(QCoreApplication.translate("FilterStep", u"N3", None))
        self.rem_checkBox.setText(QCoreApplication.translate("FilterStep", u"REM", None))
        self.unscored_radioButton.setText(QCoreApplication.translate("FilterStep", u"Unscored", None))
        self.unscored_help_label.setText(QCoreApplication.translate("FilterStep", u"The entire recording, or a segment of it: start time and duration.", None))
        self.trim_checkBox.setText(QCoreApplication.translate("FilterStep", u"Trim the signal", None))
        self.start_time_label.setText(QCoreApplication.translate("FilterStep", u"Start time", None))
        self.start_time_unit_label.setText(QCoreApplication.translate("FilterStep", u"s", None))
        self.duration_time_label.setText(QCoreApplication.translate("FilterStep", u"Duration", None))
        self.duration_time_unit_label.setText(QCoreApplication.translate("FilterStep", u"s", None))
        self.specific_annotations_radioButton.setText(QCoreApplication.translate("FilterStep", u"Specific annotations (chosen in the next step)", None))
        self.annotations_help_label.setText(QCoreApplication.translate("FilterStep", u"The analysis is based on the events you choose.", None))
        self.about_filter_title_label.setText(QCoreApplication.translate("FilterStep", u"About the filter", None))
        self.about_filter_label.setText(QCoreApplication.translate("FilterStep", u"Butterworth design in second-order-section (SOS) form, applied with bidirectional zero-phase filtering: the requested magnitude response is preserved and there is no phase distortion. The order is halved internally before the forward and backward passes.", None))
    # retranslateUi

