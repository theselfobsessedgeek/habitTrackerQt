from PyQt5 import QtWidgets
from PyQt5.uic import loadUi 
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow, QStackedWidget,QWidget
import sys
import auth

class Dashboard(QDialog):
    def __init__(self,name):
        super(Dashboard, self).__init__()
        loadUi('dashboard.ui', self)

        self.setWindowTitle('Dashboard')
        self.welcome.setText('Welcome '+ name)