# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SlowWaveClassifierSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QHBoxLayout,
    QLabel, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)
import themes_rc

class Ui_SlowWaveClassifierSettingsView(object):
    def setupUi(self, SlowWaveClassifierSettingsView):
        if not SlowWaveClassifierSettingsView.objectName():
            SlowWaveClassifierSettingsView.setObjectName(u"SlowWaveClassifierSettingsView")
        SlowWaveClassifierSettingsView.resize(900, 700)
        self.verticalLayout = QVBoxLayout(SlowWaveClassifierSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(SlowWaveClassifierSettingsView)
        self.content_widget.setObjectName(u"content_widget")
        self.content_widget.setMaximumSize(QSize(800, 16777215))
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setSpacing(16)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 0, 0)
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
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.criteria_card_layout.addWidget(self.label)

        self.textEdit = QLabel(self.criteria_card)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setWordWrap(True)
        self.textEdit.setProperty(u"variant", u"help")

        self.criteria_card_layout.addWidget(self.textEdit)

        self.criteria_options = QVBoxLayout()
        self.criteria_options.setSpacing(8)
        self.criteria_options.setObjectName(u"criteria_options")
        self.criteria_options_1_layout = QVBoxLayout()
        self.criteria_options_1_layout.setSpacing(2)
        self.criteria_options_1_layout.setObjectName(u"criteria_options_1_layout")
        self.radioButton_automatic_classification = QRadioButton(self.criteria_card)
        self.buttonGroup = QButtonGroup(SlowWaveClassifierSettingsView)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_automatic_classification)
        self.radioButton_automatic_classification.setObjectName(u"radioButton_automatic_classification")
        self.radioButton_automatic_classification.setChecked(True)

        self.criteria_options_1_layout.addWidget(self.radioButton_automatic_classification)

        self.automatic_help_label = QLabel(self.criteria_card)
        self.automatic_help_label.setObjectName(u"automatic_help_label")
        font1 = QFont()
        font1.setPointSize(10)
        self.automatic_help_label.setFont(font1)
        self.automatic_help_label.setWordWrap(True)
        self.automatic_help_label.setIndent(26)
        self.automatic_help_label.setProperty(u"variant", u"help")

        self.criteria_options_1_layout.addWidget(self.automatic_help_label)


        self.criteria_options.addLayout(self.criteria_options_1_layout)

        self.criteria_options_line_1 = QFrame(self.criteria_card)
        self.criteria_options_line_1.setObjectName(u"criteria_options_line_1")
        self.criteria_options_line_1.setFrameShape(QFrame.Shape.HLine)
        self.criteria_options_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.criteria_options.addWidget(self.criteria_options_line_1)

        self.criteria_options_2_layout = QVBoxLayout()
        self.criteria_options_2_layout.setSpacing(2)
        self.criteria_options_2_layout.setObjectName(u"criteria_options_2_layout")
        self.radioButton_categories = QRadioButton(self.criteria_card)
        self.buttonGroup.addButton(self.radioButton_categories)
        self.radioButton_categories.setObjectName(u"radioButton_categories")

        self.criteria_options_2_layout.addWidget(self.radioButton_categories)

        self.categories_layout = QVBoxLayout()
        self.categories_layout.setSpacing(8)
        self.categories_layout.setObjectName(u"categories_layout")
        self.categories_help_label = QLabel(self.criteria_card)
        self.categories_help_label.setObjectName(u"categories_help_label")
        self.categories_help_label.setFont(font1)
        self.categories_help_label.setWordWrap(True)
        self.categories_help_label.setIndent(26)
        self.categories_help_label.setProperty(u"variant", u"help")

        self.categories_layout.addWidget(self.categories_help_label)

        self.num_categories_layout = QHBoxLayout()
        self.num_categories_layout.setSpacing(12)
        self.num_categories_layout.setObjectName(u"num_categories_layout")
        self.num_categories_layout.setContentsMargins(26, 0, 0, 0)
        self.categories_label = QLabel(self.criteria_card)
        self.categories_label.setObjectName(u"categories_label")
        self.categories_label.setEnabled(False)

        self.num_categories_layout.addWidget(self.categories_label)

        self.num_categories_spinBox = QSpinBox(self.criteria_card)
        self.num_categories_spinBox.setObjectName(u"num_categories_spinBox")
        self.num_categories_spinBox.setEnabled(False)
        self.num_categories_spinBox.setMinimum(1)
        self.num_categories_spinBox.setMaximum(4)
        self.num_categories_spinBox.setValue(2)

        self.num_categories_layout.addWidget(self.num_categories_spinBox)

        self.num_categories_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.num_categories_layout.addItem(self.num_categories_spacer)

        self.num_categories_layout.setStretch(2, 1)

        self.categories_layout.addLayout(self.num_categories_layout)


        self.criteria_options_2_layout.addLayout(self.categories_layout)


        self.criteria_options.addLayout(self.criteria_options_2_layout)


        self.criteria_card_layout.addLayout(self.criteria_options)


        self.content_layout.addWidget(self.criteria_card)

        self.about_categories_layout = QVBoxLayout()
        self.about_categories_layout.setSpacing(6)
        self.about_categories_layout.setObjectName(u"about_categories_layout")
        self.about_categories_title_label = QLabel(self.content_widget)
        self.about_categories_title_label.setObjectName(u"about_categories_title_label")
        self.about_categories_title_label.setFont(font)

        self.about_categories_layout.addWidget(self.about_categories_title_label)

        self.about_categories_label = QLabel(self.content_widget)
        self.about_categories_label.setObjectName(u"about_categories_label")
        self.about_categories_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_categories_label.setWordWrap(True)
        self.about_categories_label.setProperty(u"variant", u"help")

        self.about_categories_layout.addWidget(self.about_categories_label)


        self.content_layout.addLayout(self.about_categories_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SlowWaveClassifierSettingsView)

        QMetaObject.connectSlotsByName(SlowWaveClassifierSettingsView)
    # setupUi

    def retranslateUi(self, SlowWaveClassifierSettingsView):
        SlowWaveClassifierSettingsView.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"Number of categories", None))
        self.textEdit.setText(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"For an automatic classification, keep the settings as they are. For a manual classification, choose \"Set the number of categories\", then change the number of categories.", None))
        self.radioButton_automatic_classification.setText(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"Classify automatically", None))
        self.automatic_help_label.setText(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"Snooz finds the number of categories, from 1 to 4, that best fits the transition frequencies.", None))
        self.radioButton_categories.setText(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"Set the number of categories", None))
        self.categories_help_label.setText(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"Snooz classifies the slow waves into the number of categories set below, from 1 to 4.", None))
        self.categories_label.setText(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"Number of categories", None))
        self.about_categories_title_label.setText(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"About the number of categories", None))
        self.about_categories_label.setText(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"<b>Automatic classification</b><br/>\u2022 Snooz fits Gaussian mixtures of 1, 2, 3 and 4 components to the distribution of the transition frequencies.<br/>\u2022 It keeps the mixture with the lowest Akaike information criterion (AIC), the one that fits best. The AIC weighs the fit against the number of components.<br/>\u2022 The number of components of this mixture is the number of categories in the data.<br/>\u2022 The log of the run lists the AIC of each mixture. The picture saved in the output folder shows them.<br/><br/><b>Manual classification</b><br/>\u2022 Snooz fits one Gaussian mixture, with the number of categories you set as its number of components.<br/>\u2022 Useful when the automatic classification does not analyze your data correctly, or when you already know the number of categories in the data.<br/>\u2022 For example, classify the whole cohort automatically to find the number of categories. Then set this number to classify each subject, if you also analyze the subjects one by one.", None))
    # retranslateUi

