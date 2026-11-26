# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SelectStagesStep.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QPushButton, QSizePolicy, QTreeView,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_SelectStagesStep(object):
    def setupUi(self, SelectStagesStep):
        if not SelectStagesStep.objectName():
            SelectStagesStep.setObjectName(u"SelectStagesStep")
        SelectStagesStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(SelectStagesStep)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.header_layout = QVBoxLayout()
        self.header_layout.setSpacing(6)
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(SelectStagesStep)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.header_layout.addWidget(self.title_label)

        self.subtitle_label = QLabel(SelectStagesStep)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setProperty(u"variant", u"help")

        self.header_layout.addWidget(self.subtitle_label)


        self.verticalLayout.addLayout(self.header_layout)

        self.lists_layout = QHBoxLayout()
        self.lists_layout.setSpacing(16)
        self.lists_layout.setObjectName(u"lists_layout")
        self.files_card = QFrame(SelectStagesStep)
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
        self.file_listview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.file_listview.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.file_listview.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.files_card_layout.addWidget(self.file_listview)


        self.lists_layout.addWidget(self.files_card)

        self.events_card = QFrame(SelectStagesStep)
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

        self.event_treeview = QTreeView(self.events_card)
        self.event_treeview.setObjectName(u"event_treeview")
        self.event_treeview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.event_treeview.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.event_treeview.setSelectionMode(QAbstractItemView.SingleSelection)
        self.event_treeview.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.events_card_layout.addWidget(self.event_treeview)

        self.events_tools_layout = QHBoxLayout()
        self.events_tools_layout.setSpacing(10)
        self.events_tools_layout.setObjectName(u"events_tools_layout")
        self.select_all_checkBox = QCheckBox(self.events_card)
        self.select_all_checkBox.setObjectName(u"select_all_checkBox")

        self.events_tools_layout.addWidget(self.select_all_checkBox)

        self.search_lineEdit = QLineEdit(self.events_card)
        self.search_lineEdit.setObjectName(u"search_lineEdit")

        self.events_tools_layout.addWidget(self.search_lineEdit)

        self.reset_all_files_pushButton = QPushButton(self.events_card)
        self.reset_all_files_pushButton.setObjectName(u"reset_all_files_pushButton")

        self.events_tools_layout.addWidget(self.reset_all_files_pushButton)

        self.events_tools_layout.setStretch(1, 1)

        self.events_card_layout.addLayout(self.events_tools_layout)

        self.reset_excl_event_checkBox = QCheckBox(self.events_card)
        self.reset_excl_event_checkBox.setObjectName(u"reset_excl_event_checkBox")
        self.reset_excl_event_checkBox.setVisible(False)

        self.events_card_layout.addWidget(self.reset_excl_event_checkBox)


        self.lists_layout.addWidget(self.events_card)

        self.lists_layout.setStretch(0, 1)
        self.lists_layout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.lists_layout)


        self.retranslateUi(SelectStagesStep)
        self.file_listview.clicked.connect(SelectStagesStep.on_file_selected)
        self.select_all_checkBox.stateChanged.connect(SelectStagesStep.on_select_all_groups)
        self.reset_all_files_pushButton.clicked.connect(SelectStagesStep.on_reset_all_files)
        self.search_lineEdit.textEdited.connect(SelectStagesStep.search_pattern_slot)

        QMetaObject.connectSlotsByName(SelectStagesStep)
    # setupUi

    def retranslateUi(self, SelectStagesStep):
        SelectStagesStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("SelectStagesStep", u"Select Stages", None))
        self.subtitle_label.setText(QCoreApplication.translate("SelectStagesStep", u"Check the sleep stages to save in the output file, for each PSG file. The list shows the stage labels renamed for Snooz (stage group).", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("SelectStagesStep", u"Select one or more files (Ctrl or Shift key) to show their sleep stages.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("SelectStagesStep", u"PSG files", None))
        self.label_2.setText(QCoreApplication.translate("SelectStagesStep", u"Events", None))
#if QT_CONFIG(tooltip)
        self.select_all_checkBox.setToolTip(QCoreApplication.translate("SelectStagesStep", u"Checks the stages shown for the selected files.", None))
#endif // QT_CONFIG(tooltip)
        self.select_all_checkBox.setText(QCoreApplication.translate("SelectStagesStep", u"Select All", None))
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("SelectStagesStep", u"Event group search", None))
#if QT_CONFIG(tooltip)
        self.reset_all_files_pushButton.setToolTip(QCoreApplication.translate("SelectStagesStep", u"Unchecks the stages of all the files.", None))
#endif // QT_CONFIG(tooltip)
        self.reset_all_files_pushButton.setText(QCoreApplication.translate("SelectStagesStep", u"Reset all files", None))
        self.reset_excl_event_checkBox.setText(QCoreApplication.translate("SelectStagesStep", u"Reset the signal of excluded events ", None))
    # retranslateUi

