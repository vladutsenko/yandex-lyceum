# -*- coding: UTF-8 -*-

import sys
import os
import sqlite3
import subprocess

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore
from str1 import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("network.db")
        self.back.clicked.connect(self.run_back)
        self.pushButton.clicked.connect(self.run_edit)
        self.publish.clicked.connect(self.run_publish)
        cur = self.con.cursor()

        # фото
        if cur.execute("SELECT photo_active FROM Users WHERE active = 'True'").fetchone()[0] == "True":
            data = cur.execute(
                """SELECT photo FROM Users WHERE active = 'True'""").fetchone()[0]
            open('photo.jpg', 'wb').write(data)
            self.photo.setPixmap(QPixmap('photo.jpg').scaled(
                251, 451, QtCore.Qt.KeepAspectRatio))
            os.remove("photo.jpg")

        # имя
        na = cur.execute(
            """SELECT name FROM Users WHERE active = 'True'""").fetchone()
        su = cur.execute(
            """SELECT surname FROM Users WHERE active = 'True'""").fetchone()
        h = na[0] + " " + su[0]
        self.name.setText(h)

        # статус
        self.status.setText(cur.execute(
            """SELECT status FROM Users WHERE active = 'True'""").fetchone()[0])

        # id
        id = cur.execute(
            """SELECT id_who FROM Users WHERE active = 'True'""").fetchone()[0]
        i = "0" * (4 - len(str(id))) + str(id)
        self.id.setText(i)

        # основная информация
        date = cur.execute(
            """SELECT date FROM Users WHERE active = 'True'""").fetchone()[0]
        sity = cur.execute(
            """SELECT sity FROM Users WHERE active = 'True'""").fetchone()[0]
        gender = cur.execute(
            """SELECT gender FROM Users WHERE active = 'True'""").fetchone()[0]
        self.info_2.setText(date + "\n" + "\n" + sity + "\n" + "\n" + gender)

        # посты
        res = cur.execute(
            """SELECT post FROM Posts WHERE id_who = ?""", (int(id), )).fetchall()
        self.posts.setColumnCount(1)
        self.posts.setRowCount(0)
        f = 0
        for i, row in enumerate(res):
            self.posts.setRowCount(
                self.posts.rowCount() + 1)
            for j, elem in enumerate(row):
                if len(elem) // 79 > f:
                    f = len(elem) // 79
                self.posts.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        if f != 0:
            self.posts.verticalHeader().setDefaultSectionSize(30 * (f + 1))
            self.posts.verticalHeader().setMinimumSectionSize(30 * (f + 1))

    # кнопка назад
    def run_back(self, exit_code=0):
        subprocess.Popen(['python', '!main.py'])
        sys.exit(exit_code)

    # кнопка "Редактировать"
    def run_edit(self, exit_code=0):
        subprocess.Popen(['python', '!edit.py'])
        sys.exit(exit_code)

    # публикация поста
    def run_publish(self):
        cur = self.con.cursor()
        id = cur.execute(
            """SELECT id_who FROM Users WHERE active = 'True'""").fetchone()[0]
        post = self.post.toPlainText()
        if post != "":
            cur.execute(
                "INSERT INTO posts(id_who,post) VALUES(?,?)", (id, post))
        self.con.commit()
        res = cur.execute(
            """SELECT post FROM Posts WHERE id_who = ?""", (int(id), )).fetchall()
        self.posts.setColumnCount(1)
        self.posts.setRowCount(0)
        f = 0
        for i, row in enumerate(res):
            self.posts.setRowCount(
                self.posts.rowCount() + 1)
            for j, elem in enumerate(row):
                if len(elem) // 79 > f:
                    f = len(elem) // 79
                self.posts.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        if f != 0:
            self.posts.verticalHeader().setDefaultSectionSize(30 * (f + 1))
            self.posts.verticalHeader().setMinimumSectionSize(30 * (f + 1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
