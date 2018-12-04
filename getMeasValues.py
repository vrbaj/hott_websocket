#!/usr/bin/python3

import sys
import tempfile
import subprocess
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
import json, time
from websocket import create_connection
import numpy as np


class MeasureThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, ip_address):
        QThread.__init__(self)
        self.git_url = ip_address

    # run method gets called when we start the thread
    def run(self):
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
        try:
            ws = create_connection("ws://10.0.0.4:8081")
        except Exception as ex:
            print(ex)

        for mereni in range(10):
            ws.send(json.dumps(json_trigger))
            result = ws.recv()
            time.sleep(.1)
            # TODO check result
            ws.send(json.dumps(json_get))
            clipx_message = ""
            while expected_message not in clipx_message:
                clipx_message = ws.recv()
                print(clipx_message + "  Data z:" + self.git_url)
            time.sleep(0.1)
            measured_values[mereni] = sensor1_values[mereni]["params"]["value"]
            print("EMIT PRE + ", measured_values)
            self.signal.emit(measured_values)
            print("EMIT POST")
        ws.close()
        self.signal.emit(measured_values)


