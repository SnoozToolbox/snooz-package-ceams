# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MiniEpochDefinition.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_MiniEpochDefinition(object):
    def setupUi(self, MiniEpochDefinition):
        if not MiniEpochDefinition.objectName():
            MiniEpochDefinition.setObjectName(u"MiniEpochDefinition")
        MiniEpochDefinition.resize(954, 806)
        MiniEpochDefinition.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(MiniEpochDefinition)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(MiniEpochDefinition)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer_2 = QSpacerItem(20, 29, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.textEdit = QTextEdit(MiniEpochDefinition)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QSize(16777215, 130))
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Shadow.Raised)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.label_5 = QLabel(MiniEpochDefinition)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(MiniEpochDefinition)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(MiniEpochDefinition)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_group = QLineEdit(MiniEpochDefinition)
        self.lineEdit_group.setObjectName(u"lineEdit_group")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_group)

        self.label_2 = QLabel(MiniEpochDefinition)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_name_Phasic = QLineEdit(MiniEpochDefinition)
        self.lineEdit_name_Phasic.setObjectName(u"lineEdit_name_Phasic")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_name_Phasic)

        self.label_3 = QLabel(MiniEpochDefinition)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_name_Tonic = QLineEdit(MiniEpochDefinition)
        self.lineEdit_name_Tonic.setObjectName(u"lineEdit_name_Tonic")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_name_Tonic)


        self.horizontalLayout.addLayout(self.formLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.textEdit_2 = QTextEdit(MiniEpochDefinition)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMaximumSize(QSize(16777215, 100))
        self.textEdit_2.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_2.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_2.setLineWidth(0)
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_8 = QLabel(MiniEpochDefinition)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.comboBox_length = QComboBox(MiniEpochDefinition)
        self.comboBox_length.addItem("")
        self.comboBox_length.addItem("")
        self.comboBox_length.addItem("")
        self.comboBox_length.addItem("")
        self.comboBox_length.setObjectName(u"comboBox_length")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox_length)


        self.horizontalLayout_2.addLayout(self.formLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(MiniEpochDefinition)

        QMetaObject.connectSlotsByName(MiniEpochDefinition)
    # setupUi

    def retranslateUi(self, MiniEpochDefinition):
        MiniEpochDefinition.setWindowTitle("")
        self.label_4.setText(QCoreApplication.translate("MiniEpochDefinition", u"<html><head/><body><p><span style=\" font-weight:700;\">Define the labels and length of the mini-epochs for Rapid Eye Movements (REMs).</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("MiniEpochDefinition", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto-Regular'; font-weight:700;\">General definition</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto-Regular'; text-decoration: underline;\">Tonic REM</span><span style=\" font-family:'Roboto-Regular';\"> corresponds to more stable REM activity with "
                        "minimal eye movements and lower physiological variability.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto-Regular'; text-decoration: underline;\">Phasic REM</span><span style=\" font-family:'Roboto-Regular';\"> is characterized by bursts of rapid eye movements, transient muscle activity, and increased neural and autonomic activation. This separation enables more detailed investigation of REM sleep dynamics and related biomarkers.</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MiniEpochDefinition", u"<html><head/><body><p><span style=\" font-weight:700;\">Mini-epochs group and name definition</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MiniEpochDefinition", u"<html><head/><body><p>Each event belongs to a group and is labeled by a name.</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MiniEpochDefinition", u"Group for the mini-epoch", None))
        self.label_2.setText(QCoreApplication.translate("MiniEpochDefinition", u"Name for the Phasic mini-epoch", None))
        self.label_3.setText(QCoreApplication.translate("MiniEpochDefinition", u"Name for the Tonic mini-epoch", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MiniEpochDefinition", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Mini-epochs length value configuration</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto-Regular';\">Configurable mini-epoch lengths (e.g., 3, 5, 10 or 30s) enable finer characterization of REM microstructure by capturing brief phasic bursts and se"
                        "parating tonic and phasic activity within standard 30-s REM epochs.</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MiniEpochDefinition", u"Window length (sec)                ", None))
        self.comboBox_length.setItemText(0, QCoreApplication.translate("MiniEpochDefinition", u"3", None))
        self.comboBox_length.setItemText(1, QCoreApplication.translate("MiniEpochDefinition", u"5", None))
        self.comboBox_length.setItemText(2, QCoreApplication.translate("MiniEpochDefinition", u"10", None))
        self.comboBox_length.setItemText(3, QCoreApplication.translate("MiniEpochDefinition", u"30", None))

    # retranslateUi

