# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_GroupDefinition.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QListView, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_GroupDefinition(object):
    def setupUi(self, GroupDefinition):
        if not GroupDefinition.objectName():
            GroupDefinition.setObjectName(u"GroupDefinition")
        GroupDefinition.resize(900, 700)
        self.verticalLayout = QVBoxLayout(GroupDefinition)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.header_layout = QVBoxLayout()
        self.header_layout.setSpacing(6)
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(GroupDefinition)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.header_layout.addWidget(self.title_label)

        self.subtitle_label = QLabel(GroupDefinition)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setProperty(u"variant", u"help")

        self.header_layout.addWidget(self.subtitle_label)


        self.verticalLayout.addLayout(self.header_layout)

        self.lists_layout = QHBoxLayout()
        self.lists_layout.setSpacing(16)
        self.lists_layout.setObjectName(u"lists_layout")
        self.files_card = QFrame(GroupDefinition)
        self.files_card.setObjectName(u"files_card")
        self.files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.files_card_layout = QVBoxLayout(self.files_card)
        self.files_card_layout.setSpacing(10)
        self.files_card_layout.setObjectName(u"files_card_layout")
        self.files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.files_card)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)

        self.files_card_layout.addWidget(self.label)

        self.file_listview = QListView(self.files_card)
        self.file_listview.setObjectName(u"file_listview")

        self.files_card_layout.addWidget(self.file_listview)


        self.lists_layout.addWidget(self.files_card)

        self.events_card = QFrame(GroupDefinition)
        self.events_card.setObjectName(u"events_card")
        self.events_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.events_card.setFrameShadow(QFrame.Shadow.Raised)
        self.events_card_layout = QVBoxLayout(self.events_card)
        self.events_card_layout.setSpacing(10)
        self.events_card_layout.setObjectName(u"events_card_layout")
        self.events_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.events_card)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.events_card_layout.addWidget(self.label_2)

        self.event_treeview = QTableView(self.events_card)
        self.event_treeview.setObjectName(u"event_treeview")
        self.event_treeview.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.event_treeview.setSelectionMode(QAbstractItemView.NoSelection)
        self.event_treeview.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.event_treeview.horizontalHeader().setDefaultSectionSize(180)
        self.event_treeview.horizontalHeader().setStretchLastSection(True)
        self.event_treeview.verticalHeader().setVisible(False)

        self.events_card_layout.addWidget(self.event_treeview)

        self.events_buttons_layout = QHBoxLayout()
        self.events_buttons_layout.setSpacing(8)
        self.events_buttons_layout.setObjectName(u"events_buttons_layout")
        self.events_buttons_layout_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.events_buttons_layout.addItem(self.events_buttons_layout_spacer)

        self.apply_all_pushButton = QPushButton(self.events_card)
        self.apply_all_pushButton.setObjectName(u"apply_all_pushButton")

        self.events_buttons_layout.addWidget(self.apply_all_pushButton)

        self.reset_all_files_pushButton = QPushButton(self.events_card)
        self.reset_all_files_pushButton.setObjectName(u"reset_all_files_pushButton")

        self.events_buttons_layout.addWidget(self.reset_all_files_pushButton)

        self.events_buttons_layout.setStretch(0, 1)

        self.events_card_layout.addLayout(self.events_buttons_layout)


        self.lists_layout.addWidget(self.events_card)

        self.lists_layout.setStretch(0, 1)
        self.lists_layout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.lists_layout)


        self.retranslateUi(GroupDefinition)
        self.file_listview.clicked.connect(GroupDefinition.on_file_selected)
        self.apply_all_pushButton.clicked.connect(GroupDefinition.on_apply_to_all_files)
        self.reset_all_files_pushButton.clicked.connect(GroupDefinition.on_reset_all_files)

        QMetaObject.connectSlotsByName(GroupDefinition)
    # setupUi

    def retranslateUi(self, GroupDefinition):
        GroupDefinition.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("GroupDefinition", u"Event Group Definition", None))
        self.subtitle_label.setText(QCoreApplication.translate("GroupDefinition", u"Optionally, edit the group of the annotations. The default group is EDFbrowser. The sleep stages and the artifacts checked in the previous steps have the group stage or art_snooz.", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("GroupDefinition", u"Select an EDFbrowser file to show its annotations.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("GroupDefinition", u"EDFbrowser files", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("GroupDefinition", u"Double-click a group to edit it.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("GroupDefinition", u"Annotations", None))
#if QT_CONFIG(tooltip)
        self.apply_all_pushButton.setToolTip(QCoreApplication.translate("GroupDefinition", u"Gives the groups of the selected file to all the files.", None))
#endif // QT_CONFIG(tooltip)
        self.apply_all_pushButton.setText(QCoreApplication.translate("GroupDefinition", u"Apply to all files", None))
#if QT_CONFIG(tooltip)
        self.reset_all_files_pushButton.setToolTip(QCoreApplication.translate("GroupDefinition", u"Gives back the default groups to all the files.", None))
#endif // QT_CONFIG(tooltip)
        self.reset_all_files_pushButton.setText(QCoreApplication.translate("GroupDefinition", u"Reset all files", None))
    # retranslateUi

