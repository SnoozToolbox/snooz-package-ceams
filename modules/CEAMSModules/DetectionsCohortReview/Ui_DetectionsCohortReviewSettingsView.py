# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DetectionsCohortReviewSettingsView.ui'
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

class Ui_DetectionsCohortReviewSettingsView(object):
    def setupUi(self, DetectionsCohortReviewSettingsView):
        if not DetectionsCohortReviewSettingsView.objectName():
            DetectionsCohortReviewSettingsView.setObjectName(u"DetectionsCohortReviewSettingsView")
        DetectionsCohortReviewSettingsView.resize(900, 700)
        self.verticalLayout = QVBoxLayout(DetectionsCohortReviewSettingsView)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lists_layout = QHBoxLayout()
        self.lists_layout.setSpacing(16)
        self.lists_layout.setObjectName(u"lists_layout")
        self.subjects_card = QFrame(DetectionsCohortReviewSettingsView)
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

        self.subject_channels_card = QFrame(DetectionsCohortReviewSettingsView)
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

        self.cohort_channels_card = QFrame(DetectionsCohortReviewSettingsView)
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

        self.information_card = QFrame(DetectionsCohortReviewSettingsView)
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


        self.retranslateUi(DetectionsCohortReviewSettingsView)
        self.clear_pushButton.clicked.connect(DetectionsCohortReviewSettingsView.clear_subject_slot)
        self.add_pushButton.clicked.connect(DetectionsCohortReviewSettingsView.add_subject_slot)
        self.all_subject_chan_checkBox.clicked.connect(DetectionsCohortReviewSettingsView.select_all_subject_chan_slot)
        self.all_cohort_chan_checkBox.clicked.connect(DetectionsCohortReviewSettingsView.select_all_cohort_chan_slot)
        self.add_ROI_pushButton.clicked.connect(DetectionsCohortReviewSettingsView.add_ROI_slot)
        self.subject_listView.clicked.connect(DetectionsCohortReviewSettingsView.subject_selection_changed_slot)

        QMetaObject.connectSlotsByName(DetectionsCohortReviewSettingsView)
    # setupUi

    def retranslateUi(self, DetectionsCohortReviewSettingsView):
        DetectionsCohortReviewSettingsView.setWindowTitle("")
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"The subjects of the reports added. Select a subject to show its channels.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Subjects", None))
#if QT_CONFIG(tooltip)
        self.clear_pushButton.setToolTip(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Removes all the reports.", None))
#endif // QT_CONFIG(tooltip)
        self.clear_pushButton.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Clear", None))
#if QT_CONFIG(tooltip)
        self.add_pushButton.setToolTip(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Adds detailed events cohort reports (.tsv).", None))
#endif // QT_CONFIG(tooltip)
        self.add_pushButton.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Add reports", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"The channels of the selected subject. Double-click a label to rename the channel for this subject; uncheck a channel to remove it.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Channels of the subject", None))
        self.all_subject_chan_checkBox.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Select All", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"The channels of all the subjects. A label renamed here is renamed for every subject; uncheck a channel to remove it from every subject.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Channels of the cohort", None))
        self.all_cohort_chan_checkBox.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Select All", None))
#if QT_CONFIG(tooltip)
        self.add_ROI_pushButton.setToolTip(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Averages channels into a region of interest (ROI), for every subject: check the channels to include. Check blank to leave the ROI empty when data are missing; otherwise the missing data are ignored. Rename your channel labels first. Adding the ROIs must be the final step.", None))
#endif // QT_CONFIG(tooltip)
        self.add_ROI_pushButton.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Add ROI", None))
        self.label_4.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Report information", None))
    # retranslateUi

