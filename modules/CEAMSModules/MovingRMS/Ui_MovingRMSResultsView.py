# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\klacourse\Documents\NGosselin\gitRepos\ceamscarms\Stand_alone_apps\scinodes_poc\src\main\python\plugins\MovingRMS\Ui_MovingRMSResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_MovingRMSResultsView(object):
    def setupUi(self, MovingRMSResultsView):
        MovingRMSResultsView.setObjectName("MovingRMSResultsView")
        MovingRMSResultsView.resize(483, 360)
        self.verticalLayout = QtWidgets.QVBoxLayout(MovingRMSResultsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.result_layout = QtWidgets.QVBoxLayout()
        self.result_layout.setObjectName("result_layout")
        self.verticalLayout.addLayout(self.result_layout)

        self.retranslateUi(MovingRMSResultsView)
        QtCore.QMetaObject.connectSlotsByName(MovingRMSResultsView)

    def retranslateUi(self, MovingRMSResultsView):
        _translate = QtCore.QCoreApplication.translate
        MovingRMSResultsView.setWindowTitle(_translate("MovingRMSResultsView", "Form"))