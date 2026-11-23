# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SpindleDetectorSelStep.ui'
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

class Ui_SpindleDetectorSelStep(object):
    def setupUi(self, SpindleDetectorSelStep):
        if not SpindleDetectorSelStep.objectName():
            SpindleDetectorSelStep.setObjectName(u"SpindleDetectorSelStep")
        SpindleDetectorSelStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(SpindleDetectorSelStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(SpindleDetectorSelStep)
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
        self.subtitle_label.setTextFormat(Qt.TextFormat.RichText)
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setProperty(u"variant", u"help")

        self.header_layout.addWidget(self.subtitle_label)


        self.content_layout.addLayout(self.header_layout)

        self.detection_cards_layout = QHBoxLayout()
        self.detection_cards_layout.setSpacing(16)
        self.detection_cards_layout.setObjectName(u"detection_cards_layout")
        self.duration_card = QFrame(self.content_widget)
        self.duration_card.setObjectName(u"duration_card")
        self.duration_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.duration_card.setFrameShadow(QFrame.Shadow.Raised)
        self.duration_card_layout = QVBoxLayout(self.duration_card)
        self.duration_card_layout.setSpacing(10)
        self.duration_card_layout.setObjectName(u"duration_card_layout")
        self.duration_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_5 = QLabel(self.duration_card)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setBold(True)
        self.label_5.setFont(font1)

        self.duration_card_layout.addWidget(self.label_5)

        self.duration_grid = QGridLayout()
        self.duration_grid.setObjectName(u"duration_grid")
        self.duration_grid.setHorizontalSpacing(12)
        self.duration_grid.setVerticalSpacing(10)
        self.label_3 = QLabel(self.duration_card)
        self.label_3.setObjectName(u"label_3")

        self.duration_grid.addWidget(self.label_3, 0, 0, 1, 1)

        self.min_length_lineEdit = QLineEdit(self.duration_card)
        self.min_length_lineEdit.setObjectName(u"min_length_lineEdit")
        self.min_length_lineEdit.setMaximumSize(QSize(110, 16777215))

        self.duration_grid.addWidget(self.min_length_lineEdit, 0, 1, 1, 1)

        self.min_length_unit_label = QLabel(self.duration_card)
        self.min_length_unit_label.setObjectName(u"min_length_unit_label")
        self.min_length_unit_label.setProperty(u"variant", u"help")

        self.duration_grid.addWidget(self.min_length_unit_label, 0, 2, 1, 1)

        self.label_4 = QLabel(self.duration_card)
        self.label_4.setObjectName(u"label_4")

        self.duration_grid.addWidget(self.label_4, 1, 0, 1, 1)

        self.max_length_lineEdit = QLineEdit(self.duration_card)
        self.max_length_lineEdit.setObjectName(u"max_length_lineEdit")
        self.max_length_lineEdit.setMaximumSize(QSize(110, 16777215))

        self.duration_grid.addWidget(self.max_length_lineEdit, 1, 1, 1, 1)

        self.max_length_unit_label = QLabel(self.duration_card)
        self.max_length_unit_label.setObjectName(u"max_length_unit_label")
        self.max_length_unit_label.setProperty(u"variant", u"help")

        self.duration_grid.addWidget(self.max_length_unit_label, 1, 2, 1, 1)

        self.duration_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.duration_grid.addItem(self.duration_grid_spacer, 0, 3, 1, 1)


        self.duration_card_layout.addLayout(self.duration_grid)

        self.label_8 = QLabel(self.duration_card)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_8.setFont(font2)
        self.label_8.setWordWrap(True)
        self.label_8.setProperty(u"variant", u"help")

        self.duration_card_layout.addWidget(self.label_8)

        self.duration_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.duration_card_layout.addItem(self.duration_stretch)


        self.detection_cards_layout.addWidget(self.duration_card)

        self.stages_card = QFrame(self.content_widget)
        self.stages_card.setObjectName(u"stages_card")
        self.stages_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.stages_card.setFrameShadow(QFrame.Shadow.Raised)
        self.stages_card_layout = QVBoxLayout(self.stages_card)
        self.stages_card_layout.setSpacing(10)
        self.stages_card_layout.setObjectName(u"stages_card_layout")
        self.stages_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_6 = QLabel(self.stages_card)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.stages_card_layout.addWidget(self.label_6)

        self.label_2 = QLabel(self.stages_card)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)
        self.label_2.setProperty(u"variant", u"help")

        self.stages_card_layout.addWidget(self.label_2)

        self.stages_layout = QHBoxLayout()
        self.stages_layout.setSpacing(22)
        self.stages_layout.setObjectName(u"stages_layout")
        self.checkBox_n1 = QCheckBox(self.stages_card)
        self.checkBox_n1.setObjectName(u"checkBox_n1")

        self.stages_layout.addWidget(self.checkBox_n1)

        self.checkBox_n2 = QCheckBox(self.stages_card)
        self.checkBox_n2.setObjectName(u"checkBox_n2")
        self.checkBox_n2.setChecked(True)

        self.stages_layout.addWidget(self.checkBox_n2)

        self.checkBox_n3 = QCheckBox(self.stages_card)
        self.checkBox_n3.setObjectName(u"checkBox_n3")
        self.checkBox_n3.setChecked(False)

        self.stages_layout.addWidget(self.checkBox_n3)

        self.checkBox_r = QCheckBox(self.stages_card)
        self.checkBox_r.setObjectName(u"checkBox_r")

        self.stages_layout.addWidget(self.checkBox_r)

        self.stages_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.stages_layout.addItem(self.stages_spacer)


        self.stages_card_layout.addLayout(self.stages_layout)

        self.stages_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.stages_card_layout.addItem(self.stages_stretch)


        self.detection_cards_layout.addWidget(self.stages_card)

        self.detection_cards_layout.setStretch(0, 1)
        self.detection_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.detection_cards_layout)

        self.cycle_cards_layout = QHBoxLayout()
        self.cycle_cards_layout.setSpacing(16)
        self.cycle_cards_layout.setObjectName(u"cycle_cards_layout")
        self.cycles_card = QFrame(self.content_widget)
        self.cycles_card.setObjectName(u"cycles_card")
        self.cycles_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.cycles_card.setFrameShadow(QFrame.Shadow.Raised)
        self.cycles_card_layout = QVBoxLayout(self.cycles_card)
        self.cycles_card_layout.setSpacing(10)
        self.cycles_card_layout.setObjectName(u"cycles_card_layout")
        self.cycles_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_7 = QLabel(self.cycles_card)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.cycles_card_layout.addWidget(self.label_7)

        self.label_9 = QLabel(self.cycles_card)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)
        self.label_9.setProperty(u"variant", u"help")

        self.cycles_card_layout.addWidget(self.label_9)

        self.cycles_layout = QVBoxLayout()
        self.cycles_layout.setSpacing(8)
        self.cycles_layout.setObjectName(u"cycles_layout")
        self.cycles_layout_1_layout = QVBoxLayout()
        self.cycles_layout_1_layout.setSpacing(2)
        self.cycles_layout_1_layout.setObjectName(u"cycles_layout_1_layout")
        self.checkBox_only_cycles = QCheckBox(self.cycles_card)
        self.checkBox_only_cycles.setObjectName(u"checkBox_only_cycles")
        self.checkBox_only_cycles.setChecked(True)

        self.cycles_layout_1_layout.addWidget(self.checkBox_only_cycles)


        self.cycles_layout.addLayout(self.cycles_layout_1_layout)

        self.cycles_layout_line_1 = QFrame(self.cycles_card)
        self.cycles_layout_line_1.setObjectName(u"cycles_layout_line_1")
        self.cycles_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.cycles_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.cycles_layout.addWidget(self.cycles_layout_line_1)

        self.cycles_layout_2_layout = QVBoxLayout()
        self.cycles_layout_2_layout.setSpacing(2)
        self.cycles_layout_2_layout.setObjectName(u"cycles_layout_2_layout")
        self.checkBox_excl_remp = QCheckBox(self.cycles_card)
        self.checkBox_excl_remp.setObjectName(u"checkBox_excl_remp")
        self.checkBox_excl_remp.setChecked(True)

        self.cycles_layout_2_layout.addWidget(self.checkBox_excl_remp)

        self.excl_remp_help_label = QLabel(self.cycles_card)
        self.excl_remp_help_label.setObjectName(u"excl_remp_help_label")
        self.excl_remp_help_label.setFont(font2)
        self.excl_remp_help_label.setWordWrap(True)
        self.excl_remp_help_label.setIndent(26)
        self.excl_remp_help_label.setProperty(u"variant", u"help")

        self.cycles_layout_2_layout.addWidget(self.excl_remp_help_label)


        self.cycles_layout.addLayout(self.cycles_layout_2_layout)

        self.cycles_layout_line_2 = QFrame(self.cycles_card)
        self.cycles_layout_line_2.setObjectName(u"cycles_layout_line_2")
        self.cycles_layout_line_2.setFrameShape(QFrame.Shape.HLine)
        self.cycles_layout_line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.cycles_layout.addWidget(self.cycles_layout_line_2)

        self.cycles_layout_3_layout = QVBoxLayout()
        self.cycles_layout_3_layout.setSpacing(2)
        self.cycles_layout_3_layout.setObjectName(u"cycles_layout_3_layout")
        self.checkBox_excl_nremp = QCheckBox(self.cycles_card)
        self.checkBox_excl_nremp.setObjectName(u"checkBox_excl_nremp")
        self.checkBox_excl_nremp.setEnabled(False)

        self.cycles_layout_3_layout.addWidget(self.checkBox_excl_nremp)


        self.cycles_layout.addLayout(self.cycles_layout_3_layout)


        self.cycles_card_layout.addLayout(self.cycles_layout)

        self.cycles_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.cycles_card_layout.addItem(self.cycles_stretch)


        self.cycle_cards_layout.addWidget(self.cycles_card)

        self.detection_card = QFrame(self.content_widget)
        self.detection_card.setObjectName(u"detection_card")
        self.detection_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.detection_card.setFrameShadow(QFrame.Shadow.Raised)
        self.detection_card_layout = QVBoxLayout(self.detection_card)
        self.detection_card_layout.setSpacing(10)
        self.detection_card_layout.setObjectName(u"detection_card_layout")
        self.detection_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_10 = QLabel(self.detection_card)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.detection_card_layout.addWidget(self.label_10)

        self.detection_layout = QVBoxLayout()
        self.detection_layout.setSpacing(8)
        self.detection_layout.setObjectName(u"detection_layout")
        self.detection_layout_1_layout = QVBoxLayout()
        self.detection_layout_1_layout.setSpacing(2)
        self.detection_layout_1_layout.setObjectName(u"detection_layout_1_layout")
        self.radioButton_detect_spindle = QRadioButton(self.detection_card)
        self.radioButton_detect_spindle.setObjectName(u"radioButton_detect_spindle")
        self.radioButton_detect_spindle.setChecked(True)

        self.detection_layout_1_layout.addWidget(self.radioButton_detect_spindle)


        self.detection_layout.addLayout(self.detection_layout_1_layout)

        self.detection_layout_line_1 = QFrame(self.detection_card)
        self.detection_layout_line_1.setObjectName(u"detection_layout_line_1")
        self.detection_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.detection_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.detection_layout.addWidget(self.detection_layout_line_1)

        self.detection_layout_2_layout = QVBoxLayout()
        self.detection_layout_2_layout.setSpacing(2)
        self.detection_layout_2_layout.setObjectName(u"detection_layout_2_layout")
        self.radioButto_analyse_spindle = QRadioButton(self.detection_card)
        self.radioButto_analyse_spindle.setObjectName(u"radioButto_analyse_spindle")

        self.detection_layout_2_layout.addWidget(self.radioButto_analyse_spindle)

        self.analyse_help_label = QLabel(self.detection_card)
        self.analyse_help_label.setObjectName(u"analyse_help_label")
        self.analyse_help_label.setFont(font2)
        self.analyse_help_label.setWordWrap(True)
        self.analyse_help_label.setIndent(26)
        self.analyse_help_label.setProperty(u"variant", u"help")

        self.detection_layout_2_layout.addWidget(self.analyse_help_label)


        self.detection_layout.addLayout(self.detection_layout_2_layout)


        self.detection_card_layout.addLayout(self.detection_layout)

        self.label_11 = QLabel(self.detection_card)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setTextFormat(Qt.TextFormat.RichText)
        self.label_11.setWordWrap(True)
        self.label_11.setProperty(u"variant", u"help")

        self.detection_card_layout.addWidget(self.label_11)

        self.detection_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.detection_card_layout.addItem(self.detection_stretch)


        self.cycle_cards_layout.addWidget(self.detection_card)

        self.cycle_cards_layout.setStretch(0, 1)
        self.cycle_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.cycle_cards_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SpindleDetectorSelStep)
        self.checkBox_only_cycles.stateChanged.connect(SpindleDetectorSelStep.detect_in_cycle_only_slot)
        self.radioButto_analyse_spindle.clicked.connect(SpindleDetectorSelStep.radio_button_slot)
        self.radioButton_detect_spindle.clicked.connect(SpindleDetectorSelStep.radio_button_slot)

        QMetaObject.connectSlotsByName(SpindleDetectorSelStep)
    # setupUi

    def retranslateUi(self, SpindleDetectorSelStep):
        SpindleDetectorSelStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Detection Settings", None))
        self.subtitle_label.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Define which spindles are kept and in which sleep stages and cycles they are detected. The threshold of the detector is in <b>Martin</b>, under Algorithm Settings in the left panel.", None))
        self.label_5.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Spindle duration", None))
        self.label_3.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Minimum duration", None))
        self.min_length_lineEdit.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"0.3", None))
        self.min_length_unit_label.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"s", None))
        self.label_4.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Maximum duration", None))
        self.max_length_lineEdit.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"2.5", None))
        self.max_length_unit_label.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"s", None))
        self.label_8.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Shorter and longer spindles are discarded.", None))
        self.label_6.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Sleep stages", None))
        self.label_2.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Select the stages in which spindles are detected.", None))
        self.checkBox_n1.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"N1", None))
        self.checkBox_n2.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"N2", None))
        self.checkBox_n3.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"N3", None))
        self.checkBox_r.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"R", None))
        self.label_7.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Sleep cycles", None))
        self.label_9.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Optional. Define in which sleep cycles (or periods) spindles are detected.", None))
        self.checkBox_only_cycles.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Detection in sleep cycles only", None))
        self.checkBox_excl_remp.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Exclude REM periods", None))
        self.excl_remp_help_label.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Not available with the stage R.", None))
        self.checkBox_excl_nremp.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Exclude NREM periods", None))
        self.label_10.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Detections and/or analyses", None))
        self.radioButton_detect_spindle.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Detect spindles", None))
        self.radioButto_analyse_spindle.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Analyze the spindles already detected", None))
        self.analyse_help_label.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Does not detect spindles: analyzes the spindles previously detected and saved in the accessory file.", None))
        self.label_11.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"The event group and name defined in <b>Martin</b> (left panel) are used.", None))
    # retranslateUi

