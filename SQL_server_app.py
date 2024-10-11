from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtSql import QSqlTableModel
from PyQt5 import uic

import pyodbc
import sys


class Add_data_window(QMainWindow):
    def __init__(self):
       super().__init__()
       uic.loadUi(r"design\add_data_form.ui", self)
       self.setWindowTitle("Add data")
       self.model = QStandardItemModel(self)
       self.pushButton.clicked.connect(self.load_data)

    def load_data(self):
        username = self.lineEdit.text()
        nubmer = self.lineEdit_2.text()
        role = "user"

        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=KLABSQLW19S1,49172;Trusted_Connection=yes; user=22200322; Database=DB_for_python_lessons;'
        conn = pyodbc.connect(conn_str)

        # вывод данных из БД
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO users_table (username, user_number, role) VALUES (?, ?, ?)""", (username, nubmer, role))


class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"design\data_form_server.ui", self)
        self.setWindowTitle("DataBase")
        self.model = QStandardItemModel(self)

        # Объявление таблицы
        self.tableView.setModel(self.model)
        self.load_data()

        self.model.setHorizontalHeaderLabels(['ID', 'Имя', 'Номер телефона', 'Роль', 'Пароль', 'Хеш пароля'])

        # Подключение кнопок
        self.add_data.clicked.connect(self.add_data_button)
        # self.del_data.clicked.connect(self.del_data_button)
        # self.edit_data.clicked.connect(self.edit_data_button)

    def load_data(self):
        # подключение к базе данных
        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=KLABSQLW19S1,49172;Trusted_Connection=yes; user=22200322; Database=DB_for_python_lessons;'
        conn = pyodbc.connect(conn_str)

        # вывод данных из БД
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM user_table""")

        for row in cursor.fetchall():
            print(row)
            items = [QStandardItem(str(field)) for field in row]
            self.model.appendRow(items)

    def add_data_button(self):
        self.add = Add_data_window()
        self.add.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec())

