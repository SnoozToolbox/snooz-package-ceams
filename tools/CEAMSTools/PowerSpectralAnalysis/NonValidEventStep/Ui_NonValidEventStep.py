# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_NonValidEventStep.ui'
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

class Ui_NonValidEventStep(object):
    def setupUi(self, NonValidEventStep):
        if not NonValidEventStep.objectName():
            NonValidEventStep.setObjectName(u"NonValidEventStep")
        NonValidEventStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(NonValidEventStep)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.lists_layout = QHBoxLayout()
        self.lists_layout.setSpacing(16)
        self.lists_layout.setObjectName(u"lists_layout")
        self.files_card = QFrame(NonValidEventStep)
        self.files_card.setObjectName(u"files_card")
        self.files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.files_card_layout = QVBoxLayout(self.files_card)
        self.files_card_layout.setSpacing(10)
        self.files_card_layout.setObjectName(u"files_card_layout")
        self.files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.files_card)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.files_card_layout.addWidget(self.label)

        self.file_listview = QListView(self.files_card)
        self.file_listview.setObjectName(u"file_listview")
        self.file_listview.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.file_listview.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.file_listview.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)

        self.files_card_layout.addWidget(self.file_listview)


        self.lists_layout.addWidget(self.files_card)

        self.events_card = QFrame(NonValidEventStep)
        self.events_card.setObjectName(u"events_card")
        self.events_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.events_card.setFrameShadow(QFrame.Shadow.Raised)
        self.events_card_layout = QVBoxLayout(self.events_card)
        self.events_card_layout.setSpacing(10)
        self.events_card_layout.setObjectName(u"events_card_layout")
        self.events_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.events_card)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.events_card_layout.addWidget(self.label_2)

        self.event_treeview = QTreeView(self.events_card)
        self.event_treeview.setObjectName(u"event_treeview")
        self.event_treeview.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.event_treeview.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.event_treeview.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.event_treeview.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)

        self.events_card_layout.addWidget(self.event_treeview)

        self.events_tools_layout = QHBoxLayout()
        self.events_tools_layout.setSpacing(10)
        self.events_tools_layout.setObjectName(u"events_tools_layout")
        self.select_all_checkBox = QCheckBox(self.events_card)
        self.select_all_checkBox.setObjectName(u"select_all_checkBox")

        self.events_tools_layout.addWidget(self.select_all_checkBox)

        self.search_lineEdit = QLineEdit(self.events_card)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        self.search_lineEdit.setMaximumSize(QSize(200, 16777215))

        self.events_tools_layout.addWidget(self.search_lineEdit)

        self.reset_all_files_pushButton = QPushButton(self.events_card)
        self.reset_all_files_pushButton.setObjectName(u"reset_all_files_pushButton")

        self.events_tools_layout.addWidget(self.reset_all_files_pushButton)

        self.events_tools_layout.setStretch(1, 1)

        self.events_card_layout.addLayout(self.events_tools_layout)

        self.events_line = QFrame(self.events_card)
        self.events_line.setObjectName(u"events_line")
        self.events_line.setFrameShape(QFrame.Shape.HLine)
        self.events_line.setFrameShadow(QFrame.Shadow.Plain)

        self.events_card_layout.addWidget(self.events_line)

        self.reset_excl_event_checkBox = QCheckBox(self.events_card)
        self.reset_excl_event_checkBox.setObjectName(u"reset_excl_event_checkBox")

        self.events_card_layout.addWidget(self.reset_excl_event_checkBox)

        self.match_event_channels_checkBox = QCheckBox(self.events_card)
        self.match_event_channels_checkBox.setObjectName(u"match_event_channels_checkBox")
        self.match_event_channels_checkBox.setChecked(True)

        self.events_card_layout.addWidget(self.match_event_channels_checkBox)


        self.lists_layout.addWidget(self.events_card)

        self.lists_layout.setStretch(0, 1)
        self.lists_layout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.lists_layout)


        self.retranslateUi(NonValidEventStep)
        self.file_listview.clicked.connect(NonValidEventStep.on_file_selected)
        self.select_all_checkBox.stateChanged.connect(NonValidEventStep.on_select_all_groups)
        self.reset_all_files_pushButton.clicked.connect(NonValidEventStep.on_reset_all_files)
        self.search_lineEdit.textEdited.connect(NonValidEventStep.search_pattern_slot)

        QMetaObject.connectSlotsByName(NonValidEventStep)
    # setupUi

    def retranslateUi(self, NonValidEventStep):
        NonValidEventStep.setWindowTitle("")
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("NonValidEventStep", u"Select one or more files (Ctrl or Shift key) to show their events.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("NonValidEventStep", u"PSG files", None))
        self.label_2.setText(QCoreApplication.translate("NonValidEventStep", u"Events", None))
#if QT_CONFIG(tooltip)
        self.select_all_checkBox.setToolTip(QCoreApplication.translate("NonValidEventStep", u"Checks the events shown for the selected files.", None))
#endif // QT_CONFIG(tooltip)
        self.select_all_checkBox.setText(QCoreApplication.translate("NonValidEventStep", u"Select All", None))
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("NonValidEventStep", u"Event group search", None))
#if QT_CONFIG(tooltip)
        self.reset_all_files_pushButton.setToolTip(QCoreApplication.translate("NonValidEventStep", u"Unchecks the events of all the files.", None))
#endif // QT_CONFIG(tooltip)
        self.reset_all_files_pushButton.setText(QCoreApplication.translate("NonValidEventStep", u"Reset all files", None))
#if QT_CONFIG(tooltip)
        self.reset_excl_event_checkBox.setToolTip(QCoreApplication.translate("NonValidEventStep", u"Sets the signal to zero during the excluded events, with smoothed edges. Only for specific artefacts, such as tACS.", None))
#endif // QT_CONFIG(tooltip)
        self.reset_excl_event_checkBox.setText(QCoreApplication.translate("NonValidEventStep", u"Reset the signal of excluded events", None))
        self.match_event_channels_checkBox.setText(QCoreApplication.translate("NonValidEventStep", u"Analyze events only on their annotated channel", None))
    # retranslateUi

