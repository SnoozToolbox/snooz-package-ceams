# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_BslVarStep.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_BslVarStep(object):
    def setupUi(self, BslVarStep):
        if not BslVarStep.objectName():
            BslVarStep.setObjectName(u"BslVarStep")
        BslVarStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(BslVarStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(BslVarStep)
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

        self.illustration_card = QFrame(self.content_widget)
        self.illustration_card.setObjectName(u"illustration_card")
        self.illustration_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.illustration_card.setFrameShadow(QFrame.Shadow.Raised)
        self.illustration_card_layout = QVBoxLayout(self.illustration_card)
        self.illustration_card_layout.setSpacing(10)
        self.illustration_card_layout.setObjectName(u"illustration_card_layout")
        self.illustration_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_7 = QLabel(self.illustration_card)
        self.label_7.setObjectName(u"label_7")

        self.illustration_card_layout.addWidget(self.label_7)

        self.illustration_caption_label = QLabel(self.illustration_card)
        self.illustration_caption_label.setObjectName(u"illustration_caption_label")
        font1 = QFont()
        font1.setPointSize(10)
        self.illustration_caption_label.setFont(font1)
        self.illustration_caption_label.setWordWrap(True)
        self.illustration_caption_label.setProperty(u"variant", u"help")

        self.illustration_card_layout.addWidget(self.illustration_caption_label)


        self.content_layout.addWidget(self.illustration_card)

        self.settings_cards_layout = QVBoxLayout()
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
        self.label_4 = QLabel(self.events_card)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setBold(True)
        self.label_4.setFont(font2)

        self.events_card_layout.addWidget(self.label_4)

        self.events_grid = QGridLayout()
        self.events_grid.setObjectName(u"events_grid")
        self.events_grid.setHorizontalSpacing(12)
        self.events_grid.setVerticalSpacing(10)
        self.label_3 = QLabel(self.events_card)
        self.label_3.setObjectName(u"label_3")

        self.events_grid.addWidget(self.label_3, 0, 0, 1, 1)

        self.group_lineEdit = QLineEdit(self.events_card)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setEnabled(False)
        self.group_lineEdit.setMaximumSize(QSize(300, 16777215))

        self.events_grid.addWidget(self.group_lineEdit, 0, 1, 1, 1)

        self.label_11 = QLabel(self.events_card)
        self.label_11.setObjectName(u"label_11")

        self.events_grid.addWidget(self.label_11, 1, 0, 1, 1)

        self.name_lineEdit = QLineEdit(self.events_card)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setEnabled(False)
        self.name_lineEdit.setMaximumSize(QSize(300, 16777215))

        self.events_grid.addWidget(self.name_lineEdit, 1, 1, 1, 1)

        self.events_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.events_grid.addItem(self.events_grid_spacer, 0, 3, 1, 1)


        self.events_card_layout.addLayout(self.events_grid)

        self.events_help_label = QLabel(self.events_card)
        self.events_help_label.setObjectName(u"events_help_label")
        self.events_help_label.setFont(font1)
        self.events_help_label.setWordWrap(True)
        self.events_help_label.setProperty(u"variant", u"help")

        self.events_card_layout.addWidget(self.events_help_label)


        self.settings_cards_layout.addWidget(self.events_card)

        self.thresholds_card = QFrame(self.content_widget)
        self.thresholds_card.setObjectName(u"thresholds_card")
        self.thresholds_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.thresholds_card.setFrameShadow(QFrame.Shadow.Raised)
        self.thresholds_card_layout = QVBoxLayout(self.thresholds_card)
        self.thresholds_card_layout.setSpacing(10)
        self.thresholds_card_layout.setObjectName(u"thresholds_card_layout")
        self.thresholds_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.thresholds_card)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.thresholds_card_layout.addWidget(self.label)

        self.thresholds_grid = QGridLayout()
        self.thresholds_grid.setObjectName(u"thresholds_grid")
        self.thresholds_grid.setHorizontalSpacing(12)
        self.thresholds_grid.setVerticalSpacing(10)
        self.label_5 = QLabel(self.thresholds_card)
        self.label_5.setObjectName(u"label_5")

        self.thresholds_grid.addWidget(self.label_5, 0, 0, 1, 1)

        self.threshold_lineEdit = QLineEdit(self.thresholds_card)
        self.threshold_lineEdit.setObjectName(u"threshold_lineEdit")
        self.threshold_lineEdit.setMaximumSize(QSize(110, 16777215))

        self.thresholds_grid.addWidget(self.threshold_lineEdit, 0, 1, 1, 1)

        self.threshold_lineEdit_unit_label = QLabel(self.thresholds_card)
        self.threshold_lineEdit_unit_label.setObjectName(u"threshold_lineEdit_unit_label")
        self.threshold_lineEdit_unit_label.setProperty(u"variant", u"help")

        self.thresholds_grid.addWidget(self.threshold_lineEdit_unit_label, 0, 2, 1, 1)

        self.thresholds_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.thresholds_grid.addItem(self.thresholds_grid_spacer, 0, 3, 1, 1)


        self.thresholds_card_layout.addLayout(self.thresholds_grid)

        self.thresholds_rule_label = QLabel(self.thresholds_card)
        self.thresholds_rule_label.setObjectName(u"thresholds_rule_label")
        self.thresholds_rule_label.setFont(font1)
        self.thresholds_rule_label.setWordWrap(True)
        self.thresholds_rule_label.setProperty(u"variant", u"help")

        self.thresholds_card_layout.addWidget(self.thresholds_rule_label)

        self.thresholds_tip_label = QLabel(self.thresholds_card)
        self.thresholds_tip_label.setObjectName(u"thresholds_tip_label")
        self.thresholds_tip_label.setTextFormat(Qt.TextFormat.RichText)
        self.thresholds_tip_label.setWordWrap(True)
        self.thresholds_tip_label.setProperty(u"variant", u"help")

        self.thresholds_card_layout.addWidget(self.thresholds_tip_label)


        self.settings_cards_layout.addWidget(self.thresholds_card)


        self.content_layout.addLayout(self.settings_cards_layout)

        self.filter_warning = QFrame(self.content_widget)
        self.filter_warning.setObjectName(u"filter_warning")
        self.filter_warning.setFrameShape(QFrame.Shape.NoFrame)
        self.filter_warning.setProperty(u"variant", u"warning")
        self.filter_warning_layout = QHBoxLayout(self.filter_warning)
        self.filter_warning_layout.setObjectName(u"filter_warning_layout")
        self.filter_warning_layout.setContentsMargins(14, 10, 14, 10)
        self.filter_warning_label = QLabel(self.filter_warning)
        self.filter_warning_label.setObjectName(u"filter_warning_label")
        self.filter_warning_label.setTextFormat(Qt.TextFormat.RichText)
        self.filter_warning_label.setWordWrap(True)

        self.filter_warning_layout.addWidget(self.filter_warning_label)


        self.content_layout.addWidget(self.filter_warning)

        self.about_baseline_layout = QVBoxLayout()
        self.about_baseline_layout.setSpacing(6)
        self.about_baseline_layout.setObjectName(u"about_baseline_layout")
        self.about_baseline_title_label = QLabel(self.content_widget)
        self.about_baseline_title_label.setObjectName(u"about_baseline_title_label")
        self.about_baseline_title_label.setFont(font2)

        self.about_baseline_layout.addWidget(self.about_baseline_title_label)

        self.about_baseline_label = QLabel(self.content_widget)
        self.about_baseline_label.setObjectName(u"about_baseline_label")
        self.about_baseline_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_baseline_label.setWordWrap(True)
        self.about_baseline_label.setProperty(u"variant", u"help")

        self.about_baseline_layout.addWidget(self.about_baseline_label)

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
        self.references_label.setFont(font1)
        self.references_label.setTextFormat(Qt.TextFormat.RichText)
        self.references_label.setWordWrap(True)
        self.references_label.setOpenExternalLinks(True)
        self.references_label.setProperty(u"variant", u"help")

        self.references_layout.addWidget(self.references_label)


        self.about_baseline_layout.addLayout(self.references_layout)


        self.content_layout.addLayout(self.about_baseline_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(BslVarStep)

        QMetaObject.connectSlotsByName(BslVarStep)
    # setupUi

    def retranslateUi(self, BslVarStep):
        BslVarStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("BslVarStep", u"Baseline Variation", None))
        self.subtitle_label.setText(QCoreApplication.translate("BslVarStep", u"Detects the segments with high power below 0.4 Hz, a slow shift of the signal caused by breathing, sweat or movement.", None))
        self.illustration_caption_label.setText(QCoreApplication.translate("BslVarStep", u"Simulated EEG with a baseline variation.", None))
        self.label_4.setText(QCoreApplication.translate("BslVarStep", u"Artifact events", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("BslVarStep", u"The group of the artifact events in the accessory file.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("BslVarStep", u"Group", None))
        self.group_lineEdit.setText(QCoreApplication.translate("BslVarStep", u"art_snooz", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("BslVarStep", u"The name of the artifact events in the accessory file.", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("BslVarStep", u"Name", None))
        self.name_lineEdit.setText(QCoreApplication.translate("BslVarStep", u"art_snooz", None))
        self.events_help_label.setText(QCoreApplication.translate("BslVarStep", u"When the group and name are common to all the detectors, edit them in \"Detectors Settings\".", None))
        self.label.setText(QCoreApplication.translate("BslVarStep", u"Thresholds", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("BslVarStep", u"Mean + x SD of the main Gaussian component, computed from all the selected channels.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("BslVarStep", u"Fixed threshold", None))
        self.threshold_lineEdit.setText(QCoreApplication.translate("BslVarStep", u"4", None))
        self.threshold_lineEdit_unit_label.setText(QCoreApplication.translate("BslVarStep", u"\u00d7 SD, optimal 3.5 to 5", None))
        self.thresholds_rule_label.setText(QCoreApplication.translate("BslVarStep", u"A window is an artifact when the threshold is exceeded.", None))
        self.thresholds_tip_label.setText(QCoreApplication.translate("BslVarStep", u"<b>Fewer false positives</b>, especially with large delta waves. Raise the threshold, for example to 5.", None))
        self.filter_warning_label.setText(QCoreApplication.translate("BslVarStep", u"<b>The bandpass filter changes the low frequencies</b><br/>The low cutoff of \"Filter EEG signals\" changes the power below 0.4 Hz. Keep the low frequencies to detect the baseline variations.", None))
        self.about_baseline_title_label.setText(QCoreApplication.translate("BslVarStep", u"About the baseline variation detector", None))
        self.about_baseline_label.setText(QCoreApplication.translate("BslVarStep", u"<b>How the power is computed</b><br/>\u2022 Before the power is computed, the signal is low-pass filtered at 0.4\u00a0Hz. The filter is a Butterworth filter of order 10, applied forward and backward (no phase distortion).<br/>\u2022 The power of the band below 0.4\u00a0Hz is computed by integrating the power spectral density, estimated with Welch's method [1].<br/>\u2022 The power is computed on 8\u00a0s windows with a 4\u00a0s step.<br/><br/><b>Fixed threshold (mean + x SD)</b><br/>\u2022 The power is log-transformed (log10) to reduce its skewness and bring it closer to a normal distribution.<br/>\u2022 Artifacts make the distribution of the power right-skewed. So it is modeled with a three-component Gaussian mixture model (GMM).<br/>\u2022 The threshold is the mean of the main Gaussian component plus a multiple of its standard deviation (SD). The main Gaussian component is the one with the largest weight. \"Fixed threshold\" is the multiple.<br/>\u2022 A window is flagged when log10(power below 0.4\u00a0Hz) "
                        "&gt; mean + threshold \u00d7 SD.<br/>\u2022 The distribution is computed from all the selected channels of the recording. Excluding a channel with a poor signal changes the threshold of the other channels.", None))
        self.references_label.setText(QCoreApplication.translate("BslVarStep", u"[1] Cox, R., &amp; Fell, J. (2020). Analyzing human sleep EEG: A methodological primer with code implementation. <i>Sleep Medicine Reviews</i>, <i>54</i>, Article 101353. <a href=\"https://doi.org/10.1016/j.smrv.2020.101353\">https://doi.org/10.1016/j.smrv.2020.101353</a>", None))
    # retranslateUi

