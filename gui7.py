# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!


from decimal import Decimal
import asyncio
import websockets
import websocket
import json
import time
import numpy as np
import _thread
import threading
from threading import Thread
import datetime

from websocket import create_connection
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QThread
import pyqtgraph as pq

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.int_validator =QtGui.QIntValidator()
        self.float_validator = QtGui.QDoubleValidator()
        self.koeficienty = {'uzavreny': [0.000615, 0.001056], 'otevreny': [0.000895, 0.000287]}
        pq.setConfigOption('background', 'y')
        pq.setConfigOption('foreground', 'k')
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(912, 732)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_hodnoty1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_hodnoty1.setGeometry(QtCore.QRect(30, 60, 151, 181))
        self.text_hodnoty1.setObjectName("text_hodnoty1")
        self.text_hodnoty2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_hodnoty2.setGeometry(QtCore.QRect(445, 50, 151, 192))
        self.text_hodnoty2.setObjectName("text_hodnoty2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 201, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 30, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 60, 121, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 110, 121, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(610, 50, 121, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(610, 110, 121, 16))
        self.label_7.setObjectName("label_7")
        self.prumer1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.prumer1.setGeometry(QtCore.QRect(200, 80, 141, 31))
        self.prumer1.setObjectName("prumer1")
        self.prumer2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.prumer2.setGeometry(QtCore.QRect(610, 70, 141, 31))
        self.prumer2.setObjectName("prumer2")
        self.smodch1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.smodch1.setGeometry(QtCore.QRect(200, 130, 141, 31))
        self.smodch1.setObjectName("smodch1")
        self.smodch2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.smodch2.setGeometry(QtCore.QRect(610, 130, 141, 31))
        self.smodch2.setObjectName("smodch2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 771, 281))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.groupBox.setPalette(palette)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.buttonMereni = QtWidgets.QPushButton(self.groupBox)
        self.buttonMereni.setGeometry(QtCore.QRect(610, 200, 141, 41))
        self.buttonMereni.setObjectName("buttonMereni")
        self.buttonMereni.clicked.connect(self.one_measure)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(770, 0, 141, 281))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.groupBox_2.setPalette(palette)
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.rozdil = QtWidgets.QTextBrowser(self.groupBox_2)
        self.rozdil.setGeometry(QtCore.QRect(20, 100, 111, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.rozdil.setPalette(palette)
        self.rozdil.setObjectName("rozdil")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 280, 911, 381))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.groupBox_3.setPalette(palette)
        self.groupBox_3.setAutoFillBackground(True)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 201, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.graphicsView = PlotWidget(self.groupBox_3)
        self.graphicsView.setGeometry(QtCore.QRect(250, 10, 651, 341))
        self.graphicsView.setObjectName("graphicsView")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(20, 60, 91, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(20, 80, 91, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(20, 100, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(datetime.datetime.now().strftime("Data_" + "%Y-%m-%d_%H%M%S" + ".csv"))
        reg_ex = QtCore.QRegExp("([a-zA-Z0-9\s_,\]\[\(\)\-:])+.csv$")
        self.lineEdit_interval = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_interval.setGeometry(QtCore.QRect(90, 60, 151, 20))
        self.lineEdit_interval.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_interval.setObjectName("lineEdit_interval")
        self.lineEdit_interval.setValidator(self.int_validator)
        self.lineEdit_pocet_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_pocet_2.setGeometry(QtCore.QRect(90, 40, 151, 20))
        self.lineEdit_pocet_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_pocet_2.setValidator(self.int_validator)

        self.lineEdit_pocet_2.setObjectName("lineEdit_pocet_2")
        self.buttonMereniDynamicke = QtWidgets.QPushButton(self.groupBox_3)
        self.buttonMereniDynamicke.setGeometry(QtCore.QRect(20, 120, 221, 21))
        self.buttonMereniDynamicke.setObjectName("buttonMereniDynamicke")
        self.buttonMereniDynamicke.clicked.connect(self.multiple_measure)
        self.text_dynhodnoty = QtWidgets.QTextBrowser(self.groupBox_3)
        self.text_dynhodnoty.setGeometry(QtCore.QRect(20, 170, 151, 181))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.text_dynhodnoty.setPalette(palette)
        self.text_dynhodnoty.setObjectName("text_dynhodnoty")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(20, 150, 47, 13))
        self.label_13.setObjectName("label_13")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(340, 660, 320, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushTare2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushTare2.setGeometry(QtCore.QRect(10, 20, 70, 23))
        self.pushTare2.setObjectName("pushTare2")
        self.pushTareZrusit2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushTareZrusit2.setGeometry(QtCore.QRect(80, 20, 90, 23))
        self.pushTareZrusit2.setObjectName("pushTareZrusit2")
        self.pushNula2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushNula2.setGeometry(QtCore.QRect(170, 20, 70, 23))
        self.pushNula2.setObjectName("pushNula2")
        self.pushNulaZrusit2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushNulaZrusit2.setGeometry(QtCore.QRect(240, 20, 70, 23))
        self.pushNulaZrusit2.setObjectName("pushNulaZrusit2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 660, 320, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushTare2_2 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushTare2_2.setGeometry(QtCore.QRect(10, 20, 70, 23))
        self.pushTare2_2.setObjectName("pushTare2_2")
        self.pushTareZrusit2_2 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushTareZrusit2_2.setGeometry(QtCore.QRect(80, 20, 90, 23))
        self.pushTareZrusit2_2.setObjectName("pushTareZrusit2_2")
        self.pushNula1 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushNula1.setGeometry(QtCore.QRect(170, 20, 70, 23))
        self.pushNula1.setObjectName("pushNula1")
        self.pushNulaZrusit1 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushNulaZrusit1.setGeometry(QtCore.QRect(240, 20, 70, 23))
        self.pushNulaZrusit1.setObjectName("pushNulaZrusit1")
        # parametry
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(680, 660, 55, 13))
        self.label_20.setObjectName("label_20")

        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(750, 675, 20, 13))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(750, 692, 20, 13))
        self.label_22.setObjectName("label_22")

        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(670, 666, 240, 45))
        self.groupBox_6.setObjectName("groupBox_6")

        self.lineEdit_koef1 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_koef1.setGeometry(QtCore.QRect(5, 7, 70, 18))
        self.lineEdit_koef1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_koef1.setObjectName("lineEdit_koef1")
        self.lineEdit_koef1.setText(str(self.koeficienty["uzavreny"][0]))
        self.lineEdit_koef1.setValidator(self.float_validator)
        self.lineEdit_koef1.textChanged.connect(self.editKoef1)

        self.lineEdit_koef2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_koef2.setGeometry(QtCore.QRect(5, 23, 70, 18))
        self.lineEdit_koef2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_koef2.setObjectName("lineEdit_koef2")
        self.lineEdit_koef2.setText(str(self.koeficienty["uzavreny"][1]))
        self.lineEdit_koef2.setValidator(self.float_validator)
        self.lineEdit_koef2.textChanged.connect(self.editKoef2)

        self.radio1 = QtWidgets.QRadioButton("Uzavřený", self.groupBox_6)
        self.radio1.setGeometry(QtCore.QRect(100, 3, 80, 25))
        self.radio1.setChecked(True)
        self.radio1.toggled.connect(lambda: self.btnstate(self.radio1))
        self.radio2 = QtWidgets.QRadioButton("Otevřený", self.groupBox_6)
        self.radio2.setGeometry(QtCore.QRect(100, 20, 80, 25))
        self.radio2.toggled.connect(lambda: self.btnstate(self.radio2))

        self.buttonRst = QtWidgets.QPushButton(self.groupBox_6)
        self.buttonRst.setGeometry(QtCore.QRect(180, 5, 50, 21))
        self.buttonRst.setObjectName("buttonRst")
        self.buttonRst.clicked.connect(self.resetKoef)


        self.pushNula1.clicked.connect(self.nula1)
        self.pushNula2.clicked.connect(self.nula2)
        self.pushTare2.clicked.connect(self.tare1)
        self.pushTare2_2.clicked.connect(self.tare2)
        self.pushNulaZrusit1.clicked.connect(self.nula1_zrusit)
        self.pushNulaZrusit2.clicked.connect(self.nula2_zrusit)
        self.pushTareZrusit2.clicked.connect(self.tare1_zrusit)
        self.pushTareZrusit2_2.clicked.connect(self.tare2_zrusit)

        self.groupBox.raise_()
        self.text_hodnoty1.raise_()
        self.text_hodnoty2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.prumer1.raise_()
        self.prumer2.raise_()
        self.smodch1.raise_()
        self.smodch2.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.radio2.click()
        self.radio1.click()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def resetKoef(self):
        self.koeficienty = {'uzavreny': [0.000615, 0.001056], 'otevreny': [0.000895, 0.000287]}
        self.radio2.click()
        self.radio1.click()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Měření"))
        self.label.setText(_translate("MainWindow", "Statické měření"))
        self.label_2.setText(_translate("MainWindow", "Čidlo 1"))
        self.label_3.setText(_translate("MainWindow", "Čidlo 2"))
        self.label_20.setText(_translate("MainWindow", "Parametry"))
        self.label_21.setText(_translate("MainWindow", "č.1"))
        self.label_22.setText(_translate("MainWindow", "č.2"))
        self.label_4.setText(_translate("MainWindow", "Průměrná hodnota"))
        self.label_5.setText(_translate("MainWindow", "Směrodatná odchylka"))
        self.label_6.setText(_translate("MainWindow", "Průměrná hodnota"))
        self.label_7.setText(_translate("MainWindow", "Směrodatná odchylka"))
        self.buttonMereni.setText(_translate("MainWindow", "Měření"))
        self.buttonRst.setText(_translate("MainWindow","Reset"))
        self.label_8.setText(_translate("MainWindow", "Rozdíl"))
        self.label_9.setText(_translate("MainWindow", "Dynamické měření"))
        self.label_10.setText(_translate("MainWindow", "Počet měření"))
        self.label_11.setText(_translate("MainWindow", "Interval [s]"))
        self.label_12.setText(_translate("MainWindow", "Název souboru"))
        self.buttonMereniDynamicke.setText(_translate("MainWindow", "Zahájit měření"))
        self.label_13.setText(_translate("MainWindow", "Hodnoty"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Čidlo 2"))
        self.pushTare2.setText(_translate("MainWindow", "Tare"))
        self.pushTareZrusit2.setText(_translate("MainWindow", "Vynulovat Tare"))
        self.pushNula2.setText(_translate("MainWindow", "Vynulovat"))
        self.pushNulaZrusit2.setText(_translate("MainWindow", "Zrušit 0"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Čidlo 1"))
        self.pushTare2_2.setText(_translate("MainWindow", "Tare"))
        self.pushTareZrusit2_2.setText(_translate("MainWindow", "Vynulovat Tare"))
        self.pushNula1.setText(_translate("MainWindow", "Vynulovat"))
        self.pushNulaZrusit1.setText(_translate("MainWindow", "Zrušit 0"))


    def editKoef1(self):
        if self.radio1.isChecked() == True:
            self.koeficienty["uzavreny"][0] = float(self.lineEdit_koef1.text())
        if self.radio2.isChecked() == True:
            self.koeficienty["otevreny"][0] = float(self.lineEdit_koef1.text())

    def editKoef2(self):
        if self.radio1.isChecked() == True:
            self.koeficienty["uzavreny"][1] = float(self.lineEdit_koef2.text())
        if self.radio2.isChecked() == True:
            self.koeficienty["otevreny"][1] = float(self.lineEdit_koef2.text())

    def btnstate(self, b):
        if b.text() == "Otevřený":
            if b.isChecked() == True:
                self.lineEdit_koef1.setText(str(self.koeficienty['otevreny'][0]))
                self.lineEdit_koef2.setText(str(self.koeficienty['otevreny'][1]))

        if b.text() == "Uzavřený":
            if b.isChecked() == True:
                self.lineEdit_koef1.setText(str(self.koeficienty['uzavreny'][0]))
                self.lineEdit_koef2.setText(str(self.koeficienty['uzavreny'][1]))


    def nula1(self):
        # {"id":27,"method":"call","params":{"path":"measval/cmdSetZeroGros","args":[]}}
        self.send_command(1, "zero")

    def nula2(self):
        self.send_command(2, "zero")

    def tare2(self):
        self.send_command(2, "tare")

    def tare1(self):
        self.send_command(1, "tare")

    def nula1_zrusit(self):
        self.send_command(1, "clear_zero")

    def nula2_zrusit(self):
        self.send_command(2, "clear_zero")

    def tare1_zrusit(self):
        self.send_command(1, "clear_tare")

    def tare2_zrusit(self):
        self.send_command(2, "clear_tare")

    def multiple_measure(self):
        print("multiple")
        self.buttonMereni.setEnabled(False)
        self.buttonMereniDynamicke.setEnabled(False)
        self.graphicsView.plotItem.clear()
        total_measurements = int(self.lineEdit_pocet_2.text())
        period_time = int(self.lineEdit_interval.text())
        dyn_value = np.array([])
        dyn_prumer1 = np.array([])
        dyn_prumer2 = np.array([])
        dyn_smodch1 = np.array([])
        dyn_smodch2 = np.array([])

        self.text_dynhodnoty.setText("")
        QtGui.QGuiApplication.processEvents()

        for measurement in range(total_measurements):
            self.text_hodnoty1.setText("")
            self.text_hodnoty2.setText("")
            self.rozdil.setText("0")
            self.prumer1.setText("0")
            self.prumer2.setText("0")
            self.smodch1.setText("0")
            self.smodch2.setText("0")
            json_trigger_command = """
                                   {"id":1,"method":"call","params":{"path":"measval/cmdTriggerCapturedValue1","args":[]}}
                                   """
            json_get_command = """
                                   {"method":"fetch_all","params":{"path":"measval/values/capturedValue1"}}
                                   """
            json_trigger = json.loads(json_trigger_command)
            json_get = json.loads(json_get_command)
            expected_message = """"path":"measval/values/capturedValue1"""""
            sensor1_values = [None] * 10
            measured_values = np.zeros((10,))
            try:
                ws = create_connection("ws://169.254.178.232:8081")
            except Exception as ex:
                print(ex)
            print("Start mereni 1:" + str(datetime.datetime.now()))
            for mereni in range(1):
                ws.send(json.dumps(json_trigger))
                result = ws.recv()
                time.sleep(.1)
                # TODO check result
                ws.send(json.dumps(json_get))
                clipx_message = ""
                while expected_message not in clipx_message:
                    try:
                        clipx_message = ws.recv()
                        print(clipx_message)
                    except Exception as ex:
                        print(ex)
                    sensor1_values[mereni] = json.loads(clipx_message)
                self.text_hodnoty1.append("{:.4E}".format(Decimal(sensor1_values[mereni]["params"]["value"])))
                QtGui.QGuiApplication.processEvents()
                measured_values[mereni] = sensor1_values[mereni]["params"]["value"]
            ws.close()
            print("Stop mereni 1:" + str(datetime.datetime.now()))
            dyn_prumer1 = np.append(dyn_prumer1, measured_values.mean())
            dyn_smodch1 = np.append(dyn_smodch1, measured_values.std())
            self.prumer1.setText("{:.4E}".format(Decimal(measured_values.mean())))
            self.smodch1.setText("{:.4E}".format(Decimal(measured_values.std())))
            QtGui.QGuiApplication.processEvents()

            sensor2_values = [None] * 10
            measured2_values = np.zeros((10, 1))
            ws2 = create_connection("ws://169.254.178.218:8081")
            self.text_hodnoty2.setText("")
            print("Start mereni 2:" + str(datetime.datetime.now()))
            for mereni in range(1):
                ws2.send(json.dumps(json_trigger))
                result = ws2.recv()
                time.sleep(.1)
                # TODO check result
                ws2.send(json.dumps(json_get))
                clipx_message = ""
                while not expected_message in clipx_message:
                    clipx_message = ws2.recv()

                    sensor2_values[mereni] = json.loads(clipx_message)

                # print(sensor1_values[mereni]["params"]["value"])
                self.text_hodnoty2.append("{:.4E}".format(Decimal(sensor2_values[mereni]["params"]["value"])))
                QtGui.QGuiApplication.processEvents()
                measured2_values[mereni] = sensor2_values[mereni]["params"]["value"]

            ws2.close()
            print("Stop mereni 2:" + str(datetime.datetime.now()))
            dyn_prumer2 = np.append(dyn_prumer2, measured2_values.mean())
            dyn_smodch2 = np.append(dyn_smodch2, measured2_values.std())
            self.prumer2.setText("{:.4E}".format(Decimal(measured2_values.mean())))
            self.smodch2.setText("{:.4E}".format(Decimal(measured2_values.std())))

            dyn_value = np.append(dyn_value, measured_values.mean() - measured2_values.mean())
            self.text_dynhodnoty.append("{:.4E}".format(Decimal(dyn_value[-1])))
            self.rozdil.setText("{:.4E}".format(Decimal(dyn_value[measurement])))
            if len(dyn_value) > 1:
                try:
                    self.graphicsView.plot(dyn_value, pen=pq.mkPen('b', width=3,
                                                                   style=QtCore.Qt.SolidLine, color=(200, 200, 255)))
                    self.graphicsView.getPlotItem().showGrid(x=True, y=True, alpha=1)
                    QtGui.QGuiApplication.processEvents()
                except Exception as ex:
                    print(ex)
            start_pause = (datetime.datetime.now())

            time_difference = start_pause - start_pause
            time_difference_seconds = time_difference.total_seconds()
            while time_difference_seconds < period_time:
                time.sleep(0.05)
                QtGui.QGuiApplication.processEvents()
                time_difference = datetime.datetime.now() - start_pause
                time_difference_seconds = time_difference.total_seconds()
        self.buttonMereni.setEnabled(True)
        self.buttonMereniDynamicke.setEnabled(True)
        QtGui.QGuiApplication.processEvents()
        output = np.asarray([dyn_value, dyn_value, dyn_value, dyn_value, dyn_value])
        try:
            np.savetxt(self.lineEdit.text(), output.transpose(), delimiter=",",
                       header="diff,smodch1,smodch2,prumer1,prumer2")
        except Exception as ex:
            print(ex)
        self.lineEdit.setText(datetime.datetime.now().strftime("Data_" + "%Y-%m-%d_%H%M%S" + ".csv"))
        QtGui.QGuiApplication.processEvents()

    def one_measure(self):
        self.buttonMereni.setEnabled(False)
        self.buttonMereniDynamicke.setEnabled(False)
        QtGui.QGuiApplication.processEvents()
        self.text_hodnoty1.setText("")
        self.text_hodnoty2.setText("")
        self.rozdil.setText("0")
        self.prumer1.setText("")
        self.prumer2.setText("")
        self.rozdil.setText("")
        json_trigger_command = """
                       {"id":1,"method":"call","params":{"path":"measval/cmdTriggerCapturedValue1","args":[]}}
                       """
        json_get_command = """
                       {"method":"fetch_all","params":{"path":"measval/adcBinVal32"}}
                       """
        json_trigger = json.loads(json_trigger_command)
        json_get = json.loads(json_get_command)
        expected_message = """"path":"measval/values/capturedValue1"""""
        sensor1_values = [None] * 10
        measured_values = np.zeros((10,))

        ws = create_connection("ws://169.254.178.232:8081")

        for mereni in range(10):
            ws.send(json.dumps(json_trigger))
            result = ws.recv()
            time.sleep(.1)
            # TODO check result
            ws.send(json.dumps(json_get))
            clipx_message = ""
            while expected_message not in clipx_message:
                clipx_message = ws.recv()

                sensor1_values[mereni] = json.loads(clipx_message)
            self.text_hodnoty1.append(str(sensor1_values[mereni]["params"]["value"]))
            QtGui.QGuiApplication.processEvents()
            measured_values[mereni] = sensor1_values[mereni]["params"]["value"]
        ws.close()

        self.prumer1.setText("{:.4E}".format(Decimal(measured_values.mean())))
        self.smodch1.setText("{:.4E}".format(Decimal(measured_values.std())))
        QtGui.QGuiApplication.processEvents()
        sensor2_values = [None] * 10
        measured2_values = np.zeros((10, 1))
        ws2 = create_connection("ws://169.254.178.218:8081")
        self.text_hodnoty2.setText("")
        for mereni in range(10):
            ws2.send(json.dumps(json_trigger))
            result = ws2.recv()
            time.sleep(.1)
            print(mereni)
            # TODO check result
            ws2.send(json.dumps(json_get))
            clipx_message = ""
            while not expected_message in clipx_message:
                clipx_message = ws2.recv()

                sensor2_values[mereni] = json.loads(clipx_message)

            # print(sensor1_values[mereni]["params"]["value"])
            self.text_hodnoty2.append("{:.4E}".format(Decimal(sensor2_values[mereni]["params"]["value"])))
            QtGui.QGuiApplication.processEvents()
            measured2_values[mereni] = sensor2_values[mereni]["params"]["value"]

        ws2.close()

        self.prumer2.setText("{:.4E}".format(Decimal(measured2_values.mean())))
        self.smodch2.setText("{:.4E}".format(Decimal(measured2_values.std())))
        rozdil = measured_values.mean() - measured2_values.mean()
        self.rozdil.setText("{:.4E}".format(Decimal(rozdil)))
        self.buttonMereni.setEnabled(True)
        self.buttonMereniDynamicke.setEnabled(True)
        QtGui.QGuiApplication.processEvents()

    def send_command(self, device, command):
        if device == 1:
            connection_string = "ws://169.254.178.218:8081"
        else:
            connection_string = "ws://169.254.178.232:8081"

        if command == "tare":
            json_command = """
            {"id":2,"method":"call","params":{"path":"measval/cmdSetZeroNet","args":[]}}"""
        elif command == "clear_tare":
            json_command = """
            {"id":31,"method":"call","params":{"path":"measval/cmdClearOffsetNet","args":[]}}"""
        elif command == "zero":
            json_command = """
            {"id":32,"method":"call","params":{"path":"measval/cmdSetZeroGros","args":[]}}"""
            # json_command = """
            # {"id":68,"method":"set","params":{"path":"measval/scaling/zeroTargetGros","value":150}}"""
        elif command == "clear_zero":
            json_command = """
            {"id":33,"method":"call","params":{"path":"measval/cmdClearOffsetGros","args":[]}}"""
        else:
            print("ERROR")
            json_command = """"""
        try:
            ws = create_connection(connection_string)
        except Exception as ex:
            print(ex)

        json_tare = json.loads(json_command)
        ws.send(json.dumps(json_tare))
        result = ws.recv()
        print(result)
        ws.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())