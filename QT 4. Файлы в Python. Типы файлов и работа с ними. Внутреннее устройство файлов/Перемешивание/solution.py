import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from one import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Перемешивание')
        self.pushButton.clicked.connect(self.run)

    def run(self):
        with open("example.txt") as f:
            data = f.read().split('\n')
            first = []
            second = []
            for i in range(1, len(data) + 1):
                if i % 2 == 1:
                    first.append(data[i - 1])
                else:
                    second.append(data[i - 1])
        self.textEdit.setPlainText("\n".join(first) + '\n' + "\n".join(second))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
