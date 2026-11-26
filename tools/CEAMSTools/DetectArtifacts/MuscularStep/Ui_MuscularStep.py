# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MuscularStep.ui'
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

class Ui_MuscularStep(object):
    def setupUi(self, MuscularStep):
        if not MuscularStep.objectName():
            MuscularStep.setObjectName(u"MuscularStep")
        MuscularStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(MuscularStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(MuscularStep)
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
        self.picture_label = QLabel(self.illustration_card)
        self.picture_label.setObjectName(u"picture_label")

        self.illustration_card_layout.addWidget(self.picture_label)

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
        self.group_lineEdit.setMaximumSize(QSize(250, 16777215))
        font3 = QFont()
        font3.setBold(False)
        font3.setItalic(False)
        self.group_lineEdit.setFont(font3)

        self.events_grid.addWidget(self.group_lineEdit, 0, 1, 1, 1)

        self.label_11 = QLabel(self.events_card)
        self.label_11.setObjectName(u"label_11")

        self.events_grid.addWidget(self.label_11, 1, 0, 1, 1)

        self.name_eeg_lineEdit = QLineEdit(self.events_card)
        self.name_eeg_lineEdit.setObjectName(u"name_eeg_lineEdit")
        self.name_eeg_lineEdit.setEnabled(False)
        self.name_eeg_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.name_eeg_lineEdit.setFont(font3)

        self.events_grid.addWidget(self.name_eeg_lineEdit, 1, 1, 1, 1)

        self.label_7 = QLabel(self.events_card)
        self.label_7.setObjectName(u"label_7")

        self.events_grid.addWidget(self.label_7, 2, 0, 1, 1)

        self.name_emg_lineEdit = QLineEdit(self.events_card)
        self.name_emg_lineEdit.setObjectName(u"name_emg_lineEdit")
        self.name_emg_lineEdit.setEnabled(False)
        self.name_emg_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.name_emg_lineEdit.setFont(font3)

        self.events_grid.addWidget(self.name_emg_lineEdit, 2, 1, 1, 1)

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

        self.EEG_lineEdit = QLineEdit(self.thresholds_card)
        self.EEG_lineEdit.setObjectName(u"EEG_lineEdit")
        self.EEG_lineEdit.setMaximumSize(QSize(110, 16777215))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EEG_lineEdit.sizePolicy().hasHeightForWidth())
        self.EEG_lineEdit.setSizePolicy(sizePolicy)
        self.EEG_lineEdit.setFont(font3)

        self.thresholds_grid.addWidget(self.EEG_lineEdit, 0, 1, 1, 1)

        self.EEG_lineEdit_unit_label = QLabel(self.thresholds_card)
        self.EEG_lineEdit_unit_label.setObjectName(u"EEG_lineEdit_unit_label")
        self.EEG_lineEdit_unit_label.setProperty(u"variant", u"help")

        self.thresholds_grid.addWidget(self.EEG_lineEdit_unit_label, 0, 2, 1, 1)

        self.label_2 = QLabel(self.thresholds_card)
        self.label_2.setObjectName(u"label_2")

        self.thresholds_grid.addWidget(self.label_2, 1, 0, 1, 1)

        self.EMG_lineEdit = QLineEdit(self.thresholds_card)
        self.EMG_lineEdit.setObjectName(u"EMG_lineEdit")
        self.EMG_lineEdit.setMaximumSize(QSize(110, 16777215))
        sizePolicy.setHeightForWidth(self.EMG_lineEdit.sizePolicy().hasHeightForWidth())
        self.EMG_lineEdit.setSizePolicy(sizePolicy)
        self.EMG_lineEdit.setFont(font3)

        self.thresholds_grid.addWidget(self.EMG_lineEdit, 1, 1, 1, 1)

        self.EMG_lineEdit_unit_label = QLabel(self.thresholds_card)
        self.EMG_lineEdit_unit_label.setObjectName(u"EMG_lineEdit_unit_label")
        self.EMG_lineEdit_unit_label.setProperty(u"variant", u"help")

        self.thresholds_grid.addWidget(self.EMG_lineEdit_unit_label, 1, 2, 1, 1)

        self.label_6 = QLabel(self.thresholds_card)
        self.label_6.setObjectName(u"label_6")

        self.thresholds_grid.addWidget(self.label_6, 2, 0, 1, 1)

        self.both_lineEdit = QLineEdit(self.thresholds_card)
        self.both_lineEdit.setObjectName(u"both_lineEdit")
        self.both_lineEdit.setMaximumSize(QSize(110, 16777215))
        sizePolicy.setHeightForWidth(self.both_lineEdit.sizePolicy().hasHeightForWidth())
        self.both_lineEdit.setSizePolicy(sizePolicy)
        self.both_lineEdit.setFont(font3)

        self.thresholds_grid.addWidget(self.both_lineEdit, 2, 1, 1, 1)

        self.both_lineEdit_unit_label = QLabel(self.thresholds_card)
        self.both_lineEdit_unit_label.setObjectName(u"both_lineEdit_unit_label")
        self.both_lineEdit_unit_label.setProperty(u"variant", u"help")

        self.thresholds_grid.addWidget(self.both_lineEdit_unit_label, 2, 2, 1, 1)

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

        self.about_muscle_layout = QVBoxLayout()
        self.about_muscle_layout.setSpacing(6)
        self.about_muscle_layout.setObjectName(u"about_muscle_layout")
        self.about_muscle_title_label = QLabel(self.content_widget)
        self.about_muscle_title_label.setObjectName(u"about_muscle_title_label")
        self.about_muscle_title_label.setFont(font2)

        self.about_muscle_layout.addWidget(self.about_muscle_title_label)

        self.about_muscle_label = QLabel(self.content_widget)
        self.about_muscle_label.setObjectName(u"about_muscle_label")
        self.about_muscle_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_muscle_label.setWordWrap(True)
        self.about_muscle_label.setProperty(u"variant", u"help")

        self.about_muscle_layout.addWidget(self.about_muscle_label)

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


        self.about_muscle_layout.addLayout(self.references_layout)


        self.content_layout.addLayout(self.about_muscle_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(MuscularStep)

        QMetaObject.connectSlotsByName(MuscularStep)
    # setupUi

    def retranslateUi(self, MuscularStep):
        MuscularStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("MuscularStep", u"Muscular Artifact", None))
        self.subtitle_label.setText(QCoreApplication.translate("MuscularStep", u"Detects the bursts of muscle activity (20.25\u201332 Hz) in the EEG, with the help of the EMG.", None))
        self.illustration_caption_label.setText(QCoreApplication.translate("MuscularStep", u"Simulated EEG with two bursts of muscle activity.", None))
        self.label_4.setText(QCoreApplication.translate("MuscularStep", u"Artifact events", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MuscularStep", u"The group of the artifact events in the accessory file.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MuscularStep", u"Group", None))
        self.group_lineEdit.setText(QCoreApplication.translate("MuscularStep", u"art_snooz", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("MuscularStep", u"The name of the artifacts detected with the EEG only (threshold A).", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("MuscularStep", u"Name, EEG only", None))
        self.name_eeg_lineEdit.setText(QCoreApplication.translate("MuscularStep", u"art_snooz", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("MuscularStep", u"The name of the artifacts detected with the EMG (thresholds B and C).", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("MuscularStep", u"Name, with the EMG", None))
        self.name_emg_lineEdit.setText(QCoreApplication.translate("MuscularStep", u"art_snooz", None))
        self.events_help_label.setText(QCoreApplication.translate("MuscularStep", u"When the group and name are common to all the detectors, edit them in \"Detectors Settings\".", None))
        self.label.setText(QCoreApplication.translate("MuscularStep", u"Thresholds", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MuscularStep", u"In times the median power of the baseline.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MuscularStep", u"(A) High threshold on the EEG", None))
        self.EEG_lineEdit.setText(QCoreApplication.translate("MuscularStep", u"4.5", None))
        self.EEG_lineEdit_unit_label.setText(QCoreApplication.translate("MuscularStep", u"\u00d7 baseline median, optimal 5 to 9", None))
        self.label_2.setText(QCoreApplication.translate("MuscularStep", u"(B) Threshold on the EMG", None))
        self.EMG_lineEdit.setText(QCoreApplication.translate("MuscularStep", u"4", None))
        self.EMG_lineEdit_unit_label.setText(QCoreApplication.translate("MuscularStep", u"\u00d7 baseline median, optimal 4 to 6", None))
        self.label_6.setText(QCoreApplication.translate("MuscularStep", u"(C) Low threshold on the EEG", None))
        self.both_lineEdit.setText(QCoreApplication.translate("MuscularStep", u"3.5", None))
        self.both_lineEdit_unit_label.setText(QCoreApplication.translate("MuscularStep", u"\u00d7 baseline median, optimal 4 to 6", None))
        self.thresholds_rule_label.setText(QCoreApplication.translate("MuscularStep", u"A window is an artifact when A is exceeded, or when B and C are both exceeded.", None))
        self.thresholds_tip_label.setText(QCoreApplication.translate("MuscularStep", u"<b>Fewer false positives</b>, especially during spindles, alpha waves or beta bursts. Raise A first. You can also raise B and C, especially when the EMG channel is unstable or very sensitive.", None))
        self.about_muscle_title_label.setText(QCoreApplication.translate("MuscularStep", u"About the muscle artifact detector", None))
        self.about_muscle_label.setText(QCoreApplication.translate("MuscularStep", u"<b>How the power is computed</b><br/>\u2022 The EEG is filtered at 0.3\u201330\u00a0Hz and downsampled to 64\u00a0Hz [1]. The filter is a Butterworth filter of order 6, applied forward and backward (no phase delay).<br/>\u2022 The power of the myogenic activity (20.25\u201332\u00a0Hz) is computed by integrating the power spectral density, estimated with Welch's method [2].<br/>\u2022 The power is computed on 4\u00a0s windows with a 2\u00a0s step, a finer time resolution than in [1].<br/><br/><b>Thresholds (\u00d7 the baseline median)</b><br/>\u2022 The baseline is the 3\u00a0min around the window. The power of each window is compared to the median power of its baseline.<br/>\u2022 (A) High threshold on the EEG. A window is an artifact when its EEG power &gt; A \u00d7 the baseline median.<br/>\u2022 (B and C) With the EMG. A smaller increase on the EEG is also an artifact when the EMG increases too. A window is an artifact when its EMG power &gt; B \u00d7 the median of the EMG baseline and its EEG power &gt; C "
                        "\u00d7 the baseline median.<br/>\u2022 The use of the EMG is new, not in the original publication [1].", None))
        self.references_label.setText(QCoreApplication.translate("MuscularStep", u"[1] Brunner, D. P., Vasko, R. C., Detka, C. S., Monahan, J. P., Reynolds, C. F., III, &amp; Kupfer, D. J. (1996). Muscle artifacts in the sleep EEG: Automated detection and effect on all-night EEG power spectra. <i>Journal of Sleep Research</i>, <i>5</i>(3), 155\u2013164. <a href=\"https://doi.org/10.1046/j.1365-2869.1996.00009.x\">https://doi.org/10.1046/j.1365-2869.1996.00009.x</a><br/>[2] Cox, R., &amp; Fell, J. (2020). Analyzing human sleep EEG: A methodological primer with code implementation. <i>Sleep Medicine Reviews</i>, <i>54</i>, Article 101353. <a href=\"https://doi.org/10.1016/j.smrv.2020.101353\">https://doi.org/10.1016/j.smrv.2020.101353</a>", None))
    # retranslateUi

