# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result.ui',
# licensing of 'Result.ui' applies.
#
# Created: Wed Mar  3 15:41:50 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Result(object):
    def setupUi(self, Result):
        Result.setObjectName("Result")
        Result.resize(304, 255)
        self.label = QtWidgets.QLabel(Result)
        self.label.setGeometry(QtCore.QRect(60, 40, 56, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Result)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 56, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Result)
        self.label_3.setGeometry(QtCore.QRect(60, 120, 56, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Result)
        self.label_4.setGeometry(QtCore.QRect(60, 160, 56, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Result)
        self.label_5.setGeometry(QtCore.QRect(60, 200, 56, 12))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Result)
        self.lineEdit.setGeometry(QtCore.QRect(140, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Result)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Result)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 120, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Result)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 160, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Result)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 200, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(Result)
        QtCore.QMetaObject.connectSlotsByName(Result)

    def retranslateUi(self, Result):
        Result.setWindowTitle(QtWidgets.QApplication.translate("Result", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Result", "Model", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Result", "Height", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Result", "Width", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Result", "Depth", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Result", "Number", None, -1))

