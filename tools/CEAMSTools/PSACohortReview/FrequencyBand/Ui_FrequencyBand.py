# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_FrequencyBand.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)
import themes_rc

class Ui_FrequencyBand(object):
    def setupUi(self, FrequencyBand):
        if not FrequencyBand.objectName():
            FrequencyBand.setObjectName(u"FrequencyBand")
        FrequencyBand.resize(900, 700)
        self.verticalLayout = QVBoxLayout(FrequencyBand)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.header_layout = QVBoxLayout()
        self.header_layout.setSpacing(6)
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(FrequencyBand)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.header_layout.addWidget(self.title_label)

        self.subtitle_label = QLabel(FrequencyBand)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setProperty(u"variant", u"help")

        self.header_layout.addWidget(self.subtitle_label)


        self.verticalLayout.addLayout(self.header_layout)

        self.lists_layout = QHBoxLayout()
        self.lists_layout.setSpacing(16)
        self.lists_layout.setObjectName(u"lists_layout")
        self.bins_card = QFrame(FrequencyBand)
        self.bins_card.setObjectName(u"bins_card")
        self.bins_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.bins_card.setFrameShadow(QFrame.Shadow.Raised)
        self.bins_card_layout = QVBoxLayout(self.bins_card)
        self.bins_card_layout.setSpacing(10)
        self.bins_card_layout.setObjectName(u"bins_card_layout")
        self.bins_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_5 = QLabel(self.bins_card)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setBold(True)
        self.label_5.setFont(font1)

        self.bins_card_layout.addWidget(self.label_5)

        self.tiny_band_tableView = QTableView(self.bins_card)
        self.tiny_band_tableView.setObjectName(u"tiny_band_tableView")
        self.tiny_band_tableView.setMinimumSize(QSize(0, 240))
        self.tiny_band_tableView.setMaximumSize(QSize(350, 16777215))
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(False)
        self.tiny_band_tableView.setFont(font2)
        self.tiny_band_tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.bins_card_layout.addWidget(self.tiny_band_tableView)


        self.lists_layout.addWidget(self.bins_card)

        self.bands_card = QFrame(FrequencyBand)
        self.bands_card.setObjectName(u"bands_card")
        self.bands_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.bands_card.setFrameShadow(QFrame.Shadow.Raised)
        self.bands_card_layout = QVBoxLayout(self.bands_card)
        self.bands_card_layout.setSpacing(10)
        self.bands_card_layout.setObjectName(u"bands_card_layout")
        self.bands_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_6 = QLabel(self.bands_card)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.bands_card_layout.addWidget(self.label_6)

        self.bands_help_label = QLabel(self.bands_card)
        self.bands_help_label.setObjectName(u"bands_help_label")
        font3 = QFont()
        font3.setPointSize(10)
        self.bands_help_label.setFont(font3)
        self.bands_help_label.setWordWrap(True)
        self.bands_help_label.setProperty(u"variant", u"help")

        self.bands_card_layout.addWidget(self.bands_help_label)

        self.new_band_tableView = QTableView(self.bands_card)
        self.new_band_tableView.setObjectName(u"new_band_tableView")
        self.new_band_tableView.setMinimumSize(QSize(0, 240))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_band_tableView.sizePolicy().hasHeightForWidth())
        self.new_band_tableView.setSizePolicy(sizePolicy)
        self.new_band_tableView.setMaximumSize(QSize(16777215, 16777215))
        self.new_band_tableView.setFont(font2)
        self.new_band_tableView.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.new_band_tableView.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)
        self.new_band_tableView.setAlternatingRowColors(False)
        self.new_band_tableView.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.new_band_tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.new_band_tableView.setTextElideMode(Qt.TextElideMode.ElideLeft)

        self.bands_card_layout.addWidget(self.new_band_tableView)

        self.bands_buttons_layout = QHBoxLayout()
        self.bands_buttons_layout.setSpacing(8)
        self.bands_buttons_layout.setObjectName(u"bands_buttons_layout")
        self.add_pushButton = QPushButton(self.bands_card)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setFont(font2)

        self.bands_buttons_layout.addWidget(self.add_pushButton)

        self.rem_pushButton = QPushButton(self.bands_card)
        self.rem_pushButton.setObjectName(u"rem_pushButton")
        self.rem_pushButton.setFont(font2)

        self.bands_buttons_layout.addWidget(self.rem_pushButton)

        self.bands_buttons_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.bands_buttons_layout.addItem(self.bands_buttons_spacer)

        self.load_pushButton = QPushButton(self.bands_card)
        self.load_pushButton.setObjectName(u"load_pushButton")
        self.load_pushButton.setFont(font2)

        self.bands_buttons_layout.addWidget(self.load_pushButton)

        self.save_pushButton = QPushButton(self.bands_card)
        self.save_pushButton.setObjectName(u"save_pushButton")
        self.save_pushButton.setFont(font2)

        self.bands_buttons_layout.addWidget(self.save_pushButton)

        self.bands_buttons_layout.setStretch(2, 1)

        self.bands_card_layout.addLayout(self.bands_buttons_layout)


        self.lists_layout.addWidget(self.bands_card)

        self.lists_layout.setStretch(0, 1)
        self.lists_layout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.lists_layout)

        self.about_bands_layout = QVBoxLayout()
        self.about_bands_layout.setSpacing(6)
        self.about_bands_layout.setObjectName(u"about_bands_layout")
        self.about_bands_title_label = QLabel(FrequencyBand)
        self.about_bands_title_label.setObjectName(u"about_bands_title_label")
        self.about_bands_title_label.setFont(font1)

        self.about_bands_layout.addWidget(self.about_bands_title_label)

        self.about_bands_label = QLabel(FrequencyBand)
        self.about_bands_label.setObjectName(u"about_bands_label")
        self.about_bands_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_bands_label.setWordWrap(True)
        self.about_bands_label.setProperty(u"variant", u"help")

        self.about_bands_layout.addWidget(self.about_bands_label)


        self.verticalLayout.addLayout(self.about_bands_layout)


        self.retranslateUi(FrequencyBand)
        self.add_pushButton.clicked.connect(FrequencyBand.add_row_freq_band_slot)
        self.rem_pushButton.clicked.connect(FrequencyBand.rem_row_freq_band_slot)
        self.load_pushButton.clicked.connect(FrequencyBand.load_freq_band_slot)
        self.save_pushButton.clicked.connect(FrequencyBand.save_freq_band_slot)

        QMetaObject.connectSlotsByName(FrequencyBand)
    # setupUi

    def retranslateUi(self, FrequencyBand):
        FrequencyBand.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("FrequencyBand", u"Frequency Band", None))
        self.subtitle_label.setText(QCoreApplication.translate("FrequencyBand", u"Define the frequency bands to compute from the frequency bins of the reports.", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("FrequencyBand", u"A frequency band includes its low bin and excludes its high bin, so the power of a frequency bin is never averaged twice.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("FrequencyBand", u"Frequency bins available [low, high[", None))
        self.label_6.setText(QCoreApplication.translate("FrequencyBand", u"Frequency bands to compute", None))
        self.bands_help_label.setText(QCoreApplication.translate("FrequencyBand", u"Fill only the numerator for absolute power, or the numerator and the denominator for relative power.", None))
        self.add_pushButton.setText(QCoreApplication.translate("FrequencyBand", u"Add", None))
        self.rem_pushButton.setText(QCoreApplication.translate("FrequencyBand", u"Remove", None))
        self.load_pushButton.setText(QCoreApplication.translate("FrequencyBand", u"&Load", None))
        self.save_pushButton.setText(QCoreApplication.translate("FrequencyBand", u"&Save", None))
        self.about_bands_title_label.setText(QCoreApplication.translate("FrequencyBand", u"About the frequency bands", None))
        self.about_bands_label.setText(QCoreApplication.translate("FrequencyBand", u"<b>Frequency bands</b><br/>\u2022 Add a new band with \"Add\", or load an existing file with \"Load\". You can edit the bands loaded.<br/>\u2022 Double-click a cell to edit its value. The values must be within the frequency bins available, so add the reports in step 1, \"Input Files\", first.<br/>\u2022 \"Remove\" removes the selected band. \"Save\" saves the bands you edited in a .tsv file, which \"Load\" can read later.<br/><br/><b>Absolute and relative power</b><br/>\u2022 The spectral power can be absolute or relative.<br/>\u2022 For absolute power, fill only the numerator of the band, \"num-start(Hz)\" and \"num-end(Hz)\". Leave \"den-start(Hz)\" and \"den-end(Hz)\" as nan (not a number).<br/>\u2022 For relative power, fill the numerator and the denominator of the band. The relative power is the power of the numerator band divided by the power of the denominator band, in percent.<br/>\u2022 For example, 1 to 4 Hz over 0.5 to 32 Hz gives the power from 1 to 4 Hz as a percentage of the power from 0.5 to 32 "
                        "Hz.<br/><br/><b>Frequency bins</b><br/>\u2022 A band includes its low frequency bin and excludes its high one, [low, high[. So the power of a frequency bin is never averaged twice in two adjacent bands.<br/>\u2022 For example, with bins of 0.5 Hz, the band 1 to 4 Hz holds the 6 bins that start at 1, 1.5, 2, 2.5, 3 and 3.5 Hz. The band 4 to 8 Hz starts with the bin at 4 Hz.<br/>\u2022 Use band limits that are limits of the frequency bins. A band whose bins are not all in a report is left empty for that channel.", None))
    # retranslateUi

