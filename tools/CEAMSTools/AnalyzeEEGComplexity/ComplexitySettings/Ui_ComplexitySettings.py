# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ComplexitySettings.ui'
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
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_ComplexitySettings(object):
    def setupUi(self, ComplexitySettings):
        if not ComplexitySettings.objectName():
            ComplexitySettings.setObjectName(u"ComplexitySettings")
        ComplexitySettings.resize(740, 590)
        ComplexitySettings.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_4 = QVBoxLayout(ComplexitySettings)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(ComplexitySettings)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.univariate_radioButton = QRadioButton(self.frame)
        self.buttonGroup = QButtonGroup(ComplexitySettings)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.univariate_radioButton)
        self.univariate_radioButton.setObjectName(u"univariate_radioButton")
        self.univariate_radioButton.setChecked(True)

        self.verticalLayout.addWidget(self.univariate_radioButton)

        self.joint_radioButton = QRadioButton(self.frame)
        self.buttonGroup.addButton(self.joint_radioButton)
        self.joint_radioButton.setObjectName(u"joint_radioButton")

        self.verticalLayout.addWidget(self.joint_radioButton)

        self.concat_radioButton = QRadioButton(self.frame)
        self.buttonGroup.addButton(self.concat_radioButton)
        self.concat_radioButton.setObjectName(u"concat_radioButton")

        self.verticalLayout.addWidget(self.concat_radioButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(ComplexitySettings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.epoch_length_doubleSpinBox = QDoubleSpinBox(self.frame_2)
        self.epoch_length_doubleSpinBox.setObjectName(u"epoch_length_doubleSpinBox")
        self.epoch_length_doubleSpinBox.setMinimum(1.000000000000000)
        self.epoch_length_doubleSpinBox.setMaximum(30.000000000000000)
        self.epoch_length_doubleSpinBox.setSingleStep(0.500000000000000)
        self.epoch_length_doubleSpinBox.setValue(10.000000000000000)

        self.horizontalLayout_2.addWidget(self.epoch_length_doubleSpinBox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.overlap_length_doubleSpinBox = QDoubleSpinBox(self.frame_2)
        self.overlap_length_doubleSpinBox.setObjectName(u"overlap_length_doubleSpinBox")
        self.overlap_length_doubleSpinBox.setMinimum(0.000000000000000)
        self.overlap_length_doubleSpinBox.setMaximum(29.000000000000000)
        self.overlap_length_doubleSpinBox.setSingleStep(0.500000000000000)
        self.overlap_length_doubleSpinBox.setValue(0.000000000000000)

        self.horizontalLayout_3.addWidget(self.overlap_length_doubleSpinBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 103, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.label_5 = QLabel(ComplexitySettings)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_5)

        self.export_details_checkBox = QCheckBox(ComplexitySettings)
        self.export_details_checkBox.setObjectName(u"export_details_checkBox")
        self.export_details_checkBox.setChecked(True)

        self.verticalLayout_4.addWidget(self.export_details_checkBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(ComplexitySettings)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.cohort_lineEdit = QLineEdit(ComplexitySettings)
        self.cohort_lineEdit.setObjectName(u"cohort_lineEdit")
        self.cohort_lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.cohort_lineEdit)

        self.cohort_pushButton = QPushButton(ComplexitySettings)
        self.cohort_pushButton.setObjectName(u"cohort_pushButton")

        self.horizontalLayout.addWidget(self.cohort_pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.retranslateUi(ComplexitySettings)

        QMetaObject.connectSlotsByName(ComplexitySettings)
    # setupUi

    def retranslateUi(self, ComplexitySettings):
        ComplexitySettings.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("ComplexitySettings", u"<html><head/><body><p><span style=\" font-weight:700;\">Complexity Type:<br/></span>Select the complexity mode you want to run. To analyze the data using a different mode, run the tool again and select another option.</p></body></html>", None))
        self.univariate_radioButton.setText(QCoreApplication.translate("ComplexitySettings", u"Univariate: one LZC value per channel", None))
        self.joint_radioButton.setText(QCoreApplication.translate("ComplexitySettings", u"Joint: Zozor joint LZC across channels", None))
        self.concat_radioButton.setText(QCoreApplication.translate("ComplexitySettings", u"Concatenated: Schartner concatenation", None))
        self.label_2.setText(QCoreApplication.translate("ComplexitySettings", u"<html><head/><body><p><span style=\" font-weight:700;\">Epoch Settings<br/></span>Set the window length and overlap used to segment the data into epochs.</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("ComplexitySettings", u"Epoch length (s)", None))
        self.label_4.setText(QCoreApplication.translate("ComplexitySettings", u"Overlap length (s)", None))
        self.label_5.setText(QCoreApplication.translate("ComplexitySettings", u"<html><head/><body><p><span style=\" font-weight:700;\">Output<br/></span>The output is one .tsv file (tab separated values) for the whole cohort. Each line corresponds to a recording (and to a channel in the univariate mode). Warning: results are appended to the file, so the file is modified each time the tool is run.</p></body></html>", None))
        self.export_details_checkBox.setText(QCoreApplication.translate("ComplexitySettings", u"Also save the detailed tables (one file per ecording in a subfolder next to the cohort file.)", None))
        self.label_6.setText(QCoreApplication.translate("ComplexitySettings", u"Filename", None))
#if QT_CONFIG(tooltip)
        self.cohort_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.cohort_lineEdit.setPlaceholderText(QCoreApplication.translate("ComplexitySettings", u"select the file to save the cohort complexity report", None))
        self.cohort_pushButton.setText(QCoreApplication.translate("ComplexitySettings", u"Choose", None))
    # retranslateUi

