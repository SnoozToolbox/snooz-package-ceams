# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\klacourse\Documents\NGosselin\gitRepos\ceamscarms\Stand_alone_apps\snooz-toolbox\src\main\python\plugins\AmplitudeDetector\Ui_AmplitudeDetectorResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_SlowWaveDetectorResultsView(object):
    def setupUi(self, AmplitudeDetectorResultsView):
        AmplitudeDetectorResultsView.setObjectName("AmplitudeDetectorResultsView")
        AmplitudeDetectorResultsView.resize(677, 303)
        self.verticalLayout = QtWidgets.QVBoxLayout(AmplitudeDetectorResultsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.result_layout = QtWidgets.QVBoxLayout()
        self.result_layout.setObjectName("result_layout")
        self.verticalLayout.addLayout(self.result_layout)

        self.retranslateUi(AmplitudeDetectorResultsView)
        QtCore.QMetaObject.connectSlotsByName(AmplitudeDetectorResultsView)

    def retranslateUi(self, AmplitudeDetectorResultsView):
        _translate = QtCore.QCoreApplication.translate
        AmplitudeDetectorResultsView.setWindowTitle(_translate("AmplitudeDetectorResultsView", "Form"))
