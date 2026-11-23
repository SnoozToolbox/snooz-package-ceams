# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EventReportStep.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QListView, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_EventReportStep(object):
    def setupUi(self, EventReportStep):
        if not EventReportStep.objectName():
            EventReportStep.setObjectName(u"EventReportStep")
        EventReportStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(EventReportStep)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.header_layout = QVBoxLayout()
        self.header_layout.setSpacing(6)
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(EventReportStep)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.header_layout.addWidget(self.title_label)

        self.subtitle_label = QLabel(EventReportStep)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setProperty(u"variant", u"help")

        self.header_layout.addWidget(self.subtitle_label)


        self.verticalLayout.addLayout(self.header_layout)

        self.lists_layout = QHBoxLayout()
        self.lists_layout.setSpacing(16)
        self.lists_layout.setObjectName(u"lists_layout")
        self.files_column_layout = QVBoxLayout()
        self.files_column_layout.setSpacing(16)
        self.files_column_layout.setObjectName(u"files_column_layout")
        self.files_card = QFrame(EventReportStep)
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
        self.file_tableview.setSortingEnabled(False)
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


        self.files_column_layout.addWidget(self.files_card)

        self.output_card = QFrame(EventReportStep)
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

        self.csv_report_checkbox = QCheckBox(self.output_card)
        self.csv_report_checkbox.setObjectName(u"csv_report_checkbox")
        self.csv_report_checkbox.setChecked(True)

        self.output_card_layout.addWidget(self.csv_report_checkbox)

        self.events_list_checkBox = QCheckBox(self.output_card)
        self.events_list_checkBox.setObjectName(u"events_list_checkBox")

        self.output_card_layout.addWidget(self.events_list_checkBox)


        self.files_column_layout.addWidget(self.output_card)


        self.lists_layout.addLayout(self.files_column_layout)

        self.events_card = QFrame(EventReportStep)
        self.events_card.setObjectName(u"events_card")
        self.events_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.events_card.setFrameShadow(QFrame.Shadow.Raised)
        self.events_card_layout = QVBoxLayout(self.events_card)
        self.events_card_layout.setSpacing(10)
        self.events_card_layout.setObjectName(u"events_card_layout")
        self.events_card_layout.setContentsMargins(10, 10, 10, 10)
        self.events_title_label = QLabel(self.events_card)
        self.events_title_label.setObjectName(u"events_title_label")
        self.events_title_label.setFont(font1)

        self.events_card_layout.addWidget(self.events_title_label)

        self.event_treewidget = QTreeWidget(self.events_card)
        self.event_treewidget.setObjectName(u"event_treewidget")
        self.event_treewidget.setAlternatingRowColors(True)
        self.event_treewidget.setColumnCount(3)

        self.events_card_layout.addWidget(self.event_treewidget)

        self.events_buttons_layout = QHBoxLayout()
        self.events_buttons_layout.setSpacing(8)
        self.events_buttons_layout.setObjectName(u"events_buttons_layout")
        self.events_buttons_layout_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.events_buttons_layout.addItem(self.events_buttons_layout_spacer)

        self.combine_pushbutton = QPushButton(self.events_card)
        self.combine_pushbutton.setObjectName(u"combine_pushbutton")

        self.events_buttons_layout.addWidget(self.combine_pushbutton)


        self.events_card_layout.addLayout(self.events_buttons_layout)


        self.lists_layout.addWidget(self.events_card)

        self.reports_column_layout = QVBoxLayout()
        self.reports_column_layout.setSpacing(16)
        self.reports_column_layout.setObjectName(u"reports_column_layout")
        self.reports_card = QFrame(EventReportStep)
        self.reports_card.setObjectName(u"reports_card")
        self.reports_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.reports_card.setFrameShadow(QFrame.Shadow.Raised)
        self.reports_card_layout = QVBoxLayout(self.reports_card)
        self.reports_card_layout.setSpacing(10)
        self.reports_card_layout.setObjectName(u"reports_card_layout")
        self.reports_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.reports_card)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.reports_card_layout.addWidget(self.label)

        self.report_combobox = QComboBox(self.reports_card)
        self.report_combobox.setObjectName(u"report_combobox")

        self.reports_card_layout.addWidget(self.report_combobox)

        self.add_buttons_layout = QHBoxLayout()
        self.add_buttons_layout.setSpacing(8)
        self.add_buttons_layout.setObjectName(u"add_buttons_layout")
        self.add_pushbutton = QPushButton(self.reports_card)
        self.add_pushbutton.setObjectName(u"add_pushbutton")

        self.add_buttons_layout.addWidget(self.add_pushbutton)

        self.add_to_all_pushbutton = QPushButton(self.reports_card)
        self.add_to_all_pushbutton.setObjectName(u"add_to_all_pushbutton")

        self.add_buttons_layout.addWidget(self.add_to_all_pushbutton)

        self.add_buttons_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.add_buttons_layout.addItem(self.add_buttons_spacer)


        self.reports_card_layout.addLayout(self.add_buttons_layout)

        self.report_listview = QListView(self.reports_card)
        self.report_listview.setObjectName(u"report_listview")
        self.report_listview.setAlternatingRowColors(True)

        self.reports_card_layout.addWidget(self.report_listview)

        self.change_buttons_layout = QHBoxLayout()
        self.change_buttons_layout.setSpacing(8)
        self.change_buttons_layout.setObjectName(u"change_buttons_layout")
        self.modify_pushbutton = QPushButton(self.reports_card)
        self.modify_pushbutton.setObjectName(u"modify_pushbutton")

        self.change_buttons_layout.addWidget(self.modify_pushbutton)

        self.remove_pushbutton = QPushButton(self.reports_card)
        self.remove_pushbutton.setObjectName(u"remove_pushbutton")

        self.change_buttons_layout.addWidget(self.remove_pushbutton)

        self.remove_to_all_pushbutton = QPushButton(self.reports_card)
        self.remove_to_all_pushbutton.setObjectName(u"remove_to_all_pushbutton")

        self.change_buttons_layout.addWidget(self.remove_to_all_pushbutton)

        self.change_buttons_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.change_buttons_layout.addItem(self.change_buttons_spacer)


        self.reports_card_layout.addLayout(self.change_buttons_layout)

        self.create_button_layout = QHBoxLayout()
        self.create_button_layout.setSpacing(8)
        self.create_button_layout.setObjectName(u"create_button_layout")
        self.create_pushbutton = QPushButton(self.reports_card)
        self.create_pushbutton.setObjectName(u"create_pushbutton")

        self.create_button_layout.addWidget(self.create_pushbutton)

        self.create_button_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.create_button_layout.addItem(self.create_button_spacer)


        self.reports_card_layout.addLayout(self.create_button_layout)


        self.reports_column_layout.addWidget(self.reports_card)

        self.criteria_card = QFrame(EventReportStep)
        self.criteria_card.setObjectName(u"criteria_card")
        self.criteria_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.criteria_card.setFrameShadow(QFrame.Shadow.Raised)
        self.criteria_card_layout = QVBoxLayout(self.criteria_card)
        self.criteria_card_layout.setSpacing(10)
        self.criteria_card_layout.setObjectName(u"criteria_card_layout")
        self.criteria_card_layout.setContentsMargins(10, 10, 10, 10)
        self.criteria_title_label = QLabel(self.criteria_card)
        self.criteria_title_label.setObjectName(u"criteria_title_label")
        self.criteria_title_label.setFont(font1)

        self.criteria_card_layout.addWidget(self.criteria_title_label)

        self.criteria_grid = QGridLayout()
        self.criteria_grid.setObjectName(u"criteria_grid")
        self.criteria_grid.setHorizontalSpacing(8)
        self.criteria_grid.setVerticalSpacing(6)
        self.label_14 = QLabel(self.criteria_card)
        self.label_14.setObjectName(u"label_14")

        self.criteria_grid.addWidget(self.label_14, 0, 0, 1, 1)

        self.report_name_label = QLabel(self.criteria_card)
        self.report_name_label.setObjectName(u"report_name_label")

        self.criteria_grid.addWidget(self.report_name_label, 0, 1, 1, 4)

        self.label_5 = QLabel(self.criteria_card)
        self.label_5.setObjectName(u"label_5")

        self.criteria_grid.addWidget(self.label_5, 1, 0, 1, 1)

        self.duration_min_label = QLabel(self.criteria_card)
        self.duration_min_label.setObjectName(u"duration_min_label")

        self.criteria_grid.addWidget(self.duration_min_label, 1, 1, 1, 1)

        self.label_2 = QLabel(self.criteria_card)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.label_2, 1, 2, 1, 1)

        self.duration_max_label = QLabel(self.criteria_card)
        self.duration_max_label.setObjectName(u"duration_max_label")

        self.criteria_grid.addWidget(self.duration_max_label, 1, 3, 1, 1)

        self.label_7 = QLabel(self.criteria_card)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.label_7, 1, 4, 1, 1)

        self.label_15 = QLabel(self.criteria_card)
        self.label_15.setObjectName(u"label_15")

        self.criteria_grid.addWidget(self.label_15, 2, 0, 1, 1)

        self.interval_min_label = QLabel(self.criteria_card)
        self.interval_min_label.setObjectName(u"interval_min_label")

        self.criteria_grid.addWidget(self.interval_min_label, 2, 1, 1, 1)

        self.label_4 = QLabel(self.criteria_card)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.label_4, 2, 2, 1, 1)

        self.interval_max_label = QLabel(self.criteria_card)
        self.interval_max_label.setObjectName(u"interval_max_label")

        self.criteria_grid.addWidget(self.interval_max_label, 2, 3, 1, 1)

        self.label_8 = QLabel(self.criteria_card)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.label_8, 2, 4, 1, 1)

        self.label_13 = QLabel(self.criteria_card)
        self.label_13.setObjectName(u"label_13")

        self.criteria_grid.addWidget(self.label_13, 3, 0, 1, 1)

        self.min_count_label = QLabel(self.criteria_card)
        self.min_count_label.setObjectName(u"min_count_label")

        self.criteria_grid.addWidget(self.min_count_label, 3, 1, 1, 1)

        self.label_11 = QLabel(self.criteria_card)
        self.label_11.setObjectName(u"label_11")

        self.criteria_grid.addWidget(self.label_11, 4, 0, 1, 1)

        self.end_period_label = QLabel(self.criteria_card)
        self.end_period_label.setObjectName(u"end_period_label")

        self.criteria_grid.addWidget(self.end_period_label, 4, 1, 1, 1)

        self.label_12 = QLabel(self.criteria_card)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.label_12, 4, 2, 1, 1)

        self.label_9 = QLabel(self.criteria_card)
        self.label_9.setObjectName(u"label_9")

        self.criteria_grid.addWidget(self.label_9, 5, 0, 1, 1)

        self.resp_event_asso_min_label = QLabel(self.criteria_card)
        self.resp_event_asso_min_label.setObjectName(u"resp_event_asso_min_label")

        self.criteria_grid.addWidget(self.resp_event_asso_min_label, 5, 1, 1, 1)

        self.label_6 = QLabel(self.criteria_card)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.label_6, 5, 2, 1, 1)

        self.resp_event_asso_max_label = QLabel(self.criteria_card)
        self.resp_event_asso_max_label.setObjectName(u"resp_event_asso_max_label")

        self.criteria_grid.addWidget(self.resp_event_asso_max_label, 5, 3, 1, 1)

        self.label_10 = QLabel(self.criteria_card)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setProperty(u"variant", u"help")

        self.criteria_grid.addWidget(self.label_10, 5, 4, 1, 1)

        self.label_28 = QLabel(self.criteria_card)
        self.label_28.setObjectName(u"label_28")

        self.criteria_grid.addWidget(self.label_28, 6, 0, 1, 1)

        self.analysis_period_label = QLabel(self.criteria_card)
        self.analysis_period_label.setObjectName(u"analysis_period_label")

        self.criteria_grid.addWidget(self.analysis_period_label, 6, 1, 1, 4)

        self.label_3 = QLabel(self.criteria_card)
        self.label_3.setObjectName(u"label_3")

        self.criteria_grid.addWidget(self.label_3, 7, 0, 1, 1)

        self.graphic_label = QLabel(self.criteria_card)
        self.graphic_label.setObjectName(u"graphic_label")
        self.graphic_label.setEnabled(False)

        self.criteria_grid.addWidget(self.graphic_label, 7, 1, 1, 1)

        self.criteria_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.criteria_grid.addItem(self.criteria_grid_spacer, 0, 5, 1, 1)

        self.criteria_grid.setColumnStretch(5, 1)

        self.criteria_card_layout.addLayout(self.criteria_grid)


        self.reports_column_layout.addWidget(self.criteria_card)


        self.lists_layout.addLayout(self.reports_column_layout)

        self.lists_layout.setStretch(0, 1)
        self.lists_layout.setStretch(1, 1)
        self.lists_layout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.lists_layout)


        self.retranslateUi(EventReportStep)
        self.event_treewidget.clicked.connect(EventReportStep.on_event_selected)
        self.combine_pushbutton.clicked.connect(EventReportStep.on_combine_events)
        self.add_to_all_pushbutton.clicked.connect(EventReportStep.on_add_to_all)
        self.add_pushbutton.clicked.connect(EventReportStep.on_add)
        self.remove_pushbutton.clicked.connect(EventReportStep.on_remove)
        self.modify_pushbutton.clicked.connect(EventReportStep.on_modify)
        self.create_pushbutton.clicked.connect(EventReportStep.on_create)
        self.report_listview.clicked.connect(EventReportStep.on_report_selected)
        self.remove_to_all_pushbutton.clicked.connect(EventReportStep.on_remove_to_all)
        self.clear_all_reports_pushbutton.clicked.connect(EventReportStep.on_clear_all)
        self.file_tableview.clicked.connect(EventReportStep.on_file_selected)

        QMetaObject.connectSlotsByName(EventReportStep)
    # setupUi

    def retranslateUi(self, EventReportStep):
        EventReportStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("EventReportStep", u"Events Report", None))
        self.subtitle_label.setText(QCoreApplication.translate("EventReportStep", u"Select a file, then an event group or name, and add the events reports to generate.", None))
#if QT_CONFIG(tooltip)
        self.files_title_label.setToolTip(QCoreApplication.translate("EventReportStep", u"Select a file to show its events. The number of events reports and temporal links of each file is shown.", None))
#endif // QT_CONFIG(tooltip)
        self.files_title_label.setText(QCoreApplication.translate("EventReportStep", u"PSG files", None))
#if QT_CONFIG(tooltip)
        self.clear_all_reports_pushbutton.setToolTip(QCoreApplication.translate("EventReportStep", u"Removes the events reports of all the files.", None))
#endif // QT_CONFIG(tooltip)
        self.clear_all_reports_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Clear all reports", None))
        self.output_title_label.setText(QCoreApplication.translate("EventReportStep", u"Output format", None))
#if QT_CONFIG(tooltip)
        self.csv_report_checkbox.setToolTip(QCoreApplication.translate("EventReportStep", u"Generated by default: the values are easy to export.", None))
#endif // QT_CONFIG(tooltip)
        self.csv_report_checkbox.setText(QCoreApplication.translate("EventReportStep", u"Events reports (.tsv)", None))
#if QT_CONFIG(tooltip)
        self.events_list_checkBox.setToolTip(QCoreApplication.translate("EventReportStep", u"One file per report and recording.", None))
#endif // QT_CONFIG(tooltip)
        self.events_list_checkBox.setText(QCoreApplication.translate("EventReportStep", u"List of the events of each report (.tsv)", None))
#if QT_CONFIG(tooltip)
        self.events_title_label.setToolTip(QCoreApplication.translate("EventReportStep", u"Select an event group or name to show its reports and to add a report to it.", None))
#endif // QT_CONFIG(tooltip)
        self.events_title_label.setText(QCoreApplication.translate("EventReportStep", u"Events", None))
        ___qtreewidgetitem = self.event_treewidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("EventReportStep", u"Report count", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("EventReportStep", u"Event count", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("EventReportStep", u"Name", None));
#if QT_CONFIG(tooltip)
        self.combine_pushbutton.setToolTip(QCoreApplication.translate("EventReportStep", u"Creates a new group from the events you select.", None))
#endif // QT_CONFIG(tooltip)
        self.combine_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Combine events", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("EventReportStep", u"Choose a predefined report, then add it to the selected event group or name, in this file or in all the files.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("EventReportStep", u"Reports", None))
        self.add_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Add", None))
#if QT_CONFIG(tooltip)
        self.add_to_all_pushbutton.setToolTip(QCoreApplication.translate("EventReportStep", u"Adds the report to the same event group or name in all the files. The files without this event are listed.", None))
#endif // QT_CONFIG(tooltip)
        self.add_to_all_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Add to all files", None))
#if QT_CONFIG(tooltip)
        self.modify_pushbutton.setToolTip(QCoreApplication.translate("EventReportStep", u"Changes the criteria of the selected report.", None))
#endif // QT_CONFIG(tooltip)
        self.modify_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Modify", None))
        self.remove_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Remove", None))
#if QT_CONFIG(tooltip)
        self.remove_to_all_pushbutton.setToolTip(QCoreApplication.translate("EventReportStep", u"Removes the report from the same event group or name in all the files.", None))
#endif // QT_CONFIG(tooltip)
        self.remove_to_all_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Remove from all files", None))
#if QT_CONFIG(tooltip)
        self.create_pushbutton.setToolTip(QCoreApplication.translate("EventReportStep", u"Creates a report with your own criteria.", None))
#endif // QT_CONFIG(tooltip)
        self.create_pushbutton.setText(QCoreApplication.translate("EventReportStep", u"Create new report", None))
#if QT_CONFIG(tooltip)
        self.criteria_title_label.setToolTip(QCoreApplication.translate("EventReportStep", u"The criteria of the report selected in the list.", None))
#endif // QT_CONFIG(tooltip)
        self.criteria_title_label.setText(QCoreApplication.translate("EventReportStep", u"Selection criteria", None))
        self.label_14.setText(QCoreApplication.translate("EventReportStep", u"Name", None))
        self.report_name_label.setText("")
        self.label_5.setText(QCoreApplication.translate("EventReportStep", u"Duration", None))
        self.duration_min_label.setText("")
        self.label_2.setText(QCoreApplication.translate("EventReportStep", u"to", None))
        self.duration_max_label.setText("")
        self.label_7.setText(QCoreApplication.translate("EventReportStep", u"s", None))
        self.label_15.setText(QCoreApplication.translate("EventReportStep", u"Interval", None))
        self.interval_min_label.setText("")
        self.label_4.setText(QCoreApplication.translate("EventReportStep", u"to", None))
        self.interval_max_label.setText("")
        self.label_8.setText(QCoreApplication.translate("EventReportStep", u"s", None))
        self.label_13.setText(QCoreApplication.translate("EventReportStep", u"Minimum count", None))
        self.min_count_label.setText("")
        self.label_11.setText(QCoreApplication.translate("EventReportStep", u"End period after", None))
        self.end_period_label.setText("")
        self.label_12.setText(QCoreApplication.translate("EventReportStep", u"min", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("EventReportStep", u"The events that start in this interval after the end of a respiratory event are excluded.", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("EventReportStep", u"Respiratory events", None))
        self.resp_event_asso_min_label.setText("")
        self.label_6.setText(QCoreApplication.translate("EventReportStep", u"to", None))
        self.resp_event_asso_max_label.setText("")
        self.label_10.setText(QCoreApplication.translate("EventReportStep", u"s", None))
        self.label_28.setText(QCoreApplication.translate("EventReportStep", u"Events in", None))
        self.analysis_period_label.setText("")
        self.label_3.setText(QCoreApplication.translate("EventReportStep", u"Graphic", None))
        self.graphic_label.setText("")
    # retranslateUi

