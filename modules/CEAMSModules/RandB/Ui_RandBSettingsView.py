# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_RandBSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_RandBSettingsView(object):
    def setupUi(self, RandBSettingsView):
        if not RandBSettingsView.objectName():
            RandBSettingsView.setObjectName(u"RandBSettingsView")
        RandBSettingsView.resize(704, 328)
        self.verticalLayout = QVBoxLayout(RandBSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signals_horizontalLayout = QHBoxLayout()
        self.signals_horizontalLayout.setObjectName(u"signals_horizontalLayout")

        self.verticalLayout.addLayout(self.signals_horizontalLayout)

        self.win_len_sec_horizontalLayout = QHBoxLayout()
        self.win_len_sec_horizontalLayout.setObjectName(u"win_len_sec_horizontalLayout")
        self.win_len_sec_label = QLabel(RandBSettingsView)
        self.win_len_sec_label.setObjectName(u"win_len_sec_label")

        self.win_len_sec_horizontalLayout.addWidget(self.win_len_sec_label)

        self.win_len_sec_lineedit = QLineEdit(RandBSettingsView)
        self.win_len_sec_lineedit.setObjectName(u"win_len_sec_lineedit")

        self.win_len_sec_horizontalLayout.addWidget(self.win_len_sec_lineedit)


        self.verticalLayout.addLayout(self.win_len_sec_horizontalLayout)

        self.win_step_sec_horizontalLayout = QHBoxLayout()
        self.win_step_sec_horizontalLayout.setObjectName(u"win_step_sec_horizontalLayout")
        self.win_step_sec_label = QLabel(RandBSettingsView)
        self.win_step_sec_label.setObjectName(u"win_step_sec_label")

        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_label)

        self.win_step_sec_lineedit = QLineEdit(RandBSettingsView)
        self.win_step_sec_lineedit.setObjectName(u"win_step_sec_lineedit")

        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_lineedit)


        self.verticalLayout.addLayout(self.win_step_sec_horizontalLayout)

        self.window_name_horizontalLayout = QHBoxLayout()
        self.window_name_horizontalLayout.setObjectName(u"window_name_horizontalLayout")
        self.window_name_label = QLabel(RandBSettingsView)
        self.window_name_label.setObjectName(u"window_name_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.window_name_label.sizePolicy().hasHeightForWidth())
        self.window_name_label.setSizePolicy(sizePolicy)

        self.window_name_horizontalLayout.addWidget(self.window_name_label)

        self.window_name_comboBox = QComboBox(RandBSettingsView)
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.setObjectName(u"window_name_comboBox")

        self.window_name_horizontalLayout.addWidget(self.window_name_comboBox)


        self.verticalLayout.addLayout(self.window_name_horizontalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.first_freq_label = QLabel(RandBSettingsView)
        self.first_freq_label.setObjectName(u"first_freq_label")

        self.horizontalLayout.addWidget(self.first_freq_label)

        self.first_freq_lineedit = QLineEdit(RandBSettingsView)
        self.first_freq_lineedit.setObjectName(u"first_freq_lineedit")

        self.horizontalLayout.addWidget(self.first_freq_lineedit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.last_freq_label = QLabel(RandBSettingsView)
        self.last_freq_label.setObjectName(u"last_freq_label")

        self.horizontalLayout_2.addWidget(self.last_freq_label)

        self.last_freq_lineedit = QLineEdit(RandBSettingsView)
        self.last_freq_lineedit.setObjectName(u"last_freq_lineedit")

        self.horizontalLayout_2.addWidget(self.last_freq_lineedit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.flag_label = QLabel(RandBSettingsView)
        self.flag_label.setObjectName(u"flag_label")

        self.horizontalLayout_3.addWidget(self.flag_label)

        self.flag_lineedit = QLineEdit(RandBSettingsView)
        self.flag_lineedit.setObjectName(u"flag_lineedit")

        self.horizontalLayout_3.addWidget(self.flag_lineedit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(RandBSettingsView)

        QMetaObject.connectSlotsByName(RandBSettingsView)
    # setupUi

    def retranslateUi(self, RandBSettingsView):
        RandBSettingsView.setWindowTitle(QCoreApplication.translate("RandBSettingsView", u"Form", None))
        self.win_len_sec_label.setText(QCoreApplication.translate("RandBSettingsView", u"win_len_sec", None))
        self.win_step_sec_label.setText(QCoreApplication.translate("RandBSettingsView", u"win_step_sec", None))
        self.window_name_label.setText(QCoreApplication.translate("RandBSettingsView", u"window_name", None))
        self.window_name_comboBox.setItemText(0, QCoreApplication.translate("RandBSettingsView", u"boxcar", None))
        self.window_name_comboBox.setItemText(1, QCoreApplication.translate("RandBSettingsView", u"trlang", None))
        self.window_name_comboBox.setItemText(2, QCoreApplication.translate("RandBSettingsView", u"blackman", None))
        self.window_name_comboBox.setItemText(3, QCoreApplication.translate("RandBSettingsView", u"hamming", None))
        self.window_name_comboBox.setItemText(4, QCoreApplication.translate("RandBSettingsView", u"hann", None))
        self.window_name_comboBox.setItemText(5, QCoreApplication.translate("RandBSettingsView", u"bartlett", None))
        self.window_name_comboBox.setItemText(6, QCoreApplication.translate("RandBSettingsView", u"flattop", None))
        self.window_name_comboBox.setItemText(7, QCoreApplication.translate("RandBSettingsView", u"parzen", None))
        self.window_name_comboBox.setItemText(8, QCoreApplication.translate("RandBSettingsView", u"bohman", None))
        self.window_name_comboBox.setItemText(9, QCoreApplication.translate("RandBSettingsView", u"blackmanharris", None))
        self.window_name_comboBox.setItemText(10, QCoreApplication.translate("RandBSettingsView", u"nuttall", None))
        self.window_name_comboBox.setItemText(11, QCoreApplication.translate("RandBSettingsView", u"barthann", None))
        self.window_name_comboBox.setItemText(12, QCoreApplication.translate("RandBSettingsView", u"kaiser", None))
        self.window_name_comboBox.setItemText(13, QCoreApplication.translate("RandBSettingsView", u"gaussian", None))
        self.window_name_comboBox.setItemText(14, QCoreApplication.translate("RandBSettingsView", u"general_gaussian", None))
        self.window_name_comboBox.setItemText(15, QCoreApplication.translate("RandBSettingsView", u"dpss", None))
        self.window_name_comboBox.setItemText(16, QCoreApplication.translate("RandBSettingsView", u"chebwin", None))
        self.window_name_comboBox.setItemText(17, QCoreApplication.translate("RandBSettingsView", u"exponential", None))
        self.window_name_comboBox.setItemText(18, QCoreApplication.translate("RandBSettingsView", u"tukey", None))
        self.window_name_comboBox.setItemText(19, QCoreApplication.translate("RandBSettingsView", u"taylor", None))

        self.window_name_comboBox.setCurrentText(QCoreApplication.translate("RandBSettingsView", u"boxcar", None))
        self.first_freq_label.setText(QCoreApplication.translate("RandBSettingsView", u"first_freq", None))
        self.last_freq_label.setText(QCoreApplication.translate("RandBSettingsView", u"last_freq", None))
        self.flag_label.setText(QCoreApplication.translate("RandBSettingsView", u"flag", None))
    # retranslateUi

