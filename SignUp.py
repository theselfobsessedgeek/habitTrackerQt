from PyQt5.uic import loadUi 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow, QStackedWidget,QWidget
import sys
import auth
import LoginScreen as ls
# import main
class SignUp(QDialog):
    def __init__(self):
        super(SignUp, self).__init__()
        loadUi('SignUp.ui', self)
        self.passwordFeild.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cnf_passwordFeild.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signUpButton.clicked.connect(self.signUp)

    def signUp(self):
        if(auth.Auth.createAcc(self.emailFeild.text(),self.passwordFeild.text(),self.cnf_passwordFeild.text(),self.nameFeild.text())):
            self.error.setText("Account Created")
            self.update()
            self.accept()
        else:
            self.error.setText("Account Not Created")
            self.update()
        