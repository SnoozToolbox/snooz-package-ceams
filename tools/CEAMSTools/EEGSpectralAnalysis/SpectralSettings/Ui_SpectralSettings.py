# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SpectralSettings.ui'
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
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_SpectralSettings(object):
    def setupUi(self, SpectralSettings):
        if not SpectralSettings.objectName():
            SpectralSettings.setObjectName(u"SpectralSettings")
        SpectralSettings.resize(900, 700)
        self.verticalLayout = QVBoxLayout(SpectralSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(SpectralSettings)
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

        self.spectral_cards_layout = QHBoxLayout()
        self.spectral_cards_layout.setSpacing(16)
        self.spectral_cards_layout.setObjectName(u"spectral_cards_layout")
        self.frequency_card = QFrame(self.content_widget)
        self.frequency_card.setObjectName(u"frequency_card")
        self.frequency_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.frequency_card.setFrameShadow(QFrame.Shadow.Raised)
        self.frequency_card_layout = QVBoxLayout(self.frequency_card)
        self.frequency_card_layout.setSpacing(10)
        self.frequency_card_layout.setObjectName(u"frequency_card_layout")
        self.frequency_card_layout.setContentsMargins(10, 10, 10, 10)
        self.frequency_title_label = QLabel(self.frequency_card)
        self.frequency_title_label.setObjectName(u"frequency_title_label")
        font1 = QFont()
        font1.setBold(True)
        self.frequency_title_label.setFont(font1)

        self.frequency_card_layout.addWidget(self.frequency_title_label)

        self.frequency_grid = QGridLayout()
        self.frequency_grid.setObjectName(u"frequency_grid")
        self.frequency_grid.setHorizontalSpacing(12)
        self.frequency_grid.setVerticalSpacing(10)
        self.first_freq_label = QLabel(self.frequency_card)
        self.first_freq_label.setObjectName(u"first_freq_label")

        self.frequency_grid.addWidget(self.first_freq_label, 0, 0, 1, 1)

        self.first_freq_lineEdit = QLineEdit(self.frequency_card)
        self.first_freq_lineEdit.setObjectName(u"first_freq_lineEdit")
        self.first_freq_lineEdit.setMaximumSize(QSize(110, 16777215))

        self.frequency_grid.addWidget(self.first_freq_lineEdit, 0, 1, 1, 1)

        self.first_freq_unit_label = QLabel(self.frequency_card)
        self.first_freq_unit_label.setObjectName(u"first_freq_unit_label")
        self.first_freq_unit_label.setProperty(u"variant", u"help")

        self.frequency_grid.addWidget(self.first_freq_unit_label, 0, 2, 1, 1)

        self.last_freq_label = QLabel(self.frequency_card)
        self.last_freq_label.setObjectName(u"last_freq_label")

        self.frequency_grid.addWidget(self.last_freq_label, 1, 0, 1, 1)

        self.last_freq_lineEdit = QLineEdit(self.frequency_card)
        self.last_freq_lineEdit.setObjectName(u"last_freq_lineEdit")
        self.last_freq_lineEdit.setMaximumSize(QSize(110, 16777215))

        self.frequency_grid.addWidget(self.last_freq_lineEdit, 1, 1, 1, 1)

        self.last_freq_unit_label = QLabel(self.frequency_card)
        self.last_freq_unit_label.setObjectName(u"last_freq_unit_label")
        self.last_freq_unit_label.setProperty(u"variant", u"help")

        self.frequency_grid.addWidget(self.last_freq_unit_label, 1, 2, 1, 1)

        self.frequency_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.frequency_grid.addItem(self.frequency_grid_spacer, 0, 3, 1, 1)


        self.frequency_card_layout.addLayout(self.frequency_grid)

        self.frequency_help_label = QLabel(self.frequency_card)
        self.frequency_help_label.setObjectName(u"frequency_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.frequency_help_label.setFont(font2)
        self.frequency_help_label.setWordWrap(True)
        self.frequency_help_label.setProperty(u"variant", u"help")

        self.frequency_card_layout.addWidget(self.frequency_help_label)

        self.frequency_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.frequency_card_layout.addItem(self.frequency_stretch)


        self.spectral_cards_layout.addWidget(self.frequency_card)

        self.fft_card = QFrame(self.content_widget)
        self.fft_card.setObjectName(u"fft_card")
        self.fft_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.fft_card.setFrameShadow(QFrame.Shadow.Raised)
        self.fft_card_layout = QVBoxLayout(self.fft_card)
        self.fft_card_layout.setSpacing(10)
        self.fft_card_layout.setObjectName(u"fft_card_layout")
        self.fft_card_layout.setContentsMargins(10, 10, 10, 10)
        self.fft_title_label = QLabel(self.fft_card)
        self.fft_title_label.setObjectName(u"fft_title_label")
        self.fft_title_label.setFont(font1)

        self.fft_card_layout.addWidget(self.fft_title_label)

        self.fft_grid = QGridLayout()
        self.fft_grid.setObjectName(u"fft_grid")
        self.fft_grid.setHorizontalSpacing(12)
        self.fft_grid.setVerticalSpacing(10)
        self.win_len_label = QLabel(self.fft_card)
        self.win_len_label.setObjectName(u"win_len_label")

        self.fft_grid.addWidget(self.win_len_label, 0, 0, 1, 1)

        self.win_len_lineEdit = QLineEdit(self.fft_card)
        self.win_len_lineEdit.setObjectName(u"win_len_lineEdit")
        self.win_len_lineEdit.setMaximumSize(QSize(110, 16777215))

        self.fft_grid.addWidget(self.win_len_lineEdit, 0, 1, 1, 1)

        self.win_len_unit_label = QLabel(self.fft_card)
        self.win_len_unit_label.setObjectName(u"win_len_unit_label")
        self.win_len_unit_label.setProperty(u"variant", u"help")

        self.fft_grid.addWidget(self.win_len_unit_label, 0, 2, 1, 1)

        self.win_step_label = QLabel(self.fft_card)
        self.win_step_label.setObjectName(u"win_step_label")

        self.fft_grid.addWidget(self.win_step_label, 1, 0, 1, 1)

        self.win_step_lineEdit = QLineEdit(self.fft_card)
        self.win_step_lineEdit.setObjectName(u"win_step_lineEdit")
        self.win_step_lineEdit.setMaximumSize(QSize(110, 16777215))

        self.fft_grid.addWidget(self.win_step_lineEdit, 1, 1, 1, 1)

        self.win_step_unit_label = QLabel(self.fft_card)
        self.win_step_unit_label.setObjectName(u"win_step_unit_label")
        self.win_step_unit_label.setProperty(u"variant", u"help")

        self.fft_grid.addWidget(self.win_step_unit_label, 1, 2, 1, 1)

        self.fft_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.fft_grid.addItem(self.fft_grid_spacer, 0, 3, 1, 1)


        self.fft_card_layout.addLayout(self.fft_grid)

        self.fft_help_label = QLabel(self.fft_card)
        self.fft_help_label.setObjectName(u"fft_help_label")
        self.fft_help_label.setFont(font2)
        self.fft_help_label.setWordWrap(True)
        self.fft_help_label.setProperty(u"variant", u"help")

        self.fft_card_layout.addWidget(self.fft_help_label)

        self.fft_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.fft_card_layout.addItem(self.fft_stretch)


        self.spectral_cards_layout.addWidget(self.fft_card)

        self.spectral_cards_layout.setStretch(0, 1)
        self.spectral_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.spectral_cards_layout)

        self.window_warning = QFrame(self.content_widget)
        self.window_warning.setObjectName(u"window_warning")
        self.window_warning.setFrameShape(QFrame.Shape.NoFrame)
        self.window_warning.setProperty(u"variant", u"warning")
        self.window_warning_layout = QHBoxLayout(self.window_warning)
        self.window_warning_layout.setObjectName(u"window_warning_layout")
        self.window_warning_layout.setContentsMargins(14, 10, 14, 10)
        self.window_warning_label = QLabel(self.window_warning)
        self.window_warning_label.setObjectName(u"window_warning_label")
        self.window_warning_label.setTextFormat(Qt.TextFormat.RichText)
        self.window_warning_label.setWordWrap(True)

        self.window_warning_layout.addWidget(self.window_warning_label)


        self.content_layout.addWidget(self.window_warning)

        self.about_resolution_layout = QVBoxLayout()
        self.about_resolution_layout.setSpacing(6)
        self.about_resolution_layout.setObjectName(u"about_resolution_layout")
        self.about_resolution_title_label = QLabel(self.content_widget)
        self.about_resolution_title_label.setObjectName(u"about_resolution_title_label")
        self.about_resolution_title_label.setFont(font1)

        self.about_resolution_layout.addWidget(self.about_resolution_title_label)

        self.about_resolution_label = QLabel(self.content_widget)
        self.about_resolution_label.setObjectName(u"about_resolution_label")
        self.about_resolution_label.setWordWrap(True)
        self.about_resolution_label.setProperty(u"variant", u"help")

        self.about_resolution_layout.addWidget(self.about_resolution_label)


        self.content_layout.addLayout(self.about_resolution_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SpectralSettings)

        QMetaObject.connectSlotsByName(SpectralSettings)
    # setupUi

    def retranslateUi(self, SpectralSettings):
        SpectralSettings.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("SpectralSettings", u"Spectral Settings", None))
        self.subtitle_label.setText(QCoreApplication.translate("SpectralSettings", u"Set the frequency range and the FFT windows of the Welch method.", None))
        self.frequency_title_label.setText(QCoreApplication.translate("SpectralSettings", u"Frequency range", None))
        self.first_freq_label.setText(QCoreApplication.translate("SpectralSettings", u"First frequency", None))
        self.first_freq_unit_label.setText(QCoreApplication.translate("SpectralSettings", u"Hz", None))
        self.last_freq_label.setText(QCoreApplication.translate("SpectralSettings", u"Last frequency", None))
        self.last_freq_unit_label.setText(QCoreApplication.translate("SpectralSettings", u"Hz", None))
        self.frequency_help_label.setText(QCoreApplication.translate("SpectralSettings", u"The power is reported in 1 Hz bands, from the first to the last frequency.", None))
        self.fft_title_label.setText(QCoreApplication.translate("SpectralSettings", u"FFT windows", None))
#if QT_CONFIG(tooltip)
        self.win_len_label.setToolTip(QCoreApplication.translate("SpectralSettings", u"Use whole seconds to align the FFT bins with the fixed 1 Hz bands.", None))
#endif // QT_CONFIG(tooltip)
        self.win_len_label.setText(QCoreApplication.translate("SpectralSettings", u"Window length", None))
        self.win_len_unit_label.setText(QCoreApplication.translate("SpectralSettings", u"s", None))
#if QT_CONFIG(tooltip)
        self.win_step_label.setToolTip(QCoreApplication.translate("SpectralSettings", u"Use a step shorter than the window length to overlap consecutive windows.", None))
#endif // QT_CONFIG(tooltip)
        self.win_step_label.setText(QCoreApplication.translate("SpectralSettings", u"Window step", None))
        self.win_step_unit_label.setText(QCoreApplication.translate("SpectralSettings", u"s", None))
        self.fft_help_label.setText(QCoreApplication.translate("SpectralSettings", u"Welch's method: an FFT on each window (Hann window), then the periodograms are averaged.", None))
        self.window_warning_label.setText(QCoreApplication.translate("SpectralSettings", u"<b>Window length and step</b><br/>Use a whole number of seconds for the window length, and a window step no longer than the window length.", None))
        self.about_resolution_title_label.setText(QCoreApplication.translate("SpectralSettings", u"About the frequency resolution", None))
        self.about_resolution_label.setText(QCoreApplication.translate("SpectralSettings", u"The frequency bin resolution is 1 / window length (s): 1 Hz with 1 s windows, 0.2 Hz with 5 s windows. The signal is filtered between 0.3 and 62 Hz before the analysis.", None))
    # retranslateUi

