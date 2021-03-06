# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ent.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(276, 96, 61, 71))
        font = QtGui.QFont()
        font.setPointSize(55)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(326, 100, 41, 71))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(326, 91, 61, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 120, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 230, 291, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.id_guest = QtWidgets.QLineEdit(self.centralwidget)
        self.id_guest.setGeometry(QtCore.QRect(140, 275, 181, 20))
        self.id_guest.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.id_guest.setText("")
        self.id_guest.setMaxLength(4)
        self.id_guest.setObjectName("id_guest")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 275, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.guest = QtWidgets.QPushButton(self.centralwidget)
        self.guest.setGeometry(QtCore.QRect(30, 320, 291, 23))
        self.guest.setObjectName("guest")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(540, 260, 181, 20))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.login.setFont(font)
        self.login.setText("")
        self.login.setObjectName("login")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 260, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 230, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.sign_in = QtWidgets.QPushButton(self.centralwidget)
        self.sign_in.setGeometry(QtCore.QRect(430, 320, 145, 23))
        self.sign_in.setObjectName("sign_in")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(430, 290, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.parol = QtWidgets.QLineEdit(self.centralwidget)
        self.parol.setGeometry(QtCore.QRect(540, 290, 181, 20))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.parol.setFont(font)
        self.parol.setText("")
        self.parol.setEchoMode(QtWidgets.QLineEdit.Password)
        self.parol.setObjectName("parol")
        self.eyes = QtWidgets.QCheckBox(self.centralwidget)
        self.eyes.setGeometry(QtCore.QRect(730, 286, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.eyes.setFont(font)
        self.eyes.setChecked(False)
        self.eyes.setAutoRepeat(False)
        self.eyes.setObjectName("eyes")
        self.sign_up = QtWidgets.QPushButton(self.centralwidget)
        self.sign_up.setGeometry(QtCore.QRect(576, 320, 145, 23))
        self.sign_up.setObjectName("sign_up")
        self.error_guest = QtWidgets.QLabel(self.centralwidget)
        self.error_guest.setGeometry(QtCore.QRect(30, 350, 291, 21))
        self.error_guest.setText("")
        self.error_guest.setObjectName("error_guest")
        self.error_sign = QtWidgets.QLabel(self.centralwidget)
        self.error_sign.setGeometry(QtCore.QRect(430, 350, 291, 21))
        self.error_sign.setText("")
        self.error_sign.setObjectName("error_sign")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "??"))
        self.label_2.setText(_translate("MainWindow", "??"))
        self.label_3.setText(_translate("MainWindow", "????"))
        self.label_4.setText(_translate("MainWindow", "?????????????????"))
        self.label_5.setText(_translate("MainWindow", "???????????????? ???????????? ???????????????? ????????????????????????"))
        self.id_guest.setInputMask(_translate("MainWindow", "9999"))
        self.label_6.setText(_translate("MainWindow", "Id ????????????????????????:"))
        self.guest.setText(_translate("MainWindow", "?????????? ?????? ??????????"))
        self.label_7.setText(_translate("MainWindow", "??????????:"))
        self.label_8.setText(_translate("MainWindow", "??????????"))
        self.sign_in.setText(_translate("MainWindow", "??????????"))
        self.label_9.setText(_translate("MainWindow", "????????????:"))
        self.eyes.setText(_translate("MainWindow", "????"))
        self.sign_up.setText(_translate("MainWindow", "??????????????????????"))
