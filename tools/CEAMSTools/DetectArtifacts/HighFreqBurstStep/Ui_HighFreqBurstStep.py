# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_HighFreqBurstStep.ui'
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

class Ui_HighFreqBurstStep(object):
    def setupUi(self, HighFreqBurstStep):
        if not HighFreqBurstStep.objectName():
            HighFreqBurstStep.setObjectName(u"HighFreqBurstStep")
        HighFreqBurstStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(HighFreqBurstStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(HighFreqBurstStep)
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
        self.label_10 = QLabel(self.illustration_card)
        self.label_10.setObjectName(u"label_10")

        self.illustration_card_layout.addWidget(self.label_10)

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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_lineEdit.sizePolicy().hasHeightForWidth())
        self.group_lineEdit.setSizePolicy(sizePolicy)
        self.group_lineEdit.setMinimumSize(QSize(500, 0))
        self.group_lineEdit.setMaximumSize(QSize(500, 16777215))

        self.events_grid.addWidget(self.group_lineEdit, 0, 1, 1, 1)

        self.label_7 = QLabel(self.events_card)
        self.label_7.setObjectName(u"label_7")

        self.events_grid.addWidget(self.label_7, 1, 0, 1, 1)

        self.name_burst_lineEdit = QLineEdit(self.events_card)
        self.name_burst_lineEdit.setObjectName(u"name_burst_lineEdit")
        self.name_burst_lineEdit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.name_burst_lineEdit.sizePolicy().hasHeightForWidth())
        self.name_burst_lineEdit.setSizePolicy(sizePolicy)
        self.name_burst_lineEdit.setMinimumSize(QSize(500, 0))
        self.name_burst_lineEdit.setMaximumSize(QSize(500, 16777215))

        self.events_grid.addWidget(self.name_burst_lineEdit, 1, 1, 1, 1)

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
        self.label_15 = QLabel(self.thresholds_card)
        self.label_15.setObjectName(u"label_15")

        self.thresholds_grid.addWidget(self.label_15, 0, 0, 1, 1)

        self.tresh_fixe_lineEdit = QLineEdit(self.thresholds_card)
        self.tresh_fixe_lineEdit.setObjectName(u"tresh_fixe_lineEdit")
        self.tresh_fixe_lineEdit.setMaximumSize(QSize(110, 16777215))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tresh_fixe_lineEdit.sizePolicy().hasHeightForWidth())
        self.tresh_fixe_lineEdit.setSizePolicy(sizePolicy1)
        self.tresh_fixe_lineEdit.setMinimumSize(QSize(0, 0))

        self.thresholds_grid.addWidget(self.tresh_fixe_lineEdit, 0, 1, 1, 1)

        self.tresh_fixe_lineEdit_unit_label = QLabel(self.thresholds_card)
        self.tresh_fixe_lineEdit_unit_label.setObjectName(u"tresh_fixe_lineEdit_unit_label")
        self.tresh_fixe_lineEdit_unit_label.setProperty(u"variant", u"help")

        self.thresholds_grid.addWidget(self.tresh_fixe_lineEdit_unit_label, 0, 2, 1, 1)

        self.label_2 = QLabel(self.thresholds_card)
        self.label_2.setObjectName(u"label_2")

        self.thresholds_grid.addWidget(self.label_2, 1, 0, 1, 1)

        self.thresh_adp_lineEdit = QLineEdit(self.thresholds_card)
        self.thresh_adp_lineEdit.setObjectName(u"thresh_adp_lineEdit")
        self.thresh_adp_lineEdit.setMaximumSize(QSize(110, 16777215))
        sizePolicy1.setHeightForWidth(self.thresh_adp_lineEdit.sizePolicy().hasHeightForWidth())
        self.thresh_adp_lineEdit.setSizePolicy(sizePolicy1)

        self.thresholds_grid.addWidget(self.thresh_adp_lineEdit, 1, 1, 1, 1)

        self.thresh_adp_lineEdit_unit_label = QLabel(self.thresholds_card)
        self.thresh_adp_lineEdit_unit_label.setObjectName(u"thresh_adp_lineEdit_unit_label")
        self.thresh_adp_lineEdit_unit_label.setProperty(u"variant", u"help")

        self.thresholds_grid.addWidget(self.thresh_adp_lineEdit_unit_label, 1, 2, 1, 1)

        self.label_11 = QLabel(self.thresholds_card)
        self.label_11.setObjectName(u"label_11")

        self.thresholds_grid.addWidget(self.label_11, 2, 0, 1, 1)

        self.thresh_ratio_lineEdit = QLineEdit(self.thresholds_card)
        self.thresh_ratio_lineEdit.setObjectName(u"thresh_ratio_lineEdit")
        self.thresh_ratio_lineEdit.setMaximumSize(QSize(110, 16777215))
        sizePolicy1.setHeightForWidth(self.thresh_ratio_lineEdit.sizePolicy().hasHeightForWidth())
        self.thresh_ratio_lineEdit.setSizePolicy(sizePolicy1)

        self.thresholds_grid.addWidget(self.thresh_ratio_lineEdit, 2, 1, 1, 1)

        self.thresh_ratio_lineEdit_unit_label = QLabel(self.thresholds_card)
        self.thresh_ratio_lineEdit_unit_label.setObjectName(u"thresh_ratio_lineEdit_unit_label")
        self.thresh_ratio_lineEdit_unit_label.setProperty(u"variant", u"help")

        self.thresholds_grid.addWidget(self.thresh_ratio_lineEdit_unit_label, 2, 2, 1, 1)

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

        self.about_burst_layout = QVBoxLayout()
        self.about_burst_layout.setSpacing(6)
        self.about_burst_layout.setObjectName(u"about_burst_layout")
        self.about_burst_title_label = QLabel(self.content_widget)
        self.about_burst_title_label.setObjectName(u"about_burst_title_label")
        self.about_burst_title_label.setFont(font2)

        self.about_burst_layout.addWidget(self.about_burst_title_label)

        self.about_burst_label = QLabel(self.content_widget)
        self.about_burst_label.setObjectName(u"about_burst_label")
        self.about_burst_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_burst_label.setWordWrap(True)
        self.about_burst_label.setProperty(u"variant", u"help")

        self.about_burst_layout.addWidget(self.about_burst_label)

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


        self.about_burst_layout.addLayout(self.references_layout)


        self.content_layout.addLayout(self.about_burst_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(HighFreqBurstStep)

        QMetaObject.connectSlotsByName(HighFreqBurstStep)
    # setupUi

    def retranslateUi(self, HighFreqBurstStep):
        HighFreqBurstStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("HighFreqBurstStep", u"High Frequency Burst", None))
        self.subtitle_label.setText(QCoreApplication.translate("HighFreqBurstStep", u"Detects the short bursts of high-frequency power (above 25 Hz), such as electrode glitches.", None))
        self.illustration_caption_label.setText(QCoreApplication.translate("HighFreqBurstStep", u"Simulated EEG with a high frequency burst.", None))
        self.label_4.setText(QCoreApplication.translate("HighFreqBurstStep", u"Artifact events", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("HighFreqBurstStep", u"The group of the artifact events in the accessory file.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("HighFreqBurstStep", u"Group", None))
        self.group_lineEdit.setText(QCoreApplication.translate("HighFreqBurstStep", u"art_snooz", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("HighFreqBurstStep", u"The name of the artifact events in the accessory file.", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("HighFreqBurstStep", u"Name", None))
        self.name_burst_lineEdit.setText(QCoreApplication.translate("HighFreqBurstStep", u"art_snooz", None))
        self.events_help_label.setText(QCoreApplication.translate("HighFreqBurstStep", u"When the group and name are common to all the detectors, edit them in \"Detectors Settings\".", None))
        self.label.setText(QCoreApplication.translate("HighFreqBurstStep", u"Thresholds", None))
#if QT_CONFIG(tooltip)
        self.label_15.setToolTip(QCoreApplication.translate("HighFreqBurstStep", u"Mean + x SD of the main Gaussian component.", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("HighFreqBurstStep", u"(A) Fixed threshold", None))
        self.tresh_fixe_lineEdit.setText(QCoreApplication.translate("HighFreqBurstStep", u"4", None))
        self.tresh_fixe_lineEdit_unit_label.setText(QCoreApplication.translate("HighFreqBurstStep", u"\u00d7 SD, optimal 3 to 5", None))
        self.label_2.setText(QCoreApplication.translate("HighFreqBurstStep", u"(B) Adaptive threshold", None))
        self.thresh_adp_lineEdit.setText(QCoreApplication.translate("HighFreqBurstStep", u"8", None))
        self.thresh_adp_lineEdit_unit_label.setText(QCoreApplication.translate("HighFreqBurstStep", u"\u00d7 baseline median, optimal 6 to 10", None))
        self.label_11.setText(QCoreApplication.translate("HighFreqBurstStep", u"(C) Power ratio, 25\u201364 Hz / 8\u201364 Hz", None))
        self.thresh_ratio_lineEdit.setText(QCoreApplication.translate("HighFreqBurstStep", u"0.1", None))
        self.thresh_ratio_lineEdit_unit_label.setText(QCoreApplication.translate("HighFreqBurstStep", u"optimal 0.05 to 0.4", None))
        self.thresholds_rule_label.setText(QCoreApplication.translate("HighFreqBurstStep", u"A window is an artifact when the three thresholds are exceeded.", None))
        self.thresholds_tip_label.setText(QCoreApplication.translate("HighFreqBurstStep", u"<b>Fewer false positives</b>, especially during spindles, alpha activity or beta bursts. Raise the power ratio (C) first.", None))
        self.about_burst_title_label.setText(QCoreApplication.translate("HighFreqBurstStep", u"About the high frequency burst detector", None))
        self.about_burst_label.setText(QCoreApplication.translate("HighFreqBurstStep", u"<b>How the power is computed</b><br/>\u2022 The power of the 25\u201364\u00a0Hz band is computed by integrating the power spectral density, estimated with Welch's method [1].<br/>\u2022 The power is computed on 0.5\u00a0s windows with a 0.25\u00a0s step.<br/><br/><b>(A) Fixed threshold (mean + x SD)</b><br/>\u2022 The power is log-transformed (log10) to reduce its skewness and bring it closer to a normal distribution.<br/>\u2022 Artifacts make the distribution of the power right-skewed. So it is modeled with a three-component Gaussian mixture model (GMM).<br/>\u2022 The threshold is the mean of the main Gaussian component plus a multiple of its standard deviation (SD). The main Gaussian component is the one with the largest weight. \"(A) Fixed threshold\" is the multiple.<br/>\u2022 A window is flagged when log10(25\u201364\u00a0Hz power) &gt; mean + threshold \u00d7 SD.<br/>\u2022 The distribution is computed from all the selected channels of the recording. Excluding a channel with a poor signal changes the t"
                        "hreshold of the other channels.<br/><br/><b>(B) Adaptive threshold (baseline)</b><br/>\u2022 The baseline is the 30\u00a0s around the window.<br/>\u2022 A window is flagged when its 25\u201364\u00a0Hz power &gt; threshold \u00d7 the median power of the baseline.<br/>\u2022 This threshold can be too sensitive when the EEG has little high-frequency noise.<br/><br/><b>(C) Power ratio (relative power)</b><br/>\u2022 A high-frequency burst can be masked by a strong low-frequency activity. It may then not disturb the EEG.<br/>\u2022 A window is flagged when (25\u201364\u00a0Hz power) / (8\u201364\u00a0Hz power) &gt; threshold.<br/>\u2022 A higher threshold asks for a larger part of the power in the 25\u201364\u00a0Hz band before a window is an artifact.", None))
        self.references_label.setText(QCoreApplication.translate("HighFreqBurstStep", u"[1] Cox, R., &amp; Fell, J. (2020). Analyzing human sleep EEG: A methodological primer with code implementation. <i>Sleep Medicine Reviews</i>, <i>54</i>, Article 101353. <a href=\"https://doi.org/10.1016/j.smrv.2020.101353\">https://doi.org/10.1016/j.smrv.2020.101353</a>", None))
    # retranslateUi

