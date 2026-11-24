# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EDFAnnotationsReaderSettingsView.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_EDFAnnotationsReaderSettingsView(object):
    def setupUi(self, EDFAnnotationsReaderSettingsView):
        if not EDFAnnotationsReaderSettingsView.objectName():
            EDFAnnotationsReaderSettingsView.setObjectName(u"EDFAnnotationsReaderSettingsView")
        EDFAnnotationsReaderSettingsView.resize(900, 700)
        self.verticalLayout = QVBoxLayout(EDFAnnotationsReaderSettingsView)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(19, 12, 19, 12)
        self.files_cards_layout = QHBoxLayout()
        self.files_cards_layout.setSpacing(16)
        self.files_cards_layout.setObjectName(u"files_cards_layout")
        self.annot_files_card = QFrame(EDFAnnotationsReaderSettingsView)
        self.annot_files_card.setObjectName(u"annot_files_card")
        self.annot_files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.annot_files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.annot_files_card_layout = QVBoxLayout(self.annot_files_card)
        self.annot_files_card_layout.setSpacing(10)
        self.annot_files_card_layout.setObjectName(u"annot_files_card_layout")
        self.annot_files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.annot_files_title_label = QLabel(self.annot_files_card)
        self.annot_files_title_label.setObjectName(u"annot_files_title_label")
        font = QFont()
        font.setBold(True)
        self.annot_files_title_label.setFont(font)

        self.annot_files_card_layout.addWidget(self.annot_files_title_label)

        self.tableWidget_files = QTableWidget(self.annot_files_card)
        self.tableWidget_files.setObjectName(u"tableWidget_files")
        self.tableWidget_files.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_files.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_files.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_files.setAutoScroll(True)
        self.tableWidget_files.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_files.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_files.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_files.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_files.setWordWrap(True)

        self.annot_files_card_layout.addWidget(self.tableWidget_files)

        self.annot_files_buttons_layout = QHBoxLayout()
        self.annot_files_buttons_layout.setSpacing(8)
        self.annot_files_buttons_layout.setObjectName(u"annot_files_buttons_layout")
        self.annot_files_buttons_layout_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.annot_files_buttons_layout.addItem(self.annot_files_buttons_layout_spacer)

        self.pushButton_choose = QPushButton(self.annot_files_card)
        self.pushButton_choose.setObjectName(u"pushButton_choose")

        self.annot_files_buttons_layout.addWidget(self.pushButton_choose)

        self.annot_files_buttons_layout.setStretch(0, 1)

        self.annot_files_card_layout.addLayout(self.annot_files_buttons_layout)


        self.files_cards_layout.addWidget(self.annot_files_card)

        self.psg_files_card = QFrame(EDFAnnotationsReaderSettingsView)
        self.psg_files_card.setObjectName(u"psg_files_card")
        self.psg_files_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.psg_files_card.setFrameShadow(QFrame.Shadow.Raised)
        self.psg_files_card_layout = QVBoxLayout(self.psg_files_card)
        self.psg_files_card_layout.setSpacing(10)
        self.psg_files_card_layout.setObjectName(u"psg_files_card_layout")
        self.psg_files_card_layout.setContentsMargins(10, 10, 10, 10)
        self.psg_files_title_label = QLabel(self.psg_files_card)
        self.psg_files_title_label.setObjectName(u"psg_files_title_label")
        self.psg_files_title_label.setFont(font)

        self.psg_files_card_layout.addWidget(self.psg_files_title_label)

        self.tableWidget_psg_files = QTableWidget(self.psg_files_card)
        self.tableWidget_psg_files.setObjectName(u"tableWidget_psg_files")
        self.tableWidget_psg_files.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.psg_files_card_layout.addWidget(self.tableWidget_psg_files)

        self.psg_files_buttons_layout = QHBoxLayout()
        self.psg_files_buttons_layout.setSpacing(8)
        self.psg_files_buttons_layout.setObjectName(u"psg_files_buttons_layout")
        self.psg_files_buttons_layout_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.psg_files_buttons_layout.addItem(self.psg_files_buttons_layout_spacer)

        self.pushButton_choose_psg = QPushButton(self.psg_files_card)
        self.pushButton_choose_psg.setObjectName(u"pushButton_choose_psg")

        self.psg_files_buttons_layout.addWidget(self.pushButton_choose_psg)

        self.psg_files_buttons_layout.setStretch(0, 1)

        self.psg_files_card_layout.addLayout(self.psg_files_buttons_layout)


        self.files_cards_layout.addWidget(self.psg_files_card)

        self.files_cards_layout.setStretch(0, 1)
        self.files_cards_layout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.files_cards_layout)

        self.clear_layout = QHBoxLayout()
        self.clear_layout.setSpacing(8)
        self.clear_layout.setObjectName(u"clear_layout")
        self.order_help_label = QLabel(EDFAnnotationsReaderSettingsView)
        self.order_help_label.setObjectName(u"order_help_label")
        font1 = QFont()
        font1.setPointSize(10)
        self.order_help_label.setFont(font1)
        self.order_help_label.setWordWrap(True)
        self.order_help_label.setProperty(u"variant", u"help")

        self.clear_layout.addWidget(self.order_help_label)

        self.pushButton_clear = QPushButton(EDFAnnotationsReaderSettingsView)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.clear_layout.addWidget(self.pushButton_clear)

        self.clear_layout.setStretch(0, 1)

        self.verticalLayout.addLayout(self.clear_layout)


        self.retranslateUi(EDFAnnotationsReaderSettingsView)
        self.pushButton_choose.clicked.connect(EDFAnnotationsReaderSettingsView.choose_slot)
        self.pushButton_clear.clicked.connect(EDFAnnotationsReaderSettingsView.clear_slot)
        self.pushButton_choose_psg.clicked.connect(EDFAnnotationsReaderSettingsView.choose_psg_slot)

        QMetaObject.connectSlotsByName(EDFAnnotationsReaderSettingsView)
    # setupUi

    def retranslateUi(self, EDFAnnotationsReaderSettingsView):
        EDFAnnotationsReaderSettingsView.setWindowTitle("")
#if QT_CONFIG(tooltip)
        self.annot_files_title_label.setToolTip(QCoreApplication.translate("EDFAnnotationsReaderSettingsView", u"The EDF+ files with the annotations to import (EDF Annotations signal).", None))
#endif // QT_CONFIG(tooltip)
        self.annot_files_title_label.setText(QCoreApplication.translate("EDFAnnotationsReaderSettingsView", u"Annotation files", None))
        self.pushButton_choose.setText(QCoreApplication.translate("EDFAnnotationsReaderSettingsView", u"Choose files", None))
#if QT_CONFIG(tooltip)
        self.psg_files_title_label.setToolTip(QCoreApplication.translate("EDFAnnotationsReaderSettingsView", u"The PSG signal file (EDF or EDF+) of each annotation file, in the same order. It gives the start time of the recording; the annotations are added to its accessory file (.tsv).", None))
#endif // QT_CONFIG(tooltip)
        self.psg_files_title_label.setText(QCoreApplication.translate("EDFAnnotationsReaderSettingsView", u"PSG files", None))
        self.pushButton_choose_psg.setText(QCoreApplication.translate("EDFAnnotationsReaderSettingsView", u"Choose files", None))
        self.order_help_label.setText(QCoreApplication.translate("EDFAnnotationsReaderSettingsView", u"Add one PSG file per annotation file, in the same order.", None))
        self.pushButton_clear.setText(QCoreApplication.translate("EDFAnnotationsReaderSettingsView", u"Clear all", None))
    # retranslateUi

