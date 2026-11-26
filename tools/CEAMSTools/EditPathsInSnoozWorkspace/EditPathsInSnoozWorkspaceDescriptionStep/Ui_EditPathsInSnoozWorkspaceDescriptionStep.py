# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EditPathsInSnoozWorkspaceDescriptionStep.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_EditPathsInSnoozWorkspaceDescriptionStep(object):
    def setupUi(self, EditPathsInSnoozWorkspaceDescriptionStep):
        if not EditPathsInSnoozWorkspaceDescriptionStep.objectName():
            EditPathsInSnoozWorkspaceDescriptionStep.setObjectName(u"EditPathsInSnoozWorkspaceDescriptionStep")
        EditPathsInSnoozWorkspaceDescriptionStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(EditPathsInSnoozWorkspaceDescriptionStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(EditPathsInSnoozWorkspaceDescriptionStep)
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

        self.steps_section_layout = QVBoxLayout()
        self.steps_section_layout.setSpacing(8)
        self.steps_section_layout.setObjectName(u"steps_section_layout")
        self.steps_title_label = QLabel(self.content_widget)
        self.steps_title_label.setObjectName(u"steps_title_label")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.steps_title_label.setFont(font1)

        self.steps_section_layout.addWidget(self.steps_title_label)

        self.steps_card = QFrame(self.content_widget)
        self.steps_card.setObjectName(u"steps_card")
        self.steps_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.steps_card.setFrameShadow(QFrame.Shadow.Raised)
        self.steps_card_layout = QVBoxLayout(self.steps_card)
        self.steps_card_layout.setSpacing(10)
        self.steps_card_layout.setObjectName(u"steps_card_layout")
        self.steps_card_layout.setContentsMargins(10, 10, 10, 10)
        self.steps_grid = QGridLayout()
        self.steps_grid.setObjectName(u"steps_grid")
        self.steps_grid.setHorizontalSpacing(12)
        self.steps_grid.setVerticalSpacing(10)
        self.step_1_number_label = QLabel(self.steps_card)
        self.step_1_number_label.setObjectName(u"step_1_number_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.step_1_number_label.setFont(font2)
        self.step_1_number_label.setProperty(u"variant", u"step_number")
        self.step_1_number_label.setMinimumSize(QSize(24, 24))
        self.step_1_number_label.setMaximumSize(QSize(24, 24))
        self.step_1_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.steps_grid.addWidget(self.step_1_number_label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.step_1_name_label = QLabel(self.steps_card)
        self.step_1_name_label.setObjectName(u"step_1_name_label")
        font3 = QFont()
        font3.setBold(True)
        self.step_1_name_label.setFont(font3)
        self.step_1_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_1_name_label, 0, 1, 1, 1)

        self.steps_gap = QSpacerItem(16, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.steps_grid.addItem(self.steps_gap, 0, 2, 1, 1)

        self.step_1_label = QLabel(self.steps_card)
        self.step_1_label.setObjectName(u"step_1_label")
        self.step_1_label.setWordWrap(True)
        self.step_1_label.setProperty(u"variant", u"help")
        self.step_1_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_1_label, 0, 3, 1, 1)

        self.steps_grid.setColumnStretch(3, 1)

        self.steps_card_layout.addLayout(self.steps_grid)


        self.steps_section_layout.addWidget(self.steps_card)


        self.content_layout.addLayout(self.steps_section_layout)

        self.files_section_layout = QVBoxLayout()
        self.files_section_layout.setSpacing(8)
        self.files_section_layout.setObjectName(u"files_section_layout")
        self.files_title_label = QLabel(self.content_widget)
        self.files_title_label.setObjectName(u"files_title_label")
        self.files_title_label.setFont(font1)

        self.files_section_layout.addWidget(self.files_title_label)

        self.files_card = QFrame(self.content_widget)
        self.files_card.setObjectName(u"files_card")
        self.files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.files_card_layout = QVBoxLayout(self.files_card)
        self.files_card_layout.setSpacing(10)
        self.files_card_layout.setObjectName(u"files_card_layout")
        self.files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.files_grid = QGridLayout()
        self.files_grid.setObjectName(u"files_grid")
        self.files_grid.setHorizontalSpacing(32)
        self.files_grid.setVerticalSpacing(6)
        self.file_1_name_label = QLabel(self.files_card)
        self.file_1_name_label.setObjectName(u"file_1_name_label")
        self.file_1_name_label.setFont(font3)

        self.files_grid.addWidget(self.file_1_name_label, 0, 0, 1, 1)

        self.file_1_label = QLabel(self.files_card)
        self.file_1_label.setObjectName(u"file_1_label")
        self.file_1_label.setWordWrap(True)

        self.files_grid.addWidget(self.file_1_label, 0, 1, 1, 1)

        self.files_grid.setColumnStretch(1, 1)

        self.files_card_layout.addLayout(self.files_grid)


        self.files_section_layout.addWidget(self.files_card)


        self.content_layout.addLayout(self.files_section_layout)

        self.selected_warning = QFrame(self.content_widget)
        self.selected_warning.setObjectName(u"selected_warning")
        self.selected_warning.setFrameShape(QFrame.Shape.NoFrame)
        self.selected_warning.setProperty(u"variant", u"warning")
        self.selected_warning_layout = QHBoxLayout(self.selected_warning)
        self.selected_warning_layout.setObjectName(u"selected_warning_layout")
        self.selected_warning_layout.setContentsMargins(14, 10, 14, 10)
        self.selected_warning_label = QLabel(self.selected_warning)
        self.selected_warning_label.setObjectName(u"selected_warning_label")
        self.selected_warning_label.setTextFormat(Qt.TextFormat.RichText)
        self.selected_warning_label.setWordWrap(True)

        self.selected_warning_layout.addWidget(self.selected_warning_label)


        self.content_layout.addWidget(self.selected_warning)

        self.about_editing_layout = QVBoxLayout()
        self.about_editing_layout.setSpacing(6)
        self.about_editing_layout.setObjectName(u"about_editing_layout")
        self.about_editing_title_label = QLabel(self.content_widget)
        self.about_editing_title_label.setObjectName(u"about_editing_title_label")
        self.about_editing_title_label.setFont(font3)

        self.about_editing_layout.addWidget(self.about_editing_title_label)

        self.about_editing_label = QLabel(self.content_widget)
        self.about_editing_label.setObjectName(u"about_editing_label")
        self.about_editing_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_editing_label.setWordWrap(True)
        self.about_editing_label.setProperty(u"variant", u"help")

        self.about_editing_layout.addWidget(self.about_editing_label)


        self.content_layout.addLayout(self.about_editing_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(EditPathsInSnoozWorkspaceDescriptionStep)

        QMetaObject.connectSlotsByName(EditPathsInSnoozWorkspaceDescriptionStep)
    # setupUi

    def retranslateUi(self, EditPathsInSnoozWorkspaceDescriptionStep):
        EditPathsInSnoozWorkspaceDescriptionStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("EditPathsInSnoozWorkspaceDescriptionStep", u"Edit Paths in Snooz Workspace", None))
        self.subtitle_label.setText(QCoreApplication.translate("EditPathsInSnoozWorkspaceDescriptionStep", u"Updates the paths inside Snooz workspaces (.json), for example after moving the recordings to another computer or folder.", None))
        self.steps_title_label.setText(QCoreApplication.translate("EditPathsInSnoozWorkspaceDescriptionStep", u"What you will do", None))
        self.step_1_number_label.setText(QCoreApplication.translate("EditPathsInSnoozWorkspaceDescriptionStep", u"1", None))
        self.step_1_name_label.setText(QCoreApplication.translate("EditPathsInSnoozWorkspaceDescriptionStep", u"Edit Paths", None))
        self.step_1_label.setText(QCoreApplication.translate("EditPathsInSnoozWorkspaceDescriptionStep", u"Add the workspaces, edit their paths, then choose the suffix and the folder of the new workspaces.", None))
        self.files_title_label.setText(QCoreApplication.translate("EditPathsInSnoozWorkspaceDescriptionStep", u"Accepted files", None))
        self.file_1_name_label.setText(QCoreApplication.translate("EditPathsInSnoozWorkspaceDescriptionStep", u"Workspaces", None))
        self.file_1_label.setText(QCoreApplication.translate("EditPathsInSnoozWorkspaceDescriptionStep", u"Snooz workspace files (.json). Add one or more files, or all the files of a folder.", None))
        self.selected_warning_label.setText(QCoreApplication.translate("EditPathsInSnoozWorkspaceDescriptionStep", u"<b>Select all the workspaces to edit</b><br/>Only the workspaces selected in the list are edited at runtime. The paths of a workspace that is loaded but not selected are not changed.", None))
        self.about_editing_title_label.setText(QCoreApplication.translate("EditPathsInSnoozWorkspaceDescriptionStep", u"About the editing", None))
        self.about_editing_label.setText(QCoreApplication.translate("EditPathsInSnoozWorkspaceDescriptionStep", u"<b>The folders shown</b><br/>When you select a workspace in the list, Snooz shows the folders that its paths point to in the \"Original Paths\" column, each folder once. A path to a file, such as C:/data/subject1.edf, is shown as its folder, C:/data. Snooz finds two kinds of paths.<br/>\u2022 Paths on a drive, which start with a drive letter, such as C:/ or C:\\.<br/>\u2022 Network paths, which start with // or \\\\.<br/>The folders are written with / between their names.<br/><br/><b>Editing a folder</b><br/>Click a folder in the \"New Paths\" column and type its new location. Every path in this folder then points to the new folder. For example, if C:/data becomes D:/recordings, the path C:/data/subject1.edf becomes D:/recordings/subject1.edf. A subfolder, such as C:/data/night2, is listed and edited on its own. When you select a workspace, the folders not changed yet are shown in orange italics.<br/>Before the run, a warning lists the folders of the \"New Paths\" column that do not exist. Click \"Cancel\" to "
                        "fix them, or \"OK\" to run anyway.<br/><br/><b>Several workspaces</b><br/>Edit the workspaces one at a time. Select a workspace in the list, edit its folders, then select the next one. \"Select all\" then selects all the workspaces and shows their folders together, to check all the changes. It is only a preview. The folders cannot be edited there. When a folder is in several workspaces, Snooz shows a warning instead of the preview. To avoid confusion, load workspaces whose folders are all different.<br/><br/><b>The new workspaces</b><br/>Snooz writes one new workspace for each selected workspace, in the chosen folder. Its name is the name of the original file, then _ and the suffix. For example, study.json with the suffix laptop gives study_laptop.json. The original files are not changed.", None))
    # retranslateUi

