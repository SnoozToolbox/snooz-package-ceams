# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DetectorStep.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_DetectorStep(object):
    def setupUi(self, DetectorStep):
        if not DetectorStep.objectName():
            DetectorStep.setObjectName(u"DetectorStep")
        DetectorStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(DetectorStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(DetectorStep)
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

        self.events_row = QHBoxLayout()
        self.events_row.setSpacing(16)
        self.events_row.setObjectName(u"events_row")
        self.events_card = QFrame(self.content_widget)
        self.events_card.setObjectName(u"events_card")
        self.events_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.events_card.setFrameShadow(QFrame.Shadow.Raised)
        self.events_card_layout = QVBoxLayout(self.events_card)
        self.events_card_layout.setSpacing(10)
        self.events_card_layout.setObjectName(u"events_card_layout")
        self.events_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_19 = QLabel(self.events_card)
        self.label_19.setObjectName(u"label_19")
        font1 = QFont()
        font1.setBold(True)
        self.label_19.setFont(font1)

        self.events_card_layout.addWidget(self.label_19)

        self.events_grid = QGridLayout()
        self.events_grid.setObjectName(u"events_grid")
        self.events_grid.setHorizontalSpacing(12)
        self.events_grid.setVerticalSpacing(10)
        self.label_15 = QLabel(self.events_card)
        self.label_15.setObjectName(u"label_15")

        self.events_grid.addWidget(self.label_15, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.events_card)
        self.lineEdit.setObjectName(u"lineEdit")

        self.events_grid.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_9 = QLabel(self.events_card)
        self.label_9.setObjectName(u"label_9")

        self.events_grid.addWidget(self.label_9, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.events_card)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.events_grid.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.events_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.events_grid.addItem(self.events_grid_spacer, 0, 3, 1, 1)


        self.events_card_layout.addLayout(self.events_grid)

        self.label_20 = QLabel(self.events_card)
        self.label_20.setObjectName(u"label_20")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_20.setFont(font2)
        self.label_20.setWordWrap(True)
        self.label_20.setProperty(u"variant", u"help")

        self.events_card_layout.addWidget(self.label_20)

        self.events_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.events_card_layout.addItem(self.events_stretch)


        self.events_row.addWidget(self.events_card)

        self.events_row_gap = QSpacerItem(16, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.events_row.addItem(self.events_row_gap)

        self.events_row_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.events_row.addItem(self.events_row_spacer)

        self.events_row.setStretch(0, 1)
        self.events_row.setStretch(2, 1)

        self.content_layout.addLayout(self.events_row)

        self.criteria_card = QFrame(self.content_widget)
        self.criteria_card.setObjectName(u"criteria_card")
        self.criteria_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.criteria_card.setFrameShadow(QFrame.Shadow.Raised)
        self.criteria_card_layout = QVBoxLayout(self.criteria_card)
        self.criteria_card_layout.setSpacing(10)
        self.criteria_card_layout.setObjectName(u"criteria_card_layout")
        self.criteria_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.criteria_card)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.criteria_card_layout.addWidget(self.label)

        self.criteria_grid = QGridLayout()
        self.criteria_grid.setObjectName(u"criteria_grid")
        self.criteria_grid.setHorizontalSpacing(12)
        self.criteria_grid.setVerticalSpacing(10)
        self.label_8 = QLabel(self.criteria_card)
        self.label_8.setObjectName(u"label_8")

        self.criteria_grid.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_18 = QLabel(self.criteria_card)
        self.label_18.setObjectName(u"label_18")

        self.criteria_grid.addWidget(self.label_18, 0, 1, 1, 1)

        self.spinBox_2 = QSpinBox(self.criteria_card)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximumSize(QSize(110, 16777215))
        self.spinBox_2.setMaximum(10000)

        self.criteria_grid.addWidget(self.spinBox_2, 0, 2, 1, 1)

        self.label_17 = QLabel(self.criteria_card)
        self.label_17.setObjectName(u"label_17")

        self.criteria_grid.addWidget(self.label_17, 0, 3, 1, 1)

        self.spinBox = QSpinBox(self.criteria_card)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(110, 16777215))
        self.spinBox.setMaximum(10000)

        self.criteria_grid.addWidget(self.spinBox, 0, 4, 1, 1)

        self.amplitude_unit_label = QLabel(self.criteria_card)
        self.amplitude_unit_label.setObjectName(u"amplitude_unit_label")
        self.amplitude_unit_label.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.amplitude_unit_label, 0, 5, 1, 1)

        self.label_2 = QLabel(self.criteria_card)
        self.label_2.setObjectName(u"label_2")

        self.criteria_grid.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_11 = QLabel(self.criteria_card)
        self.label_11.setObjectName(u"label_11")

        self.criteria_grid.addWidget(self.label_11, 1, 1, 1, 1)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.criteria_card)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setMaximumSize(QSize(110, 16777215))
        self.doubleSpinBox_6.setSingleStep(0.010000000000000)

        self.criteria_grid.addWidget(self.doubleSpinBox_6, 1, 2, 1, 1)

        self.label_12 = QLabel(self.criteria_card)
        self.label_12.setObjectName(u"label_12")

        self.criteria_grid.addWidget(self.label_12, 1, 3, 1, 1)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.criteria_card)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setMaximumSize(QSize(110, 16777215))
        self.doubleSpinBox_5.setSingleStep(0.010000000000000)

        self.criteria_grid.addWidget(self.doubleSpinBox_5, 1, 4, 1, 1)

        self.duration_unit_label = QLabel(self.criteria_card)
        self.duration_unit_label.setObjectName(u"duration_unit_label")
        self.duration_unit_label.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.duration_unit_label, 1, 5, 1, 1)

        self.label_3 = QLabel(self.criteria_card)
        self.label_3.setObjectName(u"label_3")

        self.criteria_grid.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_13 = QLabel(self.criteria_card)
        self.label_13.setObjectName(u"label_13")

        self.criteria_grid.addWidget(self.label_13, 2, 1, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.criteria_card)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMaximumSize(QSize(110, 16777215))
        self.doubleSpinBox.setSingleStep(0.010000000000000)

        self.criteria_grid.addWidget(self.doubleSpinBox, 2, 2, 1, 1)

        self.label_14 = QLabel(self.criteria_card)
        self.label_14.setObjectName(u"label_14")

        self.criteria_grid.addWidget(self.label_14, 2, 3, 1, 1)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.criteria_card)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setMaximumSize(QSize(110, 16777215))
        self.doubleSpinBox_3.setSingleStep(0.010000000000000)

        self.criteria_grid.addWidget(self.doubleSpinBox_3, 2, 4, 1, 1)

        self.frequency_unit_label = QLabel(self.criteria_card)
        self.frequency_unit_label.setObjectName(u"frequency_unit_label")
        self.frequency_unit_label.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.frequency_unit_label, 2, 5, 1, 1)

        self.label_4 = QLabel(self.criteria_card)
        self.label_4.setObjectName(u"label_4")

        self.criteria_grid.addWidget(self.label_4, 3, 0, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.criteria_card)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setMaximumSize(QSize(110, 16777215))
        self.doubleSpinBox_2.setSingleStep(0.010000000000000)

        self.criteria_grid.addWidget(self.doubleSpinBox_2, 3, 2, 1, 1)

        self.criteria_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.criteria_grid.addItem(self.criteria_grid_spacer, 0, 6, 1, 1)


        self.criteria_card_layout.addLayout(self.criteria_grid)

        self.criteria_help_label = QLabel(self.criteria_card)
        self.criteria_help_label.setObjectName(u"criteria_help_label")
        self.criteria_help_label.setFont(font2)
        self.criteria_help_label.setWordWrap(True)
        self.criteria_help_label.setProperty(u"variant", u"help")

        self.criteria_card_layout.addWidget(self.criteria_help_label)


        self.content_layout.addWidget(self.criteria_card)

        self.stages_cards_layout = QHBoxLayout()
        self.stages_cards_layout.setSpacing(16)
        self.stages_cards_layout.setObjectName(u"stages_cards_layout")
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

        self.stages_label = QLabel(self.stages_card)
        self.stages_label.setObjectName(u"stages_label")
        self.stages_label.setWordWrap(True)
        self.stages_label.setProperty(u"variant", u"help")

        self.stages_card_layout.addWidget(self.stages_label)

        self.stages_options_layout = QVBoxLayout()
        self.stages_options_layout.setSpacing(8)
        self.stages_options_layout.setObjectName(u"stages_options_layout")
        self.stages_options_layout_1_layout = QVBoxLayout()
        self.stages_options_layout_1_layout.setSpacing(2)
        self.stages_options_layout_1_layout.setObjectName(u"stages_options_layout_1_layout")
        self.radioButton_scored = QRadioButton(self.stages_card)
        self.radioButton_scored.setObjectName(u"radioButton_scored")

        self.stages_options_layout_1_layout.addWidget(self.radioButton_scored)

        self.scored_help_label = QLabel(self.stages_card)
        self.scored_help_label.setObjectName(u"scored_help_label")
        self.scored_help_label.setFont(font2)
        self.scored_help_label.setWordWrap(True)
        self.scored_help_label.setIndent(26)
        self.scored_help_label.setProperty(u"variant", u"help")

        self.stages_options_layout_1_layout.addWidget(self.scored_help_label)


        self.stages_options_layout.addLayout(self.stages_options_layout_1_layout)

        self.stages_options_layout_line_1 = QFrame(self.stages_card)
        self.stages_options_layout_line_1.setObjectName(u"stages_options_layout_line_1")
        self.stages_options_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.stages_options_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.stages_options_layout.addWidget(self.stages_options_layout_line_1)

        self.stages_options_layout_2_layout = QVBoxLayout()
        self.stages_options_layout_2_layout.setSpacing(2)
        self.stages_options_layout_2_layout.setObjectName(u"stages_options_layout_2_layout")
        self.radioButton_unscored = QRadioButton(self.stages_card)
        self.radioButton_unscored.setObjectName(u"radioButton_unscored")

        self.stages_options_layout_2_layout.addWidget(self.radioButton_unscored)

        self.unscored_help_label = QLabel(self.stages_card)
        self.unscored_help_label.setObjectName(u"unscored_help_label")
        self.unscored_help_label.setFont(font2)
        self.unscored_help_label.setWordWrap(True)
        self.unscored_help_label.setIndent(26)
        self.unscored_help_label.setProperty(u"variant", u"help")

        self.stages_options_layout_2_layout.addWidget(self.unscored_help_label)


        self.stages_options_layout.addLayout(self.stages_options_layout_2_layout)


        self.stages_card_layout.addLayout(self.stages_options_layout)

        self.stages_layout = QHBoxLayout()
        self.stages_layout.setSpacing(22)
        self.stages_layout.setObjectName(u"stages_layout")
        self.checkBox_W = QCheckBox(self.stages_card)
        self.checkBox_W.setObjectName(u"checkBox_W")

        self.stages_layout.addWidget(self.checkBox_W)

        self.checkBox_N1 = QCheckBox(self.stages_card)
        self.checkBox_N1.setObjectName(u"checkBox_N1")

        self.stages_layout.addWidget(self.checkBox_N1)

        self.checkBox_N2 = QCheckBox(self.stages_card)
        self.checkBox_N2.setObjectName(u"checkBox_N2")

        self.stages_layout.addWidget(self.checkBox_N2)

        self.checkBox_N3 = QCheckBox(self.stages_card)
        self.checkBox_N3.setObjectName(u"checkBox_N3")

        self.stages_layout.addWidget(self.checkBox_N3)

        self.checkBox_R = QCheckBox(self.stages_card)
        self.checkBox_R.setObjectName(u"checkBox_R")

        self.stages_layout.addWidget(self.checkBox_R)

        self.stages_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.stages_layout.addItem(self.stages_spacer)


        self.stages_card_layout.addLayout(self.stages_layout)

        self.stages_help_label = QLabel(self.stages_card)
        self.stages_help_label.setObjectName(u"stages_help_label")
        self.stages_help_label.setFont(font2)
        self.stages_help_label.setWordWrap(True)
        self.stages_help_label.setProperty(u"variant", u"help")

        self.stages_card_layout.addWidget(self.stages_help_label)

        self.stages_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.stages_card_layout.addItem(self.stages_stretch)


        self.stages_cards_layout.addWidget(self.stages_card)

        self.outliers_card = QFrame(self.content_widget)
        self.outliers_card.setObjectName(u"outliers_card")
        self.outliers_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.outliers_card.setFrameShadow(QFrame.Shadow.Raised)
        self.outliers_card_layout = QVBoxLayout(self.outliers_card)
        self.outliers_card_layout.setSpacing(10)
        self.outliers_card_layout.setObjectName(u"outliers_card_layout")
        self.outliers_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_7 = QLabel(self.outliers_card)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.outliers_card_layout.addWidget(self.label_7)

        self.outliers_layout = QVBoxLayout()
        self.outliers_layout.setSpacing(8)
        self.outliers_layout.setObjectName(u"outliers_layout")
        self.outliers_layout_1_layout = QVBoxLayout()
        self.outliers_layout_1_layout.setSpacing(2)
        self.outliers_layout_1_layout.setObjectName(u"outliers_layout_1_layout")
        self.checkBox = QCheckBox(self.outliers_card)
        self.checkBox.setObjectName(u"checkBox")

        self.outliers_layout_1_layout.addWidget(self.checkBox)

        self.outliers_help_label = QLabel(self.outliers_card)
        self.outliers_help_label.setObjectName(u"outliers_help_label")
        self.outliers_help_label.setFont(font2)
        self.outliers_help_label.setWordWrap(True)
        self.outliers_help_label.setIndent(26)
        self.outliers_help_label.setProperty(u"variant", u"help")

        self.outliers_layout_1_layout.addWidget(self.outliers_help_label)


        self.outliers_layout.addLayout(self.outliers_layout_1_layout)


        self.outliers_card_layout.addLayout(self.outliers_layout)

        self.outliers_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.outliers_card_layout.addItem(self.outliers_stretch)


        self.stages_cards_layout.addWidget(self.outliers_card)

        self.stages_cards_layout.setStretch(0, 1)
        self.stages_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.stages_cards_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(DetectorStep)

        QMetaObject.connectSlotsByName(DetectorStep)
    # setupUi

    def retranslateUi(self, DetectorStep):
        DetectorStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("DetectorStep", u"Detector Step", None))
        self.subtitle_label.setText(QCoreApplication.translate("DetectorStep", u"Define the REM events created, the detection criteria and the sleep stages in which REMs are detected.", None))
        self.label_19.setText(QCoreApplication.translate("DetectorStep", u"REM events", None))
        self.label_15.setText(QCoreApplication.translate("DetectorStep", u"Group", None))
        self.label_9.setText(QCoreApplication.translate("DetectorStep", u"Name", None))
        self.label_20.setText(QCoreApplication.translate("DetectorStep", u"The group and name of the REM events added to the accessory file.", None))
        self.label.setText(QCoreApplication.translate("DetectorStep", u"Detection criteria", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("DetectorStep", u"Minimum and maximum amplitude of the peak of the REMs.", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("DetectorStep", u"Amplitude", None))
        self.label_18.setText(QCoreApplication.translate("DetectorStep", u"Min", None))
        self.label_17.setText(QCoreApplication.translate("DetectorStep", u"Max", None))
        self.amplitude_unit_label.setText(QCoreApplication.translate("DetectorStep", u"\u00b5V", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("DetectorStep", u"Minimum and maximum duration of the REMs.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("DetectorStep", u"Duration", None))
        self.label_11.setText(QCoreApplication.translate("DetectorStep", u"Min", None))
        self.label_12.setText(QCoreApplication.translate("DetectorStep", u"Max", None))
        self.duration_unit_label.setText(QCoreApplication.translate("DetectorStep", u"s", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("DetectorStep", u"Frequency range of the REMs. The LOC and ROC signals are filtered in this band before the detection.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("DetectorStep", u"REM frequency", None))
        self.label_13.setText(QCoreApplication.translate("DetectorStep", u"Min", None))
        self.label_14.setText(QCoreApplication.translate("DetectorStep", u"Max", None))
        self.frequency_unit_label.setText(QCoreApplication.translate("DetectorStep", u"Hz", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("DetectorStep", u"Scales the minimum prominence threshold as a fraction of the minimum amplitude. With a relative prominence of 0.5, the peaks must stand out by at least 50% of the minimum amplitude.", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("DetectorStep", u"Relative prominence", None))
        self.criteria_help_label.setText(QCoreApplication.translate("DetectorStep", u"Defaults: 50\u2013325 \u00b5V, 0.3\u20131.5 s, 0.5\u20135 Hz and a relative prominence of 0.8.", None))
        self.label_6.setText(QCoreApplication.translate("DetectorStep", u"Sleep stages", None))
        self.stages_label.setText(QCoreApplication.translate("DetectorStep", u"Select whether the annotation files hold scored sleep stages.", None))
        self.radioButton_scored.setText(QCoreApplication.translate("DetectorStep", u"Scored", None))
        self.scored_help_label.setText(QCoreApplication.translate("DetectorStep", u"REMs are detected in the R epochs only, and the REM report is generated.", None))
        self.radioButton_unscored.setText(QCoreApplication.translate("DetectorStep", u"Unscored", None))
        self.unscored_help_label.setText(QCoreApplication.translate("DetectorStep", u"No annotation file with sleep stages: REMs are detected in the whole recording, without report.", None))
        self.checkBox_W.setText(QCoreApplication.translate("DetectorStep", u"W", None))
        self.checkBox_N1.setText(QCoreApplication.translate("DetectorStep", u"N1", None))
        self.checkBox_N2.setText(QCoreApplication.translate("DetectorStep", u"N2", None))
        self.checkBox_N3.setText(QCoreApplication.translate("DetectorStep", u"N3", None))
        self.checkBox_R.setText(QCoreApplication.translate("DetectorStep", u"R", None))
        self.stages_help_label.setText(QCoreApplication.translate("DetectorStep", u"The stages follow the choice above.", None))
        self.label_7.setText(QCoreApplication.translate("DetectorStep", u"Outliers", None))
        self.checkBox.setText(QCoreApplication.translate("DetectorStep", u"Remove the outliers", None))
        self.outliers_help_label.setText(QCoreApplication.translate("DetectorStep", u"YASA detects and removes the outlier REMs, only when at least 50 REMs are detected.", None))
    # retranslateUi

