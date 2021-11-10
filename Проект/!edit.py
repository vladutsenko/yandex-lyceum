import sys
import sqlite3
import subprocess
import pymorphy2

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from edit import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("network.db")
        self.save.clicked.connect(self.run_save)
        self.photo.clicked.connect(self.photo_save)

    # сохранение основной информации
    def run_save(self, exit_code=0):
        cur = self.con.cursor()
        cur.execute(
            "UPDATE Users SET name = ? WHERE active = 'True'", (self.name.text(),))
        cur.execute(
            "UPDATE Users SET surname = ? WHERE active = 'True'", (self.surname.text(),))
        cur.execute(
            "UPDATE Users SET status = ? WHERE active = 'True'", (self.status.text(),))

        # дата рождения
        f = self.date.date()
        date = str(self.date.date())
        date = date[date.find("(") + 1:date.find(")")].split(", ")
        day = date[2]

        months = ["январь", "февраль", "март", "апрель", "май", "июнь",
                  "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
        month2 = months[int(date[1]) - 1]
        morph = pymorphy2.MorphAnalyzer()
        word = morph.parse(month2)[0]
        month = word.inflect({'gent'}).word

        year = date[0]
        if self.how.currentText() == "Показывать дату полностью":
            total = day + " " + month + " " + year
        elif self.how.currentText() == "Показывать только день и месяц":
            total = day + " " + month
        elif self.how.currentText() == "Показывать только месяц и год":
            total = month2 + " " + year
        else:
            total = year
        cur.execute(
            "UPDATE Users SET date = ? WHERE active = 'True'", (total,))

        cur.execute(
            "UPDATE Users SET sity = ? WHERE active = 'True'", (self.sity.text(),))
        cur.execute(
            "UPDATE Users SET gender = ? WHERE active = 'True'", (self.gender.currentText(),))

        if self.name.text() == "":
            self.error.setText("Не указано имя")
        elif self.surname.text() == "":
            self.error.setText("Не указана фамилия")
        else:
            self.con.commit()
            self.con.close()
            subprocess.Popen(['python', '!str+.py'])
            sys.exit(exit_code)

    # загрузка фото
    def photo_save(self):
        cur = self.con.cursor()
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Все файлы (*)')[0]
        fin = open(fname, "rb")
        f = fin.read()
        cur.execute(
            "UPDATE Users SET photo = ? WHERE active = 'True'", (f,))
        self.photo.setText("Загружено ✔️")
        self.con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
