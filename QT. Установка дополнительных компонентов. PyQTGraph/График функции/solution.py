import sys
import math

from PyQt5.QtWidgets import QApplication, QMainWindow
from oneui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.runstep)
        self.pushButton_2.clicked.connect(self.runcor)
        self.pushButton_3.clicked.connect(self.runtri)

    def runstep(self):
        minX = self.minX.value()
        maxX = self.maxX.value()
        step = self.step.value()
        k = self.stepK.value()
        self.graphicsView.clear()
        self.graphicsView.plot([i for i in range(
            minX, maxX + 1)], [k * (i ** step) for i in range(minX, maxX + 1)], pen='r')

    def runcor(self):
        minX = self.minX.value()
        maxX = self.maxX.value()
        self.graphicsView.clear()
        minX = max(minX, 0)
        self.graphicsView.plot([i for i in range(
            minX, maxX + 1)], [i ** 0.5 for i in range(minX, maxX + 1)], pen='g')

    def runtri(self):
        minX = self.minX.value()
        maxX = self.maxX.value()
        self.graphicsView.clear()
        if self.sin.isChecked():
            self.graphicsView.plot([i for i in range(
                minX, maxX + 1)], [math.sin(i) for i in range(minX, maxX + 1)], pen='b')
        elif self.cos.isChecked():
            self.graphicsView.plot([i for i in range(
                minX, maxX + 1)], [math.cos(i) for i in range(minX, maxX + 1)], pen='b')
        elif self.tg.isChecked():
            self.graphicsView.plot([i for i in range(
                minX, maxX + 1)], [math.tan(i) for i in range(minX, maxX + 1)], pen='b')
        elif self.ctg.isChecked():
            if (minX < 0 and maxX > 0) or minX == 0 or maxX == 0:
                pass
            else:
                self.graphicsView.plot([i for i in range(
                    minX, maxX + 1)], [(math.cos(i) / math.sin(i)) for i in range(minX, maxX + 1)], pen='b')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
