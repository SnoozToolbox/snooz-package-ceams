# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AlgorithmDetail.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_AlgorithmDetail(object):
    def setupUi(self, AlgorithmDetail):
        if not AlgorithmDetail.objectName():
            AlgorithmDetail.setObjectName(u"AlgorithmDetail")
        AlgorithmDetail.resize(900, 700)
        self.verticalLayout = QVBoxLayout(AlgorithmDetail)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.content_row = QHBoxLayout()
        self.content_row.setObjectName(u"content_row")
        self.content_row.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(AlgorithmDetail)
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

        self.picture_card = QFrame(self.content_widget)
        self.picture_card.setObjectName(u"picture_card")
        self.picture_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.picture_card.setFrameShadow(QFrame.Shadow.Raised)
        self.picture_card_layout = QVBoxLayout(self.picture_card)
        self.picture_card_layout.setSpacing(10)
        self.picture_card_layout.setObjectName(u"picture_card_layout")
        self.picture_card_layout.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.picture_card)
        self.label_2.setObjectName(u"label_2")

        self.picture_card_layout.addWidget(self.label_2)

        self.picture_caption_label = QLabel(self.picture_card)
        self.picture_caption_label.setObjectName(u"picture_caption_label")
        font1 = QFont()
        font1.setPointSize(10)
        self.picture_caption_label.setFont(font1)
        self.picture_caption_label.setWordWrap(True)
        self.picture_caption_label.setProperty(u"variant", u"help")

        self.picture_card_layout.addWidget(self.picture_caption_label)


        self.content_layout.addWidget(self.picture_card)

        self.artefacts_info = QFrame(self.content_widget)
        self.artefacts_info.setObjectName(u"artefacts_info")
        self.artefacts_info.setFrameShape(QFrame.Shape.NoFrame)
        self.artefacts_info.setProperty(u"variant", u"info")
        self.artefacts_info_layout = QHBoxLayout(self.artefacts_info)
        self.artefacts_info_layout.setObjectName(u"artefacts_info_layout")
        self.artefacts_info_layout.setContentsMargins(14, 10, 14, 10)
        self.artefacts_info_label = QLabel(self.artefacts_info)
        self.artefacts_info_label.setObjectName(u"artefacts_info_label")
        self.artefacts_info_label.setTextFormat(Qt.TextFormat.RichText)
        self.artefacts_info_label.setWordWrap(True)

        self.artefacts_info_layout.addWidget(self.artefacts_info_label)


        self.content_layout.addWidget(self.artefacts_info)

        self.about_detector_layout = QVBoxLayout()
        self.about_detector_layout.setSpacing(6)
        self.about_detector_layout.setObjectName(u"about_detector_layout")
        self.label = QLabel(self.content_widget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setBold(True)
        self.label.setFont(font2)

        self.about_detector_layout.addWidget(self.label)

        self.textEdit = QLabel(self.content_widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setTextFormat(Qt.TextFormat.RichText)
        self.textEdit.setWordWrap(True)
        self.textEdit.setProperty(u"variant", u"help")

        self.about_detector_layout.addWidget(self.textEdit)

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
        self.references_label.setFont(font1)
        self.references_label.setTextFormat(Qt.TextFormat.RichText)
        self.references_label.setWordWrap(True)
        self.references_label.setOpenExternalLinks(True)
        self.references_label.setProperty(u"variant", u"help")

        self.references_layout.addWidget(self.references_label)


        self.about_detector_layout.addLayout(self.references_layout)


        self.content_layout.addLayout(self.about_detector_layout)


        self.content_row.addWidget(self.content_widget)

        self.content_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.content_row.addItem(self.content_spacer)

        self.content_row.setStretch(0, 1)

        self.verticalLayout.addLayout(self.content_row)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(AlgorithmDetail)

        QMetaObject.connectSlotsByName(AlgorithmDetail)
    # setupUi

    def retranslateUi(self, AlgorithmDetail):
        AlgorithmDetail.setWindowTitle("")
        self.title_label.setText(QCoreApplication.translate("AlgorithmDetail", u"Algorithm's Details", None))
        self.subtitle_label.setText(QCoreApplication.translate("AlgorithmDetail", u"How YASA detects the rapid eye movements.", None))
        self.picture_caption_label.setText(QCoreApplication.translate("AlgorithmDetail", u"Simulated EOG of REM sleep: each rapid eye movement (REM) deflects the left and right EOG channels (LOC and ROC) in opposite directions.", None))
        self.artefacts_info_label.setText(QCoreApplication.translate("AlgorithmDetail", u"<b>For the best results</b><br/>Apply this detection only to artefact-free REM sleep data.", None))
        self.label.setText(QCoreApplication.translate("AlgorithmDetail", u"About the YASA REM detector", None))
        self.textEdit.setText(QCoreApplication.translate("AlgorithmDetail", u"The detector of YASA [1] builds on the methods proposed by Yetton et al. [2] and Agarwal et al. [3], mainly on the approach of Agarwal et al.: an amplitude threshold applied to the negative product of the filtered LOC and ROC signals. With this technique, it finds the peaks of the signal and computes, for each REM, its duration, the absolute values of LOC and ROC at its peak, and the absolute rise and fall slopes of both signals.<br/><br/>With <b>Remove outliers</b> (Detector Step), the outliers are detected with an Isolation Forest (scikit-learn) and removed from the detected REMs. This step is applied only when at least 50 REMs are detected.<br/><br/>All the characteristics are computed on the LOC and ROC signals filtered in the REM frequency band of <b>Detector Step</b>.", None))
        self.references_label.setText(QCoreApplication.translate("AlgorithmDetail", u"[1] Vallat, R., &amp; Walker, M. P. (2021). An open-source, high-performance tool for automated sleep staging. <i>eLife</i>, <i>10</i>, Article e70092. <a href=\"https://doi.org/10.7554/eLife.70092\">https://doi.org/10.7554/eLife.70092</a><br/>[2] Yetton, B. D., Niknazar, M., Duggan, K. A., McDevitt, E. A., Whitehurst, L. N., Sattari, N., &amp; Mednick, S. C. (2016). Automatic detection of rapid eye movements (REMs): A machine learning approach. <i>Journal of Neuroscience Methods</i>, <i>259</i>, 72\u201382. <a href=\"https://doi.org/10.1016/j.jneumeth.2015.11.015\">https://doi.org/10.1016/j.jneumeth.2015.11.015</a><br/>[3] Agarwal, R., Takeuchi, T., Laroche, S., &amp; Gotman, J. (2005). Detection of rapid-eye movements in sleep studies. <i>IEEE Transactions on Biomedical Engineering</i>, <i>52</i>(8), 1390\u20131396. <a href=\"https://doi.org/10.1109/TBME.2005.851512\">https://doi.org/10.1109/TBME.2005.851512</a>", None))
    # retranslateUi

