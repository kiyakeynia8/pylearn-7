from datetime import datetime
from PySide2.QtCore import *
from mytime import MyTime

class T_w_c_us(QThread):
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
    
    def run(self):
        while True:
            self.now = datetime.today()
            h = self.now.hour - 8
            m = self.now.minute - 30
            s = self.now.second
            if h <= 0:
                h += 24
            if m <= 0:
                m += 60
            if s <= 0:
                s += 60
            self.worldclock_time = MyTime(h,m,s)
            self.show_worldclock_number(self.worldclock_time)

    def show_worldclock_number(self,time):
        self.ui.label_worldclock.setText(f"{time.h}:{time.m}:{time.s}")
