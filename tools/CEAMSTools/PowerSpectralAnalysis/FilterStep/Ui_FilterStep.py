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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QRadioButton,
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

        self.filter_cards_layout = QHBoxLayout()
        self.filter_cards_layout.setSpacing(16)
        self.filter_cards_layout.setObjectName(u"filter_cards_layout")
        self.bandpass_card = QFrame(self.content_widget)
        self.bandpass_card.setObjectName(u"bandpass_card")
        self.bandpass_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.bandpass_card.setFrameShadow(QFrame.Shadow.Raised)
        self.bandpass_card_layout = QVBoxLayout(self.bandpass_card)
        self.bandpass_card_layout.setSpacing(10)
        self.bandpass_card_layout.setObjectName(u"bandpass_card_layout")
        self.bandpass_card_layout.setContentsMargins(10, 10, 10, 10)
        self.bp_checkBox = QCheckBox(self.bandpass_card)
        self.bp_checkBox.setObjectName(u"bp_checkBox")
        font1 = QFont()
        font1.setBold(True)
        self.bp_checkBox.setFont(font1)
        self.bp_checkBox.setChecked(True)

        self.bandpass_card_layout.addWidget(self.bp_checkBox)

        self.cutoff_grid = QGridLayout()
        self.cutoff_grid.setObjectName(u"cutoff_grid")
        self.cutoff_grid.setHorizontalSpacing(12)
        self.cutoff_grid.setVerticalSpacing(10)
        self.label = QLabel(self.bandpass_card)
        self.label.setObjectName(u"label")

        self.cutoff_grid.addWidget(self.label, 0, 0, 1, 1)

        self.low_cutoff_lineEdit = QLineEdit(self.bandpass_card)
        self.low_cutoff_lineEdit.setObjectName(u"low_cutoff_lineEdit")
        self.low_cutoff_lineEdit.setMaximumSize(QSize(110, 16777215))

        self.cutoff_grid.addWidget(self.low_cutoff_lineEdit, 0, 1, 1, 1)

        self.low_cutoff_unit_label = QLabel(self.bandpass_card)
        self.low_cutoff_unit_label.setObjectName(u"low_cutoff_unit_label")
        self.low_cutoff_unit_label.setProperty(u"variant", u"help")

        self.cutoff_grid.addWidget(self.low_cutoff_unit_label, 0, 2, 1, 1)

        self.label_6 = QLabel(self.bandpass_card)
        self.label_6.setObjectName(u"label_6")

        self.cutoff_grid.addWidget(self.label_6, 1, 0, 1, 1)

        self.high_cutoff_lineEdit = QLineEdit(self.bandpass_card)
        self.high_cutoff_lineEdit.setObjectName(u"high_cutoff_lineEdit")
        self.high_cutoff_lineEdit.setMaximumSize(QSize(110, 16777215))

        self.cutoff_grid.addWidget(self.high_cutoff_lineEdit, 1, 1, 1, 1)

        self.high_cutoff_unit_label = QLabel(self.bandpass_card)
        self.high_cutoff_unit_label.setObjectName(u"high_cutoff_unit_label")
        self.high_cutoff_unit_label.setProperty(u"variant", u"help")

        self.cutoff_grid.addWidget(self.high_cutoff_unit_label, 1, 2, 1, 1)

        self.cutoff_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cutoff_grid.addItem(self.cutoff_grid_spacer, 0, 3, 1, 1)


        self.bandpass_card_layout.addLayout(self.cutoff_grid)

        self.bandpass_help_label = QLabel(self.bandpass_card)
        self.bandpass_help_label.setObjectName(u"bandpass_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.bandpass_help_label.setFont(font2)
        self.bandpass_help_label.setWordWrap(True)
        self.bandpass_help_label.setProperty(u"variant", u"help")

        self.bandpass_card_layout.addWidget(self.bandpass_help_label)

        self.bandpass_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.bandpass_card_layout.addItem(self.bandpass_stretch)


        self.filter_cards_layout.addWidget(self.bandpass_card)

        self.notch_card = QFrame(self.content_widget)
        self.notch_card.setObjectName(u"notch_card")
        self.notch_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.notch_card.setFrameShadow(QFrame.Shadow.Raised)
        self.notch_card_layout = QVBoxLayout(self.notch_card)
        self.notch_card_layout.setSpacing(10)
        self.notch_card_layout.setObjectName(u"notch_card_layout")
        self.notch_card_layout.setContentsMargins(10, 10, 10, 10)
        self.notch_checkBox = QCheckBox(self.notch_card)
        self.notch_checkBox.setObjectName(u"notch_checkBox")
        self.notch_checkBox.setFont(font1)

        self.notch_card_layout.addWidget(self.notch_checkBox)

        self.radioButton_60Hz = QRadioButton(self.notch_card)
        self.radioButton_60Hz.setObjectName(u"radioButton_60Hz")
        self.radioButton_60Hz.setEnabled(False)

        self.notch_card_layout.addWidget(self.radioButton_60Hz)

        self.radioButton_50Hz = QRadioButton(self.notch_card)
        self.radioButton_50Hz.setObjectName(u"radioButton_50Hz")
        self.radioButton_50Hz.setEnabled(False)

        self.notch_card_layout.addWidget(self.radioButton_50Hz)

        self.notch_help_label = QLabel(self.notch_card)
        self.notch_help_label.setObjectName(u"notch_help_label")
        self.notch_help_label.setFont(font2)
        self.notch_help_label.setWordWrap(True)
        self.notch_help_label.setProperty(u"variant", u"help")

        self.notch_card_layout.addWidget(self.notch_help_label)

        self.notch_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.notch_card_layout.addItem(self.notch_stretch)


        self.filter_cards_layout.addWidget(self.notch_card)

        self.filter_cards_layout.setStretch(0, 1)
        self.filter_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.filter_cards_layout)

        self.nyquist_warning = QFrame(self.content_widget)
        self.nyquist_warning.setObjectName(u"nyquist_warning")
        self.nyquist_warning.setFrameShape(QFrame.Shape.NoFrame)
        self.nyquist_warning.setProperty(u"variant", u"warning")
        self.nyquist_warning_layout = QHBoxLayout(self.nyquist_warning)
        self.nyquist_warning_layout.setObjectName(u"nyquist_warning_layout")
        self.nyquist_warning_layout.setContentsMargins(14, 10, 14, 10)
        self.nyquist_warning_label = QLabel(self.nyquist_warning)
        self.nyquist_warning_label.setObjectName(u"nyquist_warning_label")
        self.nyquist_warning_label.setTextFormat(Qt.TextFormat.RichText)
        self.nyquist_warning_label.setWordWrap(True)

        self.nyquist_warning_layout.addWidget(self.nyquist_warning_label)


        self.content_layout.addWidget(self.nyquist_warning)

        self.about_filters_layout = QVBoxLayout()
        self.about_filters_layout.setSpacing(6)
        self.about_filters_layout.setObjectName(u"about_filters_layout")
        self.about_filters_title_label = QLabel(self.content_widget)
        self.about_filters_title_label.setObjectName(u"about_filters_title_label")
        self.about_filters_title_label.setFont(font1)

        self.about_filters_layout.addWidget(self.about_filters_title_label)

        self.about_filters_label = QLabel(self.content_widget)
        self.about_filters_label.setObjectName(u"about_filters_label")
        self.about_filters_label.setWordWrap(True)
        self.about_filters_label.setProperty(u"variant", u"help")

        self.about_filters_layout.addWidget(self.about_filters_label)


        self.content_layout.addLayout(self.about_filters_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(FilterStep)
        self.bp_checkBox.clicked.connect(FilterStep.update_filter_settings_slot)
        self.notch_checkBox.clicked.connect(FilterStep.update_filter_settings_slot)
        self.radioButton_50Hz.clicked.connect(FilterStep.update_filter_settings_slot)
        self.radioButton_60Hz.clicked.connect(FilterStep.update_filter_settings_slot)

        QMetaObject.connectSlotsByName(FilterStep)
    # setupUi

    def retranslateUi(self, FilterStep):
        FilterStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("FilterStep", u"Filter Settings", None))
        self.subtitle_label.setText(QCoreApplication.translate("FilterStep", u"Optionally, add a bandpass filter and a power-line notch filter, depending on the signal quality and your research question. We recommend applying the same filters as during the visual review. The filters are applied for the analysis only: the PSG file is not modified.", None))
        self.bp_checkBox.setText(QCoreApplication.translate("FilterStep", u"Bandpass filter", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("FilterStep", u"Edit the low cutoff frequency in Hz (i.e. 0.3).", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("FilterStep", u"Low cutoff", None))
        self.low_cutoff_lineEdit.setText(QCoreApplication.translate("FilterStep", u"0.3", None))
        self.low_cutoff_unit_label.setText(QCoreApplication.translate("FilterStep", u"Hz", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("FilterStep", u"Edit the high cutoff frequency in Hz (i.e. 100).", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("FilterStep", u"High cutoff", None))
        self.high_cutoff_lineEdit.setText(QCoreApplication.translate("FilterStep", u"100", None))
        self.high_cutoff_unit_label.setText(QCoreApplication.translate("FilterStep", u"Hz", None))
        self.bandpass_help_label.setText(QCoreApplication.translate("FilterStep", u"IIR bandpass, order 6", None))
        self.notch_checkBox.setText(QCoreApplication.translate("FilterStep", u"Power line notch filter", None))
        self.radioButton_60Hz.setText(QCoreApplication.translate("FilterStep", u"60 Hz", None))
        self.radioButton_50Hz.setText(QCoreApplication.translate("FilterStep", u"50 Hz", None))
        self.notch_help_label.setText(QCoreApplication.translate("FilterStep", u"IIR stopband, order 20", None))
        self.nyquist_warning_label.setText(QCoreApplication.translate("FilterStep", u"<b>Highest cutoff frequency</b><br/>It must be lower than <b>sample rate / 2</b>.", None))
        self.about_filters_title_label.setText(QCoreApplication.translate("FilterStep", u"About the filters", None))
        self.about_filters_label.setText(QCoreApplication.translate("FilterStep", u"Butterworth design in second-order-section (SOS) form, applied with bidirectional zero-phase filtering: the requested magnitude response is preserved and there is no phase distortion. The orders are halved internally before the forward and backward passes.", None))
    # retranslateUi

