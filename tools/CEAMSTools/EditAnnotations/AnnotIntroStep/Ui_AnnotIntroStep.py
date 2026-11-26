# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AnnotIntroStep.ui'
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

class Ui_AnnotIntroStep(object):
    def setupUi(self, AnnotIntroStep):
        if not AnnotIntroStep.objectName():
            AnnotIntroStep.setObjectName(u"AnnotIntroStep")
        AnnotIntroStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(AnnotIntroStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(AnnotIntroStep)
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

        self.before_info = QFrame(self.content_widget)
        self.before_info.setObjectName(u"before_info")
        self.before_info.setFrameShape(QFrame.Shape.NoFrame)
        self.before_info.setProperty(u"variant", u"info")
        self.before_info_layout = QHBoxLayout(self.before_info)
        self.before_info_layout.setObjectName(u"before_info_layout")
        self.before_info_layout.setContentsMargins(14, 10, 14, 10)
        self.before_info_label = QLabel(self.before_info)
        self.before_info_label.setObjectName(u"before_info_label")
        self.before_info_label.setTextFormat(Qt.TextFormat.RichText)
        self.before_info_label.setWordWrap(True)

        self.before_info_layout.addWidget(self.before_info_label)


        self.content_layout.addWidget(self.before_info)

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

        self.file_2_name_label = QLabel(self.files_card)
        self.file_2_name_label.setObjectName(u"file_2_name_label")
        self.file_2_name_label.setFont(font3)

        self.files_grid.addWidget(self.file_2_name_label, 1, 0, 1, 1)

        self.file_2_label = QLabel(self.files_card)
        self.file_2_label.setObjectName(u"file_2_label")
        self.file_2_label.setWordWrap(True)

        self.files_grid.addWidget(self.file_2_label, 1, 1, 1, 1)

        self.file_3_name_label = QLabel(self.files_card)
        self.file_3_name_label.setObjectName(u"file_3_name_label")
        self.file_3_name_label.setFont(font3)

        self.files_grid.addWidget(self.file_3_name_label, 2, 0, 1, 1)

        self.file_3_label = QLabel(self.files_card)
        self.file_3_label.setObjectName(u"file_3_label")
        self.file_3_label.setWordWrap(True)

        self.files_grid.addWidget(self.file_3_label, 2, 1, 1, 1)

        self.files_grid.setColumnStretch(1, 1)

        self.files_card_layout.addLayout(self.files_grid)


        self.files_section_layout.addWidget(self.files_card)


        self.content_layout.addLayout(self.files_section_layout)

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


        self.retranslateUi(AnnotIntroStep)

        QMetaObject.connectSlotsByName(AnnotIntroStep)
    # setupUi

    def retranslateUi(self, AnnotIntroStep):
        AnnotIntroStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("AnnotIntroStep", u"Edit Snooz Annotations", None))
        self.subtitle_label.setText(QCoreApplication.translate("AnnotIntroStep", u"Deletes or renames annotations in batches, for example to make the annotations of a cohort more concise.", None))
        self.before_info_label.setText(QCoreApplication.translate("AnnotIntroStep", u"<b>Before you start</b><br/>Make a copy of your annotation files (.tsv, .sts or .ent). At runtime, the tool overwrites the annotations of the original files with your changes.", None))
        self.steps_title_label.setText(QCoreApplication.translate("AnnotIntroStep", u"What you will do", None))
        self.step_1_number_label.setText(QCoreApplication.translate("AnnotIntroStep", u"1", None))
        self.step_1_name_label.setText(QCoreApplication.translate("AnnotIntroStep", u"Input Files", None))
        self.step_1_label.setText(QCoreApplication.translate("AnnotIntroStep", u"Add the PSG files whose annotations you want to edit.", None))
        self.step_2_number_label.setText(QCoreApplication.translate("AnnotIntroStep", u"2", None))
        self.step_2_name_label.setText(QCoreApplication.translate("AnnotIntroStep", u"Remove or edit", None))
        self.step_2_label.setText(QCoreApplication.translate("AnnotIntroStep", u"Uncheck the annotations to remove and edit the labels to rename, for one recording or for the cohort.", None))
        self.files_title_label.setText(QCoreApplication.translate("AnnotIntroStep", u"Accepted files", None))
        self.file_1_name_label.setText(QCoreApplication.translate("AnnotIntroStep", u"EDF", None))
        self.file_1_label.setText(QCoreApplication.translate("AnnotIntroStep", u"The .edf and .tsv files must have the exact same filename and be stored in the same directory.", None))
        self.file_2_name_label.setText(QCoreApplication.translate("AnnotIntroStep", u"Stellate", None))
        self.file_2_label.setText(QCoreApplication.translate("AnnotIntroStep", u"The .sig and .sts files must have the exact same filename and be stored in the same directory.", None))
        self.file_3_name_label.setText(QCoreApplication.translate("AnnotIntroStep", u"NATUS", None))
        self.file_3_label.setText(QCoreApplication.translate("AnnotIntroStep", u"For CEAMS users only. The whole NATUS subject folder is required.", None))
        self.about_editing_title_label.setText(QCoreApplication.translate("AnnotIntroStep", u"About the editing", None))
        self.about_editing_label.setText(QCoreApplication.translate("AnnotIntroStep", u"<b>Removing and renaming</b><br/>To remove annotations, uncheck their group or name. To rename them, edit the label in the \"Group\u2011Name\" column.<br/>\u2022 In \"Events from selection\", the changes apply to the recording selected in \"PSG Files\".<br/>\u2022 In \"Events from cohort\", the changes apply to all the recordings.<br/><br/><b>Buttons</b><br/>\u2022 \"Refresh\" updates \"Events from cohort\". It merges the edited groups that have the same label and sorts the annotations by their new label.<br/>\u2022 \"Back to original labels\" undoes the changes made since the files were opened.<br/>\u2022 \"Export\" shows all the changes to apply at runtime, in tables you can download as TSV. The annotations to rename come first, then the annotations to remove.", None))
    # retranslateUi

