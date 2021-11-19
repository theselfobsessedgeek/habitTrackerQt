from PyQt5.uic import loadUi 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow, QStackedWidget,QWidget
import sys

from Dashboard import Dashboard
from LoginScreen import LoginScreen
from SignUp import SignUp

class WelcomScreen(QDialog):
    def __init__(self):
        super(WelcomScreen,self).__init__()
        loadUi('SignInWindow.ui',self)
        self.login.clicked.connect(self.login_clicked)
        self.signUp.clicked.connect(self.signup_clicked)

    def login_clicked(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

        if login.exec_()==QDialog.Accepted:
            dash = Dashboard(login.getOutput1(),login.getOutput2())
            widget.addWidget(dash)
            widget.setCurrentIndex(widget.currentIndex()+1)

    def signup_clicked(self):
        signup = SignUp()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)
        if signup.exec_() == QDialog.Accepted:
            self.login_clicked()
        

app = QApplication(sys.argv)
widget = QStackedWidget()
widget.addWidget(WelcomScreen())
widget.setFixedHeight(631)
widget.setFixedWidth(811)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("EXITed")
    