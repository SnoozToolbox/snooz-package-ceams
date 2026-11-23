# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_GenerateReportStep.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_GenerateReportStep(object):
    def setupUi(self, GenerateReportStep):
        if not GenerateReportStep.objectName():
            GenerateReportStep.setObjectName(u"GenerateReportStep")
        GenerateReportStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(GenerateReportStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(GenerateReportStep)
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

        self.output_card = QFrame(self.content_widget)
        self.output_card.setObjectName(u"output_card")
        self.output_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.output_card.setFrameShadow(QFrame.Shadow.Raised)
        self.output_card_layout = QVBoxLayout(self.output_card)
        self.output_card_layout.setSpacing(10)
        self.output_card_layout.setObjectName(u"output_card_layout")
        self.output_card_layout.setContentsMargins(10, 10, 10, 10)
        self.output_title_label = QLabel(self.output_card)
        self.output_title_label.setObjectName(u"output_title_label")
        font1 = QFont()
        font1.setBold(True)
        self.output_title_label.setFont(font1)

        self.output_card_layout.addWidget(self.output_title_label)

        self.output_grid = QGridLayout()
        self.output_grid.setObjectName(u"output_grid")
        self.output_grid.setHorizontalSpacing(12)
        self.output_grid.setVerticalSpacing(10)
        self.label = QLabel(self.output_card)
        self.label.setObjectName(u"label")

        self.output_grid.addWidget(self.label, 0, 0, 1, 1)

        self.output_directory_layout = QHBoxLayout()
        self.output_directory_layout.setSpacing(8)
        self.output_directory_layout.setObjectName(u"output_directory_layout")
        self.output_lineedit = QLineEdit(self.output_card)
        self.output_lineedit.setObjectName(u"output_lineedit")

        self.output_directory_layout.addWidget(self.output_lineedit)

        self.choose_pushbutton = QPushButton(self.output_card)
        self.choose_pushbutton.setObjectName(u"choose_pushbutton")

        self.output_directory_layout.addWidget(self.choose_pushbutton)


        self.output_grid.addLayout(self.output_directory_layout, 0, 1, 1, 1)

        self.label_3 = QLabel(self.output_card)
        self.label_3.setObjectName(u"label_3")

        self.output_grid.addWidget(self.label_3, 1, 0, 1, 1)

        self.prefix_lineedit = QLineEdit(self.output_card)
        self.prefix_lineedit.setObjectName(u"prefix_lineedit")

        self.output_grid.addWidget(self.prefix_lineedit, 1, 1, 1, 1)

        self.output_grid.setColumnStretch(1, 1)

        self.output_card_layout.addLayout(self.output_grid)

        self.prefix_help_label = QLabel(self.output_card)
        self.prefix_help_label.setObjectName(u"prefix_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.prefix_help_label.setFont(font2)
        self.prefix_help_label.setTextFormat(Qt.TextFormat.RichText)
        self.prefix_help_label.setWordWrap(True)
        self.prefix_help_label.setProperty(u"variant", u"help")

        self.output_card_layout.addWidget(self.prefix_help_label)


        self.content_layout.addWidget(self.output_card)

        self.sleep_card = QFrame(self.content_widget)
        self.sleep_card.setObjectName(u"sleep_card")
        self.sleep_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.sleep_card.setFrameShadow(QFrame.Shadow.Raised)
        self.sleep_card_layout = QVBoxLayout(self.sleep_card)
        self.sleep_card_layout.setSpacing(10)
        self.sleep_card_layout.setObjectName(u"sleep_card_layout")
        self.sleep_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_5 = QLabel(self.sleep_card)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.sleep_card_layout.addWidget(self.label_5)

        self.sleep_layout = QVBoxLayout()
        self.sleep_layout.setSpacing(8)
        self.sleep_layout.setObjectName(u"sleep_layout")
        self.sleep_layout_1_layout = QVBoxLayout()
        self.sleep_layout_1_layout.setSpacing(2)
        self.sleep_layout_1_layout.setObjectName(u"sleep_layout_1_layout")
        self.csv_report_checkbox = QCheckBox(self.sleep_card)
        self.csv_report_checkbox.setObjectName(u"csv_report_checkbox")

        self.sleep_layout_1_layout.addWidget(self.csv_report_checkbox)

        self.sleep_help_label = QLabel(self.sleep_card)
        self.sleep_help_label.setObjectName(u"sleep_help_label")
        self.sleep_help_label.setFont(font2)
        self.sleep_help_label.setWordWrap(True)
        self.sleep_help_label.setIndent(26)
        self.sleep_help_label.setProperty(u"variant", u"help")

        self.sleep_layout_1_layout.addWidget(self.sleep_help_label)


        self.sleep_layout.addLayout(self.sleep_layout_1_layout)


        self.sleep_card_layout.addLayout(self.sleep_layout)

        self.cycles_help_label = QLabel(self.sleep_card)
        self.cycles_help_label.setObjectName(u"cycles_help_label")
        self.cycles_help_label.setFont(font2)
        self.cycles_help_label.setTextFormat(Qt.TextFormat.RichText)
        self.cycles_help_label.setWordWrap(True)
        self.cycles_help_label.setProperty(u"variant", u"help")

        self.sleep_card_layout.addWidget(self.cycles_help_label)


        self.content_layout.addWidget(self.sleep_card)

        self.lists_cards_layout = QHBoxLayout()
        self.lists_cards_layout.setSpacing(16)
        self.lists_cards_layout.setObjectName(u"lists_cards_layout")
        self.events_list_card = QFrame(self.content_widget)
        self.events_list_card.setObjectName(u"events_list_card")
        self.events_list_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.events_list_card.setFrameShadow(QFrame.Shadow.Raised)
        self.events_list_card_layout = QVBoxLayout(self.events_list_card)
        self.events_list_card_layout.setSpacing(10)
        self.events_list_card_layout.setObjectName(u"events_list_card_layout")
        self.events_list_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.events_list_card)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.events_list_card_layout.addWidget(self.label_2)

        self.events_list_label = QLabel(self.events_list_card)
        self.events_list_label.setObjectName(u"events_list_label")
        self.events_list_label.setWordWrap(True)
        self.events_list_label.setProperty(u"variant", u"help")

        self.events_list_card_layout.addWidget(self.events_list_label)

        self.event_report_listwidget = QListWidget(self.events_list_card)
        self.event_report_listwidget.setObjectName(u"event_report_listwidget")
        self.event_report_listwidget.setEditTriggers(QAbstractItemView.EditTrigger.CurrentChanged|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.event_report_listwidget.setAlternatingRowColors(True)

        self.events_list_card_layout.addWidget(self.event_report_listwidget)


        self.lists_cards_layout.addWidget(self.events_list_card)

        self.links_list_card = QFrame(self.content_widget)
        self.links_list_card.setObjectName(u"links_list_card")
        self.links_list_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.links_list_card.setFrameShadow(QFrame.Shadow.Raised)
        self.links_list_card_layout = QVBoxLayout(self.links_list_card)
        self.links_list_card_layout.setSpacing(10)
        self.links_list_card_layout.setObjectName(u"links_list_card_layout")
        self.links_list_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_4 = QLabel(self.links_list_card)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.links_list_card_layout.addWidget(self.label_4)

        self.links_list_label = QLabel(self.links_list_card)
        self.links_list_label.setObjectName(u"links_list_label")
        self.links_list_label.setWordWrap(True)
        self.links_list_label.setProperty(u"variant", u"help")

        self.links_list_card_layout.addWidget(self.links_list_label)

        self.temporallinks_listwidget = QListWidget(self.links_list_card)
        self.temporallinks_listwidget.setObjectName(u"temporallinks_listwidget")
        self.temporallinks_listwidget.setAlternatingRowColors(True)

        self.links_list_card_layout.addWidget(self.temporallinks_listwidget)


        self.lists_cards_layout.addWidget(self.links_list_card)

        self.lists_cards_layout.setStretch(0, 1)
        self.lists_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.lists_cards_layout)

        self.append_warning = QFrame(self.content_widget)
        self.append_warning.setObjectName(u"append_warning")
        self.append_warning.setFrameShape(QFrame.Shape.NoFrame)
        self.append_warning.setProperty(u"variant", u"warning")
        self.append_warning_layout = QHBoxLayout(self.append_warning)
        self.append_warning_layout.setObjectName(u"append_warning_layout")
        self.append_warning_layout.setContentsMargins(14, 10, 14, 10)
        self.append_warning_label = QLabel(self.append_warning)
        self.append_warning_label.setObjectName(u"append_warning_label")
        self.append_warning_label.setTextFormat(Qt.TextFormat.RichText)
        self.append_warning_label.setWordWrap(True)

        self.append_warning_layout.addWidget(self.append_warning_label)


        self.content_layout.addWidget(self.append_warning)

        self.about_reports_layout = QVBoxLayout()
        self.about_reports_layout.setSpacing(6)
        self.about_reports_layout.setObjectName(u"about_reports_layout")
        self.about_reports_title_label = QLabel(self.content_widget)
        self.about_reports_title_label.setObjectName(u"about_reports_title_label")
        self.about_reports_title_label.setFont(font1)

        self.about_reports_layout.addWidget(self.about_reports_title_label)

        self.about_reports_label = QLabel(self.content_widget)
        self.about_reports_label.setObjectName(u"about_reports_label")
        self.about_reports_label.setWordWrap(True)
        self.about_reports_label.setProperty(u"variant", u"help")

        self.about_reports_layout.addWidget(self.about_reports_label)


        self.content_layout.addLayout(self.about_reports_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(GenerateReportStep)
        self.choose_pushbutton.clicked.connect(GenerateReportStep.on_choose)

        QMetaObject.connectSlotsByName(GenerateReportStep)
    # setupUi

    def retranslateUi(self, GenerateReportStep):
        GenerateReportStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("GenerateReportStep", u"Generate Reports", None))
        self.subtitle_label.setText(QCoreApplication.translate("GenerateReportStep", u"Choose where to save the reports, then check the list of the reports to generate. Go back to a step to fix the list.", None))
        self.output_title_label.setText(QCoreApplication.translate("GenerateReportStep", u"Output files", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("GenerateReportStep", u"Choose the output directory for all the reports to generate.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("GenerateReportStep", u"Output directory", None))
        self.output_lineedit.setPlaceholderText(QCoreApplication.translate("GenerateReportStep", u"Select a folder", None))
#if QT_CONFIG(tooltip)
        self.output_lineedit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.choose_pushbutton.setText(QCoreApplication.translate("GenerateReportStep", u"Choose", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("GenerateReportStep", u"Label added to each report to identify your reports.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("GenerateReportStep", u"Report prefix", None))
#if QT_CONFIG(tooltip)
        self.prefix_lineedit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.prefix_help_label.setText(QCoreApplication.translate("GenerateReportStep", u"The filenames start with the prefix: <i>prefix</i>.tsv for the sleep report, <i>prefix</i>_<i>report name</i>.tsv for the events and temporal links reports.", None))
        self.label_5.setText(QCoreApplication.translate("GenerateReportStep", u"Sleep report", None))
        self.csv_report_checkbox.setText(QCoreApplication.translate("GenerateReportStep", u"Generate the sleep report", None))
        self.sleep_help_label.setText(QCoreApplication.translate("GenerateReportStep", u"The distribution of the sleep stages and the transitions between them.", None))
        self.cycles_help_label.setText(QCoreApplication.translate("GenerateReportStep", u"The number of sleep cycles reported is set in <b>Hours and Cycles</b>, under Optional settings in the left panel.", None))
        self.label_2.setText(QCoreApplication.translate("GenerateReportStep", u"Events reports", None))
        self.events_list_label.setText(QCoreApplication.translate("GenerateReportStep", u"Added in Events Report: the events by sleep stage, sleep cycle, and thirds and halves of the night.", None))
        self.label_4.setText(QCoreApplication.translate("GenerateReportStep", u"Temporal links reports", None))
        self.links_list_label.setText(QCoreApplication.translate("GenerateReportStep", u"Checked in Temporal Links: the links between the events of two reports.", None))
        self.append_warning_label.setText(QCoreApplication.translate("GenerateReportStep", u"<b>The data are appended</b><br/>Each report gets one row per PSG recording, added at the end of the file when it exists.", None))
        self.about_reports_title_label.setText(QCoreApplication.translate("GenerateReportStep", u"About the reports", None))
        self.about_reports_label.setText(QCoreApplication.translate("GenerateReportStep", u"Each report is a .tsv file: one row per PSG recording and one column per variable. The variables are defined in the _info.tsv file written with each report. In the lists, the number after a report is its number of files.", None))
    # retranslateUi

