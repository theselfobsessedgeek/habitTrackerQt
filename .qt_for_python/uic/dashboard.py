# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/shubhamahlawat/Course Work/oopsProject/dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(806, 640)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setEnabled(True)
        self.bgwidget.setGeometry(QtCore.QRect(-40, -21, 881, 671))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.983, stop:0 rgba(86, 153, 255, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.bgwidget.setObjectName("bgwidget")
        self.error = QtWidgets.QLabel(self.bgwidget)
        self.error.setGeometry(QtCore.QRect(360, 560, 161, 20))
        self.error.setStyleSheet("color:rgb(255, 0, 0)")
        self.error.setText("")
        self.error.setObjectName("error")
        self.taskScrollArea = QtWidgets.QScrollArea(self.bgwidget)
        self.taskScrollArea.setGeometry(QtCore.QRect(50, 280, 781, 351))
        self.taskScrollArea.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border-style:outset;\n"
"border-width: 1px;\n"
"border-color:white;")
        self.taskScrollArea.setWidgetResizable(True)
        self.taskScrollArea.setObjectName("taskScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 349))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.taskScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.ATwidget = QtWidgets.QWidget(self.bgwidget)
        self.ATwidget.setGeometry(QtCore.QRect(50, 110, 781, 161))
        self.ATwidget.setStyleSheet("QWidget#ATwidget{\n"
"background-color: rgba(0,0,0,0);\n"
"border-style:outset;\n"
"border-width: 1px;\n"
"border-color:white;\n"
"}")
        self.ATwidget.setObjectName("ATwidget")
        self.label = QtWidgets.QLabel(self.ATwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 21))
        self.label.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.ATwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 31, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.ATwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 40, 191, 21))
        self.lineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border-style:outset;\n"
"border-width: 1px;\n"
"border-color:white;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.ATwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.ATwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 70, 681, 41))
        self.textEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border-style:outset;\n"
"border-width: 1px;\n"
"border-color:white;")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.ATwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 120, 171, 31))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.welcome = QtWidgets.QLabel(self.bgwidget)
        self.welcome.setGeometry(QtCore.QRect(630, 30, 151, 41))
        self.welcome.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.welcome.setObjectName("welcome")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Add Task"))
        self.label_2.setText(_translate("Dialog", "Title"))
        self.label_3.setText(_translate("Dialog", "Desciption"))
        self.pushButton.setText(_translate("Dialog", "Add Task"))
        self.welcome.setText(_translate("Dialog", "Welcome Human"))
