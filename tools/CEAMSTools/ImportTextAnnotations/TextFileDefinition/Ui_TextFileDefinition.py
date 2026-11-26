# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_TextFileDefinition.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)
import themes_rc

class Ui_TextFileDefinition(object):
    def setupUi(self, TextFileDefinition):
        if not TextFileDefinition.objectName():
            TextFileDefinition.setObjectName(u"TextFileDefinition")
        TextFileDefinition.resize(900, 700)
        self.verticalLayout = QVBoxLayout(TextFileDefinition)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(TextFileDefinition)
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

        self.reader_card = QFrame(self.content_widget)
        self.reader_card.setObjectName(u"reader_card")
        self.reader_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.reader_card.setFrameShadow(QFrame.Shadow.Raised)
        self.reader_card_layout = QVBoxLayout(self.reader_card)
        self.reader_card_layout.setSpacing(10)
        self.reader_card_layout.setObjectName(u"reader_card_layout")
        self.reader_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_10 = QLabel(self.reader_card)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setBold(True)
        self.label_10.setFont(font1)

        self.reader_card_layout.addWidget(self.label_10)

        self.reader_grid = QGridLayout()
        self.reader_grid.setObjectName(u"reader_grid")
        self.reader_grid.setHorizontalSpacing(12)
        self.reader_grid.setVerticalSpacing(10)
        self.label_11 = QLabel(self.reader_card)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(150, 16777215))

        self.reader_grid.addWidget(self.label_11, 0, 0, 1, 1)

        self.delimiter_lineedit = QLineEdit(self.reader_card)
        self.delimiter_lineedit.setObjectName(u"delimiter_lineedit")
        self.delimiter_lineedit.setInputMethodHints(Qt.InputMethodHint.ImhDialableCharactersOnly)
        self.delimiter_lineedit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.reader_grid.addWidget(self.delimiter_lineedit, 0, 1, 1, 1)

        self.label = QLabel(self.reader_card)
        self.label.setObjectName(u"label")

        self.reader_grid.addWidget(self.label, 1, 0, 1, 1)

        self.spinBox_nrows_hdr = QSpinBox(self.reader_card)
        self.spinBox_nrows_hdr.setObjectName(u"spinBox_nrows_hdr")

        self.reader_grid.addWidget(self.spinBox_nrows_hdr, 1, 1, 1, 1)

        self.label_13 = QLabel(self.reader_card)
        self.label_13.setObjectName(u"label_13")

        self.reader_grid.addWidget(self.label_13, 2, 0, 1, 1)

        self.comboBox_encoding = QComboBox(self.reader_card)
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.setObjectName(u"comboBox_encoding")

        self.reader_grid.addWidget(self.comboBox_encoding, 2, 1, 1, 1)

        self.reader_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.reader_grid.addItem(self.reader_grid_spacer, 0, 3, 1, 1)


        self.reader_card_layout.addLayout(self.reader_grid)

        self.rows_help_label = QLabel(self.reader_card)
        self.rows_help_label.setObjectName(u"rows_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.rows_help_label.setFont(font2)
        self.rows_help_label.setWordWrap(True)
        self.rows_help_label.setProperty(u"variant", u"help")

        self.reader_card_layout.addWidget(self.rows_help_label)


        self.content_layout.addWidget(self.reader_card)

        self.time_card = QFrame(self.content_widget)
        self.time_card.setObjectName(u"time_card")
        self.time_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.time_card.setFrameShadow(QFrame.Shadow.Raised)
        self.time_card_layout = QVBoxLayout(self.time_card)
        self.time_card_layout.setSpacing(10)
        self.time_card_layout.setObjectName(u"time_card_layout")
        self.time_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_5 = QLabel(self.time_card)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.time_card_layout.addWidget(self.label_5)

        self.time_help_label = QLabel(self.time_card)
        self.time_help_label.setObjectName(u"time_help_label")
        self.time_help_label.setWordWrap(True)
        self.time_help_label.setProperty(u"variant", u"help")

        self.time_card_layout.addWidget(self.time_help_label)

        self.time_options = QVBoxLayout()
        self.time_options.setSpacing(8)
        self.time_options.setObjectName(u"time_options")
        self.time_options_1_layout = QVBoxLayout()
        self.time_options_1_layout.setSpacing(2)
        self.time_options_1_layout.setObjectName(u"time_options_1_layout")
        self.time_option_layout = QVBoxLayout()
        self.time_option_layout.setSpacing(6)
        self.time_option_layout.setObjectName(u"time_option_layout")
        self.time_radiobutton = QRadioButton(self.time_card)
        self.buttonGroup_2 = QButtonGroup(TextFileDefinition)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.time_radiobutton)
        self.time_radiobutton.setObjectName(u"time_radiobutton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_radiobutton.sizePolicy().hasHeightForWidth())
        self.time_radiobutton.setSizePolicy(sizePolicy)
        self.time_radiobutton.setChecked(True)

        self.time_option_layout.addWidget(self.time_radiobutton)

        self.label_7 = QLabel(self.time_card)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setTextFormat(Qt.TextFormat.RichText)
        self.label_7.setWordWrap(True)
        self.label_7.setIndent(26)
        self.label_7.setProperty(u"variant", u"help")

        self.time_option_layout.addWidget(self.label_7)

        self.time_formats_layout = QHBoxLayout()
        self.time_formats_layout.setObjectName(u"time_formats_layout")
        self.time_formats_layout.setContentsMargins(26, 0, 0, 0)
        self.time_formats_grid = QGridLayout()
        self.time_formats_grid.setObjectName(u"time_formats_grid")
        self.time_formats_grid.setHorizontalSpacing(12)
        self.time_formats_grid.setVerticalSpacing(10)
        self.label_12 = QLabel(self.time_card)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setMinimumSize(QSize(250, 0))
        self.label_12.setMaximumSize(QSize(16777215, 16777215))

        self.time_formats_grid.addWidget(self.label_12, 0, 0, 1, 1)

        self.lineEdit_onset_time_format = QLineEdit(self.time_card)
        self.lineEdit_onset_time_format.setObjectName(u"lineEdit_onset_time_format")

        self.time_formats_grid.addWidget(self.lineEdit_onset_time_format, 0, 1, 1, 1)

        self.label_14 = QLabel(self.time_card)
        self.label_14.setObjectName(u"label_14")

        self.time_formats_grid.addWidget(self.label_14, 1, 0, 1, 1)

        self.lineEdit_dur_time_format = QLineEdit(self.time_card)
        self.lineEdit_dur_time_format.setObjectName(u"lineEdit_dur_time_format")

        self.time_formats_grid.addWidget(self.lineEdit_dur_time_format, 1, 1, 1, 1)

        self.time_formats_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.time_formats_grid.addItem(self.time_formats_grid_spacer, 0, 3, 1, 1)


        self.time_formats_layout.addLayout(self.time_formats_grid)


        self.time_option_layout.addLayout(self.time_formats_layout)


        self.time_options_1_layout.addLayout(self.time_option_layout)


        self.time_options.addLayout(self.time_options_1_layout)

        self.time_options_line_1 = QFrame(self.time_card)
        self.time_options_line_1.setObjectName(u"time_options_line_1")
        self.time_options_line_1.setFrameShape(QFrame.Shape.HLine)
        self.time_options_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.time_options.addWidget(self.time_options_line_1)

        self.time_options_2_layout = QVBoxLayout()
        self.time_options_2_layout.setSpacing(2)
        self.time_options_2_layout.setObjectName(u"time_options_2_layout")
        self.samples_option_layout = QVBoxLayout()
        self.samples_option_layout.setSpacing(6)
        self.samples_option_layout.setObjectName(u"samples_option_layout")
        self.sample_radiobutton = QRadioButton(self.time_card)
        self.buttonGroup_2.addButton(self.sample_radiobutton)
        self.sample_radiobutton.setObjectName(u"sample_radiobutton")

        self.samples_option_layout.addWidget(self.sample_radiobutton)

        self.samples_help_label = QLabel(self.time_card)
        self.samples_help_label.setObjectName(u"samples_help_label")
        self.samples_help_label.setFont(font2)
        self.samples_help_label.setWordWrap(True)
        self.samples_help_label.setIndent(26)
        self.samples_help_label.setProperty(u"variant", u"help")

        self.samples_option_layout.addWidget(self.samples_help_label)

        self.sample_rate_layout = QHBoxLayout()
        self.sample_rate_layout.setObjectName(u"sample_rate_layout")
        self.sample_rate_layout.setContentsMargins(26, 0, 0, 0)
        self.sample_rate_grid = QGridLayout()
        self.sample_rate_grid.setObjectName(u"sample_rate_grid")
        self.sample_rate_grid.setHorizontalSpacing(12)
        self.sample_rate_grid.setVerticalSpacing(10)
        self.label_6 = QLabel(self.time_card)
        self.label_6.setObjectName(u"label_6")

        self.sample_rate_grid.addWidget(self.label_6, 0, 0, 1, 1)

        self.sample_rate_lineedit = QLineEdit(self.time_card)
        self.sample_rate_lineedit.setObjectName(u"sample_rate_lineedit")
        self.sample_rate_lineedit.setEnabled(False)

        self.sample_rate_grid.addWidget(self.sample_rate_lineedit, 0, 1, 1, 1)

        self.sample_rate_unit_label = QLabel(self.time_card)
        self.sample_rate_unit_label.setObjectName(u"sample_rate_unit_label")
        self.sample_rate_unit_label.setProperty(u"variant", u"help")

        self.sample_rate_grid.addWidget(self.sample_rate_unit_label, 0, 2, 1, 1)

        self.sample_rate_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.sample_rate_grid.addItem(self.sample_rate_grid_spacer, 0, 3, 1, 1)


        self.sample_rate_layout.addLayout(self.sample_rate_grid)


        self.samples_option_layout.addLayout(self.sample_rate_layout)


        self.time_options_2_layout.addLayout(self.samples_option_layout)


        self.time_options.addLayout(self.time_options_2_layout)


        self.time_card_layout.addLayout(self.time_options)


        self.content_layout.addWidget(self.time_card)

        self.columns_card = QFrame(self.content_widget)
        self.columns_card.setObjectName(u"columns_card")
        self.columns_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.columns_card.setFrameShadow(QFrame.Shadow.Raised)
        self.columns_card_layout = QVBoxLayout(self.columns_card)
        self.columns_card_layout.setSpacing(10)
        self.columns_card_layout.setObjectName(u"columns_card_layout")
        self.columns_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_15 = QLabel(self.columns_card)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.columns_card_layout.addWidget(self.label_15)

        self.columns_help_label = QLabel(self.columns_card)
        self.columns_help_label.setObjectName(u"columns_help_label")
        self.columns_help_label.setWordWrap(True)
        self.columns_help_label.setProperty(u"variant", u"help")

        self.columns_card_layout.addWidget(self.columns_help_label)

        self.columns_grid = QGridLayout()
        self.columns_grid.setObjectName(u"columns_grid")
        self.columns_grid.setHorizontalSpacing(12)
        self.columns_grid.setVerticalSpacing(10)
        self.label_9 = QLabel(self.columns_card)
        self.label_9.setObjectName(u"label_9")

        self.columns_grid.addWidget(self.label_9, 0, 0, 1, 1)

        self.checkBox_group_enabled = QCheckBox(self.columns_card)
        self.checkBox_group_enabled.setObjectName(u"checkBox_group_enabled")
        self.checkBox_group_enabled.setChecked(True)

        self.columns_grid.addWidget(self.checkBox_group_enabled, 0, 1, 1, 1)

        self.group_spinbox = QSpinBox(self.columns_card)
        self.group_spinbox.setObjectName(u"group_spinbox")
        self.group_spinbox.setValue(1)

        self.columns_grid.addWidget(self.group_spinbox, 0, 2, 1, 1)

        self.checkBox_define_group = QCheckBox(self.columns_card)
        self.checkBox_define_group.setObjectName(u"checkBox_define_group")
        self.checkBox_define_group.setEnabled(False)

        self.columns_grid.addWidget(self.checkBox_define_group, 0, 3, 1, 1)

        self.group_lineEdit = QLineEdit(self.columns_card)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setEnabled(False)

        self.columns_grid.addWidget(self.group_lineEdit, 0, 4, 1, 1)

        self.label_2 = QLabel(self.columns_card)
        self.label_2.setObjectName(u"label_2")

        self.columns_grid.addWidget(self.label_2, 1, 0, 1, 1)

        self.event_name_spinbox = QSpinBox(self.columns_card)
        self.event_name_spinbox.setObjectName(u"event_name_spinbox")
        self.event_name_spinbox.setMinimum(0)
        self.event_name_spinbox.setValue(2)

        self.columns_grid.addWidget(self.event_name_spinbox, 1, 2, 1, 1)

        self.checkBox_define_name = QCheckBox(self.columns_card)
        self.checkBox_define_name.setObjectName(u"checkBox_define_name")
        self.checkBox_define_name.setEnabled(False)

        self.columns_grid.addWidget(self.checkBox_define_name, 1, 3, 1, 1)

        self.name_lineEdit = QLineEdit(self.columns_card)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setEnabled(False)

        self.columns_grid.addWidget(self.name_lineEdit, 1, 4, 1, 1)

        self.label_3 = QLabel(self.columns_card)
        self.label_3.setObjectName(u"label_3")

        self.columns_grid.addWidget(self.label_3, 2, 0, 1, 1)

        self.onset_spinbox = QSpinBox(self.columns_card)
        self.onset_spinbox.setObjectName(u"onset_spinbox")
        self.onset_spinbox.setMinimum(0)
        self.onset_spinbox.setValue(3)

        self.columns_grid.addWidget(self.onset_spinbox, 2, 2, 1, 1)

        self.center_checkBox = QCheckBox(self.columns_card)
        self.center_checkBox.setObjectName(u"center_checkBox")

        self.columns_grid.addWidget(self.center_checkBox, 2, 3, 1, 2)

        self.label_4 = QLabel(self.columns_card)
        self.label_4.setObjectName(u"label_4")

        self.columns_grid.addWidget(self.label_4, 3, 0, 1, 1)

        self.checkBox_dur_enabled = QCheckBox(self.columns_card)
        self.checkBox_dur_enabled.setObjectName(u"checkBox_dur_enabled")
        self.checkBox_dur_enabled.setChecked(True)

        self.columns_grid.addWidget(self.checkBox_dur_enabled, 3, 1, 1, 1)

        self.duration_spinbox = QSpinBox(self.columns_card)
        self.duration_spinbox.setObjectName(u"duration_spinbox")
        self.duration_spinbox.setMinimum(0)
        self.duration_spinbox.setValue(4)

        self.columns_grid.addWidget(self.duration_spinbox, 3, 2, 1, 1)

        self.checkBox_define_dur = QCheckBox(self.columns_card)
        self.checkBox_define_dur.setObjectName(u"checkBox_define_dur")
        self.checkBox_define_dur.setEnabled(False)

        self.columns_grid.addWidget(self.checkBox_define_dur, 3, 3, 1, 1)

        self.fixed_dur_lineEdit = QLineEdit(self.columns_card)
        self.fixed_dur_lineEdit.setObjectName(u"fixed_dur_lineEdit")
        self.fixed_dur_lineEdit.setEnabled(False)

        self.columns_grid.addWidget(self.fixed_dur_lineEdit, 3, 4, 1, 1)

        self.label_8 = QLabel(self.columns_card)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(90, 16777215))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.columns_grid.addWidget(self.label_8, 4, 0, 1, 1)

        self.checkBox_chan_enabled = QCheckBox(self.columns_card)
        self.checkBox_chan_enabled.setObjectName(u"checkBox_chan_enabled")
        self.checkBox_chan_enabled.setChecked(True)

        self.columns_grid.addWidget(self.checkBox_chan_enabled, 4, 1, 1, 1)

        self.channel_spinBox = QSpinBox(self.columns_card)
        self.channel_spinBox.setObjectName(u"channel_spinBox")
        self.channel_spinBox.setValue(5)

        self.columns_grid.addWidget(self.channel_spinBox, 4, 2, 1, 1)

        self.checkBox_define_chan = QCheckBox(self.columns_card)
        self.checkBox_define_chan.setObjectName(u"checkBox_define_chan")
        self.checkBox_define_chan.setEnabled(False)

        self.columns_grid.addWidget(self.checkBox_define_chan, 4, 3, 1, 1)

        self.fixed_chan_lineEdit = QLineEdit(self.columns_card)
        self.fixed_chan_lineEdit.setObjectName(u"fixed_chan_lineEdit")
        self.fixed_chan_lineEdit.setEnabled(False)

        self.columns_grid.addWidget(self.fixed_chan_lineEdit, 4, 4, 1, 1)

        self.columns_grid.setColumnStretch(4, 1)

        self.columns_card_layout.addLayout(self.columns_grid)

        self.columns_rules_label = QLabel(self.columns_card)
        self.columns_rules_label.setObjectName(u"columns_rules_label")
        self.columns_rules_label.setFont(font2)
        self.columns_rules_label.setTextFormat(Qt.TextFormat.RichText)
        self.columns_rules_label.setWordWrap(True)
        self.columns_rules_label.setProperty(u"variant", u"help")

        self.columns_card_layout.addWidget(self.columns_rules_label)


        self.content_layout.addWidget(self.columns_card)

        self.about_time_formats_layout = QVBoxLayout()
        self.about_time_formats_layout.setSpacing(6)
        self.about_time_formats_layout.setObjectName(u"about_time_formats_layout")
        self.about_time_formats_title_label = QLabel(self.content_widget)
        self.about_time_formats_title_label.setObjectName(u"about_time_formats_title_label")
        self.about_time_formats_title_label.setFont(font1)

        self.about_time_formats_layout.addWidget(self.about_time_formats_title_label)

        self.about_time_formats_label = QLabel(self.content_widget)
        self.about_time_formats_label.setObjectName(u"about_time_formats_label")
        self.about_time_formats_label.setTextFormat(Qt.TextFormat.RichText)
        self.about_time_formats_label.setWordWrap(True)
        self.about_time_formats_label.setOpenExternalLinks(True)
        self.about_time_formats_label.setProperty(u"variant", u"help")

        self.about_time_formats_layout.addWidget(self.about_time_formats_label)


        self.content_layout.addLayout(self.about_time_formats_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TextFileDefinition)
        self.channel_spinBox.valueChanged.connect(TextFileDefinition.on_chan_index_changed)
        self.checkBox_chan_enabled.clicked.connect(TextFileDefinition.chan_enabled_slot)
        self.sample_radiobutton.clicked.connect(TextFileDefinition.on_input_format_changed)
        self.checkBox_define_chan.clicked.connect(TextFileDefinition.on_event_pos_changed)
        self.duration_spinbox.valueChanged.connect(TextFileDefinition.on_duration_index_changed)
        self.checkBox_define_dur.clicked.connect(TextFileDefinition.on_event_pos_changed)
        self.event_name_spinbox.valueChanged.connect(TextFileDefinition.on_name_index_changed)
        self.checkBox_define_name.clicked.connect(TextFileDefinition.on_event_pos_changed)
        self.checkBox_group_enabled.clicked.connect(TextFileDefinition.group_enabled_slot)
        self.checkBox_define_group.clicked.connect(TextFileDefinition.on_event_pos_changed)
        self.checkBox_dur_enabled.clicked.connect(TextFileDefinition.dur_enabled_slot)
        self.group_spinbox.valueChanged.connect(TextFileDefinition.on_group_index_changed)
        self.time_radiobutton.clicked.connect(TextFileDefinition.on_input_format_changed)

        QMetaObject.connectSlotsByName(TextFileDefinition)
    # setupUi

    def retranslateUi(self, TextFileDefinition):
        TextFileDefinition.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("TextFileDefinition", u"Text File Format", None))
        self.subtitle_label.setText(QCoreApplication.translate("TextFileDefinition", u"Describe the format of the text file. The default values read a text file written like a Snooz accessory file (.tsv).", None))
        self.label_10.setText(QCoreApplication.translate("TextFileDefinition", u"Annotations reader", None))
        self.label_11.setText(QCoreApplication.translate("TextFileDefinition", u"Item separator", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("TextFileDefinition", u"<html><head/><body><p>For tabulation write \\t.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.delimiter_lineedit.setPlaceholderText(QCoreApplication.translate("TextFileDefinition", u"Insert delimiter(s)", None))
        self.label.setText(QCoreApplication.translate("TextFileDefinition", u"Rows to skip", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("TextFileDefinition", u"Blank rows are skipped automatically, so do not include them in the row count to skip. This feature is important to prevent issues with files that end with blank rows.", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("TextFileDefinition", u"File encoding", None))
        self.comboBox_encoding.setItemText(0, QCoreApplication.translate("TextFileDefinition", u"utf-8", None))
        self.comboBox_encoding.setItemText(1, QCoreApplication.translate("TextFileDefinition", u"latin-1", None))
        self.comboBox_encoding.setItemText(2, QCoreApplication.translate("TextFileDefinition", u"utf-16", None))
        self.comboBox_encoding.setItemText(3, QCoreApplication.translate("TextFileDefinition", u"utf-32", None))
        self.comboBox_encoding.setItemText(4, QCoreApplication.translate("TextFileDefinition", u"iso-8859", None))
        self.comboBox_encoding.setItemText(5, QCoreApplication.translate("TextFileDefinition", u"ascii", None))
        self.comboBox_encoding.setItemText(6, QCoreApplication.translate("TextFileDefinition", u"ansi", None))

        self.rows_help_label.setText(QCoreApplication.translate("TextFileDefinition", u"Rows reserved for the header. Do not include the blank rows nor the row with the column titles in the count.", None))
        self.label_5.setText(QCoreApplication.translate("TextFileDefinition", u"Onset and duration", None))
        self.time_help_label.setText(QCoreApplication.translate("TextFileDefinition", u"Choose how the text file writes the onset and the duration of the annotations, as times or as numbers of samples. The onset counts from the start of the recording. For example, an onset 5 minutes after the start is written 300 in seconds, 00:05:00 as a time or 76800 in samples at 256\u00a0Hz.", None))
        self.time_radiobutton.setText(QCoreApplication.translate("TextFileDefinition", u"Time", None))
        self.label_7.setText(QCoreApplication.translate("TextFileDefinition", u"The onset and the duration are in seconds or written as times. Leave a time format empty when its column is in seconds. Otherwise, write its format, for example <nobr>%H:%M:%S</nobr> for 00:05:00 (see \"About the time formats\").", None))
        self.label_12.setText(QCoreApplication.translate("TextFileDefinition", u"Onset time format", None))
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("TextFileDefinition", u"Let empty to define the time elapsed in seconds. Otherwise define the string format (see https://strftime.org/). ", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("TextFileDefinition", u"Duration time format", None))
        self.sample_radiobutton.setText(QCoreApplication.translate("TextFileDefinition", u"Samples", None))
        self.samples_help_label.setText(QCoreApplication.translate("TextFileDefinition", u"The onset and the duration are numbers of samples. Enter the sample rate at which they are counted, usually the sample rate of the recording. Snooz uses it to convert the samples to seconds. For example, 76800 samples at 256\u00a0Hz are 300\u00a0s.", None))
        self.label_6.setText(QCoreApplication.translate("TextFileDefinition", u"Sample rate", None))
        self.sample_rate_lineedit.setText(QCoreApplication.translate("TextFileDefinition", u"256", None))
        self.sample_rate_unit_label.setText(QCoreApplication.translate("TextFileDefinition", u"Hz", None))
        self.label_15.setText(QCoreApplication.translate("TextFileDefinition", u"Column index", None))
        self.columns_help_label.setText(QCoreApplication.translate("TextFileDefinition", u"For each Snooz column, enter the number of the column of the text file that holds it. 1 is the first column. If the text file does not have a column, set its number to 0 or uncheck its box.", None))
        self.label_9.setText(QCoreApplication.translate("TextFileDefinition", u"Group", None))
        self.checkBox_group_enabled.setText("")
#if QT_CONFIG(tooltip)
        self.checkBox_define_group.setToolTip(QCoreApplication.translate("TextFileDefinition", u"To define a default event group (when group index column is 0).", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_define_group.setText(QCoreApplication.translate("TextFileDefinition", u"Define a group", None))
        self.group_lineEdit.setPlaceholderText(QCoreApplication.translate("TextFileDefinition", u"Group of all the annotations", None))
        self.label_2.setText(QCoreApplication.translate("TextFileDefinition", u"Name", None))
#if QT_CONFIG(tooltip)
        self.checkBox_define_name.setToolTip(QCoreApplication.translate("TextFileDefinition", u"To define a default event name (when name index column is 0).", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_define_name.setText(QCoreApplication.translate("TextFileDefinition", u"Define a name", None))
        self.name_lineEdit.setPlaceholderText(QCoreApplication.translate("TextFileDefinition", u"Name of all the annotations", None))
        self.label_3.setText(QCoreApplication.translate("TextFileDefinition", u"Onset/Center", None))
#if QT_CONFIG(tooltip)
        self.center_checkBox.setToolTip(QCoreApplication.translate("TextFileDefinition", u"Check if the event is identified by its center instead of its onset.", None))
#endif // QT_CONFIG(tooltip)
        self.center_checkBox.setText(QCoreApplication.translate("TextFileDefinition", u"Event identified by its center", None))
        self.label_4.setText(QCoreApplication.translate("TextFileDefinition", u"Duration", None))
        self.checkBox_dur_enabled.setText("")
#if QT_CONFIG(tooltip)
        self.checkBox_define_dur.setToolTip(QCoreApplication.translate("TextFileDefinition", u"To define a duration for all the annotations.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_define_dur.setText(QCoreApplication.translate("TextFileDefinition", u"Define a duration   ", None))
        self.fixed_dur_lineEdit.setPlaceholderText(QCoreApplication.translate("TextFileDefinition", u"Duration of all the annotations", None))
        self.label_8.setText(QCoreApplication.translate("TextFileDefinition", u"Channels", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("TextFileDefinition", u"Mark 0 if events are not channel specific (as sleep stage).", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_chan_enabled.setText("")
        self.checkBox_define_chan.setText(QCoreApplication.translate("TextFileDefinition", u"Define a channel", None))
        self.fixed_chan_lineEdit.setPlaceholderText(QCoreApplication.translate("TextFileDefinition", u"Channel of all the annotations", None))
        self.columns_rules_label.setText(QCoreApplication.translate("TextFileDefinition", u"A column that the text file does not have gets one value for all the annotations.<br/>\u2022 To choose the value, check \"Define a group\", \"Define a name\" or \"Define a duration\", then write it in the field next to it. For example, write spindle as the group when the text file has only spindles.<br/>\u2022 A duration written there is in seconds, or in samples when the times are in samples.<br/>\u2022 Without a value, the group and the name are n/a, the duration is 0 and the annotations have no channel.", None))
        self.about_time_formats_title_label.setText(QCoreApplication.translate("TextFileDefinition", u"About the time formats", None))
        self.about_time_formats_label.setText(QCoreApplication.translate("TextFileDefinition", u"The time formats use the codes of Python (strftime), listed at <a href=\"https://strftime.org/\">https://strftime.org/</a>. The onset is a time elapsed from the start of the recording, not a clock time. Here are some examples.<br/>\u2022 <nobr>%H:%M:%S</nobr> matches 01:05:30.<br/>\u2022 <nobr>%H.%M.%S</nobr> matches 01.05.30.<br/>\u2022 <nobr>%M:%S</nobr> matches 05:30.<br/>\u2022 <nobr>%H:%M:%S.%f</nobr> matches 01:05:30.250.", None))
    # retranslateUi

