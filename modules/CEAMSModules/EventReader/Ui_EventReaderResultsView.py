# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\sampo\Python\PycharmProjects\scinode\scinodes_poc\src\main\python\plugins\EventReader\Ui_EventReaderResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_EventReaderResultsView(object):
    def setupUi(self, EventReaderResultsView):
        EventReaderResultsView.setObjectName("EventReaderResultsView")
        EventReaderResultsView.resize(483, 218)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EventReaderResultsView)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.result_tablewidget = QtWidgets.QTableWidget(EventReaderResultsView)
        self.result_tablewidget.setObjectName("result_tablewidget")
        self.result_tablewidget.setColumnCount(0)
        self.result_tablewidget.setRowCount(0)
        self.verticalLayout.addWidget(self.result_tablewidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(EventReaderResultsView)
        QtCore.QMetaObject.connectSlotsByName(EventReaderResultsView)

    def retranslateUi(self, EventReaderResultsView):
        _translate = QtCore.QCoreApplication.translate
        EventReaderResultsView.setWindowTitle(_translate("EventReaderResultsView", "Form"))
