# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\\edu.local\public\studenthomes\22200322\Desktop\sql_server\data_form_server.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 460, 761, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_data = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_data.sizePolicy().hasHeightForWidth())
        self.add_data.setSizePolicy(sizePolicy)
        self.add_data.setStyleSheet("QPushButton:hover {\n"
"    background-color: #ffdbcc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fcb9aa;\n"
"}\n"
"QPushButton {\n"
"    ;\n"
"    background-color: rgb(49, 223, 211);\n"
"    border-radius: 31px;\n"
"}")
        self.add_data.setObjectName("add_data")
        self.horizontalLayout.addWidget(self.add_data)
        self.del_data = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_data.sizePolicy().hasHeightForWidth())
        self.del_data.setSizePolicy(sizePolicy)
        self.del_data.setStyleSheet("QPushButton:hover {\n"
"    background-color: #ffdbcc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fcb9aa;\n"
"}\n"
"QPushButton {\n"
"    ;\n"
"    background-color: rgb(49, 223, 211);\n"
"    border-radius: 31px;\n"
"}")
        self.del_data.setObjectName("del_data")
        self.horizontalLayout.addWidget(self.del_data)
        self.edit_data = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_data.sizePolicy().hasHeightForWidth())
        self.edit_data.setSizePolicy(sizePolicy)
        self.edit_data.setStyleSheet("QPushButton:hover {\n"
"    background-color: #ffdbcc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fcb9aa;\n"
"}\n"
"QPushButton {\n"
"    ;\n"
"    background-color: rgb(49, 223, 211);\n"
"    border-radius: 31px;\n"
"}")
        self.edit_data.setObjectName("edit_data")
        self.horizontalLayout.addWidget(self.edit_data)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 761, 441))
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_data.setText(_translate("MainWindow", "Добавить"))
        self.del_data.setText(_translate("MainWindow", "Удалить"))
        self.edit_data.setText(_translate("MainWindow", "Редактировать"))
