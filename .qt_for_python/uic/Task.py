# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/shubhamahlawat/Course Work/oopsProject/Task.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fo(object):
    def setupUi(self, fo):
        fo.setObjectName("fo")
        fo.setWindowModality(QtCore.Qt.WindowModal)
        fo.resize(777, 124)
        fo.setWindowTitle("")
        fo.setWindowOpacity(1.0)
        fo.setToolTipDuration(-5)
        fo.setAutoFillBackground(True)
        fo.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border-style:outset;\n"
"border-width: 1px;\n"
"border-color:white;")
        self.stackedWidget = QtWidgets.QStackedWidget(fo)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 761, 101))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.task = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.task.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.task.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.task.setObjectName("task")
        self.desc = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.desc.setGeometry(QtCore.QRect(10, 40, 741, 51))
        self.desc.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.desc.setAutoFillBackground(False)
        self.desc.setObjectName("desc")
        self.stackedWidget.addWidget(self.stackedWidgetPage1)

        self.retranslateUi(fo)
        QtCore.QMetaObject.connectSlotsByName(fo)

    def retranslateUi(self, fo):
        _translate = QtCore.QCoreApplication.translate
        self.task.setText(_translate("fo", "Title"))
        self.desc.setText(_translate("fo", "Description"))
