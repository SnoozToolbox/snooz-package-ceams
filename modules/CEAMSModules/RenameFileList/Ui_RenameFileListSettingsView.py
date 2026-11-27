# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_RenameFileListSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_RenameFileListSettingsView(object):
    def setupUi(self, RenameFileListSettingsView):
        if not RenameFileListSettingsView.objectName():
            RenameFileListSettingsView.setObjectName(u"RenameFileListSettingsView")
        RenameFileListSettingsView.resize(900, 700)
        self.verticalLayout = QVBoxLayout(RenameFileListSettingsView)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.files_card = QFrame(RenameFileListSettingsView)
        self.files_card.setObjectName(u"files_card")
        self.files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.files_card_layout = QVBoxLayout(self.files_card)
        self.files_card_layout.setSpacing(10)
        self.files_card_layout.setObjectName(u"files_card_layout")
        self.files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.files_title_label = QLabel(self.files_card)
        self.files_title_label.setObjectName(u"files_title_label")
        font = QFont()
        font.setBold(True)
        self.files_title_label.setFont(font)

        self.files_card_layout.addWidget(self.files_title_label)

        self.tableWidget_files = QTableWidget(self.files_card)
        self.tableWidget_files.setObjectName(u"tableWidget_files")

        self.files_card_layout.addWidget(self.tableWidget_files)

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

        self.pushButton_choose = QPushButton(self.files_card)
        self.pushButton_choose.setObjectName(u"pushButton_choose")

        self.files_buttons_layout.addWidget(self.pushButton_choose)

        self.pushButton_clear = QPushButton(self.files_card)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.files_buttons_layout.addWidget(self.pushButton_clear)

        self.files_buttons_layout.setStretch(0, 1)

        self.files_card_layout.addLayout(self.files_buttons_layout)


        self.verticalLayout.addWidget(self.files_card)

        self.rules_card = QFrame(RenameFileListSettingsView)
        self.rules_card.setObjectName(u"rules_card")
        self.rules_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.rules_card.setFrameShadow(QFrame.Shadow.Raised)
        self.rules_card_layout = QVBoxLayout(self.rules_card)
        self.rules_card_layout.setSpacing(10)
        self.rules_card_layout.setObjectName(u"rules_card_layout")
        self.rules_card_layout.setContentsMargins(10, 10, 10, 10)
        self.rules_title_label = QLabel(self.rules_card)
        self.rules_title_label.setObjectName(u"rules_title_label")
        self.rules_title_label.setFont(font)

        self.rules_card_layout.addWidget(self.rules_title_label)

        self.rules_help_label = QLabel(self.rules_card)
        self.rules_help_label.setObjectName(u"rules_help_label")
        self.rules_help_label.setWordWrap(True)
        self.rules_help_label.setProperty(u"variant", u"help")

        self.rules_card_layout.addWidget(self.rules_help_label)

        self.rules_grid = QGridLayout()
        self.rules_grid.setObjectName(u"rules_grid")
        self.rules_grid.setHorizontalSpacing(12)
        self.rules_grid.setVerticalSpacing(10)
        self.ext_selection_label = QLabel(self.rules_card)
        self.ext_selection_label.setObjectName(u"ext_selection_label")

        self.rules_grid.addWidget(self.ext_selection_label, 0, 0, 1, 1)

        self.ext_selection_lineedit = QLineEdit(self.rules_card)
        self.ext_selection_lineedit.setObjectName(u"ext_selection_lineedit")

        self.rules_grid.addWidget(self.ext_selection_lineedit, 0, 1, 1, 1)

        self.ext_selection_unit_label = QLabel(self.rules_card)
        self.ext_selection_unit_label.setObjectName(u"ext_selection_unit_label")
        self.ext_selection_unit_label.setProperty(u"variant", u"help")

        self.rules_grid.addWidget(self.ext_selection_unit_label, 0, 2, 1, 1)

        self.pattern_to_rem_label = QLabel(self.rules_card)
        self.pattern_to_rem_label.setObjectName(u"pattern_to_rem_label")

        self.rules_grid.addWidget(self.pattern_to_rem_label, 1, 0, 1, 1)

        self.pattern_to_rem_lineedit = QLineEdit(self.rules_card)
        self.pattern_to_rem_lineedit.setObjectName(u"pattern_to_rem_lineedit")

        self.rules_grid.addWidget(self.pattern_to_rem_lineedit, 1, 1, 1, 1)

        self.pattern_to_rem_unit_label = QLabel(self.rules_card)
        self.pattern_to_rem_unit_label.setObjectName(u"pattern_to_rem_unit_label")
        self.pattern_to_rem_unit_label.setProperty(u"variant", u"help")

        self.rules_grid.addWidget(self.pattern_to_rem_unit_label, 1, 2, 1, 1)

        self.n_char_to_keep_label = QLabel(self.rules_card)
        self.n_char_to_keep_label.setObjectName(u"n_char_to_keep_label")

        self.rules_grid.addWidget(self.n_char_to_keep_label, 2, 0, 1, 1)

        self.n_char_to_keep_layout = QHBoxLayout()
        self.n_char_to_keep_layout.setSpacing(12)
        self.n_char_to_keep_layout.setObjectName(u"n_char_to_keep_layout")
        self.spinBox_n_char_to_keep = QSpinBox(self.rules_card)
        self.spinBox_n_char_to_keep.setObjectName(u"spinBox_n_char_to_keep")
        self.spinBox_n_char_to_keep.setEnabled(False)
        self.spinBox_n_char_to_keep.setMinimum(-1)
        self.spinBox_n_char_to_keep.setValue(-1)

        self.n_char_to_keep_layout.addWidget(self.spinBox_n_char_to_keep)

        self.checkBox_keep_all_char = QCheckBox(self.rules_card)
        self.checkBox_keep_all_char.setObjectName(u"checkBox_keep_all_char")
        self.checkBox_keep_all_char.setChecked(True)

        self.n_char_to_keep_layout.addWidget(self.checkBox_keep_all_char)

        self.n_char_to_keep_layout.setStretch(0, 1)

        self.rules_grid.addLayout(self.n_char_to_keep_layout, 2, 1, 1, 1)

        self.n_char_to_keep_unit_label = QLabel(self.rules_card)
        self.n_char_to_keep_unit_label.setObjectName(u"n_char_to_keep_unit_label")
        self.n_char_to_keep_unit_label.setProperty(u"variant", u"help")

        self.rules_grid.addWidget(self.n_char_to_keep_unit_label, 2, 2, 1, 1)

        self.prefix_label = QLabel(self.rules_card)
        self.prefix_label.setObjectName(u"prefix_label")

        self.rules_grid.addWidget(self.prefix_label, 3, 0, 1, 1)

        self.prefix_lineedit = QLineEdit(self.rules_card)
        self.prefix_lineedit.setObjectName(u"prefix_lineedit")

        self.rules_grid.addWidget(self.prefix_lineedit, 3, 1, 1, 1)

        self.prefix_unit_label = QLabel(self.rules_card)
        self.prefix_unit_label.setObjectName(u"prefix_unit_label")
        self.prefix_unit_label.setProperty(u"variant", u"help")

        self.rules_grid.addWidget(self.prefix_unit_label, 3, 2, 1, 1)

        self.suffix_label = QLabel(self.rules_card)
        self.suffix_label.setObjectName(u"suffix_label")

        self.rules_grid.addWidget(self.suffix_label, 4, 0, 1, 1)

        self.suffix_lineedit = QLineEdit(self.rules_card)
        self.suffix_lineedit.setObjectName(u"suffix_lineedit")

        self.rules_grid.addWidget(self.suffix_lineedit, 4, 1, 1, 1)

        self.suffix_unit_label = QLabel(self.rules_card)
        self.suffix_unit_label.setObjectName(u"suffix_unit_label")
        self.suffix_unit_label.setProperty(u"variant", u"help")

        self.rules_grid.addWidget(self.suffix_unit_label, 4, 2, 1, 1)

        self.rules_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rules_grid.addItem(self.rules_grid_spacer, 0, 3, 1, 1)


        self.rules_card_layout.addLayout(self.rules_grid)


        self.verticalLayout.addWidget(self.rules_card)

        self.originals_card = QFrame(RenameFileListSettingsView)
        self.originals_card.setObjectName(u"originals_card")
        self.originals_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.originals_card.setFrameShadow(QFrame.Shadow.Raised)
        self.originals_card_layout = QVBoxLayout(self.originals_card)
        self.originals_card_layout.setSpacing(10)
        self.originals_card_layout.setObjectName(u"originals_card_layout")
        self.originals_card_layout.setContentsMargins(10, 10, 10, 10)
        self.originals_title_label = QLabel(self.originals_card)
        self.originals_title_label.setObjectName(u"originals_title_label")
        self.originals_title_label.setFont(font)

        self.originals_card_layout.addWidget(self.originals_title_label)

        self.originals_layout = QVBoxLayout()
        self.originals_layout.setSpacing(8)
        self.originals_layout.setObjectName(u"originals_layout")
        self.originals_layout_1_layout = QVBoxLayout()
        self.originals_layout_1_layout.setSpacing(2)
        self.originals_layout_1_layout.setObjectName(u"originals_layout_1_layout")
        self.checkBox_keep_original = QCheckBox(self.originals_card)
        self.checkBox_keep_original.setObjectName(u"checkBox_keep_original")
        self.checkBox_keep_original.setChecked(True)

        self.originals_layout_1_layout.addWidget(self.checkBox_keep_original)

        self.keep_original_help_label = QLabel(self.originals_card)
        self.keep_original_help_label.setObjectName(u"keep_original_help_label")
        self.keep_original_help_label.setFont(font1)
        self.keep_original_help_label.setWordWrap(True)
        self.keep_original_help_label.setIndent(26)
        self.keep_original_help_label.setProperty(u"variant", u"help")

        self.originals_layout_1_layout.addWidget(self.keep_original_help_label)


        self.originals_layout.addLayout(self.originals_layout_1_layout)


        self.originals_card_layout.addLayout(self.originals_layout)

        self.originals_help_label = QLabel(self.originals_card)
        self.originals_help_label.setObjectName(u"originals_help_label")
        self.originals_help_label.setFont(font1)
        self.originals_help_label.setWordWrap(True)
        self.originals_help_label.setProperty(u"variant", u"help")

        self.originals_card_layout.addWidget(self.originals_help_label)


        self.verticalLayout.addWidget(self.originals_card)


        self.retranslateUi(RenameFileListSettingsView)
        self.checkBox_keep_all_char.clicked.connect(RenameFileListSettingsView.keep_all_char_slot)
        self.pushButton_choose.clicked.connect(RenameFileListSettingsView.choose_slot)
        self.pushButton_clear.clicked.connect(RenameFileListSettingsView.clear_slot)

        QMetaObject.connectSlotsByName(RenameFileListSettingsView)
    # setupUi

    def retranslateUi(self, RenameFileListSettingsView):
        RenameFileListSettingsView.setWindowTitle("")
#if QT_CONFIG(tooltip)
        self.files_title_label.setToolTip(QCoreApplication.translate("RenameFileListSettingsView", u"The files to rename, of any kind (.tsv, .txt, .csv...).", None))
#endif // QT_CONFIG(tooltip)
        self.files_title_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Files to rename", None))
        self.files_help_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Choosing files again replaces the list.", None))
        self.pushButton_choose.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Choose files", None))
        self.pushButton_clear.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Clear all", None))
        self.rules_title_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Renaming rules", None))
        self.rules_help_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Applied in this order to the name of each file, without its extension. The extension is kept.", None))
#if QT_CONFIG(tooltip)
        self.ext_selection_label.setToolTip(QCoreApplication.translate("RenameFileListSettingsView", u"Only the files of the list with this extension are renamed, for example tsv, txt, csv, xml or edf.", None))
#endif // QT_CONFIG(tooltip)
        self.ext_selection_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"File extension", None))
#if QT_CONFIG(tooltip)
        self.ext_selection_lineedit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.ext_selection_lineedit.setPlaceholderText(QCoreApplication.translate("RenameFileListSettingsView", u"tsv", None))
        self.ext_selection_unit_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Empty for all the files", None))
#if QT_CONFIG(tooltip)
        self.pattern_to_rem_label.setToolTip(QCoreApplication.translate("RenameFileListSettingsView", u"For example, removing _annotations renames subject01_annotations.txt to subject01.txt.", None))
#endif // QT_CONFIG(tooltip)
        self.pattern_to_rem_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Pattern to remove", None))
#if QT_CONFIG(tooltip)
        self.pattern_to_rem_lineedit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pattern_to_rem_unit_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Every occurrence", None))
#if QT_CONFIG(tooltip)
        self.n_char_to_keep_label.setToolTip(QCoreApplication.translate("RenameFileListSettingsView", u"For example, 9 characters rename subject01 filtered.tsv to subject01.tsv.", None))
#endif // QT_CONFIG(tooltip)
        self.n_char_to_keep_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Characters to keep", None))
#if QT_CONFIG(tooltip)
        self.spinBox_n_char_to_keep.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_keep_all_char.setToolTip(QCoreApplication.translate("RenameFileListSettingsView", u"Keeps the whole name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_keep_all_char.setText(QCoreApplication.translate("RenameFileListSettingsView", u"All", None))
        self.n_char_to_keep_unit_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"From the start of the name", None))
#if QT_CONFIG(tooltip)
        self.prefix_label.setToolTip(QCoreApplication.translate("RenameFileListSettingsView", u"For example, the prefix visit1_ renames subject01.tsv to visit1_subject01.tsv.", None))
#endif // QT_CONFIG(tooltip)
        self.prefix_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Prefix", None))
#if QT_CONFIG(tooltip)
        self.prefix_lineedit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.prefix_unit_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Added at the start", None))
#if QT_CONFIG(tooltip)
        self.suffix_label.setToolTip(QCoreApplication.translate("RenameFileListSettingsView", u"For example, the suffix _visit1 renames subject01.tsv to subject01_visit1.tsv.", None))
#endif // QT_CONFIG(tooltip)
        self.suffix_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Suffix", None))
#if QT_CONFIG(tooltip)
        self.suffix_lineedit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.suffix_unit_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Added at the end", None))
        self.originals_title_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Original files", None))
        self.checkBox_keep_original.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Keep the original file", None))
#if QT_CONFIG(tooltip)
        self.checkBox_keep_original.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.keep_original_help_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"Checked, each file is copied under its new name and the original stays. Unchecked, each file is renamed.", None))
        self.originals_help_label.setText(QCoreApplication.translate("RenameFileListSettingsView", u"The new files are written in the folder of the original files. Check that no file there already has one of the new names.", None))
    # retranslateUi

