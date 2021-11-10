from PyQt5.uic import loadUi 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow, QStackedWidget,QWidget
import sys
import auth

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi('LoginScreen.ui', self)
        self.passwordFeild.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginButton.clicked.connect(self.login)

    def login(self):
        username = self.emailFeild.text()
        password = self.passwordFeild.text()
        det = auth.Auth.login(username, password)
        if det[0]==True:
            self._output = det[1]   #returns the NAME of the user
            # print(self._output)
            self.accept()
        else:
            print(det[1])
            self.reject()

    def getOutput(self):
        return self._output
