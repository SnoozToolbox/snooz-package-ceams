# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SpectralSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_SpectralSettings(object):
    def setupUi(self, SpectralSettings):
        if not SpectralSettings.objectName():
            SpectralSettings.setObjectName(u"SpectralSettings")
        self.verticalLayout = QVBoxLayout(SpectralSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.method_label = QLabel(SpectralSettings)
        self.method_label.setObjectName(u"method_label")

        self.verticalLayout.addWidget(self.method_label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.first_freq_label = QLabel(SpectralSettings)
        self.first_freq_label.setObjectName(u"first_freq_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.first_freq_label)

        self.first_freq_lineEdit = QLineEdit(SpectralSettings)
        self.first_freq_lineEdit.setObjectName(u"first_freq_lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.first_freq_lineEdit)

        self.last_freq_label = QLabel(SpectralSettings)
        self.last_freq_label.setObjectName(u"last_freq_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.last_freq_label)

        self.last_freq_lineEdit = QLineEdit(SpectralSettings)
        self.last_freq_lineEdit.setObjectName(u"last_freq_lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.last_freq_lineEdit)

        self.win_len_label = QLabel(SpectralSettings)
        self.win_len_label.setObjectName(u"win_len_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.win_len_label)

        self.win_len_lineEdit = QLineEdit(SpectralSettings)
        self.win_len_lineEdit.setObjectName(u"win_len_lineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.win_len_lineEdit)

        self.win_step_label = QLabel(SpectralSettings)
        self.win_step_label.setObjectName(u"win_step_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.win_step_label)

        self.win_step_lineEdit = QLineEdit(SpectralSettings)
        self.win_step_lineEdit.setObjectName(u"win_step_lineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.win_step_lineEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

#if QT_CONFIG(shortcut)
        self.first_freq_label.setBuddy(self.first_freq_lineEdit)
        self.last_freq_label.setBuddy(self.last_freq_lineEdit)
        self.win_len_label.setBuddy(self.win_len_lineEdit)
        self.win_step_label.setBuddy(self.win_step_lineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(SpectralSettings)

        QMetaObject.connectSlotsByName(SpectralSettings)
    # setupUi

    def retranslateUi(self, SpectralSettings):
        self.method_label.setText(QCoreApplication.translate("SpectralSettings", u"Welch method \u00b7 Hann window \u00b7 1 Hz bands", None))
        self.first_freq_label.setText(QCoreApplication.translate("SpectralSettings", u"First frequency (Hz)", None))
        self.last_freq_label.setText(QCoreApplication.translate("SpectralSettings", u"Last frequency (Hz)", None))
        self.win_len_label.setText(QCoreApplication.translate("SpectralSettings", u"Window length (s)", None))
#if QT_CONFIG(tooltip)
        self.win_len_lineEdit.setToolTip(QCoreApplication.translate("SpectralSettings", u"Use whole seconds to align the FFT bins with the fixed 1 Hz bands.", None))
#endif // QT_CONFIG(tooltip)
        self.win_step_label.setText(QCoreApplication.translate("SpectralSettings", u"Window step (s)", None))
#if QT_CONFIG(tooltip)
        self.win_step_lineEdit.setToolTip(QCoreApplication.translate("SpectralSettings", u"Use a step shorter than the window length to overlap consecutive windows.", None))
#endif // QT_CONFIG(tooltip)
        pass
    # retranslateUi

