# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detail_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
import requests
import printPage

class Ui_MainWindow(object):
    def open_window(self, form_data):
        self.window = QtWidgets.QMainWindow()
        self.ui = printPage.Window(form_data)

    def setupUi(self, MainWindow, id):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        base_url = "https://reqres.in/api/users?page=2"
        payload = {"id": id}
        request = requests.get(base_url, params=payload)
        data = request.json()
        print(data)
        avatar = data["data"]["avatar"]
        image = QImage()
        image.loadFromData(requests.get(avatar).content)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(969, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 815, 502))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_7)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(data["data"]["email"])
        self.lineEdit.setReadOnly(True)
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText(data["data"]["email"])
        self.lineEdit_2.setReadOnly(True)
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_9)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText(data["data"]["email"])
        self.lineEdit_3.setReadOnly(True)
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame_10)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setReadOnly(True)
        self.horizontalLayout_6.addWidget(self.lineEdit_4)
        self.verticalLayout_3.addWidget(self.frame_10)
        
        self.frame_11 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_11)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setReadOnly(True)
        self.horizontalLayout_7.addWidget(self.lineEdit_5)
        self.verticalLayout_3.addWidget(self.frame_11)

        self.frame_12 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_12)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_12)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setReadOnly(True)
        self.horizontalLayout_8.addWidget(self.lineEdit_6)
        self.verticalLayout_3.addWidget(self.frame_12)

        self.frame_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.frame_13)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_13)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setReadOnly(True)
        self.horizontalLayout_9.addWidget(self.lineEdit_7)
        self.verticalLayout_3.addWidget(self.frame_13)

        self.frame_14 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.frame_14)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_14)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setReadOnly(True)
        self.horizontalLayout_10.addWidget(self.lineEdit_8)
        self.verticalLayout_3.addWidget(self.frame_14)

        self.frame_15 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.frame_15)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_15)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setReadOnly(True)
        self.horizontalLayout_11.addWidget(self.lineEdit_9)
        self.verticalLayout_3.addWidget(self.frame_15)

        self.frame_16 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(self.frame_16)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_16)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setReadOnly(True)
        self.horizontalLayout_12.addWidget(self.lineEdit_10)
        self.verticalLayout_3.addWidget(self.frame_16)

        self.frame_18 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_11 = QtWidgets.QLabel(self.frame_18)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_14.addWidget(self.label_11)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_18)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.setReadOnly(True)
        self.horizontalLayout_14.addWidget(self.lineEdit_11)
        self.verticalLayout_3.addWidget(self.frame_18)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.scrollArea)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_6.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.edit_button)

        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_5, clicked = lambda: self.open_window(form_data))
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_17 = QtWidgets.QFrame(self.frame)
        self.frame_17.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.frame_17.hide()
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.cancel_button)

        self.horizontalLayout_13.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.confirm_button(form_data))
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        
        self.horizontalLayout_13.addWidget(self.pushButton_5)
        self.verticalLayout_6.addWidget(self.frame_17)
    
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.image_label = QtWidgets.QLabel(self.frame_4)
        self.image_label.setGeometry(QtCore.QRect(0, 0, 381, 381))
        self.image_label.setObjectName("image_1")
        self.image_label.setPixmap(QPixmap(image).scaled(QtCore.QSize(1000, 250)))
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_5.addWidget(self.image_label)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        form_data = {
                        'plate_number': "xxx",
                        'road': "xxx",
                        'speed': 0,
                        'hour': 0,
                        'minute': 0,
                        'type': "xxx",
                        'name': "xxx",
                        'gender': "xxx",
                        'birth_year': 0,
                        'birth_month': 0,
                        'birth_day': 0,
                        'nationality': "xxx",
                        'cmnd_id': 0,
                        'comment': "xxx",
                    }
        self.data_fields(form_data)

        print(form_data)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Bien so"))
        self.label_2.setText(_translate("MainWindow", "Tuyen duong"))
        self.label_3.setText(_translate("MainWindow", "Toc do"))
        self.label_4.setText(_translate("MainWindow", "Thoi gian vi pham"))
        self.label_5.setText(_translate("MainWindow", "Loai phuong tien"))
        self.label_6.setText(_translate("MainWindow", "Ho va ten nguoi vi pham"))
        self.label_7.setText(_translate("MainWindow", "Gioi tinh nguoi vi pham"))
        self.label_8.setText(_translate("MainWindow", "Ngay thang nam sinh"))
        self.label_9.setText(_translate("MainWindow", "Quoc tich"))
        self.label_10.setText(_translate("MainWindow", "So CMND"))
        self.label_11.setText(_translate("MainWindow", "Y kien cua nguoi vi pham"))
        self.pushButton.setText(_translate("MainWindow", "Quay lai"))
        self.pushButton_2.setText(_translate("MainWindow", "Chinh sua"))
        self.pushButton_3.setText(_translate("MainWindow", "Xuat PDF"))
        self.pushButton_4.setText(_translate("MainWindow", "Quay lai"))
        self.pushButton_5.setText(_translate("MainWindow", "Xac nhan"))

    def edit_button(self, MainWindow):
        self.frame_5.hide()
        self.frame_17.show()
        self.lineEdit.setReadOnly(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_6.setReadOnly(False)
        self.lineEdit_7.setReadOnly(False)
        self.lineEdit_8.setReadOnly(False)
        self.lineEdit_9.setReadOnly(False)
        self.lineEdit_10.setReadOnly(False)
        self.lineEdit_11.setReadOnly(False)
        
    def cancel_button(self, MainWindow):
        self.frame_17.hide()
        self.frame_5.show()
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_11.setReadOnly(True)

    def confirm_button(self, form_data):
        self.frame_17.hide()
        self.frame_5.show()
        self.data_fields(form_data)
        print(form_data)
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_11.setReadOnly(True)

    def data_fields(self, form_data):
        form_data['plate_number'] = self.lineEdit.text()
        form_data['road'] = self.lineEdit_2.text()
        form_data['speed'] = self.lineEdit_3.text()
        form_data['hour'] = self.lineEdit_4.text()
        form_data['type'] = self.lineEdit_5.text()
        form_data['name'] = self.lineEdit_6.text()
        form_data['gender'] = self.lineEdit_7.text()
        form_data['birth_year'] = self.lineEdit_8.text()
        form_data['nationality'] = self.lineEdit_9.text()
        form_data['cmnd_id'] = self.lineEdit_10.text()
        form_data['comment'] = self.lineEdit_11.text()
    
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, id)
    MainWindow.show()
    sys.exit(app.exec_())