from time import sleep
import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from mainwindow import Ui_MainWindow
from mytime import MyTime
from T_timer import Thread_timer
from T_stopwatch import Thread_stopwatch
from W_c_ir import T_w_c_ir
from W_c_de import T_w_c_de
from W_c_us import T_w_c_us
from Alarm import Alarm
from alarm_data import Database
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global thread_stopwatch
        global thread_timer
        global ir_w_c
        global de_w_c
        global us_w_c
        global t_alarm

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        thread_stopwatch = Thread_stopwatch()
        t_alarm = Alarm_Thread()
        ir_w_c = T_w_c_ir(self.ui)
        de_w_c = T_w_c_de(self.ui)
        us_w_c = T_w_c_us(self.ui)
        d_alarm = Alarm(self.ui)
        self.ui.btn_start_stopwatch.clicked.connect(start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(reset_stopwatch)
        thread_stopwatch.stopwatch_signal.connect(self.show_stopwatch_number)
        self.ui.lineEdit_2.setReadOnly(True)
        self.ui.lineEdit_3.setReadOnly(True)
        self.ui.btn_start_timer.clicked.connect(start_timer)
        self.ui.btn_stop_timer.clicked.connect(stop_timer)
        h = int(self.ui.tb_h.text())
        m = int(self.ui.tb_m.text())
        s = int(self.ui.tb_s.text())
        thread_timer = Thread_timer(h,s,m)
        self.timer_time = MyTime(h,m,s)
        self.show_timer_number(self.timer_time)
        thread_timer.timer_signal.connect(self.show_timer_number)
        self.ui.btn_ir_worldclock.clicked.connect(ir_worldclock)
        self.ui.btn_de_worldclock.clicked.connect(de_worldclock)
        self.ui.btn_us_worldclock.clicked.connect(us_worldclock)
        ir_worldclock()
        t_alarm.start()


    def show_stopwatch_number(self,time):
        self.ui.label_stopwatch.setText(f"{time.h}:{time.m}:{time.s}")

    def show_timer_number(self,time):
        self.ui.tb_h.setText(str(time.h))
        self.ui.tb_m.setText(str(time.m))
        self.ui.tb_s.setText(str(time.s))

class Alarm_Thread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            self.db = Database()
            now = datetime.now()
            h = now.hour
            m = now.minute
            s = now.second
            alarms = self.db.get_alarms()
            for i in range(len(alarms)):
                time = alarms[i][2]
                time = time.split(":")
                if time[0] == str(h) and time[1] == str(m) and time[2] == str(s):
                    msg = QMessageBox()
                    msg.setText(f"{alarms[i][0]}")
                    msg.exec_()
            sleep(1)

@Slot()
def ir_worldclock():
    ir_w_c.start()
    de_w_c.terminate()
    us_w_c.terminate()

@Slot()
def de_worldclock():
    de_w_c.start()
    us_w_c.terminate()
    ir_w_c.terminate()

@Slot()
def us_worldclock():
    us_w_c.start()
    ir_w_c.terminate()
    de_w_c.terminate()

@Slot()
def stop_timer():
    thread_timer.terminate()

@Slot()
def start_timer():
    thread_timer.start()

@Slot()
def reset_stopwatch():
    thread_stopwatch.reset()

@Slot()
def stop_stopwatch():
    thread_stopwatch.terminate()

@Slot()
def start_stopwatch():
    thread_stopwatch.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()