# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MartinSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_MartinSettings(object):
    def setupUi(self, MartinSettings):
        if not MartinSettings.objectName():
            MartinSettings.setObjectName(u"MartinSettings")
        MartinSettings.resize(900, 700)
        self.verticalLayout = QVBoxLayout(MartinSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(MartinSettings)
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

        self.settings_cards_layout = QHBoxLayout()
        self.settings_cards_layout.setSpacing(16)
        self.settings_cards_layout.setObjectName(u"settings_cards_layout")
        self.events_card = QFrame(self.content_widget)
        self.events_card.setObjectName(u"events_card")
        self.events_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.events_card.setFrameShadow(QFrame.Shadow.Raised)
        self.events_card_layout = QVBoxLayout(self.events_card)
        self.events_card_layout.setSpacing(10)
        self.events_card_layout.setObjectName(u"events_card_layout")
        self.events_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.events_card)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)

        self.events_card_layout.addWidget(self.label)

        self.events_grid = QGridLayout()
        self.events_grid.setObjectName(u"events_grid")
        self.events_grid.setHorizontalSpacing(12)
        self.events_grid.setVerticalSpacing(10)
        self.label_2 = QLabel(self.events_card)
        self.label_2.setObjectName(u"label_2")

        self.events_grid.addWidget(self.label_2, 0, 0, 1, 1)

        self.group_lineEdit = QLineEdit(self.events_card)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setMinimumSize(QSize(120, 0))
        self.group_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.events_grid.addWidget(self.group_lineEdit, 0, 1, 1, 1)

        self.label_3 = QLabel(self.events_card)
        self.label_3.setObjectName(u"label_3")

        self.events_grid.addWidget(self.label_3, 1, 0, 1, 1)

        self.name_lineEdit = QLineEdit(self.events_card)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(120, 0))
        self.name_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.events_grid.addWidget(self.name_lineEdit, 1, 1, 1, 1)

        self.events_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.events_grid.addItem(self.events_grid_spacer, 0, 3, 1, 1)


        self.events_card_layout.addLayout(self.events_grid)

        self.events_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.events_card_layout.addItem(self.events_stretch)


        self.settings_cards_layout.addWidget(self.events_card)

        self.threshold_card = QFrame(self.content_widget)
        self.threshold_card.setObjectName(u"threshold_card")
        self.threshold_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.threshold_card.setFrameShadow(QFrame.Shadow.Raised)
        self.threshold_card_layout = QVBoxLayout(self.threshold_card)
        self.threshold_card_layout.setSpacing(10)
        self.threshold_card_layout.setObjectName(u"threshold_card_layout")
        self.threshold_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_5 = QLabel(self.threshold_card)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.threshold_card_layout.addWidget(self.label_5)

        self.threshold_grid = QGridLayout()
        self.threshold_grid.setObjectName(u"threshold_grid")
        self.threshold_grid.setHorizontalSpacing(12)
        self.threshold_grid.setVerticalSpacing(10)
        self.label_4 = QLabel(self.threshold_card)
        self.label_4.setObjectName(u"label_4")

        self.threshold_grid.addWidget(self.label_4, 0, 0, 1, 1)

        self.threshold_lineEdit = QLineEdit(self.threshold_card)
        self.threshold_lineEdit.setObjectName(u"threshold_lineEdit")
        self.threshold_lineEdit.setMinimumSize(QSize(120, 0))
        self.threshold_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.threshold_grid.addWidget(self.threshold_lineEdit, 0, 1, 1, 1)

        self.threshold_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.threshold_grid.addItem(self.threshold_grid_spacer, 0, 3, 1, 1)


        self.threshold_card_layout.addLayout(self.threshold_grid)

        self.threshold_help_label = QLabel(self.threshold_card)
        self.threshold_help_label.setObjectName(u"threshold_help_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.threshold_help_label.setFont(font2)
        self.threshold_help_label.setWordWrap(True)
        self.threshold_help_label.setProperty(u"variant", u"help")

        self.threshold_card_layout.addWidget(self.threshold_help_label)

        self.threshold_options_layout = QVBoxLayout()
        self.threshold_options_layout.setSpacing(8)
        self.threshold_options_layout.setObjectName(u"threshold_options_layout")
        self.threshold_options_layout_1_layout = QVBoxLayout()
        self.threshold_options_layout_1_layout.setSpacing(2)
        self.threshold_options_layout_1_layout.setObjectName(u"threshold_options_layout_1_layout")
        self.threshold_cycle_checkBox = QCheckBox(self.threshold_card)
        self.threshold_cycle_checkBox.setObjectName(u"threshold_cycle_checkBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threshold_cycle_checkBox.sizePolicy().hasHeightForWidth())
        self.threshold_cycle_checkBox.setSizePolicy(sizePolicy)
        self.threshold_cycle_checkBox.setMaximumSize(QSize(16777215, 16777215))

        self.threshold_options_layout_1_layout.addWidget(self.threshold_cycle_checkBox)

        self.threshold_cycle_help_label = QLabel(self.threshold_card)
        self.threshold_cycle_help_label.setObjectName(u"threshold_cycle_help_label")
        self.threshold_cycle_help_label.setFont(font2)
        self.threshold_cycle_help_label.setWordWrap(True)
        self.threshold_cycle_help_label.setIndent(26)
        self.threshold_cycle_help_label.setProperty(u"variant", u"help")

        self.threshold_options_layout_1_layout.addWidget(self.threshold_cycle_help_label)


        self.threshold_options_layout.addLayout(self.threshold_options_layout_1_layout)

        self.threshold_options_layout_line_1 = QFrame(self.threshold_card)
        self.threshold_options_layout_line_1.setObjectName(u"threshold_options_layout_line_1")
        self.threshold_options_layout_line_1.setFrameShape(QFrame.Shape.HLine)
        self.threshold_options_layout_line_1.setFrameShadow(QFrame.Shadow.Plain)

        self.threshold_options_layout.addWidget(self.threshold_options_layout_line_1)

        self.threshold_options_layout_2_layout = QVBoxLayout()
        self.threshold_options_layout_2_layout.setSpacing(2)
        self.threshold_options_layout_2_layout.setObjectName(u"threshold_options_layout_2_layout")
        self.precise_checkBox = QCheckBox(self.threshold_card)
        self.precise_checkBox.setObjectName(u"precise_checkBox")

        self.threshold_options_layout_2_layout.addWidget(self.precise_checkBox)


        self.threshold_options_layout.addLayout(self.threshold_options_layout_2_layout)


        self.threshold_card_layout.addLayout(self.threshold_options_layout)

        self.threshold_stretch = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.threshold_card_layout.addItem(self.threshold_stretch)


        self.settings_cards_layout.addWidget(self.threshold_card)

        self.settings_cards_layout.setStretch(0, 1)
        self.settings_cards_layout.setStretch(1, 1)

        self.content_layout.addLayout(self.settings_cards_layout)

        self.about_martin_layout = QVBoxLayout()
        self.about_martin_layout.setSpacing(6)
        self.about_martin_layout.setObjectName(u"about_martin_layout")
        self.label_6 = QLabel(self.content_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.about_martin_layout.addWidget(self.label_6)

        self.textEdit = QLabel(self.content_widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setWordWrap(True)
        self.textEdit.setProperty(u"variant", u"help")

        self.about_martin_layout.addWidget(self.textEdit)

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


        self.about_martin_layout.addLayout(self.references_layout)


        self.content_layout.addLayout(self.about_martin_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(MartinSettings)
        self.threshold_cycle_checkBox.stateChanged.connect(MartinSettings.thresh_per_cycle_slot)

        QMetaObject.connectSlotsByName(MartinSettings)
    # setupUi

    def retranslateUi(self, MartinSettings):
        MartinSettings.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("MartinSettings", u"Martin", None))
        self.subtitle_label.setText(QCoreApplication.translate("MartinSettings", u"The spindle events created and the threshold of the Martin detector, based on the RMS of the EEG in the sigma band.", None))
        self.label.setText(QCoreApplication.translate("MartinSettings", u"Spindle events", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MartinSettings", u"Define in which group the spindles will be added.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MartinSettings", u"Group", None))
        self.group_lineEdit.setText(QCoreApplication.translate("MartinSettings", u"spindle", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MartinSettings", u"Define the name of the spindle events.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MartinSettings", u"Name", None))
        self.name_lineEdit.setText(QCoreApplication.translate("MartinSettings", u"a4", None))
        self.label_5.setText(QCoreApplication.translate("MartinSettings", u"Threshold", None))
        self.label_4.setText(QCoreApplication.translate("MartinSettings", u"Percentile", None))
        self.threshold_lineEdit.setText(QCoreApplication.translate("MartinSettings", u"95", None))
        self.threshold_help_label.setText(QCoreApplication.translate("MartinSettings", u"A spindle is detected when the RMS exceeds this percentile of the RMS values (default: 95).", None))
        self.threshold_cycle_checkBox.setText(QCoreApplication.translate("MartinSettings", u"Compute the threshold for each sleep cycle", None))
        self.threshold_cycle_help_label.setText(QCoreApplication.translate("MartinSettings", u"Turns on the detection in the sleep cycles only (Detection Settings). Otherwise, one threshold per channel for the whole recording.", None))
#if QT_CONFIG(tooltip)
        self.precise_checkBox.setToolTip(QCoreApplication.translate("MartinSettings", u"The RMS is computed on a sliding window (at each sample) before the onset and after the end of each event to refine its onset and duration. A detected event keeps its length or becomes longer, never shorter.", None))
#endif // QT_CONFIG(tooltip)
        self.precise_checkBox.setText(QCoreApplication.translate("MartinSettings", u"Refine the onset and duration of the detected events", None))
        self.label_6.setText(QCoreApplication.translate("MartinSettings", u"About the Martin detector", None))
        self.textEdit.setText(QCoreApplication.translate("MartinSettings", u"Also named a4. Martin band-pass filters the EEG in the sigma band (11.1\u201314.9 Hz), computes the root mean square (RMS) on sliding windows (0.25 s long with a 0.25 s step), and then applies a threshold (95th percentile by default) [1].", None))
        self.references_label.setText(QCoreApplication.translate("MartinSettings", u"[1] Martin, N., Lafortune, M., Godbout, J., Barakat, M., Robillard, R., Poirier, G., Bastien, C., &amp; Carrier, J. (2013). Topography of age-related changes in sleep spindles. <i>Neurobiology of Aging</i>, <i>34</i>(2), 468\u2013476. <a href=\"https://doi.org/10.1016/j.neurobiolaging.2012.05.020\">https://doi.org/10.1016/j.neurobiolaging.2012.05.020</a>", None))
    # retranslateUi

