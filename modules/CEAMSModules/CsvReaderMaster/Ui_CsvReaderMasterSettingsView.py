# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_CsvReaderMasterSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_CsvReaderMasterSettingsView(object):
    def setupUi(self, CsvReaderMasterSettingsView):
        if not CsvReaderMasterSettingsView.objectName():
            CsvReaderMasterSettingsView.setObjectName(u"CsvReaderMasterSettingsView")
        CsvReaderMasterSettingsView.resize(900, 700)
        self.verticalLayout = QVBoxLayout(CsvReaderMasterSettingsView)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.reader_layout = QHBoxLayout()
        self.reader_layout.setSpacing(16)
        self.reader_layout.setObjectName(u"reader_layout")
        self.files_card = QFrame(CsvReaderMasterSettingsView)
        self.files_card.setObjectName(u"files_card")
        self.files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.files_card_layout = QVBoxLayout(self.files_card)
        self.files_card_layout.setSpacing(10)
        self.files_card_layout.setObjectName(u"files_card_layout")
        self.files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.files_card)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.files_card_layout.addWidget(self.label)

        self.fileListWidget = QListWidget(self.files_card)
        self.fileListWidget.setObjectName(u"fileListWidget")

        self.files_card_layout.addWidget(self.fileListWidget)

        self.files_buttons_layout = QHBoxLayout()
        self.files_buttons_layout.setSpacing(8)
        self.files_buttons_layout.setObjectName(u"files_buttons_layout")
        self.files_buttons_layout_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.files_buttons_layout.addItem(self.files_buttons_layout_spacer)

        self.choose_pushbutton = QPushButton(self.files_card)
        self.choose_pushbutton.setObjectName(u"choose_pushbutton")

        self.files_buttons_layout.addWidget(self.choose_pushbutton)

        self.clear_pushButton = QPushButton(self.files_card)
        self.clear_pushButton.setObjectName(u"clear_pushButton")

        self.files_buttons_layout.addWidget(self.clear_pushButton)

        self.files_buttons_layout.setStretch(0, 1)

        self.files_card_layout.addLayout(self.files_buttons_layout)


        self.reader_layout.addWidget(self.files_card)

        self.settings_layout = QVBoxLayout()
        self.settings_layout.setSpacing(16)
        self.settings_layout.setObjectName(u"settings_layout")
        self.format_card = QFrame(CsvReaderMasterSettingsView)
        self.format_card.setObjectName(u"format_card")
        self.format_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.format_card.setFrameShadow(QFrame.Shadow.Raised)
        self.format_card_layout = QVBoxLayout(self.format_card)
        self.format_card_layout.setSpacing(10)
        self.format_card_layout.setObjectName(u"format_card_layout")
        self.format_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_7 = QLabel(self.format_card)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.format_card_layout.addWidget(self.label_7)

        self.format_grid = QGridLayout()
        self.format_grid.setObjectName(u"format_grid")
        self.format_grid.setHorizontalSpacing(16)
        self.format_grid.setVerticalSpacing(10)
        self.label_11 = QLabel(self.format_card)
        self.label_11.setObjectName(u"label_11")

        self.format_grid.addWidget(self.label_11, 0, 0, 1, 1)

        self.radioButton_tab = QRadioButton(self.format_card)
        self.buttonGroup = QButtonGroup(CsvReaderMasterSettingsView)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_tab)
        self.radioButton_tab.setObjectName(u"radioButton_tab")
        self.radioButton_tab.setChecked(True)

        self.format_grid.addWidget(self.radioButton_tab, 0, 1, 1, 1)

        self.radioButton_comma = QRadioButton(self.format_card)
        self.buttonGroup.addButton(self.radioButton_comma)
        self.radioButton_comma.setObjectName(u"radioButton_comma")

        self.format_grid.addWidget(self.radioButton_comma, 0, 2, 1, 1)

        self.label_5 = QLabel(self.format_card)
        self.label_5.setObjectName(u"label_5")

        self.format_grid.addWidget(self.label_5, 1, 0, 1, 1)

        self.time_radiobutton = QRadioButton(self.format_card)
        self.buttonGroup_2 = QButtonGroup(CsvReaderMasterSettingsView)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.time_radiobutton)
        self.time_radiobutton.setObjectName(u"time_radiobutton")
        self.time_radiobutton.setChecked(True)

        self.format_grid.addWidget(self.time_radiobutton, 1, 1, 1, 1)

        self.sample_radiobutton = QRadioButton(self.format_card)
        self.buttonGroup_2.addButton(self.sample_radiobutton)
        self.sample_radiobutton.setObjectName(u"sample_radiobutton")

        self.format_grid.addWidget(self.sample_radiobutton, 1, 2, 1, 1)

        self.label_6 = QLabel(self.format_card)
        self.label_6.setObjectName(u"label_6")

        self.format_grid.addWidget(self.label_6, 2, 0, 1, 1)

        self.sample_rate_lineedit = QLineEdit(self.format_card)
        self.sample_rate_lineedit.setObjectName(u"sample_rate_lineedit")
        self.sample_rate_lineedit.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sample_rate_lineedit.sizePolicy().hasHeightForWidth())
        self.sample_rate_lineedit.setSizePolicy(sizePolicy)

        self.format_grid.addWidget(self.sample_rate_lineedit, 2, 1, 1, 2)

        self.sample_rate_unit_label = QLabel(self.format_card)
        self.sample_rate_unit_label.setObjectName(u"sample_rate_unit_label")
        self.sample_rate_unit_label.setProperty(u"variant", u"help")

        self.format_grid.addWidget(self.sample_rate_unit_label, 2, 3, 1, 1)

        self.format_grid.setColumnStretch(4, 1)

        self.format_card_layout.addLayout(self.format_grid)

        self.personnalized_header_checkBox = QCheckBox(self.format_card)
        self.personnalized_header_checkBox.setObjectName(u"personnalized_header_checkBox")

        self.format_card_layout.addWidget(self.personnalized_header_checkBox)


        self.settings_layout.addWidget(self.format_card)

        self.columns_card = QFrame(CsvReaderMasterSettingsView)
        self.columns_card.setObjectName(u"columns_card")
        self.columns_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.columns_card.setFrameShadow(QFrame.Shadow.Raised)
        self.columns_card_layout = QVBoxLayout(self.columns_card)
        self.columns_card_layout.setSpacing(10)
        self.columns_card_layout.setObjectName(u"columns_card_layout")
        self.columns_card_layout.setContentsMargins(10, 10, 10, 10)
        self.columns_title_label = QLabel(self.columns_card)
        self.columns_title_label.setObjectName(u"columns_title_label")
        self.columns_title_label.setFont(font)

        self.columns_card_layout.addWidget(self.columns_title_label)

        self.columns_help_label = QLabel(self.columns_card)
        self.columns_help_label.setObjectName(u"columns_help_label")
        self.columns_help_label.setWordWrap(True)
        self.columns_help_label.setProperty(u"variant", u"help")

        self.columns_card_layout.addWidget(self.columns_help_label)

        self.columns_grid = QGridLayout()
        self.columns_grid.setObjectName(u"columns_grid")
        self.columns_grid.setHorizontalSpacing(16)
        self.columns_grid.setVerticalSpacing(10)
        self.label_10 = QLabel(self.columns_card)
        self.label_10.setObjectName(u"label_10")

        self.columns_grid.addWidget(self.label_10, 0, 0, 1, 1)

        self.group_spinbox = QSpinBox(self.columns_card)
        self.group_spinbox.setObjectName(u"group_spinbox")
        sizePolicy.setHeightForWidth(self.group_spinbox.sizePolicy().hasHeightForWidth())
        self.group_spinbox.setSizePolicy(sizePolicy)
        self.group_spinbox.setValue(1)

        self.columns_grid.addWidget(self.group_spinbox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.columns_card)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.columns_grid.addWidget(self.label_2, 1, 0, 1, 1)

        self.event_name_spinbox = QSpinBox(self.columns_card)
        self.event_name_spinbox.setObjectName(u"event_name_spinbox")
        sizePolicy.setHeightForWidth(self.event_name_spinbox.sizePolicy().hasHeightForWidth())
        self.event_name_spinbox.setSizePolicy(sizePolicy)
        self.event_name_spinbox.setMinimum(1)
        self.event_name_spinbox.setValue(2)

        self.columns_grid.addWidget(self.event_name_spinbox, 1, 1, 1, 1)

        self.label_3 = QLabel(self.columns_card)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.columns_grid.addWidget(self.label_3, 2, 0, 1, 1)

        self.onset_spinbox = QSpinBox(self.columns_card)
        self.onset_spinbox.setObjectName(u"onset_spinbox")
        sizePolicy.setHeightForWidth(self.onset_spinbox.sizePolicy().hasHeightForWidth())
        self.onset_spinbox.setSizePolicy(sizePolicy)
        self.onset_spinbox.setMinimum(1)
        self.onset_spinbox.setValue(3)

        self.columns_grid.addWidget(self.onset_spinbox, 2, 1, 1, 1)

        self.center_checkBox = QCheckBox(self.columns_card)
        self.center_checkBox.setObjectName(u"center_checkBox")

        self.columns_grid.addWidget(self.center_checkBox, 2, 2, 1, 1)

        self.label_4 = QLabel(self.columns_card)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.columns_grid.addWidget(self.label_4, 3, 0, 1, 1)

        self.duration_spinbox = QSpinBox(self.columns_card)
        self.duration_spinbox.setObjectName(u"duration_spinbox")
        sizePolicy.setHeightForWidth(self.duration_spinbox.sizePolicy().hasHeightForWidth())
        self.duration_spinbox.setSizePolicy(sizePolicy)
        self.duration_spinbox.setMinimum(0)
        self.duration_spinbox.setValue(4)

        self.columns_grid.addWidget(self.duration_spinbox, 3, 1, 1, 1)

        self.label_8 = QLabel(self.columns_card)
        self.label_8.setObjectName(u"label_8")

        self.columns_grid.addWidget(self.label_8, 4, 0, 1, 1)

        self.fixed_dur_lineEdit = QLineEdit(self.columns_card)
        self.fixed_dur_lineEdit.setObjectName(u"fixed_dur_lineEdit")
        self.fixed_dur_lineEdit.setEnabled(False)

        self.columns_grid.addWidget(self.fixed_dur_lineEdit, 4, 1, 1, 2)

        self.label_9 = QLabel(self.columns_card)
        self.label_9.setObjectName(u"label_9")

        self.columns_grid.addWidget(self.label_9, 5, 0, 1, 1)

        self.channel_spinBox = QSpinBox(self.columns_card)
        self.channel_spinBox.setObjectName(u"channel_spinBox")
        sizePolicy.setHeightForWidth(self.channel_spinBox.sizePolicy().hasHeightForWidth())
        self.channel_spinBox.setSizePolicy(sizePolicy)
        self.channel_spinBox.setValue(5)

        self.columns_grid.addWidget(self.channel_spinBox, 5, 1, 1, 1)

        self.columns_grid.setColumnStretch(2, 1)

        self.columns_card_layout.addLayout(self.columns_grid)


        self.settings_layout.addWidget(self.columns_card)

        self.settings_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.settings_layout.addItem(self.settings_stretch)


        self.reader_layout.addLayout(self.settings_layout)

        self.reader_layout.setStretch(0, 1)
        self.reader_layout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.reader_layout)


        self.retranslateUi(CsvReaderMasterSettingsView)
        self.choose_pushbutton.clicked.connect(CsvReaderMasterSettingsView.on_choose)
        self.time_radiobutton.clicked.connect(CsvReaderMasterSettingsView.on_input_format_changed)
        self.sample_radiobutton.clicked.connect(CsvReaderMasterSettingsView.on_input_format_changed)
        self.clear_pushButton.clicked.connect(self.fileListWidget.clear)
        self.duration_spinbox.valueChanged.connect(CsvReaderMasterSettingsView.on_event_pos_changed)
        self.clear_pushButton.clicked.connect(CsvReaderMasterSettingsView.clear_list_slot)

        QMetaObject.connectSlotsByName(CsvReaderMasterSettingsView)
    # setupUi

    def retranslateUi(self, CsvReaderMasterSettingsView):
        CsvReaderMasterSettingsView.setWindowTitle("")
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"The text files of annotations to read (.csv, .tsv or .txt), one annotation per row.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Annotation files", None))
        self.choose_pushbutton.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Add files", None))
#if QT_CONFIG(tooltip)
        self.choose_pushbutton.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Select csv files", None))
#endif // QT_CONFIG(tooltip)
        self.clear_pushButton.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Clear all", None))
        self.label_7.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"File format", None))
        self.label_11.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Separator", None))
        self.radioButton_tab.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"tab", None))
        self.radioButton_comma.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"comma", None))
        self.label_5.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Input format", None))
        self.time_radiobutton.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Time(s)", None))
        self.sample_radiobutton.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Samples", None))
        self.label_6.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Sample rate", None))
        self.sample_rate_lineedit.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"256", None))
        self.sample_rate_unit_label.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Hz", None))
        self.personnalized_header_checkBox.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Personalized header", None))
#if QT_CONFIG(tooltip)
        self.personnalized_header_checkBox.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Check to keep the read file header, otherwise the header will be replaced with the Snooz header.", None))
#endif // QT_CONFIG(tooltip)
        self.columns_title_label.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Columns", None))
        self.columns_help_label.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"The column of each annotation feature. 1 is the first column. Use 0 when the files do not have this column.", None))
        self.label_10.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Group", None))
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"The index of the column for the event group. To disable the group mark 0.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.group_spinbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Name", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"The index of the column for the event name. Can not be disabled.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.event_name_spinbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Onset/Center", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"The index of the column for the event onset or center. Can not be disabled.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.onset_spinbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.center_checkBox.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Event identified by its center", None))
#if QT_CONFIG(tooltip)
        self.center_checkBox.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Check if the event is identified by its center instead of its onset.", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Duration", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"The index of the column for the event duration. To disable the duration mark 0.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.duration_spinbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Fixed duration", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Enter a fixed duration for all events.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.fixed_dur_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Channel", None))
    # retranslateUi

