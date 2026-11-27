# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SSWCOutputFiles.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)
import themes_rc

class Ui_SSWCOutputFiles(object):
    def setupUi(self, SSWCOutputFiles):
        if not SSWCOutputFiles.objectName():
            SSWCOutputFiles.setObjectName(u"SSWCOutputFiles")
        SSWCOutputFiles.resize(900, 700)
        self.verticalLayout = QVBoxLayout(SSWCOutputFiles)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(SSWCOutputFiles)
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

        self.folder_card = QFrame(self.content_widget)
        self.folder_card.setObjectName(u"folder_card")
        self.folder_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.folder_card.setFrameShadow(QFrame.Shadow.Raised)
        self.folder_card_layout = QVBoxLayout(self.folder_card)
        self.folder_card_layout.setSpacing(10)
        self.folder_card_layout.setObjectName(u"folder_card_layout")
        self.folder_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_10 = QLabel(self.folder_card)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setBold(True)
        self.label_10.setFont(font1)

        self.folder_card_layout.addWidget(self.label_10)

        self.folder_layout = QHBoxLayout()
        self.folder_layout.setSpacing(8)
        self.folder_layout.setObjectName(u"folder_layout")
        self.label = QLabel(self.folder_card)
        self.label.setObjectName(u"label")

        self.folder_layout.addWidget(self.label)

        self.foldername_lineEdit = QLineEdit(self.folder_card)
        self.foldername_lineEdit.setObjectName(u"foldername_lineEdit")

        self.folder_layout.addWidget(self.foldername_lineEdit)

        self.choose_pushButton = QPushButton(self.folder_card)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.folder_layout.addWidget(self.choose_pushButton)


        self.folder_card_layout.addLayout(self.folder_layout)

        self.folder_help_label = QLabel(self.folder_card)
        self.folder_help_label.setObjectName(u"folder_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.folder_help_label.setFont(font2)
        self.folder_help_label.setWordWrap(True)
        self.folder_help_label.setProperty(u"variant", u"help")

        self.folder_card_layout.addWidget(self.folder_help_label)


        self.content_layout.addWidget(self.folder_card)

        self.event_level_card = QFrame(self.content_widget)
        self.event_level_card.setObjectName(u"event_level_card")
        self.event_level_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.event_level_card.setFrameShadow(QFrame.Shadow.Raised)
        self.event_level_card_layout = QVBoxLayout(self.event_level_card)
        self.event_level_card_layout.setSpacing(10)
        self.event_level_card_layout.setObjectName(u"event_level_card_layout")
        self.event_level_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_4 = QLabel(self.event_level_card)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.event_level_card_layout.addWidget(self.label_4)

        self.event_level_text_layout = QVBoxLayout()
        self.event_level_text_layout.setSpacing(4)
        self.event_level_text_layout.setObjectName(u"event_level_text_layout")
        self.label_2 = QLabel(self.event_level_card)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)
        self.label_2.setProperty(u"variant", u"help")

        self.event_level_text_layout.addWidget(self.label_2)

        self.label_3 = QLabel(self.event_level_card)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)
        self.label_3.setProperty(u"variant", u"help")

        self.event_level_text_layout.addWidget(self.label_3)

        self.label_6 = QLabel(self.event_level_card)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)
        self.label_6.setProperty(u"variant", u"help")

        self.event_level_text_layout.addWidget(self.label_6)


        self.event_level_card_layout.addLayout(self.event_level_text_layout)


        self.content_layout.addWidget(self.event_level_card)

        self.subject_level_card = QFrame(self.content_widget)
        self.subject_level_card.setObjectName(u"subject_level_card")
        self.subject_level_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.subject_level_card.setFrameShadow(QFrame.Shadow.Raised)
        self.subject_level_card_layout = QVBoxLayout(self.subject_level_card)
        self.subject_level_card_layout.setSpacing(10)
        self.subject_level_card_layout.setObjectName(u"subject_level_card_layout")
        self.subject_level_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_5 = QLabel(self.subject_level_card)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.subject_level_card_layout.addWidget(self.label_5)

        self.subject_level_text_layout = QVBoxLayout()
        self.subject_level_text_layout.setSpacing(4)
        self.subject_level_text_layout.setObjectName(u"subject_level_text_layout")
        self.label_7 = QLabel(self.subject_level_card)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)
        self.label_7.setProperty(u"variant", u"help")

        self.subject_level_text_layout.addWidget(self.label_7)

        self.label_8 = QLabel(self.subject_level_card)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setWordWrap(True)
        self.label_8.setProperty(u"variant", u"help")

        self.subject_level_text_layout.addWidget(self.label_8)

        self.label_18 = QLabel(self.subject_level_card)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setWordWrap(True)
        self.label_18.setProperty(u"variant", u"help")

        self.subject_level_text_layout.addWidget(self.label_18)

        self.label_17 = QLabel(self.subject_level_card)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setWordWrap(True)
        self.label_17.setProperty(u"variant", u"help")

        self.subject_level_text_layout.addWidget(self.label_17)


        self.subject_level_card_layout.addLayout(self.subject_level_text_layout)

        self.label_11 = QLabel(self.subject_level_card)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setWordWrap(True)
        self.label_11.setProperty(u"variant", u"help")

        self.subject_level_card_layout.addWidget(self.label_11)

        self.segments_grid = QGridLayout()
        self.segments_grid.setObjectName(u"segments_grid")
        self.segments_grid.setHorizontalSpacing(12)
        self.segments_grid.setVerticalSpacing(10)
        self.label_9 = QLabel(self.subject_level_card)
        self.label_9.setObjectName(u"label_9")

        self.segments_grid.addWidget(self.label_9, 0, 0, 1, 1)

        self.spinBox_n_division = QSpinBox(self.subject_level_card)
        self.spinBox_n_division.setObjectName(u"spinBox_n_division")

        self.segments_grid.addWidget(self.spinBox_n_division, 0, 1, 1, 1)

        self.segments_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.segments_grid.addItem(self.segments_grid_spacer, 0, 3, 1, 1)


        self.subject_level_card_layout.addLayout(self.segments_grid)

        self.label_16 = QLabel(self.subject_level_card)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setWordWrap(True)
        self.label_16.setProperty(u"variant", u"help")

        self.subject_level_card_layout.addWidget(self.label_16)


        self.content_layout.addWidget(self.subject_level_card)

        self.model_card = QFrame(self.content_widget)
        self.model_card.setObjectName(u"model_card")
        self.model_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.model_card.setFrameShadow(QFrame.Shadow.Raised)
        self.model_card_layout = QVBoxLayout(self.model_card)
        self.model_card_layout.setSpacing(10)
        self.model_card_layout.setObjectName(u"model_card_layout")
        self.model_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_12 = QLabel(self.model_card)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.model_card_layout.addWidget(self.label_12)

        self.model_text_layout = QVBoxLayout()
        self.model_text_layout.setSpacing(4)
        self.model_text_layout.setObjectName(u"model_text_layout")
        self.label_title = QLabel(self.model_card)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setWordWrap(True)
        self.label_title.setProperty(u"variant", u"help")

        self.model_text_layout.addWidget(self.label_title)

        self.label_13 = QLabel(self.model_card)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setWordWrap(True)
        self.label_13.setProperty(u"variant", u"help")

        self.model_text_layout.addWidget(self.label_13)

        self.label_14 = QLabel(self.model_card)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setWordWrap(True)
        self.label_14.setProperty(u"variant", u"help")

        self.model_text_layout.addWidget(self.label_14)


        self.model_card_layout.addLayout(self.model_text_layout)


        self.content_layout.addWidget(self.model_card)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SSWCOutputFiles)
        self.choose_pushButton.clicked.connect(SSWCOutputFiles.on_choose)

        QMetaObject.connectSlotsByName(SSWCOutputFiles)
    # setupUi

    def retranslateUi(self, SSWCOutputFiles):
        SSWCOutputFiles.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("SSWCOutputFiles", u"Output Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("SSWCOutputFiles", u"Choose the output folder and the number of segments of the night for the cohort report.", None))
        self.label_10.setText(QCoreApplication.translate("SSWCOutputFiles", u"Output folder", None))
        self.label.setText(QCoreApplication.translate("SSWCOutputFiles", u"Folder", None))
        self.foldername_lineEdit.setPlaceholderText(QCoreApplication.translate("SSWCOutputFiles", u"Choose a destination folder for the output files", None))
        self.foldername_lineEdit.setText("")
        self.choose_pushButton.setText(QCoreApplication.translate("SSWCOutputFiles", u"Choose", None))
        self.folder_help_label.setText(QCoreApplication.translate("SSWCOutputFiles", u"Files with the same names are replaced. The slow wave characteristics files keep their names, so choose a folder other than theirs to keep the original files.", None))
        self.label_4.setText(QCoreApplication.translate("SSWCOutputFiles", u"Slow wave characteristics by event level", None))
        self.label_2.setText(QCoreApplication.translate("SSWCOutputFiles", u"Each slow wave is labeled with its category.", None))
        self.label_3.setText(QCoreApplication.translate("SSWCOutputFiles", u"The slow wave characteristics files are copied to the output folder, under the same names, with the category of each slow wave in a new column, category.", None))
        self.label_6.setText(QCoreApplication.translate("SSWCOutputFiles", u"There is one slow wave characteristics file per PSG recording.", None))
        self.label_5.setText(QCoreApplication.translate("SSWCOutputFiles", u"Slow wave characteristics by subject level", None))
        self.label_7.setText(QCoreApplication.translate("SSWCOutputFiles", u"A cohort report, sw_cohort_details_per_categories.tsv, holds the slow wave characteristics averaged per category.", None))
        self.label_8.setText(QCoreApplication.translate("SSWCOutputFiles", u"The slow wave characteristics are also given per sleep cycle and per segment of the night.", None))
        self.label_18.setText(QCoreApplication.translate("SSWCOutputFiles", u"\u2022 Per sleep cycle, only the valid data is counted. The artifacts and the sleep stages not selected for the detection are left out.", None))
        self.label_17.setText(QCoreApplication.translate("SSWCOutputFiles", u"\u2022 Per segment of the night, all the epochs of the sleep stages file are divided into segments, artifacts included. These are the epochs of the sleep stages selected for the detection, inside the sleep cycles.", None))
        self.label_11.setText(QCoreApplication.translate("SSWCOutputFiles", u"Choose the granularity of the segments. Select 2 to divide the night into halves, 3 for thirds, 4 for quarters, and so on.", None))
        self.label_9.setText(QCoreApplication.translate("SSWCOutputFiles", u"Number of segments", None))
        self.label_16.setText(QCoreApplication.translate("SSWCOutputFiles", u"A description file, sw_cohort_details_per_categories_info.tsv, gives the definition of each column of the cohort report.", None))
        self.label_12.setText(QCoreApplication.translate("SSWCOutputFiles", u"Classification model", None))
        self.label_title.setText(QCoreApplication.translate("SSWCOutputFiles", u"The distribution of the transition frequencies of the cohort is modeled with a Gaussian mixture.", None))
        self.label_13.setText(QCoreApplication.translate("SSWCOutputFiles", u"The histogram of the transition frequencies, with the resulting model, is saved in the output folder as a picture (.pdf).", None))
        self.label_14.setText(QCoreApplication.translate("SSWCOutputFiles", u"When the number of categories is found automatically (not set manually), the picture also shows the Akaike information criterion (AIC) for 1 to 4 categories.", None))
    # retranslateUi

