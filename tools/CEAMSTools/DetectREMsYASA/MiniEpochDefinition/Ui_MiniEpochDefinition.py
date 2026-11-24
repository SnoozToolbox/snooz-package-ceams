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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_MiniEpochDefinition(object):
    def setupUi(self, MiniEpochDefinition):
        if not MiniEpochDefinition.objectName():
            MiniEpochDefinition.setObjectName(u"MiniEpochDefinition")
        MiniEpochDefinition.resize(900, 700)
        self.verticalLayout = QVBoxLayout(MiniEpochDefinition)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(MiniEpochDefinition)
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

        self.mini_epoch_cards_layout = QHBoxLayout()
        self.mini_epoch_cards_layout.setSpacing(16)
        self.mini_epoch_cards_layout.setObjectName(u"mini_epoch_cards_layout")
        self.names_card = QFrame(self.content_widget)
        self.names_card.setObjectName(u"names_card")
        self.names_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.names_card.setFrameShadow(QFrame.Shadow.Raised)
        self.names_card_layout = QVBoxLayout(self.names_card)
        self.names_card_layout.setSpacing(10)
        self.names_card_layout.setObjectName(u"names_card_layout")
        self.names_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_5 = QLabel(self.names_card)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setBold(True)
        self.label_5.setFont(font1)

        self.names_card_layout.addWidget(self.label_5)

        self.label_6 = QLabel(self.names_card)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)
        self.label_6.setProperty(u"variant", u"help")

        self.names_card_layout.addWidget(self.label_6)

        self.names_grid = QGridLayout()
        self.names_grid.setObjectName(u"names_grid")
        self.names_grid.setHorizontalSpacing(12)
        self.names_grid.setVerticalSpacing(10)
        self.label = QLabel(self.names_card)
        self.label.setObjectName(u"label")

        self.names_grid.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_group = QLineEdit(self.names_card)
        self.lineEdit_group.setObjectName(u"lineEdit_group")

        self.names_grid.addWidget(self.lineEdit_group, 0, 1, 1, 1)

        self.label_2 = QLabel(self.names_card)
        self.label_2.setObjectName(u"label_2")

        self.names_grid.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_name_Phasic = QLineEdit(self.names_card)
        self.lineEdit_name_Phasic.setObjectName(u"lineEdit_name_Phasic")

        self.names_grid.addWidget(self.lineEdit_name_Phasic, 1, 1, 1, 1)

        self.label_3 = QLabel(self.names_card)
        self.label_3.setObjectName(u"label_3")

        self.names_grid.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_name_Tonic = QLineEdit(self.names_card)
        self.lineEdit_name_Tonic.setObjectName(u"lineEdit_name_Tonic")

        self.names_grid.addWidget(self.lineEdit_name_Tonic, 2, 1, 1, 1)

        self.names_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.names_grid.addItem(self.names_grid_spacer, 0, 3, 1, 1)


        self.names_card_layout.addLayout(self.names_grid)

        self.names_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.names_card_layout.addItem(self.names_stretch)


        self.mini_epoch_cards_layout.addWidget(self.names_card)

        self.length_card = QFrame(self.content_widget)
        self.length_card.setObjectName(u"length_card")
        self.length_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.length_card.setFrameShadow(QFrame.Shadow.Raised)
        self.length_card_layout = QVBoxLayout(self.length_card)
        self.length_card_layout.setSpacing(10)
        self.length_card_layout.setObjectName(u"length_card_layout")
        self.length_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_7 = QLabel(self.length_card)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.length_card_layout.addWidget(self.label_7)

        self.length_grid = QGridLayout()
        self.length_grid.setObjectName(u"length_grid")
        self.length_grid.setHorizontalSpacing(12)
        self.length_grid.setVerticalSpacing(10)
        self.label_8 = QLabel(self.length_card)
        self.label_8.setObjectName(u"label_8")

        self.length_grid.addWidget(self.label_8, 0, 0, 1, 1)

        self.comboBox_length = QComboBox(self.length_card)
        self.comboBox_length.addItem("")
        self.comboBox_length.addItem("")
        self.comboBox_length.addItem("")
        self.comboBox_length.addItem("")
        self.comboBox_length.setObjectName(u"comboBox_length")

        self.length_grid.addWidget(self.comboBox_length, 0, 1, 1, 1)

        self.length_unit_label = QLabel(self.length_card)
        self.length_unit_label.setObjectName(u"length_unit_label")
        self.length_unit_label.setProperty(u"variant", u"help")

        self.length_grid.addWidget(self.length_unit_label, 0, 2, 1, 1)

        self.length_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.length_grid.addItem(self.length_grid_spacer, 0, 3, 1, 1)


        self.length_card_layout.addLayout(self.length_grid)

        self.length_help_label = QLabel(self.length_card)
        self.length_help_label.setObjectName(u"length_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.length_help_label.setFont(font2)
        self.length_help_label.setWordWrap(True)
        self.length_help_label.setProperty(u"variant", u"help")

        self.length_card_layout.addWidget(self.length_help_label)

        self.length_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.length_card_layout.addItem(self.length_stretch)


        self.mini_epoch_cards_layout.addWidget(self.length_card)

        self.mini_epoch_cards_layout.setStretch(0, 1)
        self.mini_epoch_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.mini_epoch_cards_layout)

        self.about_mini_epochs_layout = QVBoxLayout()
        self.about_mini_epochs_layout.setSpacing(6)
        self.about_mini_epochs_layout.setObjectName(u"about_mini_epochs_layout")
        self.label_4 = QLabel(self.content_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.about_mini_epochs_layout.addWidget(self.label_4)

        self.label_9 = QLabel(self.content_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setTextFormat(Qt.TextFormat.RichText)
        self.label_9.setWordWrap(True)
        self.label_9.setProperty(u"variant", u"help")

        self.about_mini_epochs_layout.addWidget(self.label_9)


        self.content_layout.addLayout(self.about_mini_epochs_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(MiniEpochDefinition)

        QMetaObject.connectSlotsByName(MiniEpochDefinition)
    # setupUi

    def retranslateUi(self, MiniEpochDefinition):
        MiniEpochDefinition.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("MiniEpochDefinition", u"Mini-Epoch Classification Step", None))
        self.subtitle_label.setText(QCoreApplication.translate("MiniEpochDefinition", u"Define the group, the names and the length of the mini-epochs of phasic and tonic REM sleep.", None))
        self.label_5.setText(QCoreApplication.translate("MiniEpochDefinition", u"Mini-epoch events", None))
        self.label_6.setText(QCoreApplication.translate("MiniEpochDefinition", u"Each event belongs to a group and is labeled by a name.", None))
        self.label.setText(QCoreApplication.translate("MiniEpochDefinition", u"Group", None))
        self.label_2.setText(QCoreApplication.translate("MiniEpochDefinition", u"Phasic name", None))
        self.label_3.setText(QCoreApplication.translate("MiniEpochDefinition", u"Tonic name", None))
        self.label_7.setText(QCoreApplication.translate("MiniEpochDefinition", u"Mini-epoch length", None))
        self.label_8.setText(QCoreApplication.translate("MiniEpochDefinition", u"Window length", None))
        self.comboBox_length.setItemText(0, QCoreApplication.translate("MiniEpochDefinition", u"3", None))
        self.comboBox_length.setItemText(1, QCoreApplication.translate("MiniEpochDefinition", u"5", None))
        self.comboBox_length.setItemText(2, QCoreApplication.translate("MiniEpochDefinition", u"10", None))
        self.comboBox_length.setItemText(3, QCoreApplication.translate("MiniEpochDefinition", u"30", None))

        self.length_unit_label.setText(QCoreApplication.translate("MiniEpochDefinition", u"s", None))
        self.length_help_label.setText(QCoreApplication.translate("MiniEpochDefinition", u"Short mini-epochs (3, 5 or 10 s) capture the brief phasic bursts and separate the tonic and phasic activity within the standard 30-s REM epochs.", None))
        self.label_4.setText(QCoreApplication.translate("MiniEpochDefinition", u"About phasic and tonic REM sleep", None))
        self.label_9.setText(QCoreApplication.translate("MiniEpochDefinition", u"<b>Tonic REM</b> corresponds to a more stable REM activity, with minimal eye movements and a lower physiological variability. <b>Phasic REM</b> is characterized by bursts of rapid eye movements, transient muscle activity, and an increased neural and autonomic activation. This separation enables a more detailed investigation of the REM sleep dynamics and of the related biomarkers.<br/><br/>The REM sleep epochs are divided into mini-epochs of the chosen length. A mini-epoch is phasic when it holds at least a third of the duration of a detected REM, tonic otherwise.", None))
    # retranslateUi

