# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_IntroStep.ui'
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

class Ui_IntroStep(object):
    def setupUi(self, IntroStep):
        if not IntroStep.objectName():
            IntroStep.setObjectName(u"IntroStep")
        IntroStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(IntroStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(IntroStep)
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

        self.names_info = QFrame(self.content_widget)
        self.names_info.setObjectName(u"names_info")
        self.names_info.setFrameShape(QFrame.Shape.NoFrame)
        self.names_info.setProperty(u"variant", u"info")
        self.names_info_layout = QHBoxLayout(self.names_info)
        self.names_info_layout.setObjectName(u"names_info_layout")
        self.names_info_layout.setContentsMargins(14, 10, 14, 10)
        self.names_info_label = QLabel(self.names_info)
        self.names_info_label.setObjectName(u"names_info_label")
        self.names_info_label.setTextFormat(Qt.TextFormat.RichText)
        self.names_info_label.setWordWrap(True)

        self.names_info_layout.addWidget(self.names_info_label)


        self.content_layout.addWidget(self.names_info)

        self.about_renaming_layout = QVBoxLayout()
        self.about_renaming_layout.setSpacing(6)
        self.about_renaming_layout.setObjectName(u"about_renaming_layout")
        self.about_renaming_title_label = QLabel(self.content_widget)
        self.about_renaming_title_label.setObjectName(u"about_renaming_title_label")
        self.about_renaming_title_label.setFont(font3)

        self.about_renaming_layout.addWidget(self.about_renaming_title_label)

        self.about_renaming_label = QLabel(self.content_widget)
        self.about_renaming_label.setObjectName(u"about_renaming_label")
        self.about_renaming_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_renaming_label.setWordWrap(True)
        self.about_renaming_label.setProperty(u"variant", u"help")

        self.about_renaming_layout.addWidget(self.about_renaming_label)


        self.content_layout.addLayout(self.about_renaming_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(IntroStep)

        QMetaObject.connectSlotsByName(IntroStep)
    # setupUi

    def retranslateUi(self, IntroStep):
        IntroStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("IntroStep", u"Rename Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("IntroStep", u"Renames a list of files with your rules, for example to give each accessory file the name of its PSG file.", None))
        self.steps_title_label.setText(QCoreApplication.translate("IntroStep", u"What you will do", None))
        self.step_1_number_label.setText(QCoreApplication.translate("IntroStep", u"1", None))
        self.step_1_name_label.setText(QCoreApplication.translate("IntroStep", u"Input Files", None))
        self.step_1_label.setText(QCoreApplication.translate("IntroStep", u"Add the files to rename, define the renaming rules, then choose whether to keep the original files.", None))
        self.files_title_label.setText(QCoreApplication.translate("IntroStep", u"Accepted files", None))
        self.file_1_name_label.setText(QCoreApplication.translate("IntroStep", u"Files", None))
        self.file_1_label.setText(QCoreApplication.translate("IntroStep", u"Any kind of file, for example Snooz accessory files (.tsv) or text files (.txt). The extension of each file is kept.", None))
        self.names_info_label.setText(QCoreApplication.translate("IntroStep", u"<b>Why the names matter</b><br/>In many tools, you add the PSG files, and Snooz looks for the accessory file of each one in the same folder, with the same name. For example, the accessory file of subject01.edf is subject01.tsv.", None))
        self.about_renaming_title_label.setText(QCoreApplication.translate("IntroStep", u"About the renaming", None))
        self.about_renaming_label.setText(QCoreApplication.translate("IntroStep", u"<b>The order of the rules</b><br/>Snooz applies the rules to the name of each file, without its extension, in this order.<br/>\u2022 \"Pattern to remove\". Every occurrence of the pattern is removed.<br/>\u2022 \"Characters to keep\". Only the first characters of the name are kept.<br/>\u2022 \"Prefix\". It is added at the start of the name.<br/>\u2022 \"Suffix\". It is added at the end of the name.<br/>Then the extension is put back.<br/><br/><b>Example</b><br/>The file subject01_annotations_v2.tsv, with the pattern _annotations, 9 characters to keep and the prefix visit1_.<br/>\u2022 Without the pattern, the name is subject01_v2.<br/>\u2022 With its first 9 characters, it is subject01.<br/>\u2022 With the prefix, the new file is visit1_subject01.tsv.<br/><br/><b>Which files are renamed</b><br/>\u2022 With an extension in \"File extension\", only the files of the list with this extension are renamed. The other files are left as they are.<br/>\u2022 With an empty \"File extension\", all the files of the list a"
                        "re renamed.<br/><br/><b>The new files</b><br/>\u2022 Snooz copies or renames each file, as set in \"Keep the original file\".<br/>\u2022 Two files of the list must not get the same new name, for example with too few characters to keep. The second one would replace the first.<br/>\u2022 The log lists each file copied or renamed.", None))
    # retranslateUi

