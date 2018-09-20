# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import asyncio
import websockets
import websocket
import json
import time
import numpy as np
import _thread
import threading
from threading import Thread

from websocket import create_connection
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(912, 600)
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
        self.buttonMereni.clicked.connect(self.on_click)
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
        self.groupBox_3.setGeometry(QtCore.QRect(0, 280, 771, 291))
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
        self.groupBox.raise_()
        self.text_hodnoty1.raise_()
        self.text_hodnoty2.raise_()
        self.label.raise_()
        self.label_2.raise_()
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def on_click(self):
        print('PyQt5 button click')
        print("running..")
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
        measured_values = np.zeros((10, 1))
        ws = create_connection("ws://10.0.0.46:8081")
        self.text_hodnoty1.setText("")
        for mereni in range(10):
            ws.send(json.dumps(json_trigger))
            result = ws.recv()
            time.sleep(.1)
            print(mereni)
            # TODO check result
            ws.send(json.dumps(json_get))
            clipx_message = ""
            while not expected_message in clipx_message:
                clipx_message = ws.recv()

                sensor1_values[mereni] = json.loads(clipx_message)

            # print(sensor1_values[mereni]["params"]["value"])
            self.text_hodnoty1.append(str(sensor1_values[mereni]["params"]["value"]))
            measured_values[mereni] = sensor1_values[mereni]["params"]["value"]

        ws.close()
        print("done")
        print("thread finished...exiting")
        print(sensor1_values)
        print(measured_values)
        self.prumer1.setText(str(measured_values.mean()))
        self.smodch1.setText(str(measured_values.std()))




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Měření"))
        self.label.setText(_translate("MainWindow", "Statické měření"))
        self.label_2.setText(_translate("MainWindow", "Čidlo 1"))
        self.label_3.setText(_translate("MainWindow", "Čidlo 2"))
        self.label_4.setText(_translate("MainWindow", "Průměrná hodnota"))
        self.label_5.setText(_translate("MainWindow", "Směrodatná odchylka"))
        self.label_6.setText(_translate("MainWindow", "Průměrná hodnota"))
        self.label_7.setText(_translate("MainWindow", "Směrodatná odchylka"))
        self.buttonMereni.setText(_translate("MainWindow", "Měření"))
        self.label_8.setText(_translate("MainWindow", "Rozdíl"))
        self.label_9.setText(_translate("MainWindow", "Dynamické měření"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


def communicate():
    print("running..")
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
    ws = create_connection("ws://10.0.0.46:8081")

    for mereni in range(10):
        ws.send(json.dumps(json_trigger))
        result = ws.recv()
        time.sleep(.2)
        # TODO check result
        ws.send(json.dumps(json_get))
        clipx_message = ""
        while not expected_message in clipx_message:
            clipx_message = ws.recv()
            sensor1_values[mereni] = json.loads(clipx_message)


    ws.close()
    print("done")