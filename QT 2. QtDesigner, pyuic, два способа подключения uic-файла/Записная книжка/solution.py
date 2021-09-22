import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from oneui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        a = self.lineEdit.text() + " " + self.lineEdit_2.text()
        self.listWidget.addItem(a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
