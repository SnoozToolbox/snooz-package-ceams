# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EditorStep.ui'
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
    QSizePolicy, QSpacerItem, QTreeView, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_EditorStep(object):
    def setupUi(self, EditorStep):
        if not EditorStep.objectName():
            EditorStep.setObjectName(u"EditorStep")
        EditorStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(EditorStep)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.header_layout = QVBoxLayout()
        self.header_layout.setSpacing(6)
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(EditorStep)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.header_layout.addWidget(self.title_label)

        self.subtitle_label = QLabel(EditorStep)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setProperty(u"variant", u"help")

        self.header_layout.addWidget(self.subtitle_label)


        self.verticalLayout.addLayout(self.header_layout)

        self.lists_layout = QHBoxLayout()
        self.lists_layout.setSpacing(16)
        self.lists_layout.setObjectName(u"lists_layout")
        self.files_card = QFrame(EditorStep)
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
        self.file_listview.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.files_card_layout.addWidget(self.file_listview)


        self.lists_layout.addWidget(self.files_card)

        self.selection_card = QFrame(EditorStep)
        self.selection_card.setObjectName(u"selection_card")
        self.selection_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.selection_card.setFrameShadow(QFrame.Shadow.Raised)
        self.selection_card_layout = QVBoxLayout(self.selection_card)
        self.selection_card_layout.setSpacing(10)
        self.selection_card_layout.setObjectName(u"selection_card_layout")
        self.selection_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.selection_card)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.selection_card_layout.addWidget(self.label_2)

        self.treeView_subject = QTreeView(self.selection_card)
        self.treeView_subject.setObjectName(u"treeView_subject")
        self.treeView_subject.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)
        self.treeView_subject.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.treeView_subject.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)

        self.selection_card_layout.addWidget(self.treeView_subject)


        self.lists_layout.addWidget(self.selection_card)

        self.cohort_card = QFrame(EditorStep)
        self.cohort_card.setObjectName(u"cohort_card")
        self.cohort_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.cohort_card.setFrameShadow(QFrame.Shadow.Raised)
        self.cohort_card_layout = QVBoxLayout(self.cohort_card)
        self.cohort_card_layout.setSpacing(10)
        self.cohort_card_layout.setObjectName(u"cohort_card_layout")
        self.cohort_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_3 = QLabel(self.cohort_card)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.cohort_card_layout.addWidget(self.label_3)

        self.treeView_cohort = QTreeView(self.cohort_card)
        self.treeView_cohort.setObjectName(u"treeView_cohort")

        self.cohort_card_layout.addWidget(self.treeView_cohort)

        self.cohort_buttons_layout = QHBoxLayout()
        self.cohort_buttons_layout.setSpacing(8)
        self.cohort_buttons_layout.setObjectName(u"cohort_buttons_layout")
        self.cohort_buttons_layout_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cohort_buttons_layout.addItem(self.cohort_buttons_layout_spacer)

        self.pushButton_refresh = QPushButton(self.cohort_card)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")

        self.cohort_buttons_layout.addWidget(self.pushButton_refresh)

        self.reset_all_files_pushButton = QPushButton(self.cohort_card)
        self.reset_all_files_pushButton.setObjectName(u"reset_all_files_pushButton")

        self.cohort_buttons_layout.addWidget(self.reset_all_files_pushButton)

        self.pushButton_export = QPushButton(self.cohort_card)
        self.pushButton_export.setObjectName(u"pushButton_export")

        self.cohort_buttons_layout.addWidget(self.pushButton_export)

        self.cohort_buttons_layout.setStretch(0, 1)

        self.cohort_card_layout.addLayout(self.cohort_buttons_layout)


        self.lists_layout.addWidget(self.cohort_card)

        self.lists_layout.setStretch(0, 2)
        self.lists_layout.setStretch(1, 3)
        self.lists_layout.setStretch(2, 3)

        self.verticalLayout.addLayout(self.lists_layout)


        self.retranslateUi(EditorStep)
        self.file_listview.clicked.connect(EditorStep.on_file_selected)
        self.reset_all_files_pushButton.clicked.connect(EditorStep.on_reset_all_files)
        self.pushButton_refresh.clicked.connect(EditorStep.refresh_view_slot)
        self.pushButton_export.clicked.connect(EditorStep.export_modifications_slot)

        QMetaObject.connectSlotsByName(EditorStep)
    # setupUi

    def retranslateUi(self, EditorStep):
        EditorStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("EditorStep", u"Remove or edit", None))
        self.subtitle_label.setText(QCoreApplication.translate("EditorStep", u"Uncheck the annotations to remove. To rename one, edit its label in the \"Group\u2011Name\" column. \"Events from selection\" changes the selected recording, and \"Events from cohort\" changes all the recordings.", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("EditorStep", u"Select a recording to show its annotations in \"Events from selection\".", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("EditorStep", u"PSG Files", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("EditorStep", u"The annotations of the selected recording. The changes apply to it only.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("EditorStep", u"Events from selection", None))
        self.label_3.setText(QCoreApplication.translate("EditorStep", u"Events from cohort", None))
#if QT_CONFIG(tooltip)
        self.pushButton_refresh.setToolTip(QCoreApplication.translate("EditorStep", u"To refresh the cohort view. Useful for merging 2 groups with the same labels.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_refresh.setText(QCoreApplication.translate("EditorStep", u"Refresh", None))
        self.reset_all_files_pushButton.setText(QCoreApplication.translate("EditorStep", u"Back to original labels", None))
#if QT_CONFIG(tooltip)
        self.reset_all_files_pushButton.setToolTip(QCoreApplication.translate("EditorStep", u"To return to the original labels saved in the file.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_export.setToolTip(QCoreApplication.translate("EditorStep", u"To display all changes that will be performed at runtime.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_export.setText(QCoreApplication.translate("EditorStep", u"Export", None))
    # retranslateUi

