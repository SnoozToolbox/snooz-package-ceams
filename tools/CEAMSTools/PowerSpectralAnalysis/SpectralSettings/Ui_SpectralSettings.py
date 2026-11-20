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
    QLabel, QLineEdit, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

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
        self.fft_card = QFrame(self.content_widget)
        self.fft_card.setObjectName(u"fft_card")
        self.fft_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.fft_card.setFrameShadow(QFrame.Shadow.Raised)
        self.fft_card_layout = QVBoxLayout(self.fft_card)
        self.fft_card_layout.setSpacing(10)
        self.fft_card_layout.setObjectName(u"fft_card_layout")
        self.fft_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_3 = QLabel(self.fft_card)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.fft_card_layout.addWidget(self.label_3)

        self.fft_grid = QGridLayout()
        self.fft_grid.setObjectName(u"fft_grid")
        self.fft_grid.setHorizontalSpacing(12)
        self.fft_grid.setVerticalSpacing(10)
        self.label = QLabel(self.fft_card)
        self.label.setObjectName(u"label")

        self.fft_grid.addWidget(self.label, 0, 0, 1, 1)

        self.win_len_lineEdit = QLineEdit(self.fft_card)
        self.win_len_lineEdit.setObjectName(u"win_len_lineEdit")
        self.win_len_lineEdit.setMaximumSize(QSize(80, 16777215))

        self.fft_grid.addWidget(self.win_len_lineEdit, 0, 1, 1, 1)

        self.win_len_unit_label = QLabel(self.fft_card)
        self.win_len_unit_label.setObjectName(u"win_len_unit_label")
        self.win_len_unit_label.setProperty(u"variant", u"help")

        self.fft_grid.addWidget(self.win_len_unit_label, 0, 2, 1, 1)

        self.label_2 = QLabel(self.fft_card)
        self.label_2.setObjectName(u"label_2")

        self.fft_grid.addWidget(self.label_2, 1, 0, 1, 1)

        self.win_step_lineEdit = QLineEdit(self.fft_card)
        self.win_step_lineEdit.setObjectName(u"win_step_lineEdit")
        self.win_step_lineEdit.setMaximumSize(QSize(80, 16777215))

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
        font2 = QFont()
        font2.setPointSize(10)
        self.fft_help_label.setFont(font2)
        self.fft_help_label.setWordWrap(True)
        self.fft_help_label.setProperty(u"variant", u"help")

        self.fft_card_layout.addWidget(self.fft_help_label)

        self.fft_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.fft_card_layout.addItem(self.fft_stretch)


        self.spectral_cards_layout.addWidget(self.fft_card)

        self.bands_card = QFrame(self.content_widget)
        self.bands_card.setObjectName(u"bands_card")
        self.bands_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.bands_card.setFrameShadow(QFrame.Shadow.Raised)
        self.bands_card_layout = QVBoxLayout(self.bands_card)
        self.bands_card_layout.setSpacing(10)
        self.bands_card_layout.setObjectName(u"bands_card_layout")
        self.bands_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_7 = QLabel(self.bands_card)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.bands_card_layout.addWidget(self.label_7)

        self.bands_grid = QGridLayout()
        self.bands_grid.setObjectName(u"bands_grid")
        self.bands_grid.setHorizontalSpacing(12)
        self.bands_grid.setVerticalSpacing(10)
        self.label_8 = QLabel(self.bands_card)
        self.label_8.setObjectName(u"label_8")

        self.bands_grid.addWidget(self.label_8, 0, 0, 1, 1)

        self.miniband_lineEdit = QLineEdit(self.bands_card)
        self.miniband_lineEdit.setObjectName(u"miniband_lineEdit")
        self.miniband_lineEdit.setMaximumSize(QSize(80, 16777215))
        self.miniband_lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.bands_grid.addWidget(self.miniband_lineEdit, 0, 1, 1, 1)

        self.miniband_unit_label = QLabel(self.bands_card)
        self.miniband_unit_label.setObjectName(u"miniband_unit_label")
        self.miniband_unit_label.setProperty(u"variant", u"help")

        self.bands_grid.addWidget(self.miniband_unit_label, 0, 2, 1, 1)

        self.label_4 = QLabel(self.bands_card)
        self.label_4.setObjectName(u"label_4")

        self.bands_grid.addWidget(self.label_4, 1, 0, 1, 1)

        self.first_freq_lineEdit = QLineEdit(self.bands_card)
        self.first_freq_lineEdit.setObjectName(u"first_freq_lineEdit")
        self.first_freq_lineEdit.setMaximumSize(QSize(80, 16777215))
        self.first_freq_lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.bands_grid.addWidget(self.first_freq_lineEdit, 1, 1, 1, 1)

        self.first_freq_unit_label = QLabel(self.bands_card)
        self.first_freq_unit_label.setObjectName(u"first_freq_unit_label")
        self.first_freq_unit_label.setProperty(u"variant", u"help")

        self.bands_grid.addWidget(self.first_freq_unit_label, 1, 2, 1, 1)

        self.label_9 = QLabel(self.bands_card)
        self.label_9.setObjectName(u"label_9")

        self.bands_grid.addWidget(self.label_9, 2, 0, 1, 1)

        self.last_freq_lineEdit = QLineEdit(self.bands_card)
        self.last_freq_lineEdit.setObjectName(u"last_freq_lineEdit")
        self.last_freq_lineEdit.setMaximumSize(QSize(80, 16777215))
        self.last_freq_lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.bands_grid.addWidget(self.last_freq_lineEdit, 2, 1, 1, 1)

        self.last_freq_unit_label = QLabel(self.bands_card)
        self.last_freq_unit_label.setObjectName(u"last_freq_unit_label")
        self.last_freq_unit_label.setProperty(u"variant", u"help")

        self.bands_grid.addWidget(self.last_freq_unit_label, 2, 2, 1, 1)

        self.bands_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.bands_grid.addItem(self.bands_grid_spacer, 0, 3, 1, 1)


        self.bands_card_layout.addLayout(self.bands_grid)

        self.bands_help_label = QLabel(self.bands_card)
        self.bands_help_label.setObjectName(u"bands_help_label")
        self.bands_help_label.setFont(font2)
        self.bands_help_label.setWordWrap(True)
        self.bands_help_label.setProperty(u"variant", u"help")

        self.bands_card_layout.addWidget(self.bands_help_label)

        self.bands_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.bands_card_layout.addItem(self.bands_stretch)


        self.spectral_cards_layout.addWidget(self.bands_card)

        self.spectral_cards_layout.setStretch(0, 1)
        self.spectral_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.spectral_cards_layout)

        self.method_card = QFrame(self.content_widget)
        self.method_card.setObjectName(u"method_card")
        self.method_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.method_card.setFrameShadow(QFrame.Shadow.Raised)
        self.method_card_layout = QVBoxLayout(self.method_card)
        self.method_card_layout.setSpacing(10)
        self.method_card_layout.setObjectName(u"method_card_layout")
        self.method_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_6 = QLabel(self.method_card)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.method_card_layout.addWidget(self.label_6)

        self.method_layout = QVBoxLayout()
        self.method_layout.setSpacing(8)
        self.method_layout.setObjectName(u"method_layout")
        self.method_layout_1_layout = QVBoxLayout()
        self.method_layout_1_layout.setSpacing(2)
        self.method_layout_1_layout.setObjectName(u"method_layout_1_layout")
        self.std_radioButton = QRadioButton(self.method_card)
        self.std_radioButton.setObjectName(u"std_radioButton")
        self.std_radioButton.setEnabled(True)
        self.std_radioButton.setChecked(True)

        self.method_layout_1_layout.addWidget(self.std_radioButton)

        self.label_5 = QLabel(self.method_card)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setWordWrap(True)
        self.label_5.setIndent(26)
        self.label_5.setProperty(u"variant", u"help")

        self.method_layout_1_layout.addWidget(self.label_5)


        self.method_layout.addLayout(self.method_layout_1_layout)

        self.method_layout_line_1 = QFrame(self.method_card)
        self.method_layout_line_1.setObjectName(u"method_layout_line_1")
        self.method_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.method_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.method_layout.addWidget(self.method_layout_line_1)

        self.method_layout_2_layout = QVBoxLayout()
        self.method_layout_2_layout.setSpacing(2)
        self.method_layout_2_layout.setObjectName(u"method_layout_2_layout")
        self.RA_radioButton = QRadioButton(self.method_card)
        self.RA_radioButton.setObjectName(u"RA_radioButton")
        self.RA_radioButton.setEnabled(True)

        self.method_layout_2_layout.addWidget(self.RA_radioButton)

        self.label_11 = QLabel(self.method_card)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setWordWrap(True)
        self.label_11.setIndent(26)
        self.label_11.setProperty(u"variant", u"help")

        self.method_layout_2_layout.addWidget(self.label_11)


        self.method_layout.addLayout(self.method_layout_2_layout)

        self.method_layout_line_2 = QFrame(self.method_card)
        self.method_layout_line_2.setObjectName(u"method_layout_line_2")
        self.method_layout_line_2.setFrameShape(QFrame.Shape.HLine)
        self.method_layout_line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.method_layout.addWidget(self.method_layout_line_2)

        self.method_layout_3_layout = QVBoxLayout()
        self.method_layout_3_layout.setSpacing(2)
        self.method_layout_3_layout.setObjectName(u"method_layout_3_layout")
        self.FoooF_radioButton = QRadioButton(self.method_card)
        self.FoooF_radioButton.setObjectName(u"FoooF_radioButton")

        self.method_layout_3_layout.addWidget(self.FoooF_radioButton)

        self.label_12 = QLabel(self.method_card)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setWordWrap(True)
        self.label_12.setIndent(26)
        self.label_12.setProperty(u"variant", u"help")

        self.method_layout_3_layout.addWidget(self.label_12)


        self.method_layout.addLayout(self.method_layout_3_layout)


        self.method_card_layout.addLayout(self.method_layout)


        self.content_layout.addWidget(self.method_card)

        self.bands_warning = QFrame(self.content_widget)
        self.bands_warning.setObjectName(u"bands_warning")
        self.bands_warning.setFrameShape(QFrame.Shape.NoFrame)
        self.bands_warning.setProperty(u"variant", u"warning")
        self.bands_warning_layout = QHBoxLayout(self.bands_warning)
        self.bands_warning_layout.setObjectName(u"bands_warning_layout")
        self.bands_warning_layout.setContentsMargins(14, 10, 14, 10)
        self.bands_warning_label = QLabel(self.bands_warning)
        self.bands_warning_label.setObjectName(u"bands_warning_label")
        self.bands_warning_label.setTextFormat(Qt.TextFormat.RichText)
        self.bands_warning_label.setWordWrap(True)

        self.bands_warning_layout.addWidget(self.bands_warning_label)


        self.content_layout.addWidget(self.bands_warning)

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
        self.win_len_lineEdit.editingFinished.connect(SpectralSettings.miniband_edit_slot)
        self.last_freq_lineEdit.editingFinished.connect(SpectralSettings.lastfreq_edit_slot)
        self.miniband_lineEdit.editingFinished.connect(SpectralSettings.miniband_edit_slot)

        QMetaObject.connectSlotsByName(SpectralSettings)
    # setupUi

    def retranslateUi(self, SpectralSettings):
        SpectralSettings.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("SpectralSettings", u"Spectral Settings", None))
        self.subtitle_label.setText(QCoreApplication.translate("SpectralSettings", u"Define how the spectral power is computed: the FFT windows, the frequency bands and the method.", None))
        self.label_3.setText(QCoreApplication.translate("SpectralSettings", u"FFT windows", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("SpectralSettings", u"Duration of the signal used to compute each FFT. Longer windows give a finer frequency resolution.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("SpectralSettings", u"Window length", None))
#if QT_CONFIG(tooltip)
        self.win_len_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.win_len_unit_label.setText(QCoreApplication.translate("SpectralSettings", u"s", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("SpectralSettings", u"Time between the start points of consecutive FFT windows, controlling the overlap and the temporal resolution.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("SpectralSettings", u"Window step", None))
#if QT_CONFIG(tooltip)
        self.win_step_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.win_step_unit_label.setText(QCoreApplication.translate("SpectralSettings", u"s", None))
        self.fft_help_label.setText(QCoreApplication.translate("SpectralSettings", u"Welch's method: an FFT on each window, then the periodograms are averaged. Longer windows give a finer frequency resolution.", None))
        self.label_7.setText(QCoreApplication.translate("SpectralSettings", u"Frequency bands", None))
        self.label_8.setText(QCoreApplication.translate("SpectralSettings", u"Width of each mini band", None))
        self.miniband_lineEdit.setText(QCoreApplication.translate("SpectralSettings", u"0.5", None))
        self.miniband_unit_label.setText(QCoreApplication.translate("SpectralSettings", u"Hz", None))
        self.label_4.setText(QCoreApplication.translate("SpectralSettings", u"First frequency analyzed", None))
        self.first_freq_lineEdit.setText(QCoreApplication.translate("SpectralSettings", u"0.0", None))
        self.first_freq_unit_label.setText(QCoreApplication.translate("SpectralSettings", u"Hz", None))
        self.label_9.setText(QCoreApplication.translate("SpectralSettings", u"Last frequency analyzed", None))
        self.last_freq_lineEdit.setText(QCoreApplication.translate("SpectralSettings", u"64", None))
        self.last_freq_unit_label.setText(QCoreApplication.translate("SpectralSettings", u"Hz", None))
        self.bands_help_label.setText(QCoreApplication.translate("SpectralSettings", u"The first band can be smaller.", None))
        self.label_6.setText(QCoreApplication.translate("SpectralSettings", u"Power spectral analysis", None))
        self.std_radioButton.setText(QCoreApplication.translate("SpectralSettings", u"Standard Spectrum (Welch)", None))
        self.label_5.setText(QCoreApplication.translate("SpectralSettings", u"Traditional power spectral density estimation.", None))
        self.RA_radioButton.setText(QCoreApplication.translate("SpectralSettings", u"Periodic/Aperiodic Decomposition (IRASA)", None))
        self.label_11.setText(QCoreApplication.translate("SpectralSettings", u"Separates the oscillatory and the fractal components using signal resampling.", None))
        self.FoooF_radioButton.setText(QCoreApplication.translate("SpectralSettings", u"Periodic/Aperiodic Decomposition (FOOOF)", None))
        self.label_12.setText(QCoreApplication.translate("SpectralSettings", u"Models the oscillatory peaks and the background activity using parametric fitting.", None))
        self.bands_warning_label.setText(QCoreApplication.translate("SpectralSettings", u"<b>Frequency limits</b><br/>The last frequency must be at most half the sampling rate of the channels (<b>FS / 2</b>). The zero frequency is not supported by IRASA.", None))
        self.about_resolution_title_label.setText(QCoreApplication.translate("SpectralSettings", u"About the frequency resolution", None))
        self.about_resolution_label.setText(QCoreApplication.translate("SpectralSettings", u"The frequency bin resolution is 1 / window length (s): 0.2 Hz with 5 s windows, 0.25 Hz with 4 s windows. The width of the mini bands must be a multiple of it: 0.2 Hz or 1 Hz with 5 s windows; 0.25 Hz, 0.5 Hz or 1 Hz with 4 s windows. IRASA and FOOOF are described in the documentation of the tool: Read more! below.", None))
    # retranslateUi

