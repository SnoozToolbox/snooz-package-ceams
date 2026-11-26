# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_JsonPathEditorMasterSettingsView.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QPushButton, QSizePolicy, QSplitter,
    QTableView, QVBoxLayout, QWidget)
import themes_rc

class Ui_JsonPathEditorMasterSettingsView(object):
    def setupUi(self, JsonPathEditorMasterSettingsView):
        if not JsonPathEditorMasterSettingsView.objectName():
            JsonPathEditorMasterSettingsView.setObjectName(u"JsonPathEditorMasterSettingsView")
        JsonPathEditorMasterSettingsView.resize(900, 700)
        self.verticalLayout = QVBoxLayout(JsonPathEditorMasterSettingsView)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.files_card = QFrame(JsonPathEditorMasterSettingsView)
        self.files_card.setObjectName(u"files_card")
        self.files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.files_card_layout = QVBoxLayout(self.files_card)
        self.files_card_layout.setSpacing(10)
        self.files_card_layout.setObjectName(u"files_card_layout")
        self.files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.Json_label = QLabel(self.files_card)
        self.Json_label.setObjectName(u"Json_label")
        font = QFont()
        font.setBold(True)
        self.Json_label.setFont(font)

        self.files_card_layout.addWidget(self.Json_label)

        self.Files_listView = QListView(self.files_card)
        self.Files_listView.setObjectName(u"Files_listView")
        self.Files_listView.setFrameShape(QFrame.Shape.NoFrame)
        self.Files_listView.setLineWidth(0)
        self.Files_listView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Files_listView.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.Files_listView.setViewMode(QListView.ViewMode.ListMode)

        self.files_card_layout.addWidget(self.Files_listView)

        self.files_buttons_layout = QHBoxLayout()
        self.files_buttons_layout.setSpacing(8)
        self.files_buttons_layout.setObjectName(u"files_buttons_layout")
        self.files_help_label = QLabel(self.files_card)
        self.files_help_label.setObjectName(u"files_help_label")
        font1 = QFont()
        font1.setPointSize(10)
        self.files_help_label.setFont(font1)
        self.files_help_label.setWordWrap(True)
        self.files_help_label.setProperty(u"variant", u"help")

        self.files_buttons_layout.addWidget(self.files_help_label)

        self.Remove_pushButton = QPushButton(self.files_card)
        self.Remove_pushButton.setObjectName(u"Remove_pushButton")

        self.files_buttons_layout.addWidget(self.Remove_pushButton)

        self.Add_from_folders_pushButton = QPushButton(self.files_card)
        self.Add_from_folders_pushButton.setObjectName(u"Add_from_folders_pushButton")

        self.files_buttons_layout.addWidget(self.Add_from_folders_pushButton)

        self.Add_files_pushButton = QPushButton(self.files_card)
        self.Add_files_pushButton.setObjectName(u"Add_files_pushButton")

        self.files_buttons_layout.addWidget(self.Add_files_pushButton)

        self.SelectAll_pushButton = QPushButton(self.files_card)
        self.SelectAll_pushButton.setObjectName(u"SelectAll_pushButton")

        self.files_buttons_layout.addWidget(self.SelectAll_pushButton)

        self.files_buttons_layout.setStretch(0, 1)

        self.files_card_layout.addLayout(self.files_buttons_layout)


        self.verticalLayout.addWidget(self.files_card)

        self.paths_card = QFrame(JsonPathEditorMasterSettingsView)
        self.paths_card.setObjectName(u"paths_card")
        self.paths_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.paths_card.setFrameShadow(QFrame.Shadow.Raised)
        self.paths_card_layout = QVBoxLayout(self.paths_card)
        self.paths_card_layout.setSpacing(10)
        self.paths_card_layout.setObjectName(u"paths_card_layout")
        self.paths_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.paths_card)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.paths_card_layout.addWidget(self.label)

        self.paths_help_label = QLabel(self.paths_card)
        self.paths_help_label.setObjectName(u"paths_help_label")
        self.paths_help_label.setWordWrap(True)
        self.paths_help_label.setProperty(u"variant", u"help")

        self.paths_card_layout.addWidget(self.paths_help_label)

        self.splitter = QSplitter(self.paths_card)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFrameShape(QFrame.Shape.NoFrame)
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(15)
        self.splitter.setChildrenCollapsible(True)
        self.Paths_tableView = QTableView(self.splitter)
        self.Paths_tableView.setObjectName(u"Paths_tableView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Paths_tableView.sizePolicy().hasHeightForWidth())
        self.Paths_tableView.setSizePolicy(sizePolicy)
        self.Paths_tableView.setMaximumSize(QSize(16777215, 16777215))
        self.Paths_tableView.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Paths_tableView.setFrameShape(QFrame.Shape.NoFrame)
        self.splitter.addWidget(self.Paths_tableView)
        self.Paths_tableView.horizontalHeader().setDefaultSectionSize(200)
        self.Paths_tableView.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.Paths_tableView.horizontalHeader().setStretchLastSection(True)
        self.New_paths_tableView = QTableView(self.splitter)
        self.New_paths_tableView.setObjectName(u"New_paths_tableView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.New_paths_tableView.sizePolicy().hasHeightForWidth())
        self.New_paths_tableView.setSizePolicy(sizePolicy1)
        self.New_paths_tableView.setFrameShape(QFrame.Shape.NoFrame)
        self.New_paths_tableView.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.splitter.addWidget(self.New_paths_tableView)
        self.New_paths_tableView.horizontalHeader().setDefaultSectionSize(300)
        self.New_paths_tableView.horizontalHeader().setStretchLastSection(True)

        self.paths_card_layout.addWidget(self.splitter)


        self.verticalLayout.addWidget(self.paths_card)

        self.output_card = QFrame(JsonPathEditorMasterSettingsView)
        self.output_card.setObjectName(u"output_card")
        self.output_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.output_card.setFrameShadow(QFrame.Shadow.Raised)
        self.output_card_layout = QVBoxLayout(self.output_card)
        self.output_card_layout.setSpacing(10)
        self.output_card_layout.setObjectName(u"output_card_layout")
        self.output_card_layout.setContentsMargins(10, 10, 10, 10)
        self.Select_label = QLabel(self.output_card)
        self.Select_label.setObjectName(u"Select_label")
        self.Select_label.setFont(font)

        self.output_card_layout.addWidget(self.Select_label)

        self.output_grid = QGridLayout()
        self.output_grid.setObjectName(u"output_grid")
        self.output_grid.setHorizontalSpacing(12)
        self.output_grid.setVerticalSpacing(10)
        self.New_Suffix = QLabel(self.output_card)
        self.New_Suffix.setObjectName(u"New_Suffix")

        self.output_grid.addWidget(self.New_Suffix, 0, 0, 1, 1)

        self.Suffix_lineEdit = QLineEdit(self.output_card)
        self.Suffix_lineEdit.setObjectName(u"Suffix_lineEdit")

        self.output_grid.addWidget(self.Suffix_lineEdit, 0, 1, 1, 1)

        self.folder_label = QLabel(self.output_card)
        self.folder_label.setObjectName(u"folder_label")

        self.output_grid.addWidget(self.folder_label, 1, 0, 1, 1)

        self.folder_layout = QHBoxLayout()
        self.folder_layout.setSpacing(8)
        self.folder_layout.setObjectName(u"folder_layout")
        self.New_files_lineEdit = QLineEdit(self.output_card)
        self.New_files_lineEdit.setObjectName(u"New_files_lineEdit")

        self.folder_layout.addWidget(self.New_files_lineEdit)

        self.Choose_pushButton = QPushButton(self.output_card)
        self.Choose_pushButton.setObjectName(u"Choose_pushButton")

        self.folder_layout.addWidget(self.Choose_pushButton)


        self.output_grid.addLayout(self.folder_layout, 1, 1, 1, 1)

        self.output_grid.setColumnStretch(1, 1)

        self.output_card_layout.addLayout(self.output_grid)

        self.output_help_label = QLabel(self.output_card)
        self.output_help_label.setObjectName(u"output_help_label")
        self.output_help_label.setFont(font1)
        self.output_help_label.setWordWrap(True)
        self.output_help_label.setProperty(u"variant", u"help")

        self.output_card_layout.addWidget(self.output_help_label)


        self.verticalLayout.addWidget(self.output_card)


        self.retranslateUi(JsonPathEditorMasterSettingsView)

        QMetaObject.connectSlotsByName(JsonPathEditorMasterSettingsView)
    # setupUi

    def retranslateUi(self, JsonPathEditorMasterSettingsView):
        JsonPathEditorMasterSettingsView.setWindowTitle("")
#if QT_CONFIG(tooltip)
        self.Json_label.setToolTip(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"The workspaces to edit (.json). Select a workspace to show its paths.", None))
#endif // QT_CONFIG(tooltip)
        self.Json_label.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Snooz workspaces", None))
        self.files_help_label.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Only the workspaces selected in the list are edited at runtime. The paths of a workspace that is loaded but not selected are not changed.", None))
        self.Remove_pushButton.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Remove", None))
        self.Add_from_folders_pushButton.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Add from folders", None))
        self.Add_files_pushButton.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Add files", None))
        self.SelectAll_pushButton.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Select all", None))
        self.label.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Paths inside the workspaces", None))
        self.paths_help_label.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Edit the folders in the \"New Paths\" column.", None))
        self.Select_label.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"New workspaces", None))
        self.New_Suffix.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Suffix", None))
        self.folder_label.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Folder", None))
        self.Choose_pushButton.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Choose", None))
        self.output_help_label.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Saved in this folder as &lt;name&gt;_&lt;suffix&gt;.json. The original files are not changed.", None))
    # retranslateUi

