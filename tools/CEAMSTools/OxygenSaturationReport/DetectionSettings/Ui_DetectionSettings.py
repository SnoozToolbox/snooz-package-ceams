# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DetectionSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_DetectionSettings(object):
    def setupUi(self, DetectionSettings):
        if not DetectionSettings.objectName():
            DetectionSettings.setObjectName(u"DetectionSettings")
        DetectionSettings.resize(900, 700)
        self.verticalLayout = QVBoxLayout(DetectionSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(DetectionSettings)
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

        self.criteria_card = QFrame(self.content_widget)
        self.criteria_card.setObjectName(u"criteria_card")
        self.criteria_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.criteria_card.setFrameShadow(QFrame.Shadow.Raised)
        self.criteria_card_layout = QVBoxLayout(self.criteria_card)
        self.criteria_card_layout.setSpacing(10)
        self.criteria_card_layout.setObjectName(u"criteria_card_layout")
        self.criteria_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.criteria_card)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)

        self.criteria_card_layout.addWidget(self.label)

        self.criteria_grid = QGridLayout()
        self.criteria_grid.setObjectName(u"criteria_grid")
        self.criteria_grid.setHorizontalSpacing(24)
        self.criteria_grid.setVerticalSpacing(10)
        self.label_2 = QLabel(self.criteria_card)
        self.label_2.setObjectName(u"label_2")

        self.criteria_grid.addWidget(self.label_2, 0, 0, 1, 1)

        self.radioButton_3perc = QRadioButton(self.criteria_card)
        self.buttonGroup = QButtonGroup(DetectionSettings)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_3perc)
        self.radioButton_3perc.setObjectName(u"radioButton_3perc")
        self.radioButton_3perc.setChecked(True)

        self.criteria_grid.addWidget(self.radioButton_3perc, 0, 1, 1, 1)

        self.radioButton_4perc = QRadioButton(self.criteria_card)
        self.buttonGroup.addButton(self.radioButton_4perc)
        self.radioButton_4perc.setObjectName(u"radioButton_4perc")

        self.criteria_grid.addWidget(self.radioButton_4perc, 0, 2, 1, 1)

        self.label_17 = QLabel(self.criteria_card)
        self.label_17.setObjectName(u"label_17")

        self.criteria_grid.addWidget(self.label_17, 1, 0, 1, 1)

        self.radioButton_180s = QRadioButton(self.criteria_card)
        self.buttonGroup_2 = QButtonGroup(DetectionSettings)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_180s)
        self.radioButton_180s.setObjectName(u"radioButton_180s")
        self.radioButton_180s.setChecked(True)

        self.criteria_grid.addWidget(self.radioButton_180s, 1, 1, 1, 1)

        self.radioButton_20s = QRadioButton(self.criteria_card)
        self.buttonGroup_2.addButton(self.radioButton_20s)
        self.radioButton_20s.setObjectName(u"radioButton_20s")

        self.criteria_grid.addWidget(self.radioButton_20s, 1, 2, 1, 1)

        self.label_4 = QLabel(self.criteria_card)
        self.label_4.setObjectName(u"label_4")

        self.criteria_grid.addWidget(self.label_4, 2, 0, 1, 1)

        self.radioButton_hold_10s = QRadioButton(self.criteria_card)
        self.buttonGroup_3 = QButtonGroup(DetectionSettings)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton_hold_10s)
        self.radioButton_hold_10s.setObjectName(u"radioButton_hold_10s")
        self.radioButton_hold_10s.setChecked(True)

        self.criteria_grid.addWidget(self.radioButton_hold_10s, 2, 1, 1, 1)

        self.radioButton_hold_5s = QRadioButton(self.criteria_card)
        self.buttonGroup_3.addButton(self.radioButton_hold_5s)
        self.radioButton_hold_5s.setObjectName(u"radioButton_hold_5s")

        self.criteria_grid.addWidget(self.radioButton_hold_5s, 2, 2, 1, 1)

        self.criteria_grid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.criteria_grid.addItem(self.criteria_grid_spacer, 0, 3, 1, 1)


        self.criteria_card_layout.addLayout(self.criteria_grid)

        self.label_7 = QLabel(self.criteria_card)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_7.setFont(font2)
        self.label_7.setWordWrap(True)
        self.label_7.setProperty(u"variant", u"help")

        self.criteria_card_layout.addWidget(self.label_7)


        self.content_layout.addWidget(self.criteria_card)

        self.about_detection_layout = QVBoxLayout()
        self.about_detection_layout.setSpacing(6)
        self.about_detection_layout.setObjectName(u"about_detection_layout")
        self.about_detection_title_label = QLabel(self.content_widget)
        self.about_detection_title_label.setObjectName(u"about_detection_title_label")
        self.about_detection_title_label.setFont(font1)

        self.about_detection_layout.addWidget(self.about_detection_title_label)

        self.label_3 = QLabel(self.content_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)
        self.label_3.setProperty(u"variant", u"help")

        self.about_detection_layout.addWidget(self.label_3)

        self.picture_card = QFrame(self.content_widget)
        self.picture_card.setObjectName(u"picture_card")
        self.picture_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.picture_card.setFrameShadow(QFrame.Shadow.Raised)
        self.picture_card_layout = QVBoxLayout(self.picture_card)
        self.picture_card_layout.setSpacing(10)
        self.picture_card_layout.setObjectName(u"picture_card_layout")
        self.picture_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_pic = QLabel(self.picture_card)
        self.label_pic.setObjectName(u"label_pic")

        self.picture_card_layout.addWidget(self.label_pic)

        self.picture_caption_label = QLabel(self.picture_card)
        self.picture_caption_label.setObjectName(u"picture_caption_label")
        self.picture_caption_label.setFont(font2)
        self.picture_caption_label.setWordWrap(True)
        self.picture_caption_label.setProperty(u"variant", u"help")

        self.picture_card_layout.addWidget(self.picture_caption_label)


        self.about_detection_layout.addWidget(self.picture_card)

        self.label_10 = QLabel(self.content_widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setTextFormat(Qt.TextFormat.RichText)
        self.label_10.setWordWrap(True)
        self.label_10.setProperty(u"variant", u"help")

        self.about_detection_layout.addWidget(self.label_10)

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


        self.about_detection_layout.addLayout(self.references_layout)


        self.content_layout.addLayout(self.about_detection_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(DetectionSettings)

        QMetaObject.connectSlotsByName(DetectionSettings)
    # setupUi

    def retranslateUi(self, DetectionSettings):
        DetectionSettings.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("DetectionSettings", u"Detection Settings", None))
        self.subtitle_label.setText(QCoreApplication.translate("DetectionSettings", u"Define the criteria for detecting an oxygen desaturation.", None))
        self.label.setText(QCoreApplication.translate("DetectionSettings", u"Desaturation criteria", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("DetectionSettings", u"The minimum drop of the oxygen saturation.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("DetectionSettings", u"Oxygen level drop", None))
        self.radioButton_3perc.setText(QCoreApplication.translate("DetectionSettings", u"3%", None))
        self.radioButton_4perc.setText(QCoreApplication.translate("DetectionSettings", u"4%", None))
#if QT_CONFIG(tooltip)
        self.label_17.setToolTip(QCoreApplication.translate("DetectionSettings", u"The maximum duration during which the oxygen level is dropping.", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("DetectionSettings", u"Maximum desaturation duration", None))
        self.radioButton_180s.setText(QCoreApplication.translate("DetectionSettings", u"180 s [1]", None))
        self.radioButton_20s.setText(QCoreApplication.translate("DetectionSettings", u"20 s [CEAMS]", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("DetectionSettings", u"The minimum duration during which the oxygen level drop is maintained.", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("DetectionSettings", u"Minimum desaturation duration", None))
        self.radioButton_hold_10s.setText(QCoreApplication.translate("DetectionSettings", u"10 s [1]", None))
        self.radioButton_hold_5s.setText(QCoreApplication.translate("DetectionSettings", u"5 s [1, CEAMS]", None))
        self.label_7.setText(QCoreApplication.translate("DetectionSettings", u"In brackets, where the value comes from: ABOSA [1] or the CEAMS. The oximeter signal is analyzed during the sleep period, from sleep onset to the final awakening.", None))
        self.about_detection_title_label.setText(QCoreApplication.translate("DetectionSettings", u"About the detection", None))
        self.label_3.setText(QCoreApplication.translate("DetectionSettings", u"The oximeter measures the percentage of oxygen in the blood. A desaturation is a drop of the oxygen level (%) during a time (s), as shown here; the recovery that follows it is detected with fixed criteria, inspired by ABOSA [1].", None))
        self.label_pic.setText("")
        self.picture_caption_label.setText(QCoreApplication.translate("DetectionSettings", u"Simulated oxygen saturation: a desaturation, from its maximum to its minimum, with its drop and its duration, then its recovery.", None))
        self.label_10.setText(QCoreApplication.translate("DetectionSettings", u"<b>Recovery criteria</b> (fixed)<br/>\u2022 minimum duration: 3 s<br/>\u2022 maximum duration: the longer of 120 s and twice the desaturation before the recovery<br/>\u2022 minimum amplitude: 2%<br/>\u2022 minimum slope: 0.05 %/s", None))
        self.references_label.setText(QCoreApplication.translate("DetectionSettings", u"[1] Karhu, T., Lepp\u00e4nen, T., T\u00f6yr\u00e4s, J., Oksenberg, A., Myllymaa, S., &amp; Nikkonen, S. (2022). ABOSA \u2013 Freely available automatic blood oxygen saturation signal analysis software: Structure and validation. <i>Computer Methods and Programs in Biomedicine</i>, <i>226</i>, Article 107120. <a href=\"https://doi.org/10.1016/j.cmpb.2022.107120\">https://doi.org/10.1016/j.cmpb.2022.107120</a>", None))
    # retranslateUi

