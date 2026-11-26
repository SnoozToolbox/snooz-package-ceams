# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DetectorsStep.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_DetectorsStep(object):
    def setupUi(self, DetectorsStep):
        if not DetectorsStep.objectName():
            DetectorsStep.setObjectName(u"DetectorsStep")
        DetectorsStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(DetectorsStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(DetectorsStep)
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

        self.events_card = QFrame(self.content_widget)
        self.events_card.setObjectName(u"events_card")
        self.events_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.events_card.setFrameShadow(QFrame.Shadow.Raised)
        self.events_card_layout = QVBoxLayout(self.events_card)
        self.events_card_layout.setSpacing(10)
        self.events_card_layout.setObjectName(u"events_card_layout")
        self.events_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_3 = QLabel(self.events_card)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.events_card_layout.addWidget(self.label_3)

        self.events_layout = QVBoxLayout()
        self.events_layout.setSpacing(8)
        self.events_layout.setObjectName(u"events_layout")
        self.events_layout_1_layout = QVBoxLayout()
        self.events_layout_1_layout.setSpacing(2)
        self.events_layout_1_layout.setObjectName(u"events_layout_1_layout")
        self.common_radioButton = QRadioButton(self.events_card)
        self.buttonGroup = QButtonGroup(DetectorsStep)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.common_radioButton)
        self.common_radioButton.setObjectName(u"common_radioButton")
        self.common_radioButton.setMinimumSize(QSize(250, 0))
        self.common_radioButton.setMaximumSize(QSize(250, 16777215))
        self.common_radioButton.setChecked(True)

        self.events_layout_1_layout.addWidget(self.common_radioButton)

        self.common_fields_layout = QHBoxLayout()
        self.common_fields_layout.setObjectName(u"common_fields_layout")
        self.common_fields_layout.setContentsMargins(26, 0, 0, 0)
        self.common_grid = QGridLayout()
        self.common_grid.setObjectName(u"common_grid")
        self.common_grid.setHorizontalSpacing(12)
        self.common_grid.setVerticalSpacing(10)
        self.label_4 = QLabel(self.events_card)
        self.label_4.setObjectName(u"label_4")

        self.common_grid.addWidget(self.label_4, 0, 0, 1, 1)

        self.unique_group_lineEdit = QLineEdit(self.events_card)
        self.unique_group_lineEdit.setObjectName(u"unique_group_lineEdit")
        self.unique_group_lineEdit.setMinimumSize(QSize(150, 0))
        self.unique_group_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.unique_group_lineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.common_grid.addWidget(self.unique_group_lineEdit, 0, 1, 1, 1)

        self.label_5 = QLabel(self.events_card)
        self.label_5.setObjectName(u"label_5")

        self.common_grid.addWidget(self.label_5, 1, 0, 1, 1)

        self.unique_name_lineEdit = QLineEdit(self.events_card)
        self.unique_name_lineEdit.setObjectName(u"unique_name_lineEdit")
        self.unique_name_lineEdit.setMinimumSize(QSize(150, 0))
        self.unique_name_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.common_grid.addWidget(self.unique_name_lineEdit, 1, 1, 1, 1)

        self.common_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.common_grid.addItem(self.common_grid_spacer, 0, 3, 1, 1)


        self.common_fields_layout.addLayout(self.common_grid)


        self.events_layout_1_layout.addLayout(self.common_fields_layout)


        self.events_layout.addLayout(self.events_layout_1_layout)

        self.events_layout_line_1 = QFrame(self.events_card)
        self.events_layout_line_1.setObjectName(u"events_layout_line_1")
        self.events_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.events_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.events_layout.addWidget(self.events_layout_line_1)

        self.events_layout_2_layout = QVBoxLayout()
        self.events_layout_2_layout.setSpacing(2)
        self.events_layout_2_layout.setObjectName(u"events_layout_2_layout")
        self.specific_radioButton = QRadioButton(self.events_card)
        self.buttonGroup.addButton(self.specific_radioButton)
        self.specific_radioButton.setObjectName(u"specific_radioButton")
        self.specific_radioButton.setMinimumSize(QSize(250, 0))
        self.specific_radioButton.setMaximumSize(QSize(250, 16777215))

        self.events_layout_2_layout.addWidget(self.specific_radioButton)

        self.specific_name_label = QLabel(self.events_card)
        self.specific_name_label.setObjectName(u"specific_name_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.specific_name_label.setFont(font2)
        self.specific_name_label.setWordWrap(True)
        self.specific_name_label.setIndent(26)
        self.specific_name_label.setProperty(u"variant", u"help")

        self.events_layout_2_layout.addWidget(self.specific_name_label)


        self.events_layout.addLayout(self.events_layout_2_layout)


        self.events_card_layout.addLayout(self.events_layout)

        self.label_7 = QLabel(self.events_card)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setWordWrap(True)
        self.label_7.setProperty(u"variant", u"help")

        self.events_card_layout.addWidget(self.label_7)


        self.content_layout.addWidget(self.events_card)

        self.detectors_card = QFrame(self.content_widget)
        self.detectors_card.setObjectName(u"detectors_card")
        self.detectors_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.detectors_card.setFrameShadow(QFrame.Shadow.Raised)
        self.detectors_card_layout = QVBoxLayout(self.detectors_card)
        self.detectors_card_layout.setSpacing(10)
        self.detectors_card_layout.setObjectName(u"detectors_card_layout")
        self.detectors_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_6 = QLabel(self.detectors_card)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.detectors_card_layout.addWidget(self.label_6)

        self.label_2 = QLabel(self.detectors_card)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)
        self.label_2.setProperty(u"variant", u"help")

        self.detectors_card_layout.addWidget(self.label_2)

        self.detectors_layout = QVBoxLayout()
        self.detectors_layout.setSpacing(8)
        self.detectors_layout.setObjectName(u"detectors_layout")
        self.detectors_layout_1_layout = QVBoxLayout()
        self.detectors_layout_1_layout.setSpacing(2)
        self.detectors_layout_1_layout.setObjectName(u"detectors_layout_1_layout")
        self.flatline_checkBox = QCheckBox(self.detectors_card)
        self.flatline_checkBox.setObjectName(u"flatline_checkBox")
        self.flatline_checkBox.setChecked(False)

        self.detectors_layout_1_layout.addWidget(self.flatline_checkBox)

        self.flatline_checkBox_help_label = QLabel(self.detectors_card)
        self.flatline_checkBox_help_label.setObjectName(u"flatline_checkBox_help_label")
        self.flatline_checkBox_help_label.setFont(font2)
        self.flatline_checkBox_help_label.setWordWrap(True)
        self.flatline_checkBox_help_label.setIndent(26)
        self.flatline_checkBox_help_label.setProperty(u"variant", u"help")

        self.detectors_layout_1_layout.addWidget(self.flatline_checkBox_help_label)


        self.detectors_layout.addLayout(self.detectors_layout_1_layout)

        self.detectors_layout_line_1 = QFrame(self.detectors_card)
        self.detectors_layout_line_1.setObjectName(u"detectors_layout_line_1")
        self.detectors_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.detectors_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.detectors_layout.addWidget(self.detectors_layout_line_1)

        self.detectors_layout_2_layout = QVBoxLayout()
        self.detectors_layout_2_layout.setSpacing(2)
        self.detectors_layout_2_layout.setObjectName(u"detectors_layout_2_layout")
        self.highfreq_checkBox = QCheckBox(self.detectors_card)
        self.highfreq_checkBox.setObjectName(u"highfreq_checkBox")
        self.highfreq_checkBox.setChecked(True)

        self.detectors_layout_2_layout.addWidget(self.highfreq_checkBox)

        self.highfreq_checkBox_help_label = QLabel(self.detectors_card)
        self.highfreq_checkBox_help_label.setObjectName(u"highfreq_checkBox_help_label")
        self.highfreq_checkBox_help_label.setFont(font2)
        self.highfreq_checkBox_help_label.setWordWrap(True)
        self.highfreq_checkBox_help_label.setIndent(26)
        self.highfreq_checkBox_help_label.setProperty(u"variant", u"help")

        self.detectors_layout_2_layout.addWidget(self.highfreq_checkBox_help_label)


        self.detectors_layout.addLayout(self.detectors_layout_2_layout)

        self.detectors_layout_line_2 = QFrame(self.detectors_card)
        self.detectors_layout_line_2.setObjectName(u"detectors_layout_line_2")
        self.detectors_layout_line_2.setFrameShape(QFrame.Shape.HLine)
        self.detectors_layout_line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.detectors_layout.addWidget(self.detectors_layout_line_2)

        self.detectors_layout_3_layout = QVBoxLayout()
        self.detectors_layout_3_layout.setSpacing(2)
        self.detectors_layout_3_layout.setObjectName(u"detectors_layout_3_layout")
        self.persistent_checkBox = QCheckBox(self.detectors_card)
        self.persistent_checkBox.setObjectName(u"persistent_checkBox")
        self.persistent_checkBox.setChecked(True)

        self.detectors_layout_3_layout.addWidget(self.persistent_checkBox)

        self.persistent_checkBox_help_label = QLabel(self.detectors_card)
        self.persistent_checkBox_help_label.setObjectName(u"persistent_checkBox_help_label")
        self.persistent_checkBox_help_label.setFont(font2)
        self.persistent_checkBox_help_label.setWordWrap(True)
        self.persistent_checkBox_help_label.setIndent(26)
        self.persistent_checkBox_help_label.setProperty(u"variant", u"help")

        self.detectors_layout_3_layout.addWidget(self.persistent_checkBox_help_label)


        self.detectors_layout.addLayout(self.detectors_layout_3_layout)

        self.detectors_layout_line_3 = QFrame(self.detectors_card)
        self.detectors_layout_line_3.setObjectName(u"detectors_layout_line_3")
        self.detectors_layout_line_3.setFrameShape(QFrame.Shape.HLine)
        self.detectors_layout_line_3.setFrameShadow(QFrame.Shadow.Plain)

        self.detectors_layout.addWidget(self.detectors_layout_line_3)

        self.detectors_layout_4_layout = QVBoxLayout()
        self.detectors_layout_4_layout.setSpacing(2)
        self.detectors_layout_4_layout.setObjectName(u"detectors_layout_4_layout")
        self.powerline_checkBox = QCheckBox(self.detectors_card)
        self.powerline_checkBox.setObjectName(u"powerline_checkBox")
        self.powerline_checkBox.setChecked(True)

        self.detectors_layout_4_layout.addWidget(self.powerline_checkBox)

        self.powerline_checkBox_help_layout = QVBoxLayout()
        self.powerline_checkBox_help_layout.setSpacing(2)
        self.powerline_checkBox_help_layout.setObjectName(u"powerline_checkBox_help_layout")
        self.powerline_checkBox_help_label = QLabel(self.detectors_card)
        self.powerline_checkBox_help_label.setObjectName(u"powerline_checkBox_help_label")
        self.powerline_checkBox_help_label.setFont(font2)
        self.powerline_checkBox_help_label.setWordWrap(True)
        self.powerline_checkBox_help_label.setIndent(26)
        self.powerline_checkBox_help_label.setProperty(u"variant", u"help")

        self.powerline_checkBox_help_layout.addWidget(self.powerline_checkBox_help_label)

        self.powerline_frequency_layout = QHBoxLayout()
        self.powerline_frequency_layout.setSpacing(22)
        self.powerline_frequency_layout.setObjectName(u"powerline_frequency_layout")
        self.powerline_frequency_layout.setContentsMargins(26, 4, 0, 0)
        self.radioButton_60Hz = QRadioButton(self.detectors_card)
        self.buttonGroup_2 = QButtonGroup(DetectorsStep)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_60Hz)
        self.radioButton_60Hz.setObjectName(u"radioButton_60Hz")
        self.radioButton_60Hz.setMaximumSize(QSize(150, 16777215))
        self.radioButton_60Hz.setChecked(True)

        self.powerline_frequency_layout.addWidget(self.radioButton_60Hz)

        self.radioButton_50Hz = QRadioButton(self.detectors_card)
        self.buttonGroup_2.addButton(self.radioButton_50Hz)
        self.radioButton_50Hz.setObjectName(u"radioButton_50Hz")
        self.radioButton_50Hz.setMaximumSize(QSize(150, 16777215))

        self.powerline_frequency_layout.addWidget(self.radioButton_50Hz)

        self.powerline_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.powerline_frequency_layout.addItem(self.powerline_spacer)


        self.powerline_checkBox_help_layout.addLayout(self.powerline_frequency_layout)

        self.label = QLabel(self.detectors_card)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setWordWrap(True)
        self.label.setIndent(26)
        self.label.setProperty(u"variant", u"help")

        self.powerline_checkBox_help_layout.addWidget(self.label)


        self.detectors_layout_4_layout.addLayout(self.powerline_checkBox_help_layout)


        self.detectors_layout.addLayout(self.detectors_layout_4_layout)

        self.detectors_layout_line_4 = QFrame(self.detectors_card)
        self.detectors_layout_line_4.setObjectName(u"detectors_layout_line_4")
        self.detectors_layout_line_4.setFrameShape(QFrame.Shape.HLine)
        self.detectors_layout_line_4.setFrameShadow(QFrame.Shadow.Plain)

        self.detectors_layout.addWidget(self.detectors_layout_line_4)

        self.detectors_layout_5_layout = QVBoxLayout()
        self.detectors_layout_5_layout.setSpacing(2)
        self.detectors_layout_5_layout.setObjectName(u"detectors_layout_5_layout")
        self.bslvar_checkBox = QCheckBox(self.detectors_card)
        self.bslvar_checkBox.setObjectName(u"bslvar_checkBox")
        self.bslvar_checkBox.setChecked(True)

        self.detectors_layout_5_layout.addWidget(self.bslvar_checkBox)

        self.bslvar_checkBox_help_label = QLabel(self.detectors_card)
        self.bslvar_checkBox_help_label.setObjectName(u"bslvar_checkBox_help_label")
        self.bslvar_checkBox_help_label.setFont(font2)
        self.bslvar_checkBox_help_label.setWordWrap(True)
        self.bslvar_checkBox_help_label.setIndent(26)
        self.bslvar_checkBox_help_label.setProperty(u"variant", u"help")

        self.detectors_layout_5_layout.addWidget(self.bslvar_checkBox_help_label)


        self.detectors_layout.addLayout(self.detectors_layout_5_layout)

        self.detectors_layout_line_5 = QFrame(self.detectors_card)
        self.detectors_layout_line_5.setObjectName(u"detectors_layout_line_5")
        self.detectors_layout_line_5.setFrameShape(QFrame.Shape.HLine)
        self.detectors_layout_line_5.setFrameShadow(QFrame.Shadow.Plain)

        self.detectors_layout.addWidget(self.detectors_layout_line_5)

        self.detectors_layout_6_layout = QVBoxLayout()
        self.detectors_layout_6_layout.setSpacing(2)
        self.detectors_layout_6_layout.setObjectName(u"detectors_layout_6_layout")
        self.muscle_checkBox = QCheckBox(self.detectors_card)
        self.muscle_checkBox.setObjectName(u"muscle_checkBox")
        self.muscle_checkBox.setChecked(True)

        self.detectors_layout_6_layout.addWidget(self.muscle_checkBox)

        self.muscle_checkBox_help_label = QLabel(self.detectors_card)
        self.muscle_checkBox_help_label.setObjectName(u"muscle_checkBox_help_label")
        self.muscle_checkBox_help_label.setFont(font2)
        self.muscle_checkBox_help_label.setWordWrap(True)
        self.muscle_checkBox_help_label.setIndent(26)
        self.muscle_checkBox_help_label.setProperty(u"variant", u"help")

        self.detectors_layout_6_layout.addWidget(self.muscle_checkBox_help_label)


        self.detectors_layout.addLayout(self.detectors_layout_6_layout)


        self.detectors_card_layout.addLayout(self.detectors_layout)


        self.content_layout.addWidget(self.detectors_card)

        self.about_tuning_layout = QVBoxLayout()
        self.about_tuning_layout.setSpacing(6)
        self.about_tuning_layout.setObjectName(u"about_tuning_layout")
        self.about_tuning_title_label = QLabel(self.content_widget)
        self.about_tuning_title_label.setObjectName(u"about_tuning_title_label")
        self.about_tuning_title_label.setFont(font1)

        self.about_tuning_layout.addWidget(self.about_tuning_title_label)

        self.about_tuning_label = QLabel(self.content_widget)
        self.about_tuning_label.setObjectName(u"about_tuning_label")
        self.about_tuning_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_tuning_label.setWordWrap(True)
        self.about_tuning_label.setProperty(u"variant", u"help")

        self.about_tuning_layout.addWidget(self.about_tuning_label)


        self.content_layout.addLayout(self.about_tuning_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(DetectorsStep)
        self.radioButton_50Hz.clicked.connect(DetectorsStep.update_settings_slot)
        self.radioButton_60Hz.clicked.connect(DetectorsStep.update_settings_slot)
        self.powerline_checkBox.clicked.connect(DetectorsStep.update_settings_slot)
        self.common_radioButton.clicked.connect(DetectorsStep.update_event_label_slot)
        self.specific_radioButton.clicked.connect(DetectorsStep.update_event_label_slot)
        self.unique_group_lineEdit.editingFinished.connect(DetectorsStep.update_event_label_slot)
        self.unique_name_lineEdit.editingFinished.connect(DetectorsStep.update_event_label_slot)

        QMetaObject.connectSlotsByName(DetectorsStep)
    # setupUi

    def retranslateUi(self, DetectorsStep):
        DetectorsStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("DetectorsStep", u"Detectors Settings", None))
        self.subtitle_label.setText(QCoreApplication.translate("DetectorsStep", u"Choose the group and name of the artifact events, then check the detectors to run. The thresholds of each detector are in its own page, under \"Detectors Settings\" in the left panel.", None))
        self.label_3.setText(QCoreApplication.translate("DetectorsStep", u"Artifact events", None))
        self.common_radioButton.setText(QCoreApplication.translate("DetectorsStep", u"Common to all the detectors", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("DetectorsStep", u"The group of the artifact events of all the detectors in the accessory file. Use letters, digits, spaces, hyphens or underscores (64 at most).", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("DetectorsStep", u"Group", None))
        self.unique_group_lineEdit.setText(QCoreApplication.translate("DetectorsStep", u"art_snooz_NREM_set1", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("DetectorsStep", u"The name of the artifact events of all the detectors in the accessory file. Use letters, digits, spaces, hyphens or underscores (64 at most).", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("DetectorsStep", u"Name", None))
        self.unique_name_lineEdit.setText(QCoreApplication.translate("DetectorsStep", u"art_snooz_NREM_set1", None))
        self.specific_radioButton.setText(QCoreApplication.translate("DetectorsStep", u"Specific to each detector", None))
        self.specific_name_label.setText(QCoreApplication.translate("DetectorsStep", u"The group and name are defined in the page of each detector.", None))
        self.label_7.setText(QCoreApplication.translate("DetectorsStep", u"The default group and name give the set of default thresholds and the selected stages, for example art_snooz_set1_NREM. Edit them when you change the thresholds.", None))
        self.label_6.setText(QCoreApplication.translate("DetectorsStep", u"Detectors", None))
        self.label_2.setText(QCoreApplication.translate("DetectorsStep", u"Check the detectors to run.", None))
        self.flatline_checkBox.setText(QCoreApplication.translate("DetectorsStep", u"Flatline", None))
        self.flatline_checkBox_help_label.setText(QCoreApplication.translate("DetectorsStep", u"Segments of low power, where the signal is nearly flat.", None))
        self.highfreq_checkBox.setText(QCoreApplication.translate("DetectorsStep", u"High frequency burst", None))
        self.highfreq_checkBox_help_label.setText(QCoreApplication.translate("DetectorsStep", u"Short bursts of power above 25\u00a0Hz.", None))
        self.persistent_checkBox.setText(QCoreApplication.translate("DetectorsStep", u"Persistent noise", None))
        self.persistent_checkBox_help_label.setText(QCoreApplication.translate("DetectorsStep", u"Lasting noise above 25\u00a0Hz.", None))
        self.powerline_checkBox.setText(QCoreApplication.translate("DetectorsStep", u"Power line contamination", None))
        self.powerline_checkBox_help_label.setText(QCoreApplication.translate("DetectorsStep", u"Power at 50 or 60\u00a0Hz.", None))
        self.radioButton_60Hz.setText(QCoreApplication.translate("DetectorsStep", u"60 Hz", None))
        self.radioButton_50Hz.setText(QCoreApplication.translate("DetectorsStep", u"50 Hz", None))
        self.label.setText(QCoreApplication.translate("DetectorsStep", u"Turned off when a notch filter is applied in \"Filter EEG signals\".", None))
        self.bslvar_checkBox.setText(QCoreApplication.translate("DetectorsStep", u"Baseline variation", None))
        self.bslvar_checkBox_help_label.setText(QCoreApplication.translate("DetectorsStep", u"Power below 0.4\u00a0Hz, from breathing or sweat.", None))
        self.muscle_checkBox.setText(QCoreApplication.translate("DetectorsStep", u"Muscle artifact", None))
        self.muscle_checkBox_help_label.setText(QCoreApplication.translate("DetectorsStep", u"Bursts of activity between 20.25 and 32\u00a0Hz.", None))
        self.about_tuning_title_label.setText(QCoreApplication.translate("DetectorsStep", u"About the thresholds", None))
        self.about_tuning_label.setText(QCoreApplication.translate("DetectorsStep", u"<b>To detect fewer artifacts</b> (more precise)<br/>\u2022 Flatline. Lower the threshold.<br/>\u2022 The other detectors. Raise the thresholds. Start with the fixed thresholds, for example from 4 to 5 \u00d7 SD.<br/><br/><b>To detect more artifacts</b> (more sensitive)<br/>\u2022 Flatline. Raise the threshold.<br/>\u2022 The other detectors. Lower the thresholds. Start with the fixed thresholds, for example from 4 to 3 \u00d7 SD. Keep the baseline variation at 3.5 \u00d7 SD or more.", None))
    # retranslateUi

