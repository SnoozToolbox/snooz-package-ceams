# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_A7Settings.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_A7Settings(object):
    def setupUi(self, A7Settings):
        if not A7Settings.objectName():
            A7Settings.setObjectName(u"A7Settings")
        A7Settings.resize(900, 700)
        self.verticalLayout = QVBoxLayout(A7Settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(A7Settings)
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
        self.label = QLabel(self.events_card)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)

        self.events_card_layout.addWidget(self.label)

        self.events_grid = QGridLayout()
        self.events_grid.setObjectName(u"events_grid")
        self.events_grid.setHorizontalSpacing(12)
        self.events_grid.setVerticalSpacing(10)
        self.label_2 = QLabel(self.events_card)
        self.label_2.setObjectName(u"label_2")

        self.events_grid.addWidget(self.label_2, 0, 0, 1, 1)

        self.group_lineEdit = QLineEdit(self.events_card)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setMinimumSize(QSize(120, 0))
        self.group_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.events_grid.addWidget(self.group_lineEdit, 0, 1, 1, 1)

        self.label_3 = QLabel(self.events_card)
        self.label_3.setObjectName(u"label_3")

        self.events_grid.addWidget(self.label_3, 1, 0, 1, 1)

        self.name_lineEdit = QLineEdit(self.events_card)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(120, 0))
        self.name_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.events_grid.addWidget(self.name_lineEdit, 1, 1, 1, 1)

        self.events_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.events_grid.addItem(self.events_grid_spacer, 0, 3, 1, 1)


        self.events_card_layout.addLayout(self.events_grid)

        self.events_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.events_card_layout.addItem(self.events_stretch)


        self.settings_cards_layout.addWidget(self.events_card)

        self.band_card = QFrame(self.content_widget)
        self.band_card.setObjectName(u"band_card")
        self.band_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.band_card.setFrameShadow(QFrame.Shadow.Raised)
        self.band_card_layout = QVBoxLayout(self.band_card)
        self.band_card_layout.setSpacing(10)
        self.band_card_layout.setObjectName(u"band_card_layout")
        self.band_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_15 = QLabel(self.band_card)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.band_card_layout.addWidget(self.label_15)

        self.band_grid = QGridLayout()
        self.band_grid.setObjectName(u"band_grid")
        self.band_grid.setHorizontalSpacing(12)
        self.band_grid.setVerticalSpacing(10)
        self.label_14 = QLabel(self.band_card)
        self.label_14.setObjectName(u"label_14")

        self.band_grid.addWidget(self.label_14, 0, 0, 1, 1)

        self.doubleSpinBox_Lower_Bound = QDoubleSpinBox(self.band_card)
        self.doubleSpinBox_Lower_Bound.setObjectName(u"doubleSpinBox_Lower_Bound")
        self.doubleSpinBox_Lower_Bound.setSingleStep(0.100000000000000)
        self.doubleSpinBox_Lower_Bound.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.doubleSpinBox_Lower_Bound.setValue(11.000000000000000)

        self.band_grid.addWidget(self.doubleSpinBox_Lower_Bound, 0, 1, 1, 1)

        self.lower_bound_unit_label = QLabel(self.band_card)
        self.lower_bound_unit_label.setObjectName(u"lower_bound_unit_label")
        self.lower_bound_unit_label.setProperty(u"variant", u"help")

        self.band_grid.addWidget(self.lower_bound_unit_label, 0, 2, 1, 1)

        self.label_16 = QLabel(self.band_card)
        self.label_16.setObjectName(u"label_16")

        self.band_grid.addWidget(self.label_16, 1, 0, 1, 1)

        self.doubleSpinBox_Upper_Bound = QDoubleSpinBox(self.band_card)
        self.doubleSpinBox_Upper_Bound.setObjectName(u"doubleSpinBox_Upper_Bound")
        self.doubleSpinBox_Upper_Bound.setSingleStep(0.100000000000000)
        self.doubleSpinBox_Upper_Bound.setValue(16.000000000000000)

        self.band_grid.addWidget(self.doubleSpinBox_Upper_Bound, 1, 1, 1, 1)

        self.upper_bound_unit_label = QLabel(self.band_card)
        self.upper_bound_unit_label.setObjectName(u"upper_bound_unit_label")
        self.upper_bound_unit_label.setProperty(u"variant", u"help")

        self.band_grid.addWidget(self.upper_bound_unit_label, 1, 2, 1, 1)

        self.band_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.band_grid.addItem(self.band_grid_spacer, 0, 3, 1, 1)


        self.band_card_layout.addLayout(self.band_grid)

        self.band_help_label = QLabel(self.band_card)
        self.band_help_label.setObjectName(u"band_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.band_help_label.setFont(font2)
        self.band_help_label.setWordWrap(True)
        self.band_help_label.setProperty(u"variant", u"help")

        self.band_card_layout.addWidget(self.band_help_label)

        self.band_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.band_card_layout.addItem(self.band_stretch)


        self.settings_cards_layout.addWidget(self.band_card)

        self.settings_cards_layout.setStretch(0, 1)
        self.settings_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.settings_cards_layout)

        self.textEdit_6 = QFrame(self.content_widget)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_6.setProperty(u"variant", u"warning")
        self.textEdit_6_layout = QHBoxLayout(self.textEdit_6)
        self.textEdit_6_layout.setObjectName(u"textEdit_6_layout")
        self.textEdit_6_layout.setContentsMargins(14, 10, 14, 10)
        self.textEdit_6_label = QLabel(self.textEdit_6)
        self.textEdit_6_label.setObjectName(u"textEdit_6_label")
        self.textEdit_6_label.setTextFormat(Qt.TextFormat.RichText)
        self.textEdit_6_label.setWordWrap(True)

        self.textEdit_6_layout.addWidget(self.textEdit_6_label)


        self.content_layout.addWidget(self.textEdit_6)

        self.thresholds_card = QFrame(self.content_widget)
        self.thresholds_card.setObjectName(u"thresholds_card")
        self.thresholds_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.thresholds_card.setFrameShadow(QFrame.Shadow.Raised)
        self.thresholds_card_layout = QVBoxLayout(self.thresholds_card)
        self.thresholds_card_layout.setSpacing(10)
        self.thresholds_card_layout.setObjectName(u"thresholds_card_layout")
        self.thresholds_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_5 = QLabel(self.thresholds_card)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.thresholds_card_layout.addWidget(self.label_5)

        self.thresholds_grid = QGridLayout()
        self.thresholds_grid.setObjectName(u"thresholds_grid")
        self.thresholds_grid.setHorizontalSpacing(12)
        self.thresholds_grid.setVerticalSpacing(10)
        self.label_4 = QLabel(self.thresholds_card)
        self.label_4.setObjectName(u"label_4")

        self.thresholds_grid.addWidget(self.label_4, 0, 0, 1, 1)

        self.doubleSpinBox_absSigma = QDoubleSpinBox(self.thresholds_card)
        self.doubleSpinBox_absSigma.setObjectName(u"doubleSpinBox_absSigma")
        self.doubleSpinBox_absSigma.setSingleStep(0.250000000000000)
        self.doubleSpinBox_absSigma.setValue(1.250000000000000)

        self.thresholds_grid.addWidget(self.doubleSpinBox_absSigma, 0, 1, 1, 1)

        self.label_10 = QLabel(self.thresholds_card)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setProperty(u"variant", u"help")

        self.thresholds_grid.addWidget(self.label_10, 0, 2, 1, 1)

        self.label_7 = QLabel(self.thresholds_card)
        self.label_7.setObjectName(u"label_7")

        self.thresholds_grid.addWidget(self.label_7, 1, 0, 1, 1)

        self.doubleSpinBox_relSigma = QDoubleSpinBox(self.thresholds_card)
        self.doubleSpinBox_relSigma.setObjectName(u"doubleSpinBox_relSigma")
        self.doubleSpinBox_relSigma.setMaximum(30.000000000000000)
        self.doubleSpinBox_relSigma.setSingleStep(0.100000000000000)
        self.doubleSpinBox_relSigma.setValue(1.600000000000000)

        self.thresholds_grid.addWidget(self.doubleSpinBox_relSigma, 1, 1, 1, 1)

        self.label_12 = QLabel(self.thresholds_card)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setProperty(u"variant", u"help")

        self.thresholds_grid.addWidget(self.label_12, 1, 2, 1, 1)

        self.label_8 = QLabel(self.thresholds_card)
        self.label_8.setObjectName(u"label_8")

        self.thresholds_grid.addWidget(self.label_8, 2, 0, 1, 1)

        self.doubleSpinBox_sigmaCov = QDoubleSpinBox(self.thresholds_card)
        self.doubleSpinBox_sigmaCov.setObjectName(u"doubleSpinBox_sigmaCov")
        self.doubleSpinBox_sigmaCov.setMaximum(30.000000000000000)
        self.doubleSpinBox_sigmaCov.setSingleStep(0.100000000000000)
        self.doubleSpinBox_sigmaCov.setValue(1.300000000000000)

        self.thresholds_grid.addWidget(self.doubleSpinBox_sigmaCov, 2, 1, 1, 1)

        self.label_11 = QLabel(self.thresholds_card)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setProperty(u"variant", u"help")

        self.thresholds_grid.addWidget(self.label_11, 2, 2, 1, 1)

        self.label_9 = QLabel(self.thresholds_card)
        self.label_9.setObjectName(u"label_9")

        self.thresholds_grid.addWidget(self.label_9, 3, 0, 1, 1)

        self.doubleSpinBox_sigmaCor = QDoubleSpinBox(self.thresholds_card)
        self.doubleSpinBox_sigmaCor.setObjectName(u"doubleSpinBox_sigmaCor")
        self.doubleSpinBox_sigmaCor.setDecimals(0)
        self.doubleSpinBox_sigmaCor.setValue(69.000000000000000)

        self.thresholds_grid.addWidget(self.doubleSpinBox_sigmaCor, 3, 1, 1, 1)

        self.label_13 = QLabel(self.thresholds_card)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setProperty(u"variant", u"help")

        self.thresholds_grid.addWidget(self.label_13, 3, 2, 1, 1)

        self.thresholds_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.thresholds_grid.addItem(self.thresholds_grid_spacer, 0, 3, 1, 1)


        self.thresholds_card_layout.addLayout(self.thresholds_grid)

        self.thresholds_help_label = QLabel(self.thresholds_card)
        self.thresholds_help_label.setObjectName(u"thresholds_help_label")
        self.thresholds_help_label.setFont(font2)
        self.thresholds_help_label.setWordWrap(True)
        self.thresholds_help_label.setProperty(u"variant", u"help")

        self.thresholds_card_layout.addWidget(self.thresholds_help_label)


        self.content_layout.addWidget(self.thresholds_card)

        self.about_a7_layout = QVBoxLayout()
        self.about_a7_layout.setSpacing(6)
        self.about_a7_layout.setObjectName(u"about_a7_layout")
        self.label_6 = QLabel(self.content_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.about_a7_layout.addWidget(self.label_6)

        self.textEdit = QLabel(self.content_widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setWordWrap(True)
        self.textEdit.setProperty(u"variant", u"help")

        self.about_a7_layout.addWidget(self.textEdit)

        self.textEdit_2 = QLabel(self.content_widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setTextFormat(Qt.TextFormat.RichText)
        self.textEdit_2.setWordWrap(True)
        self.textEdit_2.setProperty(u"variant", u"help")

        self.about_a7_layout.addWidget(self.textEdit_2)

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


        self.about_a7_layout.addLayout(self.references_layout)


        self.content_layout.addLayout(self.about_a7_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(A7Settings)

        QMetaObject.connectSlotsByName(A7Settings)
    # setupUi

    def retranslateUi(self, A7Settings):
        A7Settings.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("A7Settings", u"A7 Settings", None))
        self.subtitle_label.setText(QCoreApplication.translate("A7Settings", u"The spindle events created and the thresholds of the A7 detector, which emulates human scoring.", None))
        self.label.setText(QCoreApplication.translate("A7Settings", u"Spindle events", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("A7Settings", u"Define in which group the spindles will be added.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("A7Settings", u"Group", None))
        self.group_lineEdit.setText(QCoreApplication.translate("A7Settings", u"spindle", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("A7Settings", u"Define the name of the spindle events.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("A7Settings", u"Name", None))
        self.name_lineEdit.setText(QCoreApplication.translate("A7Settings", u"a7", None))
        self.label_15.setText(QCoreApplication.translate("A7Settings", u"Sigma band", None))
        self.label_14.setText(QCoreApplication.translate("A7Settings", u"Lower bound", None))
        self.lower_bound_unit_label.setText(QCoreApplication.translate("A7Settings", u"Hz", None))
        self.label_16.setText(QCoreApplication.translate("A7Settings", u"Upper bound", None))
        self.upper_bound_unit_label.setText(QCoreApplication.translate("A7Settings", u"Hz", None))
        self.band_help_label.setText(QCoreApplication.translate("A7Settings", u"Default: 11\u201316 Hz.", None))
        self.textEdit_6_label.setText(QCoreApplication.translate("A7Settings", u"<b>Thresholds and sigma band</b><br/>The thresholds are set and validated for the default sigma band (<b>11\u201316 Hz</b>). If you change the band, you may need to adjust the thresholds to keep an accurate detection.", None))
        self.label_5.setText(QCoreApplication.translate("A7Settings", u"Thresholds", None))
        self.label_4.setText(QCoreApplication.translate("A7Settings", u"Absolute sigma power (mean square)", None))
        self.label_10.setText(QCoreApplication.translate("A7Settings", u"\u00b5V\u00b2", None))
        self.label_7.setText(QCoreApplication.translate("A7Settings", u"Relative sigma power (PSD)", None))
        self.label_12.setText(QCoreApplication.translate("A7Settings", u"\u00d7 STD", None))
        self.label_8.setText(QCoreApplication.translate("A7Settings", u"Sigma covariance", None))
        self.label_11.setText(QCoreApplication.translate("A7Settings", u"\u00d7 STD", None))
        self.label_9.setText(QCoreApplication.translate("A7Settings", u"Sigma correlation", None))
        self.label_13.setText(QCoreApplication.translate("A7Settings", u"%", None))
        self.thresholds_help_label.setText(QCoreApplication.translate("A7Settings", u"A spindle is detected when the four features exceed their thresholds. The features are described at the end of the page.", None))
        self.label_6.setText(QCoreApplication.translate("A7Settings", u"About the A7 detector", None))
        self.textEdit.setText(QCoreApplication.translate("A7Settings", u"Over sliding windows (0.3 s long with a 0.1 s step), A7 computes the absolute power (mean square) in the sigma band, the relative sigma power based on the power spectral density (PSD), and the covariance and the correlation between the sigma-filtered and the unfiltered EEG signals [1]. It detects a spindle when the 4 features exceed their thresholds (1.25 \u00b5V\u00b2, 1.6 \u00d7 STD, 1.3 \u00d7 STD and 69%), set for the default sigma band (11\u201316 Hz).", None))
        self.textEdit_2.setText(QCoreApplication.translate("A7Settings", u"\u2022 <b>Absolute sigma power:</b> log10(mean squared sigma power).<br/>\u2022 <b>Relative sigma power:</b> z-score(log10(PSD sigma band / PSD 4.5\u201330 Hz)).<br/>\u2022 <b>Sigma covariance:</b> z-score(log10(cov(EEG 0.3\u201330 Hz, EEG sigma band))).<br/>\u2022 <b>Sigma correlation:</b> cov(EEG 0.3\u201330 Hz, EEG sigma band) / (std(EEG 0.3\u201330 Hz) \u00d7 std(EEG sigma band)).", None))
        self.references_label.setText(QCoreApplication.translate("A7Settings", u"[1] Lacourse, K., Delfrate, J., Beaudry, J., Peppard, P., &amp; Warby, S. C. (2019). A sleep spindle detection algorithm that emulates human expert spindle scoring. <i>Journal of Neuroscience Methods</i>, <i>316</i>, 3\u201311. <a href=\"https://doi.org/10.1016/j.jneumeth.2018.08.014\">https://doi.org/10.1016/j.jneumeth.2018.08.014</a>", None))
    # retranslateUi

