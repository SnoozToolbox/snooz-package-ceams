# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_InputFilesStep.ui'
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
    QDateTimeEdit, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTableView, QVBoxLayout, QWidget)
import themes_rc

class Ui_InputFilesStep(object):
    def setupUi(self, InputFilesStep):
        if not InputFilesStep.objectName():
            InputFilesStep.setObjectName(u"InputFilesStep")
        InputFilesStep.resize(900, 700)
        self.verticalLayout = QVBoxLayout(InputFilesStep)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.header_layout = QVBoxLayout()
        self.header_layout.setSpacing(6)
        self.header_layout.setObjectName(u"header_layout")
        self.title_label = QLabel(InputFilesStep)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.header_layout.addWidget(self.title_label)

        self.subtitle_label = QLabel(InputFilesStep)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setProperty(u"variant", u"help")

        self.header_layout.addWidget(self.subtitle_label)


        self.verticalLayout.addLayout(self.header_layout)

        self.lists_layout = QHBoxLayout()
        self.lists_layout.setSpacing(16)
        self.lists_layout.setObjectName(u"lists_layout")
        self.files_card = QFrame(InputFilesStep)
        self.files_card.setObjectName(u"files_card")
        self.files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.files_card_layout = QVBoxLayout(self.files_card)
        self.files_card_layout.setSpacing(10)
        self.files_card_layout.setObjectName(u"files_card_layout")
        self.files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_12 = QLabel(self.files_card)
        self.label_12.setObjectName(u"label_12")
        font1 = QFont()
        font1.setBold(True)
        self.label_12.setFont(font1)

        self.files_card_layout.addWidget(self.label_12)

        self.file_tableview = QTableView(self.files_card)
        self.file_tableview.setObjectName(u"file_tableview")
        self.file_tableview.setAlternatingRowColors(True)
        self.file_tableview.setSelectionMode(QAbstractItemView.SingleSelection)
        self.file_tableview.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.file_tableview.horizontalHeader().setStretchLastSection(True)

        self.files_card_layout.addWidget(self.file_tableview)

        self.files_buttons_layout = QHBoxLayout()
        self.files_buttons_layout.setSpacing(8)
        self.files_buttons_layout.setObjectName(u"files_buttons_layout")
        self.add_pushbutton = QPushButton(self.files_card)
        self.add_pushbutton.setObjectName(u"add_pushbutton")

        self.files_buttons_layout.addWidget(self.add_pushbutton)

        self.add_from_folder_pushbutton = QPushButton(self.files_card)
        self.add_from_folder_pushbutton.setObjectName(u"add_from_folder_pushbutton")

        self.files_buttons_layout.addWidget(self.add_from_folder_pushbutton)

        self.files_buttons_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.files_buttons_layout.addItem(self.files_buttons_spacer)

        self.remove_pushbutton = QPushButton(self.files_card)
        self.remove_pushbutton.setObjectName(u"remove_pushbutton")

        self.files_buttons_layout.addWidget(self.remove_pushbutton)


        self.files_card_layout.addLayout(self.files_buttons_layout)


        self.lists_layout.addWidget(self.files_card)

        self.subject_card = QFrame(InputFilesStep)
        self.subject_card.setObjectName(u"subject_card")
        self.subject_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.subject_card.setFrameShadow(QFrame.Shadow.Raised)
        self.subject_card_layout = QVBoxLayout(self.subject_card)
        self.subject_card_layout.setSpacing(10)
        self.subject_card_layout.setObjectName(u"subject_card_layout")
        self.subject_card_layout.setContentsMargins(10, 10, 10, 10)
        self.subject_title_label = QLabel(self.subject_card)
        self.subject_title_label.setObjectName(u"subject_title_label")
        self.subject_title_label.setFont(font1)

        self.subject_card_layout.addWidget(self.subject_title_label)

        self.identification_grid = QGridLayout()
        self.identification_grid.setObjectName(u"identification_grid")
        self.identification_grid.setHorizontalSpacing(12)
        self.identification_grid.setVerticalSpacing(10)
        self.label = QLabel(self.subject_card)
        self.label.setObjectName(u"label")

        self.identification_grid.addWidget(self.label, 0, 0, 1, 1)

        self.id1_lineedit = QLineEdit(self.subject_card)
        self.id1_lineedit.setObjectName(u"id1_lineedit")

        self.identification_grid.addWidget(self.id1_lineedit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.subject_card)
        self.label_2.setObjectName(u"label_2")

        self.identification_grid.addWidget(self.label_2, 1, 0, 1, 1)

        self.id2_lineedit = QLineEdit(self.subject_card)
        self.id2_lineedit.setObjectName(u"id2_lineedit")

        self.identification_grid.addWidget(self.id2_lineedit, 1, 1, 1, 1)

        self.label_3 = QLabel(self.subject_card)
        self.label_3.setObjectName(u"label_3")

        self.identification_grid.addWidget(self.label_3, 2, 0, 1, 1)

        self.last_name_lineedit = QLineEdit(self.subject_card)
        self.last_name_lineedit.setObjectName(u"last_name_lineedit")

        self.identification_grid.addWidget(self.last_name_lineedit, 2, 1, 1, 1)

        self.label_4 = QLabel(self.subject_card)
        self.label_4.setObjectName(u"label_4")

        self.identification_grid.addWidget(self.label_4, 3, 0, 1, 1)

        self.first_name_lineedit = QLineEdit(self.subject_card)
        self.first_name_lineedit.setObjectName(u"first_name_lineedit")

        self.identification_grid.addWidget(self.first_name_lineedit, 3, 1, 1, 1)

        self.sex_label = QLabel(self.subject_card)
        self.sex_label.setObjectName(u"sex_label")

        self.identification_grid.addWidget(self.sex_label, 4, 0, 1, 1)

        self.sex_combobox = QComboBox(self.subject_card)
        self.sex_combobox.addItem("")
        self.sex_combobox.addItem("")
        self.sex_combobox.addItem("")
        self.sex_combobox.setObjectName(u"sex_combobox")

        self.identification_grid.addWidget(self.sex_combobox, 4, 1, 1, 1)

        self.label_7 = QLabel(self.subject_card)
        self.label_7.setObjectName(u"label_7")

        self.identification_grid.addWidget(self.label_7, 5, 0, 1, 1)

        self.age_spinbox = QSpinBox(self.subject_card)
        self.age_spinbox.setObjectName(u"age_spinbox")
        self.age_spinbox.setMinimum(0)
        self.age_spinbox.setMaximum(200)
        self.age_spinbox.setValue(0)

        self.identification_grid.addWidget(self.age_spinbox, 5, 1, 1, 1)

        self.label_5 = QLabel(self.subject_card)
        self.label_5.setObjectName(u"label_5")

        self.identification_grid.addWidget(self.label_5, 6, 0, 1, 1)

        self.birthdate_timeedit = QDateTimeEdit(self.subject_card)
        self.birthdate_timeedit.setObjectName(u"birthdate_timeedit")
        self.birthdate_timeedit.setCalendarPopup(True)

        self.identification_grid.addWidget(self.birthdate_timeedit, 6, 1, 1, 1)

        self.label_6 = QLabel(self.subject_card)
        self.label_6.setObjectName(u"label_6")

        self.identification_grid.addWidget(self.label_6, 7, 0, 1, 1)

        self.record_date_timeedit = QDateTimeEdit(self.subject_card)
        self.record_date_timeedit.setObjectName(u"record_date_timeedit")
        self.record_date_timeedit.setCalendarPopup(True)

        self.identification_grid.addWidget(self.record_date_timeedit, 7, 1, 1, 1)

        self.identification_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.identification_grid.addItem(self.identification_grid_spacer, 0, 3, 1, 1)


        self.subject_card_layout.addLayout(self.identification_grid)

        self.subject_line = QFrame(self.subject_card)
        self.subject_line.setObjectName(u"subject_line")
        self.subject_line.setFrameShape(QFrame.Shape.HLine)
        self.subject_line.setFrameShadow(QFrame.Shadow.Plain)

        self.subject_card_layout.addWidget(self.subject_line)

        self.measurements_title_label = QLabel(self.subject_card)
        self.measurements_title_label.setObjectName(u"measurements_title_label")
        self.measurements_title_label.setFont(font1)

        self.subject_card_layout.addWidget(self.measurements_title_label)

        self.measurements_grid = QGridLayout()
        self.measurements_grid.setObjectName(u"measurements_grid")
        self.measurements_grid.setHorizontalSpacing(12)
        self.measurements_grid.setVerticalSpacing(10)
        self.label_8 = QLabel(self.subject_card)
        self.label_8.setObjectName(u"label_8")

        self.measurements_grid.addWidget(self.label_8, 0, 0, 1, 1)

        self.height_doublespinbox = QDoubleSpinBox(self.subject_card)
        self.height_doublespinbox.setObjectName(u"height_doublespinbox")
        self.height_doublespinbox.setMaximum(1000.000000000000000)

        self.measurements_grid.addWidget(self.height_doublespinbox, 0, 1, 1, 1)

        self.height_unit_combobox = QComboBox(self.subject_card)
        self.height_unit_combobox.addItem("")
        self.height_unit_combobox.addItem("")
        self.height_unit_combobox.setObjectName(u"height_unit_combobox")

        self.measurements_grid.addWidget(self.height_unit_combobox, 0, 2, 1, 1)

        self.label_9 = QLabel(self.subject_card)
        self.label_9.setObjectName(u"label_9")

        self.measurements_grid.addWidget(self.label_9, 1, 0, 1, 1)

        self.weight_doublespinbox = QDoubleSpinBox(self.subject_card)
        self.weight_doublespinbox.setObjectName(u"weight_doublespinbox")
        self.weight_doublespinbox.setMaximum(1000.000000000000000)

        self.measurements_grid.addWidget(self.weight_doublespinbox, 1, 1, 1, 1)

        self.weight_unit_combobox = QComboBox(self.subject_card)
        self.weight_unit_combobox.addItem("")
        self.weight_unit_combobox.addItem("")
        self.weight_unit_combobox.setObjectName(u"weight_unit_combobox")

        self.measurements_grid.addWidget(self.weight_unit_combobox, 1, 2, 1, 1)

        self.label_10 = QLabel(self.subject_card)
        self.label_10.setObjectName(u"label_10")

        self.measurements_grid.addWidget(self.label_10, 2, 0, 1, 1)

        self.waistline_doublespinbox = QDoubleSpinBox(self.subject_card)
        self.waistline_doublespinbox.setObjectName(u"waistline_doublespinbox")
        self.waistline_doublespinbox.setMaximum(1000.000000000000000)

        self.measurements_grid.addWidget(self.waistline_doublespinbox, 2, 1, 1, 1)

        self.waistline_unit_combobox = QComboBox(self.subject_card)
        self.waistline_unit_combobox.addItem("")
        self.waistline_unit_combobox.addItem("")
        self.waistline_unit_combobox.setObjectName(u"waistline_unit_combobox")

        self.measurements_grid.addWidget(self.waistline_unit_combobox, 2, 2, 1, 1)

        self.label_11 = QLabel(self.subject_card)
        self.label_11.setObjectName(u"label_11")

        self.measurements_grid.addWidget(self.label_11, 3, 0, 1, 1)

        self.bmi_doublespinbox = QDoubleSpinBox(self.subject_card)
        self.bmi_doublespinbox.setObjectName(u"bmi_doublespinbox")
        self.bmi_doublespinbox.setMaximum(1000.000000000000000)

        self.measurements_grid.addWidget(self.bmi_doublespinbox, 3, 1, 1, 1)

        self.measurements_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.measurements_grid.addItem(self.measurements_grid_spacer, 0, 3, 1, 1)


        self.subject_card_layout.addLayout(self.measurements_grid)

        self.deidentify_line = QFrame(self.subject_card)
        self.deidentify_line.setObjectName(u"deidentify_line")
        self.deidentify_line.setFrameShape(QFrame.Shape.HLine)
        self.deidentify_line.setFrameShadow(QFrame.Shadow.Plain)

        self.subject_card_layout.addWidget(self.deidentify_line)

        self.deidentify_checkbox = QCheckBox(self.subject_card)
        self.deidentify_checkbox.setObjectName(u"deidentify_checkbox")

        self.subject_card_layout.addWidget(self.deidentify_checkbox)

        self.subject_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.subject_card_layout.addItem(self.subject_stretch)


        self.lists_layout.addWidget(self.subject_card)

        self.lists_layout.setStretch(0, 1)
        self.lists_layout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.lists_layout)


        self.retranslateUi(InputFilesStep)
        self.remove_pushbutton.clicked.connect(InputFilesStep.on_remove_file)
        self.add_pushbutton.clicked.connect(InputFilesStep.on_add_files)
        self.add_from_folder_pushbutton.clicked.connect(InputFilesStep.on_add_from_folder)
        self.deidentify_checkbox.clicked.connect(InputFilesStep.on_deidentify_change)

        self.sex_combobox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(InputFilesStep)
    # setupUi

    def retranslateUi(self, InputFilesStep):
        InputFilesStep.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("InputFilesStep", u"Input Files", None))
        self.subtitle_label.setText(QCoreApplication.translate("InputFilesStep", u"Add the PSG files, then check the information of each subject: it is written in the reports.", None))
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("InputFilesStep", u"Select a file to show the information of its subject. A file without sleep stages is not added.", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("InputFilesStep", u"PSG files", None))
        self.add_pushbutton.setText(QCoreApplication.translate("InputFilesStep", u"Add", None))
#if QT_CONFIG(tooltip)
        self.add_from_folder_pushbutton.setToolTip(QCoreApplication.translate("InputFilesStep", u"Adds the PSG files found in the folders you select.", None))
#endif // QT_CONFIG(tooltip)
        self.add_from_folder_pushbutton.setText(QCoreApplication.translate("InputFilesStep", u"Add from folder", None))
#if QT_CONFIG(tooltip)
        self.remove_pushbutton.setToolTip(QCoreApplication.translate("InputFilesStep", u"Removes the selected file and its reports.", None))
#endif // QT_CONFIG(tooltip)
        self.remove_pushbutton.setText(QCoreApplication.translate("InputFilesStep", u"Remove", None))
#if QT_CONFIG(tooltip)
        self.subject_title_label.setToolTip(QCoreApplication.translate("InputFilesStep", u"Read from the PSG file and written in the reports. Your changes are kept for the selected file.", None))
#endif // QT_CONFIG(tooltip)
        self.subject_title_label.setText(QCoreApplication.translate("InputFilesStep", u"Subject information", None))
        self.label.setText(QCoreApplication.translate("InputFilesStep", u"Id 1", None))
        self.label_2.setText(QCoreApplication.translate("InputFilesStep", u"Id 2", None))
        self.label_3.setText(QCoreApplication.translate("InputFilesStep", u"Last name", None))
        self.label_4.setText(QCoreApplication.translate("InputFilesStep", u"First name", None))
        self.sex_label.setText(QCoreApplication.translate("InputFilesStep", u"Sex", None))
        self.sex_combobox.setItemText(0, QCoreApplication.translate("InputFilesStep", u"F", None))
        self.sex_combobox.setItemText(1, QCoreApplication.translate("InputFilesStep", u"M", None))
        self.sex_combobox.setItemText(2, QCoreApplication.translate("InputFilesStep", u"X", None))

        self.label_7.setText(QCoreApplication.translate("InputFilesStep", u"Age", None))
        self.age_spinbox.setSpecialValueText(QCoreApplication.translate("InputFilesStep", u"Not defined", None))
        self.age_spinbox.setSuffix("")
        self.label_5.setText(QCoreApplication.translate("InputFilesStep", u"Birthdate", None))
        self.birthdate_timeedit.setDisplayFormat(QCoreApplication.translate("InputFilesStep", u"yyyy-MM-dd", None))
        self.label_6.setText(QCoreApplication.translate("InputFilesStep", u"Record date", None))
        self.measurements_title_label.setText(QCoreApplication.translate("InputFilesStep", u"Measurements", None))
        self.label_8.setText(QCoreApplication.translate("InputFilesStep", u"Height", None))
        self.height_doublespinbox.setSpecialValueText(QCoreApplication.translate("InputFilesStep", u"Not defined", None))
        self.height_unit_combobox.setItemText(0, QCoreApplication.translate("InputFilesStep", u"meters", None))
        self.height_unit_combobox.setItemText(1, QCoreApplication.translate("InputFilesStep", u"feets", None))

        self.label_9.setText(QCoreApplication.translate("InputFilesStep", u"Weight", None))
        self.weight_doublespinbox.setSpecialValueText(QCoreApplication.translate("InputFilesStep", u"Not defined", None))
        self.weight_unit_combobox.setItemText(0, QCoreApplication.translate("InputFilesStep", u"kg", None))
        self.weight_unit_combobox.setItemText(1, QCoreApplication.translate("InputFilesStep", u"lbs", None))

        self.label_10.setText(QCoreApplication.translate("InputFilesStep", u"Waistline", None))
        self.waistline_doublespinbox.setSpecialValueText(QCoreApplication.translate("InputFilesStep", u"Not defined", None))
        self.waistline_unit_combobox.setItemText(0, QCoreApplication.translate("InputFilesStep", u"cm", None))
        self.waistline_unit_combobox.setItemText(1, QCoreApplication.translate("InputFilesStep", u"inches", None))

        self.label_11.setText(QCoreApplication.translate("InputFilesStep", u"BMI", None))
        self.bmi_doublespinbox.setSpecialValueText(QCoreApplication.translate("InputFilesStep", u"Not defined", None))
#if QT_CONFIG(tooltip)
        self.deidentify_checkbox.setToolTip(QCoreApplication.translate("InputFilesStep", u"The first name, the last name and the birthdate of all the files are not written in the reports.", None))
#endif // QT_CONFIG(tooltip)
        self.deidentify_checkbox.setText(QCoreApplication.translate("InputFilesStep", u"De-identify all files", None))
    # retranslateUi

