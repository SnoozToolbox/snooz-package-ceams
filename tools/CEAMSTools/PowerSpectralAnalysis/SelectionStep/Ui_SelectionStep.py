# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SelectionStep.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_SelectionStep(object):
    def setupUi(self, SelectionStep):
        if not SelectionStep.objectName():
            SelectionStep.setObjectName(u"SelectionStep")
        SelectionStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(SelectionStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(SelectionStep)
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

        self.section_layout = QVBoxLayout()
        self.section_layout.setSpacing(6)
        self.section_layout.setObjectName(u"section_layout")
        self.radioButton_annotations = QRadioButton(self.content_widget)
        self.radioButton_annotations.setObjectName(u"radioButton_annotations")

        self.section_layout.addWidget(self.radioButton_annotations)

        self.radioButton_sleep = QRadioButton(self.content_widget)
        self.radioButton_sleep.setObjectName(u"radioButton_sleep")
        self.radioButton_sleep.setChecked(True)

        self.section_layout.addWidget(self.radioButton_sleep)


        self.content_layout.addLayout(self.section_layout)

        self.stages_card = QFrame(self.content_widget)
        self.stages_card.setObjectName(u"stages_card")
        self.stages_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.stages_card.setFrameShadow(QFrame.Shadow.Raised)
        self.stages_card_layout = QVBoxLayout(self.stages_card)
        self.stages_card_layout.setSpacing(10)
        self.stages_card_layout.setObjectName(u"stages_card_layout")
        self.stages_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_5 = QLabel(self.stages_card)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setBold(True)
        self.label_5.setFont(font1)

        self.stages_card_layout.addWidget(self.label_5)

        self.label_3 = QLabel(self.stages_card)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)
        self.label_3.setProperty(u"variant", u"help")

        self.stages_card_layout.addWidget(self.label_3)

        self.stages_layout = QHBoxLayout()
        self.stages_layout.setSpacing(22)
        self.stages_layout.setObjectName(u"stages_layout")
        self.w_checkBox = QCheckBox(self.stages_card)
        self.w_checkBox.setObjectName(u"w_checkBox")
        self.w_checkBox.setChecked(True)

        self.stages_layout.addWidget(self.w_checkBox)

        self.n1_checkBox = QCheckBox(self.stages_card)
        self.n1_checkBox.setObjectName(u"n1_checkBox")
        self.n1_checkBox.setChecked(True)

        self.stages_layout.addWidget(self.n1_checkBox)

        self.n2_checkBox = QCheckBox(self.stages_card)
        self.n2_checkBox.setObjectName(u"n2_checkBox")
        self.n2_checkBox.setChecked(True)

        self.stages_layout.addWidget(self.n2_checkBox)

        self.n3_checkBox = QCheckBox(self.stages_card)
        self.n3_checkBox.setObjectName(u"n3_checkBox")
        self.n3_checkBox.setChecked(True)

        self.stages_layout.addWidget(self.n3_checkBox)

        self.r_checkBox = QCheckBox(self.stages_card)
        self.r_checkBox.setObjectName(u"r_checkBox")
        self.r_checkBox.setChecked(True)

        self.stages_layout.addWidget(self.r_checkBox)

        self.nrem_checkBox = QCheckBox(self.stages_card)
        self.nrem_checkBox.setObjectName(u"nrem_checkBox")
        self.nrem_checkBox.setChecked(True)

        self.stages_layout.addWidget(self.nrem_checkBox)

        self.unscored_checkBox = QCheckBox(self.stages_card)
        self.unscored_checkBox.setObjectName(u"unscored_checkBox")

        self.stages_layout.addWidget(self.unscored_checkBox)

        self.s4_checkBox = QCheckBox(self.stages_card)
        self.s4_checkBox.setObjectName(u"s4_checkBox")
        self.s4_checkBox.setEnabled(False)

        self.stages_layout.addWidget(self.s4_checkBox)

        self.stages_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.stages_layout.addItem(self.stages_spacer)


        self.stages_card_layout.addLayout(self.stages_layout)


        self.content_layout.addWidget(self.stages_card)

        self.periods_card = QFrame(self.content_widget)
        self.periods_card.setObjectName(u"periods_card")
        self.periods_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.periods_card.setFrameShadow(QFrame.Shadow.Raised)
        self.periods_card_layout = QVBoxLayout(self.periods_card)
        self.periods_card_layout.setSpacing(10)
        self.periods_card_layout.setObjectName(u"periods_card_layout")
        self.periods_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_4 = QLabel(self.periods_card)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.periods_card_layout.addWidget(self.label_4)

        self.label_7 = QLabel(self.periods_card)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)
        self.label_7.setProperty(u"variant", u"help")

        self.periods_card_layout.addWidget(self.label_7)

        self.periods_layout = QVBoxLayout()
        self.periods_layout.setSpacing(8)
        self.periods_layout.setObjectName(u"periods_layout")
        self.periods_layout_1_layout = QVBoxLayout()
        self.periods_layout_1_layout.setSpacing(2)
        self.periods_layout_1_layout.setObjectName(u"periods_layout_1_layout")
        self.in_cycle_checkBox = QCheckBox(self.periods_card)
        self.in_cycle_checkBox.setObjectName(u"in_cycle_checkBox")
        self.in_cycle_checkBox.setEnabled(True)
        self.in_cycle_checkBox.setCheckable(True)
        self.in_cycle_checkBox.setChecked(True)

        self.periods_layout_1_layout.addWidget(self.in_cycle_checkBox)

        self.textEdit = QLabel(self.periods_card)
        self.textEdit.setObjectName(u"textEdit")
        font2 = QFont()
        font2.setPointSize(10)
        self.textEdit.setFont(font2)
        self.textEdit.setWordWrap(True)
        self.textEdit.setIndent(26)
        self.textEdit.setProperty(u"variant", u"help")

        self.periods_layout_1_layout.addWidget(self.textEdit)


        self.periods_layout.addLayout(self.periods_layout_1_layout)

        self.periods_layout_line_1 = QFrame(self.periods_card)
        self.periods_layout_line_1.setObjectName(u"periods_layout_line_1")
        self.periods_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.periods_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.periods_layout.addWidget(self.periods_layout_line_1)

        self.periods_layout_2_layout = QVBoxLayout()
        self.periods_layout_2_layout.setSpacing(2)
        self.periods_layout_2_layout.setObjectName(u"periods_layout_2_layout")
        self.excl_nremp_checkBox = QCheckBox(self.periods_card)
        self.excl_nremp_checkBox.setObjectName(u"excl_nremp_checkBox")
        self.excl_nremp_checkBox.setMinimumSize(QSize(0, 0))
        self.excl_nremp_checkBox.setMaximumSize(QSize(300, 16777215))

        self.periods_layout_2_layout.addWidget(self.excl_nremp_checkBox)

        self.excl_nremp_help_label = QLabel(self.periods_card)
        self.excl_nremp_help_label.setObjectName(u"excl_nremp_help_label")
        self.excl_nremp_help_label.setFont(font2)
        self.excl_nremp_help_label.setWordWrap(True)
        self.excl_nremp_help_label.setIndent(26)
        self.excl_nremp_help_label.setProperty(u"variant", u"help")

        self.periods_layout_2_layout.addWidget(self.excl_nremp_help_label)


        self.periods_layout.addLayout(self.periods_layout_2_layout)

        self.periods_layout_line_2 = QFrame(self.periods_card)
        self.periods_layout_line_2.setObjectName(u"periods_layout_line_2")
        self.periods_layout_line_2.setFrameShape(QFrame.Shape.HLine)
        self.periods_layout_line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.periods_layout.addWidget(self.periods_layout_line_2)

        self.periods_layout_3_layout = QVBoxLayout()
        self.periods_layout_3_layout.setSpacing(2)
        self.periods_layout_3_layout.setObjectName(u"periods_layout_3_layout")
        self.excl_remp_checkBox = QCheckBox(self.periods_card)
        self.excl_remp_checkBox.setObjectName(u"excl_remp_checkBox")

        self.periods_layout_3_layout.addWidget(self.excl_remp_checkBox)

        self.textEdit_2 = QLabel(self.periods_card)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setFont(font2)
        self.textEdit_2.setWordWrap(True)
        self.textEdit_2.setIndent(26)
        self.textEdit_2.setProperty(u"variant", u"help")

        self.periods_layout_3_layout.addWidget(self.textEdit_2)


        self.periods_layout.addLayout(self.periods_layout_3_layout)


        self.periods_card_layout.addLayout(self.periods_layout)


        self.content_layout.addWidget(self.periods_card)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SelectionStep)
        self.radioButton_annotations.clicked.connect(SelectionStep.update_section_selection_slot)
        self.radioButton_sleep.clicked.connect(SelectionStep.update_section_selection_slot)
        self.nrem_checkBox.clicked.connect(SelectionStep.NREM_checkbox_slot)
        self.excl_nremp_checkBox.clicked.connect(SelectionStep.NREM_stages_and_periods_slot)
        self.excl_remp_checkBox.clicked.connect(SelectionStep.REM_stages_and_periods_slot)
        self.n2_checkBox.clicked.connect(SelectionStep.NREM_stages_and_periods_slot)
        self.n3_checkBox.clicked.connect(SelectionStep.NREM_stages_and_periods_slot)
        self.nrem_checkBox.clicked.connect(SelectionStep.NREM_stages_and_periods_slot)
        self.r_checkBox.clicked.connect(SelectionStep.REM_stages_and_periods_slot)

        QMetaObject.connectSlotsByName(SelectionStep)
    # setupUi

    def retranslateUi(self, SelectionStep):
        SelectionStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("SelectionStep", u"Section Selection", None))
        self.subtitle_label.setText(QCoreApplication.translate("SelectionStep", u"Choose the part of the signal on which the EEG spectral power is analysed.", None))
        self.radioButton_annotations.setText(QCoreApplication.translate("SelectionStep", u"Specific annotations (chosen in the next step)", None))
        self.radioButton_sleep.setText(QCoreApplication.translate("SelectionStep", u"Sleep stages and/or cycles", None))
        self.label_5.setText(QCoreApplication.translate("SelectionStep", u"Sleep stages", None))
        self.label_3.setText(QCoreApplication.translate("SelectionStep", u"The spectral power is analysed per sleep stage. Select the stages to include.", None))
        self.w_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Wake", None))
        self.n1_checkBox.setText(QCoreApplication.translate("SelectionStep", u"N1", None))
        self.n2_checkBox.setText(QCoreApplication.translate("SelectionStep", u"N2", None))
        self.n3_checkBox.setText(QCoreApplication.translate("SelectionStep", u"N3", None))
        self.r_checkBox.setText(QCoreApplication.translate("SelectionStep", u"R", None))
        self.nrem_checkBox.setText(QCoreApplication.translate("SelectionStep", u"NREM", None))
#if QT_CONFIG(tooltip)
        self.unscored_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the power spectral analysis on signal unscored.  PSG recording without sleep staging will be marked \"unscored\".", None))
#endif // QT_CONFIG(tooltip)
        self.unscored_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Unscored", None))
        self.s4_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Stage 4", None))
        self.label_4.setText(QCoreApplication.translate("SelectionStep", u"Sleep periods", None))
        self.label_7.setText(QCoreApplication.translate("SelectionStep", u"Optional. To analyse a specific section of the recording.", None))
#if QT_CONFIG(tooltip)
        self.in_cycle_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the power spectral analysis only on the signal included in the sleep cycles i.e. from sleep onset to the last asleep stage.", None))
#endif // QT_CONFIG(tooltip)
        self.in_cycle_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Analyse power in sleep cycles only", None))
        self.textEdit.setText(QCoreApplication.translate("SelectionStep", u"From sleep onset to the last asleep stage. Useful to analyse complete sleep cycles only (incomplete cycles are excluded in \"Common settings\" \u203a \"Sleep Cycles\").", None))
#if QT_CONFIG(tooltip)
        self.excl_nremp_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to exclude NREM periods from the power spectral analysis.", None))
#endif // QT_CONFIG(tooltip)
        self.excl_nremp_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Exclude NREM periods", None))
        self.excl_nremp_help_label.setText(QCoreApplication.translate("SelectionStep", u"Keeps the stages included in REM periods only.", None))
#if QT_CONFIG(tooltip)
        self.excl_remp_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to exclude REM periods from the power spectral analysis.", None))
#endif // QT_CONFIG(tooltip)
        self.excl_remp_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Exclude REM periods", None))
        self.textEdit_2.setText(QCoreApplication.translate("SelectionStep", u"Keeps the NREM stages included in NREM periods only (not those in REM periods).", None))
    # retranslateUi

