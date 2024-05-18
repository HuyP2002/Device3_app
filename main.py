from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import welcomePage, homepage

ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def homeUi():
    global ui
    ui = welcomePage.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(home)
    MainWindow.show()

def home():
    global ui
    ui = homepage.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

homeUi()
sys.exit(app.exec())