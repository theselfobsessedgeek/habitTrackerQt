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
            self._output1 = det[1]  #returns the NAME of the user 
            self._output2 = det[2]    #returns the UID of the user
            self.accept()
        else:
            self.error.setText('Invalid email or password')

    def getOutput1(self):
        return self._output1
    def getOutput2(self):
        return self._output2
