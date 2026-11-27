# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SSWCIntroStep.ui'
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

class Ui_SSWCIntroStep(object):
    def setupUi(self, SSWCIntroStep):
        if not SSWCIntroStep.objectName():
            SSWCIntroStep.setObjectName(u"SSWCIntroStep")
        SSWCIntroStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(SSWCIntroStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(SSWCIntroStep)
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

        self.classification_card = QFrame(self.content_widget)
        self.classification_card.setObjectName(u"classification_card")
        self.classification_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.classification_card.setFrameShadow(QFrame.Shadow.Raised)
        self.classification_card_layout = QVBoxLayout(self.classification_card)
        self.classification_card_layout.setSpacing(10)
        self.classification_card_layout.setObjectName(u"classification_card_layout")
        self.classification_card_layout.setContentsMargins(10, 10, 10, 10)
        self.image_hist = QLabel(self.classification_card)
        self.image_hist.setObjectName(u"image_hist")

        self.classification_card_layout.addWidget(self.image_hist)


        self.content_layout.addWidget(self.classification_card)

        self.files_info = QFrame(self.content_widget)
        self.files_info.setObjectName(u"files_info")
        self.files_info.setFrameShape(QFrame.Shape.NoFrame)
        self.files_info.setProperty(u"variant", u"info")
        self.files_info_layout = QHBoxLayout(self.files_info)
        self.files_info_layout.setObjectName(u"files_info_layout")
        self.files_info_layout.setContentsMargins(14, 10, 14, 10)
        self.files_info_label = QLabel(self.files_info)
        self.files_info_label.setObjectName(u"files_info_label")
        self.files_info_label.setTextFormat(Qt.TextFormat.RichText)
        self.files_info_label.setWordWrap(True)

        self.files_info_layout.addWidget(self.files_info_label)


        self.content_layout.addWidget(self.files_info)

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

        self.step_line_2 = QFrame(self.steps_card)
        self.step_line_2.setObjectName(u"step_line_2")
        self.step_line_2.setFrameShape(QFrame.Shape.HLine)
        self.step_line_2.setFrameShadow(QFrame.Shadow.Plain)

        self.steps_grid.addWidget(self.step_line_2, 1, 0, 1, 4)

        self.step_2_number_label = QLabel(self.steps_card)
        self.step_2_number_label.setObjectName(u"step_2_number_label")
        self.step_2_number_label.setFont(font2)
        self.step_2_number_label.setProperty(u"variant", u"step_number")
        self.step_2_number_label.setMinimumSize(QSize(24, 24))
        self.step_2_number_label.setMaximumSize(QSize(24, 24))
        self.step_2_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.steps_grid.addWidget(self.step_2_number_label, 2, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.step_2_name_label = QLabel(self.steps_card)
        self.step_2_name_label.setObjectName(u"step_2_name_label")
        self.step_2_name_label.setFont(font3)
        self.step_2_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_2_name_label, 2, 1, 1, 1)

        self.step_2_label = QLabel(self.steps_card)
        self.step_2_label.setObjectName(u"step_2_label")
        self.step_2_label.setWordWrap(True)
        self.step_2_label.setProperty(u"variant", u"help")
        self.step_2_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_2_label, 2, 3, 1, 1)

        self.step_line_3 = QFrame(self.steps_card)
        self.step_line_3.setObjectName(u"step_line_3")
        self.step_line_3.setFrameShape(QFrame.Shape.HLine)
        self.step_line_3.setFrameShadow(QFrame.Shadow.Plain)

        self.steps_grid.addWidget(self.step_line_3, 3, 0, 1, 4)

        self.step_3_number_label = QLabel(self.steps_card)
        self.step_3_number_label.setObjectName(u"step_3_number_label")
        self.step_3_number_label.setFont(font2)
        self.step_3_number_label.setProperty(u"variant", u"step_number")
        self.step_3_number_label.setMinimumSize(QSize(24, 24))
        self.step_3_number_label.setMaximumSize(QSize(24, 24))
        self.step_3_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.steps_grid.addWidget(self.step_3_number_label, 4, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.step_3_name_label = QLabel(self.steps_card)
        self.step_3_name_label.setObjectName(u"step_3_name_label")
        self.step_3_name_label.setFont(font3)
        self.step_3_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_3_name_label, 4, 1, 1, 1)

        self.step_3_label = QLabel(self.steps_card)
        self.step_3_label.setObjectName(u"step_3_label")
        self.step_3_label.setWordWrap(True)
        self.step_3_label.setProperty(u"variant", u"help")
        self.step_3_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.steps_grid.addWidget(self.step_3_label, 4, 3, 1, 1)

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
        self.file_grid = QGridLayout()
        self.file_grid.setObjectName(u"file_grid")
        self.file_grid.setHorizontalSpacing(32)
        self.file_grid.setVerticalSpacing(10)
        self.file_1_name_label = QLabel(self.files_card)
        self.file_1_name_label.setObjectName(u"file_1_name_label")
        self.file_1_name_label.setFont(font3)
        self.file_1_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.file_grid.addWidget(self.file_1_name_label, 0, 0, 1, 1)

        self.file_1_label = QLabel(self.files_card)
        self.file_1_label.setObjectName(u"file_1_label")
        self.file_1_label.setWordWrap(True)

        self.file_grid.addWidget(self.file_1_label, 0, 1, 1, 1)

        self.file_2_name_label = QLabel(self.files_card)
        self.file_2_name_label.setObjectName(u"file_2_name_label")
        self.file_2_name_label.setFont(font3)
        self.file_2_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.file_grid.addWidget(self.file_2_name_label, 1, 0, 1, 1)

        self.file_2_label = QLabel(self.files_card)
        self.file_2_label.setObjectName(u"file_2_label")
        self.file_2_label.setWordWrap(True)

        self.file_grid.addWidget(self.file_2_label, 1, 1, 1, 1)

        self.file_3_name_label = QLabel(self.files_card)
        self.file_3_name_label.setObjectName(u"file_3_name_label")
        self.file_3_name_label.setFont(font3)
        self.file_3_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.file_grid.addWidget(self.file_3_name_label, 2, 0, 1, 1)

        self.file_3_label = QLabel(self.files_card)
        self.file_3_label.setObjectName(u"file_3_label")
        self.file_3_label.setWordWrap(True)

        self.file_grid.addWidget(self.file_3_label, 2, 1, 1, 1)

        self.file_grid.setColumnStretch(1, 1)

        self.files_card_layout.addLayout(self.file_grid)


        self.files_section_layout.addWidget(self.files_card)


        self.content_layout.addLayout(self.files_section_layout)

        self.about_classification_layout = QVBoxLayout()
        self.about_classification_layout.setSpacing(6)
        self.about_classification_layout.setObjectName(u"about_classification_layout")
        self.about_classification_title_label = QLabel(self.content_widget)
        self.about_classification_title_label.setObjectName(u"about_classification_title_label")
        self.about_classification_title_label.setFont(font3)

        self.about_classification_layout.addWidget(self.about_classification_title_label)

        self.about_classification_label = QLabel(self.content_widget)
        self.about_classification_label.setObjectName(u"about_classification_label")
        self.about_classification_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_classification_label.setWordWrap(True)
        self.about_classification_label.setProperty(u"variant", u"help")

        self.about_classification_layout.addWidget(self.about_classification_label)

        self.references_layout = QVBoxLayout()
        self.references_layout.setSpacing(8)
        self.references_layout.setObjectName(u"references_layout")
        self.references_layout.setContentsMargins(0, 6, 0, 0)
        self.references_line = QFrame(self.content_widget)
        self.references_line.setObjectName(u"references_line")
        self.references_line.setFrameShape(QFrame.Shape.HLine)
        self.references_line.setFrameShadow(QFrame.Shadow.Plain)

        self.references_layout.addWidget(self.references_line)

        self.references_label = QLabel(self.content_widget)
        self.references_label.setObjectName(u"references_label")
        self.references_label.setFont(font2)
        self.references_label.setTextFormat(Qt.TextFormat.RichText)
        self.references_label.setWordWrap(True)
        self.references_label.setOpenExternalLinks(True)
        self.references_label.setProperty(u"variant", u"help")

        self.references_layout.addWidget(self.references_label)


        self.about_classification_layout.addLayout(self.references_layout)


        self.content_layout.addLayout(self.about_classification_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SSWCIntroStep)

        QMetaObject.connectSlotsByName(SSWCIntroStep)
    # setupUi

    def retranslateUi(self, SSWCIntroStep):
        SSWCIntroStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("SSWCIntroStep", u"Classify Slow Waves", None))
        self.subtitle_label.setText(QCoreApplication.translate("SSWCIntroStep", u"Classifies the slow waves of a cohort into categories based on their transition frequency, and reports their characteristics per category.", None))
        self.image_hist.setText("")
        self.files_info_label.setText(QCoreApplication.translate("SSWCIntroStep", u"<b>Before you start</b><br/>Run \"Detect Slow Waves\" on your cohort with \"Detailed report for the cohort\" and \"Characteristics of each slow wave\" checked in its step \"Output Files\". This tool needs the three kinds of file it writes.", None))
        self.steps_title_label.setText(QCoreApplication.translate("SSWCIntroStep", u"What you will do", None))
        self.step_1_number_label.setText(QCoreApplication.translate("SSWCIntroStep", u"1", None))
        self.step_1_name_label.setText(QCoreApplication.translate("SSWCIntroStep", u"Input Files", None))
        self.step_1_label.setText(QCoreApplication.translate("SSWCIntroStep", u"Add the slow wave characteristics files, the slow wave cohort report and the sleep stages files written by \"Detect Slow Waves\".", None))
        self.step_2_number_label.setText(QCoreApplication.translate("SSWCIntroStep", u"2", None))
        self.step_2_name_label.setText(QCoreApplication.translate("SSWCIntroStep", u"Classification Criteria", None))
        self.step_2_label.setText(QCoreApplication.translate("SSWCIntroStep", u"Classify the slow waves automatically, or set the number of categories.", None))
        self.step_3_number_label.setText(QCoreApplication.translate("SSWCIntroStep", u"3", None))
        self.step_3_name_label.setText(QCoreApplication.translate("SSWCIntroStep", u"Output Files", None))
        self.step_3_label.setText(QCoreApplication.translate("SSWCIntroStep", u"Choose the output folder and the number of segments of the night. Optionally, change the maximum number of sleep cycles in \"Hours and Cycles\".", None))
        self.files_title_label.setText(QCoreApplication.translate("SSWCIntroStep", u"Accepted files", None))
        self.file_1_name_label.setText(QCoreApplication.translate("SSWCIntroStep", u"Slow wave characteristics", None))
        self.file_1_label.setText(QCoreApplication.translate("SSWCIntroStep", u"One file per recording (.tsv), with one row per slow wave.", None))
        self.file_2_name_label.setText(QCoreApplication.translate("SSWCIntroStep", u"Slow wave cohort report", None))
        self.file_2_label.setText(QCoreApplication.translate("SSWCIntroStep", u"One file for the cohort (.tsv), with one row per recording and channel.", None))
        self.file_3_name_label.setText(QCoreApplication.translate("SSWCIntroStep", u"Sleep stages", None))
        self.file_3_label.setText(QCoreApplication.translate("SSWCIntroStep", u"One file per recording (.tsv), with the epochs in which the slow waves were detected.", None))
        self.about_classification_title_label.setText(QCoreApplication.translate("SSWCIntroStep", u"About the classification", None))
        self.about_classification_label.setText(QCoreApplication.translate("SSWCIntroStep", u"<b>The transition frequency</b><br/>\u2022 It tells how fast a slow wave goes from its negative peak to its positive peak.<br/>\u2022 It is 1/(2\u03c4), where \u03c4 is the time from the negative peak to the positive peak [1].<br/>\u2022 \"Detect Slow Waves\" writes it for each slow wave, in the column trans_freq_Hz of the slow wave characteristics files.<br/><br/><b>The categories</b><br/>\u2022 Snooz puts together the slow waves of all the files and channels. Then it fits a Gaussian mixture to the distribution of their transition frequencies.<br/>\u2022 Each Gaussian component is a category of slow waves. The number of components is found automatically or set by you, in the step \"Classification Criteria\".<br/>\u2022 Each slow wave goes to the closest category, with a k-means clustering started from the means of the components.<br/>\u2022 The categories are numbered by transition frequency. Category 1 holds the slow waves with the slowest transitions.<br/>\u2022 The same categories are used for all the reco"
                        "rdings of the cohort.", None))
        self.references_label.setText(QCoreApplication.translate("SSWCIntroStep", u"[1] Bouchard, M., Lina, J.-M., Gaudreault, P.-O., Lafreni\u00e8re, A., Dub\u00e9, J., Gosselin, N., &amp; Carrier, J. (2021). Sleeping at the switch. <i>eLife</i>, <i>10</i>, Article e64337. <a href=\"https://doi.org/10.7554/eLife.64337\">https://doi.org/10.7554/eLife.64337</a>", None))
    # retranslateUi

