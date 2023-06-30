import time
from PySide2.QtCore import *
from mytime import MyTime

class Thread_stopwatch(QThread):
    stopwatch_signal = Signal(MyTime)
    def __init__(self):
        super().__init__()
        self.stopwatch_time = MyTime(0,0,0)

    def run(self):
        while True:
            self.stopwatch_time.plus()
            self.stopwatch_signal.emit(self.stopwatch_time)
            time.sleep(1)

    def reset(self):
        self.stopwatch_time = MyTime(0,0,0)