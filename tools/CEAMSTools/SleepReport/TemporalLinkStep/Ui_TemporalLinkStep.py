# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_TemporalLinkStep.ui'
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
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)
import themes_rc

class Ui_TemporalLinkStep(object):
    def setupUi(self, TemporalLinkStep):
        if not TemporalLinkStep.objectName():
            TemporalLinkStep.setObjectName(u"TemporalLinkStep")
        TemporalLinkStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(TemporalLinkStep)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.header_layout = QVBoxLayout()
        self.header_layout.setSpacing(6)
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(TemporalLinkStep)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.header_layout.addWidget(self.title_label)

        self.subtitle_label = QLabel(TemporalLinkStep)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setProperty(u"variant", u"help")

        self.header_layout.addWidget(self.subtitle_label)


        self.verticalLayout.addLayout(self.header_layout)

        self.lists_layout = QHBoxLayout()
        self.lists_layout.setSpacing(16)
        self.lists_layout.setObjectName(u"lists_layout")
        self.files_card = QFrame(TemporalLinkStep)
        self.files_card.setObjectName(u"files_card")
        self.files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.files_card_layout = QVBoxLayout(self.files_card)
        self.files_card_layout.setSpacing(10)
        self.files_card_layout.setObjectName(u"files_card_layout")
        self.files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.files_title_label = QLabel(self.files_card)
        self.files_title_label.setObjectName(u"files_title_label")
        font1 = QFont()
        font1.setBold(True)
        self.files_title_label.setFont(font1)

        self.files_card_layout.addWidget(self.files_title_label)

        self.file_tableview = QTableView(self.files_card)
        self.file_tableview.setObjectName(u"file_tableview")
        self.file_tableview.setAlternatingRowColors(True)
        self.file_tableview.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.file_tableview.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.file_tableview.horizontalHeader().setStretchLastSection(True)

        self.files_card_layout.addWidget(self.file_tableview)

        self.files_buttons_layout = QHBoxLayout()
        self.files_buttons_layout.setSpacing(8)
        self.files_buttons_layout.setObjectName(u"files_buttons_layout")
        self.files_buttons_layout_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.files_buttons_layout.addItem(self.files_buttons_layout_spacer)

        self.clear_all_reports_pushbutton = QPushButton(self.files_card)
        self.clear_all_reports_pushbutton.setObjectName(u"clear_all_reports_pushbutton")

        self.files_buttons_layout.addWidget(self.clear_all_reports_pushbutton)


        self.files_card_layout.addLayout(self.files_buttons_layout)


        self.lists_layout.addWidget(self.files_card)

        self.links_column_layout = QVBoxLayout()
        self.links_column_layout.setSpacing(16)
        self.links_column_layout.setObjectName(u"links_column_layout")
        self.links_card = QFrame(TemporalLinkStep)
        self.links_card.setObjectName(u"links_card")
        self.links_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.links_card.setFrameShadow(QFrame.Shadow.Raised)
        self.links_card_layout = QVBoxLayout(self.links_card)
        self.links_card_layout.setSpacing(10)
        self.links_card_layout.setObjectName(u"links_card_layout")
        self.links_card_layout.setContentsMargins(10, 10, 10, 10)
        self.links_title_label = QLabel(self.links_card)
        self.links_title_label.setObjectName(u"links_title_label")
        self.links_title_label.setFont(font1)

        self.links_card_layout.addWidget(self.links_title_label)

        self.window_grid = QGridLayout()
        self.window_grid.setObjectName(u"window_grid")
        self.window_grid.setHorizontalSpacing(12)
        self.window_grid.setVerticalSpacing(10)
        self.label = QLabel(self.links_card)
        self.label.setObjectName(u"label")

        self.window_grid.addWidget(self.label, 0, 0, 1, 1)

        self.analysis_window_lineedit = QLineEdit(self.links_card)
        self.analysis_window_lineedit.setObjectName(u"analysis_window_lineedit")
        self.analysis_window_lineedit.setMaximumSize(QSize(110, 16777215))

        self.window_grid.addWidget(self.analysis_window_lineedit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.links_card)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setProperty(u"variant", u"help")

        self.window_grid.addWidget(self.label_2, 0, 2, 1, 1)

        self.window_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.window_grid.addItem(self.window_grid_spacer, 0, 3, 1, 1)


        self.links_card_layout.addLayout(self.window_grid)

        self.label_3 = QLabel(self.links_card)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)
        self.label_3.setProperty(u"variant", u"help")

        self.links_card_layout.addWidget(self.label_3)

        self.temporal_links_tableview = QTableView(self.links_card)
        self.temporal_links_tableview.setObjectName(u"temporal_links_tableview")
        self.temporal_links_tableview.setAlternatingRowColors(True)
        self.temporal_links_tableview.setWordWrap(False)
        self.temporal_links_tableview.verticalHeader().setVisible(False)

        self.links_card_layout.addWidget(self.temporal_links_tableview)

        self.links_buttons_layout = QHBoxLayout()
        self.links_buttons_layout.setSpacing(8)
        self.links_buttons_layout.setObjectName(u"links_buttons_layout")
        self.links_buttons_layout_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.links_buttons_layout.addItem(self.links_buttons_layout_spacer)

        self.apply_to_all_pushbutton = QPushButton(self.links_card)
        self.apply_to_all_pushbutton.setObjectName(u"apply_to_all_pushbutton")

        self.links_buttons_layout.addWidget(self.apply_to_all_pushbutton)


        self.links_card_layout.addLayout(self.links_buttons_layout)


        self.links_column_layout.addWidget(self.links_card)

        self.output_card = QFrame(TemporalLinkStep)
        self.output_card.setObjectName(u"output_card")
        self.output_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.output_card.setFrameShadow(QFrame.Shadow.Raised)
        self.output_card_layout = QVBoxLayout(self.output_card)
        self.output_card_layout.setSpacing(10)
        self.output_card_layout.setObjectName(u"output_card_layout")
        self.output_card_layout.setContentsMargins(10, 10, 10, 10)
        self.output_title_label = QLabel(self.output_card)
        self.output_title_label.setObjectName(u"output_title_label")
        self.output_title_label.setFont(font1)

        self.output_card_layout.addWidget(self.output_title_label)

        self.csv_reports_checkbox = QCheckBox(self.output_card)
        self.csv_reports_checkbox.setObjectName(u"csv_reports_checkbox")
        self.csv_reports_checkbox.setChecked(True)

        self.output_card_layout.addWidget(self.csv_reports_checkbox)


        self.links_column_layout.addWidget(self.output_card)


        self.lists_layout.addLayout(self.links_column_layout)

        self.lists_layout.setStretch(0, 1)
        self.lists_layout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.lists_layout)

        self.about_links_layout = QVBoxLayout()
        self.about_links_layout.setSpacing(6)
        self.about_links_layout.setObjectName(u"about_links_layout")
        self.about_links_title_label = QLabel(TemporalLinkStep)
        self.about_links_title_label.setObjectName(u"about_links_title_label")
        self.about_links_title_label.setFont(font1)

        self.about_links_layout.addWidget(self.about_links_title_label)

        self.about_links_label = QLabel(TemporalLinkStep)
        self.about_links_label.setObjectName(u"about_links_label")
        self.about_links_label.setWordWrap(True)
        self.about_links_label.setProperty(u"variant", u"help")

        self.about_links_layout.addWidget(self.about_links_label)

        self.link_case_grid = QGridLayout()
        self.link_case_grid.setObjectName(u"link_case_grid")
        self.link_case_grid.setHorizontalSpacing(32)
        self.link_case_grid.setVerticalSpacing(10)
        self.link_case_1_name_label = QLabel(TemporalLinkStep)
        self.link_case_1_name_label.setObjectName(u"link_case_1_name_label")
        self.link_case_1_name_label.setFont(font1)
        self.link_case_1_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.link_case_grid.addWidget(self.link_case_1_name_label, 0, 0, 1, 1)

        self.link_case_1_label = QLabel(TemporalLinkStep)
        self.link_case_1_label.setObjectName(u"link_case_1_label")
        self.link_case_1_label.setWordWrap(True)
        self.link_case_1_label.setProperty(u"variant", u"help")

        self.link_case_grid.addWidget(self.link_case_1_label, 0, 1, 1, 1)

        self.link_case_2_name_label = QLabel(TemporalLinkStep)
        self.link_case_2_name_label.setObjectName(u"link_case_2_name_label")
        self.link_case_2_name_label.setFont(font1)
        self.link_case_2_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.link_case_grid.addWidget(self.link_case_2_name_label, 1, 0, 1, 1)

        self.link_case_2_label = QLabel(TemporalLinkStep)
        self.link_case_2_label.setObjectName(u"link_case_2_label")
        self.link_case_2_label.setWordWrap(True)
        self.link_case_2_label.setProperty(u"variant", u"help")

        self.link_case_grid.addWidget(self.link_case_2_label, 1, 1, 1, 1)

        self.link_case_3_name_label = QLabel(TemporalLinkStep)
        self.link_case_3_name_label.setObjectName(u"link_case_3_name_label")
        self.link_case_3_name_label.setFont(font1)
        self.link_case_3_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.link_case_grid.addWidget(self.link_case_3_name_label, 2, 0, 1, 1)

        self.link_case_3_label = QLabel(TemporalLinkStep)
        self.link_case_3_label.setObjectName(u"link_case_3_label")
        self.link_case_3_label.setWordWrap(True)
        self.link_case_3_label.setProperty(u"variant", u"help")

        self.link_case_grid.addWidget(self.link_case_3_label, 2, 1, 1, 1)

        self.link_case_grid.setColumnStretch(1, 1)

        self.about_links_layout.addLayout(self.link_case_grid)

        self.about_links_values_label = QLabel(TemporalLinkStep)
        self.about_links_values_label.setObjectName(u"about_links_values_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.about_links_values_label.setFont(font2)
        self.about_links_values_label.setWordWrap(True)
        self.about_links_values_label.setProperty(u"variant", u"help")

        self.about_links_layout.addWidget(self.about_links_values_label)


        self.verticalLayout.addLayout(self.about_links_layout)


        self.retranslateUi(TemporalLinkStep)
        self.apply_to_all_pushbutton.clicked.connect(TemporalLinkStep.on_apply_to_all)
        self.file_tableview.clicked.connect(TemporalLinkStep.on_file_selection_change)
        self.clear_all_reports_pushbutton.clicked.connect(TemporalLinkStep.clear_all_reports)

        QMetaObject.connectSlotsByName(TemporalLinkStep)
    # setupUi

    def retranslateUi(self, TemporalLinkStep):
        TemporalLinkStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("TemporalLinkStep", u"Temporal Links", None))
        self.subtitle_label.setText(QCoreApplication.translate("TemporalLinkStep", u"Choose the pairs of events reports to link and the analysis window.", None))
#if QT_CONFIG(tooltip)
        self.files_title_label.setToolTip(QCoreApplication.translate("TemporalLinkStep", u"Select a file to show its pairs of events reports. The number of events reports and temporal links of each file is shown.", None))
#endif // QT_CONFIG(tooltip)
        self.files_title_label.setText(QCoreApplication.translate("TemporalLinkStep", u"PSG files", None))
#if QT_CONFIG(tooltip)
        self.clear_all_reports_pushbutton.setToolTip(QCoreApplication.translate("TemporalLinkStep", u"Unchecks the temporal links of all the files.", None))
#endif // QT_CONFIG(tooltip)
        self.clear_all_reports_pushbutton.setText(QCoreApplication.translate("TemporalLinkStep", u"Clear all reports", None))
        self.links_title_label.setText(QCoreApplication.translate("TemporalLinkStep", u"Temporal links", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("TemporalLinkStep", u"The maximum delay between the start or the end of an event and the start of the linked event. Default: 0.5 s.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("TemporalLinkStep", u"Analysis window", None))
        self.label_2.setText(QCoreApplication.translate("TemporalLinkStep", u"s", None))
        self.label_3.setText(QCoreApplication.translate("TemporalLinkStep", u"Check the pairs of events reports to link (added in \"Events Report\").", None))
#if QT_CONFIG(tooltip)
        self.apply_to_all_pushbutton.setToolTip(QCoreApplication.translate("TemporalLinkStep", u"Applies the pairs checked for this file to all the files, replacing their previous selections.", None))
#endif // QT_CONFIG(tooltip)
        self.apply_to_all_pushbutton.setText(QCoreApplication.translate("TemporalLinkStep", u"Apply to all files", None))
        self.output_title_label.setText(QCoreApplication.translate("TemporalLinkStep", u"Output format", None))
#if QT_CONFIG(tooltip)
        self.csv_reports_checkbox.setToolTip(QCoreApplication.translate("TemporalLinkStep", u"Generated by default: the values are easy to export.", None))
#endif // QT_CONFIG(tooltip)
        self.csv_reports_checkbox.setText(QCoreApplication.translate("TemporalLinkStep", u"Temporal links reports (.tsv)", None))
        self.about_links_title_label.setText(QCoreApplication.translate("TemporalLinkStep", u"About the temporal links", None))
        self.about_links_label.setText(QCoreApplication.translate("TemporalLinkStep", u"Events 1 are the events kept by the 1st report, events 2 those of the 2nd report. Two events are linked when:", None))
        self.link_case_1_name_label.setText(QCoreApplication.translate("TemporalLinkStep", u"After a start", None))
        self.link_case_1_label.setText(QCoreApplication.translate("TemporalLinkStep", u"One starts within the analysis window after the start of the other.", None))
        self.link_case_2_name_label.setText(QCoreApplication.translate("TemporalLinkStep", u"After an end", None))
        self.link_case_2_label.setText(QCoreApplication.translate("TemporalLinkStep", u"One starts within the analysis window after the end of the other.", None))
        self.link_case_3_name_label.setText(QCoreApplication.translate("TemporalLinkStep", u"Overlap", None))
        self.link_case_3_label.setText(QCoreApplication.translate("TemporalLinkStep", u"They overlap in time (the window is not used).", None))
        self.about_links_values_label.setText(QCoreApplication.translate("TemporalLinkStep", u"For each case, in both orders, the report gives the number of links, the index per hour and the percentage of events 1 and events 2 linked, plus the mean delay (s) after a start or an end. It also counts the events linked in at least one case.", None))
    # retranslateUi

