# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Wed Mar  3 14:35:24 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(592, 347)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Load1 = QtWidgets.QPushButton(self.centralwidget)
        self.Load1.setGeometry(QtCore.QRect(120, 260, 75, 23))
        self.Load1.setObjectName("Load1")
        self.Predict = QtWidgets.QPushButton(self.centralwidget)
        self.Predict.setGeometry(QtCore.QRect(260, 300, 75, 23))
        self.Predict.setObjectName("Predict")
        self.Load2 = QtWidgets.QPushButton(self.centralwidget)
        self.Load2.setGeometry(QtCore.QRect(410, 260, 75, 23))
        self.Load2.setObjectName("Load2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 10, 61, 16))
        self.label_2.setObjectName("label_2")
        self.graphicsView1 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView1.setGeometry(QtCore.QRect(20, 40, 261, 192))
        self.graphicsView1.setObjectName("graphicsView1")
        self.Display1 = QtWidgets.QLabel(self.centralwidget)
        self.Display1.setGeometry(QtCore.QRect(20, 40, 261, 191))
        self.Display1.setText("")
        self.Display1.setObjectName("Display1")
        self.graphicsView2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView2.setGeometry(QtCore.QRect(310, 40, 261, 192))
        self.graphicsView2.setObjectName("graphicsView2")
        self.Display2 = QtWidgets.QLabel(self.centralwidget)
        self.Display2.setGeometry(QtCore.QRect(310, 40, 261, 191))
        self.Display2.setText("")
        self.Display2.setObjectName("Display2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.Load1.setText(QtWidgets.QApplication.translate("MainWindow", "Load", None, -1))
        self.Predict.setText(QtWidgets.QApplication.translate("MainWindow", "Predict", None, -1))
        self.Load2.setText(QtWidgets.QApplication.translate("MainWindow", "Load", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "부재리스트", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "구조평면도", None, -1))

