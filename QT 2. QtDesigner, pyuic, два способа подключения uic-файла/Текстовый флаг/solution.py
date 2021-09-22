import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from oneui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setFixedSize(700, 340)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        if self.blue1.isChecked():
            a = "Синий"
        elif self.red1.isChecked():
            a = "Красный"
        else:
            a = "Зелёный"
        if self.blue2.isChecked():
            b = "Синий"
        elif self.red2.isChecked():
            b = "Красный"
        else:
            b = "Зелёный"
        if self.blue3.isChecked():
            c = "Синий"
        elif self.red3.isChecked():
            c = "Красный"
        else:
            c = "Зелёный"

        self.label.setText("Цвета: " + a + ", " + b + " и " + c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
