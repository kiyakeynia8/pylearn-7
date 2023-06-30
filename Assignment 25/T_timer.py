import time
from PySide2.QtCore import *
from mytime import MyTime

class Thread_timer(QThread):
    timer_signal = Signal(MyTime)
    def __init__(self,h,m,s):
        super().__init__()
        self.timer_time = MyTime(h,s,m)

    def run(self):
        while True:
            self.timer_time.minus()
            self.timer_signal.emit(self.timer_time)
            time.sleep(1)