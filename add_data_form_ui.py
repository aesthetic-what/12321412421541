# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\\edu.local\public\studenthomes\22200322\Desktop\sql_server\add_data_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(406, 279)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 200, 191, 71))
        self.pushButton.setStyleSheet("QPushButton:hover {\n"
"    background-color: #ffdbcc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fcb9aa;\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(57, 208, 208);\n"
"    border-radius: 31px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 20, 301, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 80, 301, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 140, 301, 51))
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Регистрация"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите имя пользователя"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Введите номер телефона"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
