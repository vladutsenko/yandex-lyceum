import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from calc import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        a = ""
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.label.setText("OK")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())