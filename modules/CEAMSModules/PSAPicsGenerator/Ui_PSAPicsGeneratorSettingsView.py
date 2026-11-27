# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_PSAPicsGeneratorSettingsView.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QHBoxLayout, QLabel, QListView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_PSAPicsGeneratorSettingsView(object):
    def setupUi(self, PSAPicsGeneratorSettingsView):
        if not PSAPicsGeneratorSettingsView.objectName():
            PSAPicsGeneratorSettingsView.setObjectName(u"PSAPicsGeneratorSettingsView")
        PSAPicsGeneratorSettingsView.resize(900, 700)
        self.verticalLayout = QVBoxLayout(PSAPicsGeneratorSettingsView)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lists_layout = QHBoxLayout()
        self.lists_layout.setSpacing(16)
        self.lists_layout.setObjectName(u"lists_layout")
        self.subjects_card = QFrame(PSAPicsGeneratorSettingsView)
        self.subjects_card.setObjectName(u"subjects_card")
        self.subjects_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.subjects_card.setFrameShadow(QFrame.Shadow.Raised)
        self.subjects_card_layout = QVBoxLayout(self.subjects_card)
        self.subjects_card_layout.setSpacing(10)
        self.subjects_card_layout.setObjectName(u"subjects_card_layout")
        self.subjects_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.subjects_card)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.subjects_card_layout.addWidget(self.label)

        self.subject_listView = QListView(self.subjects_card)
        self.subject_listView.setObjectName(u"subject_listView")
        self.subject_listView.setMinimumSize(QSize(0, 240))
        self.subject_listView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.subjects_card_layout.addWidget(self.subject_listView)

        self.subjects_buttons_layout = QHBoxLayout()
        self.subjects_buttons_layout.setSpacing(8)
        self.subjects_buttons_layout.setObjectName(u"subjects_buttons_layout")
        self.clear_pushButton = QPushButton(self.subjects_card)
        self.clear_pushButton.setObjectName(u"clear_pushButton")

        self.subjects_buttons_layout.addWidget(self.clear_pushButton)

        self.add_pushButton = QPushButton(self.subjects_card)
        self.add_pushButton.setObjectName(u"add_pushButton")

        self.subjects_buttons_layout.addWidget(self.add_pushButton)


        self.subjects_card_layout.addLayout(self.subjects_buttons_layout)


        self.lists_layout.addWidget(self.subjects_card)

        self.subject_channels_card = QFrame(PSAPicsGeneratorSettingsView)
        self.subject_channels_card.setObjectName(u"subject_channels_card")
        self.subject_channels_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.subject_channels_card.setFrameShadow(QFrame.Shadow.Raised)
        self.subject_channels_card_layout = QVBoxLayout(self.subject_channels_card)
        self.subject_channels_card_layout.setSpacing(10)
        self.subject_channels_card_layout.setObjectName(u"subject_channels_card_layout")
        self.subject_channels_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.subject_channels_card)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.subject_channels_card_layout.addWidget(self.label_2)

        self.chan_subject_listView = QListView(self.subject_channels_card)
        self.chan_subject_listView.setObjectName(u"chan_subject_listView")
        self.chan_subject_listView.setMinimumSize(QSize(0, 240))

        self.subject_channels_card_layout.addWidget(self.chan_subject_listView)

        self.all_subject_chan_checkBox = QCheckBox(self.subject_channels_card)
        self.all_subject_chan_checkBox.setObjectName(u"all_subject_chan_checkBox")

        self.subject_channels_card_layout.addWidget(self.all_subject_chan_checkBox)


        self.lists_layout.addWidget(self.subject_channels_card)

        self.cohort_channels_card = QFrame(PSAPicsGeneratorSettingsView)
        self.cohort_channels_card.setObjectName(u"cohort_channels_card")
        self.cohort_channels_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.cohort_channels_card.setFrameShadow(QFrame.Shadow.Raised)
        self.cohort_channels_card_layout = QVBoxLayout(self.cohort_channels_card)
        self.cohort_channels_card_layout.setSpacing(10)
        self.cohort_channels_card_layout.setObjectName(u"cohort_channels_card_layout")
        self.cohort_channels_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_3 = QLabel(self.cohort_channels_card)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.cohort_channels_card_layout.addWidget(self.label_3)

        self.chan_cohort_listWidget = QListWidget(self.cohort_channels_card)
        self.chan_cohort_listWidget.setObjectName(u"chan_cohort_listWidget")
        self.chan_cohort_listWidget.setMinimumSize(QSize(0, 240))

        self.cohort_channels_card_layout.addWidget(self.chan_cohort_listWidget)

        self.cohort_tools_layout = QHBoxLayout()
        self.cohort_tools_layout.setSpacing(10)
        self.cohort_tools_layout.setObjectName(u"cohort_tools_layout")
        self.all_cohort_chan_checkBox = QCheckBox(self.cohort_channels_card)
        self.all_cohort_chan_checkBox.setObjectName(u"all_cohort_chan_checkBox")

        self.cohort_tools_layout.addWidget(self.all_cohort_chan_checkBox)

        self.cohort_tools_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cohort_tools_layout.addItem(self.cohort_tools_spacer)

        self.add_ROI_pushButton = QPushButton(self.cohort_channels_card)
        self.add_ROI_pushButton.setObjectName(u"add_ROI_pushButton")

        self.cohort_tools_layout.addWidget(self.add_ROI_pushButton)


        self.cohort_channels_card_layout.addLayout(self.cohort_tools_layout)


        self.lists_layout.addWidget(self.cohort_channels_card)

        self.lists_layout.setStretch(0, 1)
        self.lists_layout.setStretch(1, 1)
        self.lists_layout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.lists_layout)

        self.information_card = QFrame(PSAPicsGeneratorSettingsView)
        self.information_card.setObjectName(u"information_card")
        self.information_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.information_card.setFrameShadow(QFrame.Shadow.Raised)
        self.information_card_layout = QVBoxLayout(self.information_card)
        self.information_card_layout.setSpacing(10)
        self.information_card_layout.setObjectName(u"information_card_layout")
        self.information_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_4 = QLabel(self.information_card)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.information_card_layout.addWidget(self.label_4)

        self.message_textEdit = QTextEdit(self.information_card)
        self.message_textEdit.setObjectName(u"message_textEdit")
        self.message_textEdit.setReadOnly(True)

        self.information_card_layout.addWidget(self.message_textEdit)


        self.verticalLayout.addWidget(self.information_card)

        self.about_inputs_layout = QVBoxLayout()
        self.about_inputs_layout.setSpacing(6)
        self.about_inputs_layout.setObjectName(u"about_inputs_layout")
        self.about_inputs_title_label = QLabel(PSAPicsGeneratorSettingsView)
        self.about_inputs_title_label.setObjectName(u"about_inputs_title_label")
        self.about_inputs_title_label.setFont(font)

        self.about_inputs_layout.addWidget(self.about_inputs_title_label)

        self.about_inputs_label = QLabel(PSAPicsGeneratorSettingsView)
        self.about_inputs_label.setObjectName(u"about_inputs_label")
        self.about_inputs_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_inputs_label.setWordWrap(True)
        self.about_inputs_label.setProperty(u"variant", u"help")

        self.about_inputs_layout.addWidget(self.about_inputs_label)


        self.verticalLayout.addLayout(self.about_inputs_layout)


        self.retranslateUi(PSAPicsGeneratorSettingsView)
        self.clear_pushButton.clicked.connect(PSAPicsGeneratorSettingsView.clear_subject_slot)
        self.add_pushButton.clicked.connect(PSAPicsGeneratorSettingsView.add_subject_slot)
        self.all_subject_chan_checkBox.clicked.connect(PSAPicsGeneratorSettingsView.select_all_subject_chan_slot)
        self.all_cohort_chan_checkBox.clicked.connect(PSAPicsGeneratorSettingsView.select_all_cohort_chan_slot)
        self.add_ROI_pushButton.clicked.connect(PSAPicsGeneratorSettingsView.add_ROI_slot)
        self.subject_listView.clicked.connect(PSAPicsGeneratorSettingsView.subject_selection_changed_slot)

        QMetaObject.connectSlotsByName(PSAPicsGeneratorSettingsView)
    # setupUi

    def retranslateUi(self, PSAPicsGeneratorSettingsView):
        PSAPicsGeneratorSettingsView.setWindowTitle("")
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"The subjects of the reports added. Select a subject to show its channels.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"Subjects", None))
#if QT_CONFIG(tooltip)
        self.clear_pushButton.setToolTip(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"Removes all the reports.", None))
#endif // QT_CONFIG(tooltip)
        self.clear_pushButton.setText(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"Clear", None))
#if QT_CONFIG(tooltip)
        self.add_pushButton.setToolTip(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"Adds EEG spectral power reports (.tsv).", None))
#endif // QT_CONFIG(tooltip)
        self.add_pushButton.setText(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"Add reports", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"The channels and ROIs of the selected subject. Check the ones to display.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"Channels of the subject", None))
        self.all_subject_chan_checkBox.setText(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"Select All", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"The channels of all the subjects. Check a channel to display it for all the subjects.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"Channels of the cohort", None))
        self.all_cohort_chan_checkBox.setText(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"Select All", None))
#if QT_CONFIG(tooltip)
        self.add_ROI_pushButton.setToolTip(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"Averages channels into a region of interest (ROI) for all the subjects. Adding the ROIs must be the final step.", None))
#endif // QT_CONFIG(tooltip)
        self.add_ROI_pushButton.setText(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"Add ROI", None))
        self.label_4.setText(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"Report information", None))
        self.about_inputs_title_label.setText(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"About the reports, channels and ROIs", None))
        self.about_inputs_label.setText(QCoreApplication.translate("PSAPicsGeneratorSettingsView", u"<b>EEG spectral power reports</b><br/>\u2022 Add your EEG spectral power reports, written by \"Analyze EEG Spectral Power\". You can add more than one report.<br/>\u2022 Each recording of the reports is a subject of \"Subjects\".<br/><br/><b>Channels</b><br/>\u2022 Select the channels to display in \"Channels of the subject\" or in \"Channels of the cohort\".<br/>\u2022 The channel labels cannot be edited here. To change the labels shown on the pictures, first edit them with \"Review EEG Spectral Power for the cohort\". Then add its clean report here.<br/><br/><b>Regions of interest</b><br/>\u2022 Add ROIs and select them. An ROI groups channels with similar labels together, for example C3-A2, C3-M2 and C3.<br/>\u2022 Click \"Add ROI\", then check the channels to include. Check \"blank\" to leave the ROI empty when data are missing for the mean. Otherwise the missing data are ignored.<br/>\u2022 The ROI is named ROI_ followed by its channel labels, with _b at the end when \"blank\" is checked. For example, ROI"
                        "_C3C4 for the channels C3 and C4.<br/>\u2022 You can display channels, ROIs, or both.", None))
    # retranslateUi

