from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog
from PyQt5 import uic

import random, sys, pyodbc


class Confirm_move(QDialog):
    def __init__(self):
       super().__init__()
       uic.loadUi("confirm_delete.ui", self)
       self.setWindowTitle("Confirm")

       # Кнопки
       self.buttonBox.clicked.connect(self.dialog)

    def dialog(self):
        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=KLABSQLW19S1,49172;Trusted_Connection=yes; user=22200322; Database=DB_for_python_lessons;'
        conn = pyodbc.connect(conn_str)

        try:
            # добавление данных в БД
            cursor = conn.cursor()
            cursor.execute("DELETE user_table WHERE COUNT(1)")
            conn.commit()
            Main_window.load_data(self)
                    # Уведомление и завершение работы окна Add_data_window
            QMessageBox.information(self, "Успех", "Данные успешно добавлены")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", "Не удалось выполнить запрос(")
            print(f"Запрос не удалось реализовать(. Ошибка: {e}")

    def dialog_no(self):
        pass


class Add_data_window(QMainWindow):
    def __init__(self):
       super().__init__()
       uic.loadUi("add_data_form.ui", self)
       self.setWindowTitle("Add data")
       self.model = QStandardItemModel(self)
       self.pushButton.clicked.connect(self.append_data)

    def append_data(self):
        username = self.lineEdit.text()
        nubmer = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        ID = random.randrange(1, 10000)
        role = "use"
        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=KLABSQLW19S1,49172;Trusted_Connection=yes; user=22200322; Database=DB_for_python_lessons;'
        conn = pyodbc.connect(conn_str)

        # добавление данных в БД
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_table (userID, username, user_number, role, password) VALUES (?, ?, ?, ?, ?)", (ID, username, nubmer, role, password, ))
        conn.commit()

        # Уведомление и завершение работы окна Add_data_window
        QMessageBox.information(self, "Успех", "Данные успешно добавлены")
        Main_window.load_data(self)
        Add_data_window.close(self)


class Edit_data_window(QMainWindow):
    def __init__(self):
       super().__init__()
       uic.loadUi("edit_data_form.ui", self)
       self.setWindowTitle("Edit data")
       self.model = QStandardItemModel(self)
       self.pushButton.clicked.connect(self.edit_data)

    def edit_data(self):
        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=KLABSQLW19S1,49172;Trusted_Connection=yes; user=22200322; Database=DB_for_python_lessons;'
        conn = pyodbc.connect(conn_str)
        ID = self.lineEdit.text()
        username = self.lineEdit_2.text()
        print(f"Имя пользователя: {username}, ID: {ID}")


        try:
            # добавление данных в БД
            cursor = conn.cursor()
            cursor.execute("UPDATE user_table SET username = ? WHERE userID = ?", (username, ID))
            conn.commit()
            QMessageBox.information(self, "Успех", "Данные обновлены")
            Main_window.load_data(self)
            Edit_data_window.close(self)
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", "Не удалось выполнить запрос(")
            print(f"Запрос не удалось реализовать(. Ошибка: {e}")


class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("data_form_server.ui", self)
        self.setWindowTitle("DataBase")
        self.model = QStandardItemModel(self)

        # Объявление таблицы
        self.tableView.setModel(self.model)
        self.model.setHorizontalHeaderLabels(['ID', 'Имя', 'Номер телефона', 'Роль', 'Пароль', 'Хеш пароля'])
        self.load_data()

        # Подключение кнопок
        self.add_data.clicked.connect(self.add_data_button)
        self.del_data.clicked.connect(self.del_data_button)
        self.edit_data.clicked.connect(self.edit_data_button)

    def load_data(self):
        # подключение к базе данных
        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=KLABSQLW19S1,49172;Trusted_Connection=yes; user=22200322; Database=DB_for_python_lessons;'
        conn = pyodbc.connect(conn_str)

        # вывод данных из БД
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_table")

        for row in cursor.fetchall():
            print(row)
            items = [QStandardItem(str(field)) for field in row]
            self.model.appendRow(items)
    
    def close_data(self):
        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=KLABSQLW19S1,49172;Trusted_Connection=yes; user=22200322; Database=DB_for_python_lessons;'
        conn = pyodbc.connect(conn_str)

        conn.close()

        if not conn.close():
            print("База данных активна")
        else:
            pyodbc.pooling = False
            print("База данных выключена")

    def add_data_button(self):
        self.add = Add_data_window()
        self.add.setFixedSize(406, 279)
        self.add.show()

    def del_data_button(self):
        self.dialog = Confirm_move()
        self.dialog.show()

    def edit_data_button(self):
        self.edit = Edit_data_window()
        self.edit.setFixedSize(406, 279)
        self.edit.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main_window()
    window.setFixedSize(784, 600)
    window.show()
    sys.exit(app.exec())

