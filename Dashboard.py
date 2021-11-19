from os import times
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi 
from PyQt5.QtWidgets import QDialog
from TaskWidget import Task
import matplotlib.pyplot as plt
import time
from plyer import notification




class Dashboard(QDialog):
    def __init__(self,name,uid):
        super(Dashboard, self).__init__()
        loadUi('dashboard.ui', self)
        self.uid = uid
        self.setWindowTitle('Dashboard')
        self.welcome.setText('Welcome '+ name)
        self.addTaskBtn.clicked.connect(self.addTask)
        self.people = Task.pull(self.uid)
        self.plotbtn.clicked.connect(self.plotGraph)
        self.refresh()

    def refresh(self):
        self.people = Task.pull(self.uid)
        row=0
        self.tableWidget.setRowCount(len(self.people))
        for person in self.people:
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person['task_name']))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person['description']))
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person['time']))
            row=row+1
        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        # self.plotGraph()
        

    def addTask(self):
        self.peoplepeople = Task.push(self.task_name.text(),self.task_description.toPlainText(),self.checkBox.isChecked(),self.uid)
        row=0
        self.tableWidget.setRowCount(len(self.people))
        # for person in self.people:
        #     self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person['task_name']))
        #     self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person['description']))
        #     self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person['time']))
        #     row=row+1
        self.refresh()
        # self.plotGraph()

    def plotGraph(self):
        productivity_score = 0
        X = []
        Y = []
        for person in self.people:
            if person['productive']:
                productivity_score = productivity_score + 1
            else:
                productivity_score = productivity_score - 1
            X.append(person['time'])
            Y.append(productivity_score)
          
        fig = plt.figure(figsize = (10, 5))

        plt.bar(X,Y , color ='maroon',
                width = 0.4)

        plt.xlabel("Time")
        plt.ylabel("Productivity score")
        plt.title("Your Progress")
        plt.show()            

                

    