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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QFrame, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)
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

        self.tableView_group = QTableView(self.files_card)
        self.tableView_group.setObjectName(u"tableView_group")
        self.tableView_group.setMinimumSize(QSize(0, 240))
        self.tableView_group.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableView_group.setToolTipDuration(-1)
        self.tableView_group.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView_group.setTextElideMode(Qt.ElideNone)
        self.tableView_group.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableView_group.horizontalHeader().setStretchLastSection(True)
        self.tableView_group.verticalHeader().setStretchLastSection(False)

        self.files_card_layout.addWidget(self.tableView_group)

        self.group_grid = QGridLayout()
        self.group_grid.setObjectName(u"group_grid")
        self.group_grid.setHorizontalSpacing(12)
        self.group_grid.setVerticalSpacing(8)
        self.label_2 = QLabel(self.files_card)
        self.label_2.setObjectName(u"label_2")

        self.group_grid.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_search = QLineEdit(self.files_card)
        self.lineEdit_search.setObjectName(u"lineEdit_search")

        self.group_grid.addWidget(self.lineEdit_search, 0, 1, 1, 1)

        self.checkBox_SelectAll = QCheckBox(self.files_card)
        self.checkBox_SelectAll.setObjectName(u"checkBox_SelectAll")
        self.checkBox_SelectAll.setMinimumSize(QSize(150, 0))

        self.group_grid.addWidget(self.checkBox_SelectAll, 0, 2, 1, 1)

        self.label_3 = QLabel(self.files_card)
        self.label_3.setObjectName(u"label_3")

        self.group_grid.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit_group = QLineEdit(self.files_card)
        self.lineEdit_group.setObjectName(u"lineEdit_group")

        self.group_grid.addWidget(self.lineEdit_group, 1, 1, 1, 1)

        self.pushButton_apply = QPushButton(self.files_card)
        self.pushButton_apply.setObjectName(u"pushButton_apply")

        self.group_grid.addWidget(self.pushButton_apply, 1, 2, 1, 1)

        self.group_grid.setColumnStretch(1, 1)

        self.files_card_layout.addLayout(self.group_grid)

        self.group_help_label = QLabel(self.files_card)
        self.group_help_label.setObjectName(u"group_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.group_help_label.setFont(font2)
        self.group_help_label.setWordWrap(True)
        self.group_help_label.setProperty(u"variant", u"help")

        self.files_card_layout.addWidget(self.group_help_label)


        self.verticalLayout.addWidget(self.files_card)

        self.about_groups_layout = QVBoxLayout()
        self.about_groups_layout.setSpacing(6)
        self.about_groups_layout.setObjectName(u"about_groups_layout")
        self.about_groups_title_label = QLabel(GroupDefinition)
        self.about_groups_title_label.setObjectName(u"about_groups_title_label")
        self.about_groups_title_label.setFont(font1)

        self.about_groups_layout.addWidget(self.about_groups_title_label)

        self.about_groups_label = QLabel(GroupDefinition)
        self.about_groups_label.setObjectName(u"about_groups_label")
        self.about_groups_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_groups_label.setWordWrap(True)
        self.about_groups_label.setProperty(u"variant", u"help")

        self.about_groups_layout.addWidget(self.about_groups_label)


        self.verticalLayout.addLayout(self.about_groups_layout)


        self.retranslateUi(GroupDefinition)
        self.pushButton_apply.clicked.connect(GroupDefinition.apply_group_slot)
        self.checkBox_SelectAll.clicked.connect(GroupDefinition.select_all_slot)
        self.lineEdit_search.textEdited.connect(GroupDefinition.edit_search_slot)

        QMetaObject.connectSlotsByName(GroupDefinition)
    # setupUi

    def retranslateUi(self, GroupDefinition):
        GroupDefinition.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("GroupDefinition", u"Group Definition", None))
        self.subtitle_label.setText(QCoreApplication.translate("GroupDefinition", u"Assign a group to each EEG spectral power report.", None))
        self.label.setText(QCoreApplication.translate("GroupDefinition", u"Report files and their group", None))
        self.label_2.setText(QCoreApplication.translate("GroupDefinition", u"Filter", None))
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("GroupDefinition", u"Type a part of the report file names", None))
        self.checkBox_SelectAll.setText(QCoreApplication.translate("GroupDefinition", u"Select all", None))
        self.label_3.setText(QCoreApplication.translate("GroupDefinition", u"Group label", None))
        self.lineEdit_group.setPlaceholderText(QCoreApplication.translate("GroupDefinition", u"Define the group label", None))
        self.pushButton_apply.setText(QCoreApplication.translate("GroupDefinition", u"Apply to the selected files", None))
        self.group_help_label.setText(QCoreApplication.translate("GroupDefinition", u"Check the report files, type a group label, then click \"Apply to the selected files\". You can also double-click a group to edit it.", None))
        self.about_groups_title_label.setText(QCoreApplication.translate("GroupDefinition", u"About the groups", None))
        self.about_groups_label.setText(QCoreApplication.translate("GroupDefinition", u"\u2022 Assign a condition group to each report file. Any group label is accepted, and the number of groups is unlimited.<br/>\u2022 At the cohort level, the report files with the same group label are put together.<br/>\u2022 To analyze the subjects of one report in two groups, create two separate report files, one for each group.<br/>\u2022 Every report file needs a group before the run.", None))
    # retranslateUi

