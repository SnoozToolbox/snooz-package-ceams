# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ConnectivitySettings.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_ConnectivitySettings(object):
    def setupUi(self, ConnectivitySettings):
        if not ConnectivitySettings.objectName():
            ConnectivitySettings.setObjectName(u"ConnectivitySettings")
        ConnectivitySettings.resize(900, 700)
        self.verticalLayout = QVBoxLayout(ConnectivitySettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(ConnectivitySettings)
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

        self.measure_card = QFrame(self.content_widget)
        self.measure_card.setObjectName(u"measure_card")
        self.measure_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.measure_card.setFrameShadow(QFrame.Shadow.Raised)
        self.measure_card_layout = QVBoxLayout(self.measure_card)
        self.measure_card_layout.setSpacing(10)
        self.measure_card_layout.setObjectName(u"measure_card_layout")
        self.measure_card_layout.setContentsMargins(10, 10, 10, 10)
        self.connectivity_type_label = QLabel(self.measure_card)
        self.connectivity_type_label.setObjectName(u"connectivity_type_label")
        font1 = QFont()
        font1.setBold(True)
        self.connectivity_type_label.setFont(font1)

        self.measure_card_layout.addWidget(self.connectivity_type_label)

        self.label_4 = QLabel(self.measure_card)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)
        self.label_4.setProperty(u"variant", u"help")

        self.measure_card_layout.addWidget(self.label_4)

        self.measure_layout = QVBoxLayout()
        self.measure_layout.setSpacing(8)
        self.measure_layout.setObjectName(u"measure_layout")
        self.measure_layout_1_layout = QVBoxLayout()
        self.measure_layout_1_layout.setSpacing(2)
        self.measure_layout_1_layout.setObjectName(u"measure_layout_1_layout")
        self.wpli_radioButton = QRadioButton(self.measure_card)
        self.connectivity_buttonGroup = QButtonGroup(ConnectivitySettings)
        self.connectivity_buttonGroup.setObjectName(u"connectivity_buttonGroup")
        self.connectivity_buttonGroup.addButton(self.wpli_radioButton)
        self.wpli_radioButton.setObjectName(u"wpli_radioButton")
        self.wpli_radioButton.setChecked(True)

        self.measure_layout_1_layout.addWidget(self.wpli_radioButton)

        self.wpli_help_label = QLabel(self.measure_card)
        self.wpli_help_label.setObjectName(u"wpli_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.wpli_help_label.setFont(font2)
        self.wpli_help_label.setWordWrap(True)
        self.wpli_help_label.setIndent(26)
        self.wpli_help_label.setProperty(u"variant", u"help")

        self.measure_layout_1_layout.addWidget(self.wpli_help_label)


        self.measure_layout.addLayout(self.measure_layout_1_layout)

        self.measure_layout_line_1 = QFrame(self.measure_card)
        self.measure_layout_line_1.setObjectName(u"measure_layout_line_1")
        self.measure_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.measure_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.measure_layout.addWidget(self.measure_layout_line_1)

        self.measure_layout_2_layout = QVBoxLayout()
        self.measure_layout_2_layout.setSpacing(2)
        self.measure_layout_2_layout.setObjectName(u"measure_layout_2_layout")
        self.dpli_radioButton = QRadioButton(self.measure_card)
        self.connectivity_buttonGroup.addButton(self.dpli_radioButton)
        self.dpli_radioButton.setObjectName(u"dpli_radioButton")

        self.measure_layout_2_layout.addWidget(self.dpli_radioButton)

        self.dpli_help_label = QLabel(self.measure_card)
        self.dpli_help_label.setObjectName(u"dpli_help_label")
        self.dpli_help_label.setFont(font2)
        self.dpli_help_label.setWordWrap(True)
        self.dpli_help_label.setIndent(26)
        self.dpli_help_label.setProperty(u"variant", u"help")

        self.measure_layout_2_layout.addWidget(self.dpli_help_label)


        self.measure_layout.addLayout(self.measure_layout_2_layout)

        self.measure_layout_line_2 = QFrame(self.measure_card)
        self.measure_layout_line_2.setObjectName(u"measure_layout_line_2")
        self.measure_layout_line_2.setFrameShape(QFrame.Shape.HLine)
        self.measure_layout_line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.measure_layout.addWidget(self.measure_layout_line_2)

        self.measure_layout_3_layout = QVBoxLayout()
        self.measure_layout_3_layout.setSpacing(2)
        self.measure_layout_3_layout.setObjectName(u"measure_layout_3_layout")
        self.aec_radioButton = QRadioButton(self.measure_card)
        self.connectivity_buttonGroup.addButton(self.aec_radioButton)
        self.aec_radioButton.setObjectName(u"aec_radioButton")

        self.measure_layout_3_layout.addWidget(self.aec_radioButton)

        self.aec_help_label = QLabel(self.measure_card)
        self.aec_help_label.setObjectName(u"aec_help_label")
        self.aec_help_label.setFont(font2)
        self.aec_help_label.setWordWrap(True)
        self.aec_help_label.setIndent(26)
        self.aec_help_label.setProperty(u"variant", u"help")

        self.measure_layout_3_layout.addWidget(self.aec_help_label)


        self.measure_layout.addLayout(self.measure_layout_3_layout)


        self.measure_card_layout.addLayout(self.measure_layout)


        self.content_layout.addWidget(self.measure_card)

        self.settings_cards_layout = QHBoxLayout()
        self.settings_cards_layout.setSpacing(16)
        self.settings_cards_layout.setObjectName(u"settings_cards_layout")
        self.epochs_card = QFrame(self.content_widget)
        self.epochs_card.setObjectName(u"epochs_card")
        self.epochs_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.epochs_card.setFrameShadow(QFrame.Shadow.Raised)
        self.epochs_card_layout = QVBoxLayout(self.epochs_card)
        self.epochs_card_layout.setSpacing(10)
        self.epochs_card_layout.setObjectName(u"epochs_card_layout")
        self.epochs_card_layout.setContentsMargins(10, 10, 10, 10)
        self.select_epoch_label = QLabel(self.epochs_card)
        self.select_epoch_label.setObjectName(u"select_epoch_label")
        self.select_epoch_label.setFont(font1)

        self.epochs_card_layout.addWidget(self.select_epoch_label)

        self.epochs_grid = QGridLayout()
        self.epochs_grid.setObjectName(u"epochs_grid")
        self.epochs_grid.setHorizontalSpacing(12)
        self.epochs_grid.setVerticalSpacing(10)
        self.epoch_length_label = QLabel(self.epochs_card)
        self.epoch_length_label.setObjectName(u"epoch_length_label")

        self.epochs_grid.addWidget(self.epoch_length_label, 0, 0, 1, 1)

        self.epoch_length_lineEdit = QLineEdit(self.epochs_card)
        self.epoch_length_lineEdit.setObjectName(u"epoch_length_lineEdit")
        self.epoch_length_lineEdit.setMaximumSize(QSize(100, 16777215))
        self.epoch_length_lineEdit.setMaxLength(3)

        self.epochs_grid.addWidget(self.epoch_length_lineEdit, 0, 1, 1, 1)

        self.epoch_length_unit_label = QLabel(self.epochs_card)
        self.epoch_length_unit_label.setObjectName(u"epoch_length_unit_label")
        self.epoch_length_unit_label.setProperty(u"variant", u"help")

        self.epochs_grid.addWidget(self.epoch_length_unit_label, 0, 2, 1, 1)

        self.epoch_overlap_label = QLabel(self.epochs_card)
        self.epoch_overlap_label.setObjectName(u"epoch_overlap_label")

        self.epochs_grid.addWidget(self.epoch_overlap_label, 1, 0, 1, 1)

        self.epoch_overlap_lineEdit = QLineEdit(self.epochs_card)
        self.epoch_overlap_lineEdit.setObjectName(u"epoch_overlap_lineEdit")
        self.epoch_overlap_lineEdit.setMaximumSize(QSize(100, 16777215))
        self.epoch_overlap_lineEdit.setMaxLength(3)

        self.epochs_grid.addWidget(self.epoch_overlap_lineEdit, 1, 1, 1, 1)

        self.epoch_overlap_unit_label = QLabel(self.epochs_card)
        self.epoch_overlap_unit_label.setObjectName(u"epoch_overlap_unit_label")
        self.epoch_overlap_unit_label.setProperty(u"variant", u"help")

        self.epochs_grid.addWidget(self.epoch_overlap_unit_label, 1, 2, 1, 1)

        self.epochs_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.epochs_grid.addItem(self.epochs_grid_spacer, 0, 3, 1, 1)


        self.epochs_card_layout.addLayout(self.epochs_grid)

        self.epochs_help_label = QLabel(self.epochs_card)
        self.epochs_help_label.setObjectName(u"epochs_help_label")
        self.epochs_help_label.setFont(font2)
        self.epochs_help_label.setWordWrap(True)
        self.epochs_help_label.setProperty(u"variant", u"help")

        self.epochs_card_layout.addWidget(self.epochs_help_label)

        self.epochs_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.epochs_card_layout.addItem(self.epochs_stretch)


        self.settings_cards_layout.addWidget(self.epochs_card)

        self.statistics_card = QFrame(self.content_widget)
        self.statistics_card.setObjectName(u"statistics_card")
        self.statistics_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.statistics_card.setFrameShadow(QFrame.Shadow.Raised)
        self.statistics_card_layout = QVBoxLayout(self.statistics_card)
        self.statistics_card_layout.setSpacing(10)
        self.statistics_card_layout.setObjectName(u"statistics_card_layout")
        self.statistics_card_layout.setContentsMargins(10, 10, 10, 10)
        self.connectivity_settings_header_label = QLabel(self.statistics_card)
        self.connectivity_settings_header_label.setObjectName(u"connectivity_settings_header_label")
        self.connectivity_settings_header_label.setFont(font1)

        self.statistics_card_layout.addWidget(self.connectivity_settings_header_label)

        self.statistics_grid = QGridLayout()
        self.statistics_grid.setObjectName(u"statistics_grid")
        self.statistics_grid.setHorizontalSpacing(12)
        self.statistics_grid.setVerticalSpacing(10)
        self.num_surr_label = QLabel(self.statistics_card)
        self.num_surr_label.setObjectName(u"num_surr_label")

        self.statistics_grid.addWidget(self.num_surr_label, 0, 0, 1, 1)

        self.num_surr_lineedit = QLineEdit(self.statistics_card)
        self.num_surr_lineedit.setObjectName(u"num_surr_lineedit")
        self.num_surr_lineedit.setMaximumSize(QSize(100, 16777215))
        self.num_surr_lineedit.setMaxLength(3)

        self.statistics_grid.addWidget(self.num_surr_lineedit, 0, 1, 1, 1)

        self.p_value_label = QLabel(self.statistics_card)
        self.p_value_label.setObjectName(u"p_value_label")

        self.statistics_grid.addWidget(self.p_value_label, 1, 0, 1, 1)

        self.p_value_lineedit = QLineEdit(self.statistics_card)
        self.p_value_lineedit.setObjectName(u"p_value_lineedit")
        self.p_value_lineedit.setMaximumSize(QSize(100, 16777215))
        self.p_value_lineedit.setMaxLength(4)

        self.statistics_grid.addWidget(self.p_value_lineedit, 1, 1, 1, 1)

        self.statistics_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.statistics_grid.addItem(self.statistics_grid_spacer, 0, 3, 1, 1)


        self.statistics_card_layout.addLayout(self.statistics_grid)

        self.connectivity_settings_label = QLabel(self.statistics_card)
        self.connectivity_settings_label.setObjectName(u"connectivity_settings_label")
        self.connectivity_settings_label.setProperty(u"variant", u"help")
        self.connectivity_settings_label.setFont(font2)
        self.connectivity_settings_label.setWordWrap(True)

        self.statistics_card_layout.addWidget(self.connectivity_settings_label)

        self.statistics_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.statistics_card_layout.addItem(self.statistics_stretch)


        self.settings_cards_layout.addWidget(self.statistics_card)

        self.settings_cards_layout.setStretch(0, 1)
        self.settings_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.settings_cards_layout)

        self.network_card = QFrame(self.content_widget)
        self.network_card.setObjectName(u"network_card")
        self.network_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.network_card.setFrameShadow(QFrame.Shadow.Raised)
        self.network_card_layout = QVBoxLayout(self.network_card)
        self.network_card_layout.setSpacing(10)
        self.network_card_layout.setObjectName(u"network_card_layout")
        self.network_card_layout.setContentsMargins(10, 10, 10, 10)
        self.network_properties_header_label = QLabel(self.network_card)
        self.network_properties_header_label.setObjectName(u"network_properties_header_label")
        self.network_properties_header_label.setFont(font1)

        self.network_card_layout.addWidget(self.network_properties_header_label)

        self.network_properties_textEdit = QLabel(self.network_card)
        self.network_properties_textEdit.setObjectName(u"network_properties_textEdit")
        self.network_properties_textEdit.setWordWrap(True)
        self.network_properties_textEdit.setProperty(u"variant", u"help")

        self.network_card_layout.addWidget(self.network_properties_textEdit)

        self.select_mode_label = QLabel(self.network_card)
        self.select_mode_label.setObjectName(u"select_mode_label")

        self.network_card_layout.addWidget(self.select_mode_label)

        self.threshold_layout = QVBoxLayout()
        self.threshold_layout.setSpacing(8)
        self.threshold_layout.setObjectName(u"threshold_layout")
        self.threshold_layout_1_layout = QVBoxLayout()
        self.threshold_layout_1_layout.setSpacing(2)
        self.threshold_layout_1_layout.setObjectName(u"threshold_layout_1_layout")
        self.mst_radioButton = QRadioButton(self.network_card)
        self.threshold_buttonGroup = QButtonGroup(ConnectivitySettings)
        self.threshold_buttonGroup.setObjectName(u"threshold_buttonGroup")
        self.threshold_buttonGroup.addButton(self.mst_radioButton)
        self.mst_radioButton.setObjectName(u"mst_radioButton")
        self.mst_radioButton.setChecked(True)

        self.threshold_layout_1_layout.addWidget(self.mst_radioButton)

        self.mst_help_label = QLabel(self.network_card)
        self.mst_help_label.setObjectName(u"mst_help_label")
        self.mst_help_label.setFont(font2)
        self.mst_help_label.setWordWrap(True)
        self.mst_help_label.setIndent(26)
        self.mst_help_label.setProperty(u"variant", u"help")

        self.threshold_layout_1_layout.addWidget(self.mst_help_label)


        self.threshold_layout.addLayout(self.threshold_layout_1_layout)

        self.threshold_layout_line_1 = QFrame(self.network_card)
        self.threshold_layout_line_1.setObjectName(u"threshold_layout_line_1")
        self.threshold_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.threshold_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.threshold_layout.addWidget(self.threshold_layout_line_1)

        self.threshold_layout_2_layout = QVBoxLayout()
        self.threshold_layout_2_layout.setSpacing(2)
        self.threshold_layout_2_layout.setObjectName(u"threshold_layout_2_layout")
        self.custom_threshold_radioButton = QRadioButton(self.network_card)
        self.threshold_buttonGroup.addButton(self.custom_threshold_radioButton)
        self.custom_threshold_radioButton.setObjectName(u"custom_threshold_radioButton")

        self.threshold_layout_2_layout.addWidget(self.custom_threshold_radioButton)

        self.custom_threshold_layout = QVBoxLayout()
        self.custom_threshold_layout.setSpacing(6)
        self.custom_threshold_layout.setObjectName(u"custom_threshold_layout")
        self.custom_threshold_help_label = QLabel(self.network_card)
        self.custom_threshold_help_label.setObjectName(u"custom_threshold_help_label")
        self.custom_threshold_help_label.setFont(font2)
        self.custom_threshold_help_label.setWordWrap(True)
        self.custom_threshold_help_label.setIndent(26)
        self.custom_threshold_help_label.setProperty(u"variant", u"help")

        self.custom_threshold_layout.addWidget(self.custom_threshold_help_label)

        self.threshold_value_layout = QHBoxLayout()
        self.threshold_value_layout.setSpacing(8)
        self.threshold_value_layout.setObjectName(u"threshold_value_layout")
        self.threshold_value_layout.setContentsMargins(26, 0, 0, 0)
        self.threshold_val_label = QLabel(self.network_card)
        self.threshold_val_label.setObjectName(u"threshold_val_label")

        self.threshold_value_layout.addWidget(self.threshold_val_label)

        self.threshold_val_doubleSpinBox = QDoubleSpinBox(self.network_card)
        self.threshold_val_doubleSpinBox.setObjectName(u"threshold_val_doubleSpinBox")
        self.threshold_val_doubleSpinBox.setMaximumSize(QSize(110, 16777215))
        self.threshold_val_doubleSpinBox.setMinimum(0.010000000000000)
        self.threshold_val_doubleSpinBox.setMaximum(0.990000000000000)
        self.threshold_val_doubleSpinBox.setSingleStep(0.010000000000000)
        self.threshold_val_doubleSpinBox.setValue(0.050000000000000)

        self.threshold_value_layout.addWidget(self.threshold_val_doubleSpinBox)

        self.threshold_value_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.threshold_value_layout.addItem(self.threshold_value_spacer)


        self.custom_threshold_layout.addLayout(self.threshold_value_layout)


        self.threshold_layout_2_layout.addLayout(self.custom_threshold_layout)


        self.threshold_layout.addLayout(self.threshold_layout_2_layout)


        self.network_card_layout.addLayout(self.threshold_layout)


        self.content_layout.addWidget(self.network_card)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ConnectivitySettings)

        QMetaObject.connectSlotsByName(ConnectivitySettings)
    # setupUi

    def retranslateUi(self, ConnectivitySettings):
        ConnectivitySettings.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Connectivity Settings", None))
        self.subtitle_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Define the connectivity settings for your study: the connectivity measure, the epochs and the statistical testing.", None))
        self.connectivity_type_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Connectivity type", None))
        self.label_4.setText(QCoreApplication.translate("ConnectivitySettings", u"Choose the connectivity analysis to run. To use more than one measure, run the tool once for each.", None))
        self.wpli_radioButton.setText(QCoreApplication.translate("ConnectivitySettings", u"Weighted phase lag index (wPLI)", None))
        self.wpli_help_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Strength of the phase-lagged coupling, robust to noise and common sources.", None))
        self.dpli_radioButton.setText(QCoreApplication.translate("ConnectivitySettings", u"Directed phase lag index (dPLI)", None))
        self.dpli_help_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Direction of the coupling: which channel leads the other.", None))
        self.aec_radioButton.setText(QCoreApplication.translate("ConnectivitySettings", u"Amplitude envelope correlation (AEC)", None))
        self.aec_help_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Coupling of the amplitude envelopes, with leakage correction.", None))
        self.select_epoch_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Epochs", None))
        self.epoch_length_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Epoch length", None))
        self.epoch_length_lineEdit.setText(QCoreApplication.translate("ConnectivitySettings", u"10", None))
        self.epoch_length_unit_label.setText(QCoreApplication.translate("ConnectivitySettings", u"s", None))
        self.epoch_overlap_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Epoch overlap", None))
        self.epoch_overlap_lineEdit.setText(QCoreApplication.translate("ConnectivitySettings", u"0", None))
        self.epoch_overlap_unit_label.setText(QCoreApplication.translate("ConnectivitySettings", u"s", None))
        self.epochs_help_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Window length and overlap for epoching the data. All measures.", None))
        self.connectivity_settings_header_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Statistical testing", None))
        self.num_surr_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Number of surrogates", None))
        self.num_surr_lineedit.setText(QCoreApplication.translate("ConnectivitySettings", u"20", None))
        self.p_value_label.setText(QCoreApplication.translate("ConnectivitySettings", u"p-value", None))
        self.p_value_lineedit.setText(QCoreApplication.translate("ConnectivitySettings", u"0.05", None))
        self.connectivity_settings_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Removes the connections that could appear by chance: only the statistically significant brain connections are kept. wPLI and dPLI only.", None))
        self.network_properties_header_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Network properties", None))
        self.network_properties_textEdit.setText(QCoreApplication.translate("ConnectivitySettings", u"Graph metrics of the wPLI connectivity matrix: characteristic path length, clustering coefficient, global efficiency, small-worldness, modularity and participation coefficient. wPLI only, with at least 32 channels.", None))
        self.select_mode_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Threshold of the connectivity matrix", None))
        self.mst_radioButton.setText(QCoreApplication.translate("ConnectivitySettings", u"Minimally spanning tree", None))
        self.mst_help_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Finds the smallest threshold that keeps the network fully connected (recommended).", None))
        self.custom_threshold_radioButton.setText(QCoreApplication.translate("ConnectivitySettings", u"Custom threshold", None))
        self.custom_threshold_help_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Keeps this fraction of the strongest connections (0.05: the top 5 %).", None))
        self.threshold_val_label.setText(QCoreApplication.translate("ConnectivitySettings", u"Threshold value", None))
    # retranslateUi

