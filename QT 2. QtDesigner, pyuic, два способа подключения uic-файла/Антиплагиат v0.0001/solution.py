import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from one import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Антиплагиат v0.0001')
        self.pushButton.clicked.connect(self.run)

    def run(self):
        t1 = self.textEdit.toPlainText()
        t2 = self.textEdit_2.toPlainText()
        p = self.doubleSpinBox.value()
        k = sum(t1[i] != t2[i] for i in range(min([len(t1), len(t2)])))
        k = k + max([len(t1), len(t2)]) - min([len(t1), len(t2)])
        k = 0 if k == 0 else k / len(t1) * 100
        self.progressBar.setValue(int(100 - k))
        if 100 - k >= p:
            self.progressBar.setStyleSheet(
                '''QProgressBar::chunk:horizontal {
                    background: qlineargradient(stop: 0 red);
                    }''')
        else:
            self.progressBar.setStyleSheet("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
