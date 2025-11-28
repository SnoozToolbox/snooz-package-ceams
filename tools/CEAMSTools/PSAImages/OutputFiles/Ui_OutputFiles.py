# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_OutputFiles.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_OutputFiles(object):
    def setupUi(self, OutputFiles):
        if not OutputFiles.objectName():
            OutputFiles.setObjectName(u"OutputFiles")
        OutputFiles.resize(956, 764)
        OutputFiles.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_5 = QVBoxLayout(OutputFiles)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea = QScrollArea(OutputFiles)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -454, 900, 1200))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(862, 1200))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(900, 1200))
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_10.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.checkBox_subject_avg = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_subject_avg.setObjectName(u"checkBox_subject_avg")

        self.verticalLayout.addWidget(self.checkBox_subject_avg)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.checkBox_subject_sel = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_subject_sel.setObjectName(u"checkBox_subject_sel")
        self.checkBox_subject_sel.setEnabled(False)

        self.verticalLayout.addWidget(self.checkBox_subject_sel)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_10.addLayout(self.horizontalLayout)


        self.verticalLayout_8.addLayout(self.verticalLayout_10)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_11.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_2.addWidget(self.label_11)

        self.checkBox_cohort_avg = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_cohort_avg.setObjectName(u"checkBox_cohort_avg")
        self.checkBox_cohort_avg.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_cohort_avg)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_2.addWidget(self.label_12)

        self.checkBox_cohort_sel = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_cohort_sel.setObjectName(u"checkBox_cohort_sel")

        self.verticalLayout_2.addWidget(self.checkBox_cohort_sel)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_11)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)

        self.verticalLayout_7.addWidget(self.label_8)

        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 100))
        self.textEdit.setTabletTracking(False)
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.textEdit)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_Wake = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_Wake.setObjectName(u"checkBox_Wake")

        self.horizontalLayout_4.addWidget(self.checkBox_Wake)

        self.checkBox_N1 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_N1.setObjectName(u"checkBox_N1")

        self.horizontalLayout_4.addWidget(self.checkBox_N1)

        self.checkBox_N2 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_N2.setObjectName(u"checkBox_N2")

        self.horizontalLayout_4.addWidget(self.checkBox_N2)

        self.checkBox_N3 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_N3.setObjectName(u"checkBox_N3")

        self.horizontalLayout_4.addWidget(self.checkBox_N3)

        self.checkBox_REM = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_REM.setObjectName(u"checkBox_REM")

        self.horizontalLayout_4.addWidget(self.checkBox_REM)

        self.checkBox_Unscored = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_Unscored.setObjectName(u"checkBox_Unscored")

        self.horizontalLayout_4.addWidget(self.checkBox_Unscored)

        self.checkBox_All = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_All.setObjectName(u"checkBox_All")

        self.horizontalLayout_4.addWidget(self.checkBox_All)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.radioButton_total = QRadioButton(self.scrollAreaWidgetContents)
        self.buttonGroup_align = QButtonGroup(OutputFiles)
        self.buttonGroup_align.setObjectName(u"buttonGroup_align")
        self.buttonGroup_align.addButton(self.radioButton_total)
        self.radioButton_total.setObjectName(u"radioButton_total")
        self.radioButton_total.setChecked(True)

        self.gridLayout_4.addWidget(self.radioButton_total, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.radioButton_stage_hour = QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_stage_hour.setObjectName(u"radioButton_stage_hour")

        self.gridLayout_4.addWidget(self.radioButton_stage_hour, 3, 0, 1, 1)

        self.radioButton_sleep_cycle = QRadioButton(self.scrollAreaWidgetContents)
        self.buttonGroup_align.addButton(self.radioButton_sleep_cycle)
        self.radioButton_sleep_cycle.setObjectName(u"radioButton_sleep_cycle")

        self.gridLayout_4.addWidget(self.radioButton_sleep_cycle, 1, 0, 1, 1)

        self.radioButton_clock_hour = QRadioButton(self.scrollAreaWidgetContents)
        self.buttonGroup_align.addButton(self.radioButton_clock_hour)
        self.radioButton_clock_hour.setObjectName(u"radioButton_clock_hour")

        self.gridLayout_4.addWidget(self.radioButton_clock_hour, 2, 0, 1, 1)

        self.spinBox_clock_hour = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_clock_hour.setObjectName(u"spinBox_clock_hour")

        self.gridLayout_4.addWidget(self.spinBox_clock_hour, 2, 2, 1, 1)

        self.spinBox_sleep_cycle = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_sleep_cycle.setObjectName(u"spinBox_sleep_cycle")

        self.gridLayout_4.addWidget(self.spinBox_sleep_cycle, 1, 2, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 1, 1, 1, 1)

        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 3, 1, 1, 1)

        self.spinBox_stage_hour = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_stage_hour.setObjectName(u"spinBox_stage_hour")

        self.gridLayout_4.addWidget(self.spinBox_stage_hour, 3, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_4)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_9)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.radioButton_all = QRadioButton(self.scrollAreaWidgetContents)
        self.buttonGroup_mean = QButtonGroup(OutputFiles)
        self.buttonGroup_mean.setObjectName(u"buttonGroup_mean")
        self.buttonGroup_mean.addButton(self.radioButton_all)
        self.radioButton_all.setObjectName(u"radioButton_all")

        self.verticalLayout_3.addWidget(self.radioButton_all)

        self.radioButton_mean = QRadioButton(self.scrollAreaWidgetContents)
        self.buttonGroup_mean.addButton(self.radioButton_mean)
        self.radioButton_mean.setObjectName(u"radioButton_mean")

        self.verticalLayout_3.addWidget(self.radioButton_mean)

        self.radioButton_meanstd = QRadioButton(self.scrollAreaWidgetContents)
        self.buttonGroup_mean.addButton(self.radioButton_meanstd)
        self.radioButton_meanstd.setObjectName(u"radioButton_meanstd")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.radioButton_meanstd.sizePolicy().hasHeightForWidth())
        self.radioButton_meanstd.setSizePolicy(sizePolicy3)
        self.radioButton_meanstd.setMinimumSize(QSize(0, 0))
        self.radioButton_meanstd.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioButton_meanstd)

        self.checkBox_log = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_log.setObjectName(u"checkBox_log")

        self.verticalLayout_3.addWidget(self.checkBox_log)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_force_axis = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_force_axis.setObjectName(u"checkBox_force_axis")

        self.horizontalLayout_5.addWidget(self.checkBox_force_axis)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_13)

        self.doubleSpinBox_xmin = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_xmin.setObjectName(u"doubleSpinBox_xmin")
        self.doubleSpinBox_xmin.setEnabled(False)
        self.doubleSpinBox_xmin.setMinimum(-5.000000000000000)
        self.doubleSpinBox_xmin.setMaximum(5.000000000000000)
        self.doubleSpinBox_xmin.setSingleStep(0.500000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_xmin)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_14)

        self.doubleSpinBox_xmax = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_xmax.setObjectName(u"doubleSpinBox_xmax")
        self.doubleSpinBox_xmax.setEnabled(False)
        self.doubleSpinBox_xmax.setMinimum(-5.000000000000000)
        self.doubleSpinBox_xmax.setMaximum(5.000000000000000)
        self.doubleSpinBox_xmax.setSingleStep(0.500000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_xmax)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_15)

        self.doubleSpinBox_ymin = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_ymin.setObjectName(u"doubleSpinBox_ymin")
        self.doubleSpinBox_ymin.setEnabled(False)
        self.doubleSpinBox_ymin.setMinimum(-500.000000000000000)
        self.doubleSpinBox_ymin.setMaximum(500.000000000000000)
        self.doubleSpinBox_ymin.setSingleStep(50.000000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_ymin)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_16)

        self.doubleSpinBox_ymax = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_ymax.setObjectName(u"doubleSpinBox_ymax")
        self.doubleSpinBox_ymax.setEnabled(False)
        self.doubleSpinBox_ymax.setMinimum(-500.000000000000000)
        self.doubleSpinBox_ymax.setMaximum(500.000000000000000)
        self.doubleSpinBox_ymax.setSingleStep(50.000000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_ymax)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_9.addWidget(self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_output = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_output.setObjectName(u"lineEdit_output")
        self.lineEdit_output.setMinimumSize(QSize(0, 0))
        self.lineEdit_output.setMaximumSize(QSize(900, 16777215))
        self.lineEdit_output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_output)

        self.pushButton_choose = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_choose.setObjectName(u"pushButton_choose")
        self.pushButton_choose.setMinimumSize(QSize(80, 0))
        self.pushButton_choose.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_choose)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)


        self.verticalLayout_8.addLayout(self.verticalLayout_9)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.retranslateUi(OutputFiles)
        self.pushButton_choose.clicked.connect(OutputFiles.choose_slot)
        self.checkBox_cohort_avg.clicked.connect(OutputFiles.out_options_slot)
        self.checkBox_cohort_sel.clicked.connect(OutputFiles.out_options_slot)
        self.checkBox_subject_avg.clicked.connect(OutputFiles.out_options_slot)
        self.checkBox_subject_sel.clicked.connect(OutputFiles.out_options_slot)
        self.buttonGroup_align.buttonClicked.connect(OutputFiles.out_options_slot)
        self.buttonGroup_mean.buttonClicked.connect(OutputFiles.out_options_slot)
        self.checkBox_force_axis.clicked.connect(OutputFiles.out_options_slot)

        QMetaObject.connectSlotsByName(OutputFiles)
    # setupUi

    def retranslateUi(self, OutputFiles):
        OutputFiles.setWindowTitle("")
        self.label_3.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Subject level : to generate pictures for each individual subject.</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">One picture per report</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.checkBox_subject_avg.setToolTip(QCoreApplication.translate("OutputFiles", u"Check the display option 'MEAN' in order to check this option.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_subject_avg.setText(QCoreApplication.translate("OutputFiles", u"All the channels or ROIs are illustrated on the same picture.\n"
"*Useful to explore topographic differences.", None))
        self.label_10.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">One picture per channel or ROI</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.checkBox_subject_sel.setToolTip(QCoreApplication.translate("OutputFiles", u"Check the display option 'Display all the SW' in order to check this option.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_subject_sel.setText(QCoreApplication.translate("OutputFiles", u"Useful to explore the PSA events set (with the option to display all PSA signals).", None))
        self.label_2.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Cohort level : to generate pictures for the cohort.</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">One picture per cohort</span></p></body></html>", None))
        self.checkBox_cohort_avg.setText(QCoreApplication.translate("OutputFiles", u"Spectral power averaged accross channels per group of subjects.\n"
"Each spectral curve represents the signal averaged accross all the selected channels\n"
"or ROIs for a group of subjects.", None))
        self.label_12.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">One picture per channel or ROI</span></p></body></html>", None))
        self.checkBox_cohort_sel.setText(QCoreApplication.translate("OutputFiles", u"Spectral power per channel per group of subjects.\n"
"Each spectral curve represents the signal for a selected channel or ROI for a group of subjects.", None))
        self.label_8.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:700;\">Sleep Stage Selection</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("OutputFiles", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Note: When N2 and N3 stages are selected together, the generated figure displays only the spectral data corresponding to the &quot;N2N3&quot; column of the report. Similarly, when N1, N2, and N3 stages are all selected, the figure presents only the data from the &quot;NREM&quot; column.</p></body></html>", None))
        self.checkBox_Wake.setText(QCoreApplication.translate("OutputFiles", u"Wake", None))
        self.checkBox_N1.setText(QCoreApplication.translate("OutputFiles", u"N1", None))
        self.checkBox_N2.setText(QCoreApplication.translate("OutputFiles", u"N2", None))
        self.checkBox_N3.setText(QCoreApplication.translate("OutputFiles", u"N3", None))
        self.checkBox_REM.setText(QCoreApplication.translate("OutputFiles", u"REM", None))
        self.checkBox_Unscored.setText(QCoreApplication.translate("OutputFiles", u"Unscored", None))
        self.checkBox_All.setText(QCoreApplication.translate("OutputFiles", u"All", None))
        self.label_6.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Section to Display</span></p></body></html>", None))
        self.radioButton_total.setText(QCoreApplication.translate("OutputFiles", u"Total", None))
        self.radioButton_stage_hour.setText(QCoreApplication.translate("OutputFiles", u"Stage Hour", None))
        self.radioButton_sleep_cycle.setText(QCoreApplication.translate("OutputFiles", u"Sleep Cycle", None))
        self.radioButton_clock_hour.setText(QCoreApplication.translate("OutputFiles", u"Clock Hour", None))
        self.label_7.setText(QCoreApplication.translate("OutputFiles", u"Desired Hour", None))
        self.label_17.setText(QCoreApplication.translate("OutputFiles", u"Desired Cycle", None))
        self.label_18.setText(QCoreApplication.translate("OutputFiles", u"Desired Hour", None))
        self.label.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Display Options</span></p></body></html>", None))
        self.radioButton_all.setText(QCoreApplication.translate("OutputFiles", u"Display all the spectral power curves on the picture.", None))
        self.radioButton_mean.setText(QCoreApplication.translate("OutputFiles", u"MEAN : Display only the mean spectral power curve", None))
        self.radioButton_meanstd.setText(QCoreApplication.translate("OutputFiles", u"MEAN + STD : Display the mean spectral power curve in bold line\n"
"and the spectral power curve standard deviation in gray shaded area.", None))
        self.checkBox_log.setText(QCoreApplication.translate("OutputFiles", u"Logarithmic Scale", None))
#if QT_CONFIG(tooltip)
        self.checkBox_force_axis.setToolTip(QCoreApplication.translate("OutputFiles", u"Enable this option for consistent axes across all pictures and define the axes limits. Otherwise, the axes are automatically determined based on the data.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_force_axis.setText(QCoreApplication.translate("OutputFiles", u"Force axis limits", None))
        self.label_13.setText(QCoreApplication.translate("OutputFiles", u"x-min:", None))
        self.label_14.setText(QCoreApplication.translate("OutputFiles", u"x-max:", None))
        self.label_15.setText(QCoreApplication.translate("OutputFiles", u"y-min:", None))
        self.label_16.setText(QCoreApplication.translate("OutputFiles", u"y-max:", None))
        self.label_4.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Ouput folder to save pictures</span></p></body></html>", None))
        self.lineEdit_output.setPlaceholderText(QCoreApplication.translate("OutputFiles", u"Select the folder where the pictures will be saved.", None))
        self.pushButton_choose.setText(QCoreApplication.translate("OutputFiles", u"Choose", None))
        self.label_5.setText(QCoreApplication.translate("OutputFiles", u"Pictures are identified with the basename of the spectral power report and\\or channel label.", None))
    # retranslateUi

