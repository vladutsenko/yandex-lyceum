# -*- coding: UTF-8 -*-

import sqlite3
import sys
import subprocess

from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow
from PyQt5 import QtCore
from ent import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.eyes.stateChanged.connect(
            lambda state=self.eyes.isChecked(): self.see(state))

        self.con = sqlite3.connect("network.db")
        cur = self.con.cursor()
        # снимаем выбор пользователя с предыдущих включений программы
        cur.execute("UPDATE Users SET active = False")

        # вход как гость
        self.guest.clicked.connect(self.write_g)
        self.sign_in.clicked.connect(self.write_in)
        self.sign_up.clicked.connect(self.write_up)

    def write_g(self):  # вход как гость
        cur = self.con.cursor()
        id = self.id_guest.text()
        if id == "":
            self.error_guest.setText("Введите id пользователя")
        else:
            result = cur.execute(
                "SELECT * FROM Users WHERE id_who=?", (int(id), )).fetchall()
            if not result:
                self.error_guest.setText("Неверный id пользователя")
            else:
                cur.execute(
                    "UPDATE Users SET active = 'True' WHERE id_who = ?", (int(id),))
                self.run_back()

    def write_in(self):  # вход пользователя
        cur = self.con.cursor()
        login = self.login.text()
        password = self.parol.text()
        result = cur.execute(
            "SELECT * FROM Users WHERE login = ?", (login, )).fetchall()
        if not result:
            self.error_sign.setText(
                "Неверный логин или он ещё не зарегестрирован")
        else:
            result = cur.execute(
                "SELECT password FROM Users WHERE login = ?", (login, )).fetchall()[0]
            if result[0] != password:
                self.error_sign.setText("Неверный логин или пароль")
            else:
                cur.execute(
                    "UPDATE Users SET active = 'True' WHERE login = ?", (login,))
                self.run_in()

    def write_up(self):  # регистрация пользователя
        cur = self.con.cursor()
        login = self.login.text()
        password = self.parol.text()
        result = cur.execute(
            "SELECT * FROM Users WHERE login = ?", (login, )).fetchall()
        if result:
            self.error_sign.setText(
                "Пользователь уже зарегистрирован")
        elif login == "" or password == "":
            self.error_sign.setText("Неверный логин или пароль")
        else:
            cur.execute("INSERT INTO Users(login, password, gender, active, name, surname, status, date, sity) VALUES(?,?,?,?,' ',' ',' ',' ',' ')",
                        (login, password, "Мужской", "True"))
            self.run_up()

    def see(self, state):  # Показ пароля
        if state == QtCore.Qt.Checked:
            self.parol.setEchoMode(QLineEdit.Normal)
            self.eyes.setText("👀")
        else:
            self.parol.setEchoMode(QLineEdit.Password)
            self.eyes.setText("🙈")

    def run_back(self, exit_code=0):
        self.con.commit()
        self.con.close()
        subprocess.Popen(['python', '!str.py'])
        sys.exit(exit_code)

    def run_in(self, exit_code=0):
        self.con.commit()
        self.con.close()
        subprocess.Popen(['python', '!str+.py'])
        sys.exit(exit_code)

    def run_up(self, exit_code=0):
        self.con.commit()
        self.con.close()
        subprocess.Popen(['python', '!edit.py'])
        sys.exit(exit_code)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
