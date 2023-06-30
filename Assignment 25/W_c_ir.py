from datetime import datetime
from PySide2.QtCore import *
from mytime import MyTime

class T_w_c_ir(QThread):
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
    
    def run(self):
        while True:
            self.now = datetime.today()
            self.worldclock_time = MyTime(self.now.hour,self.now.minute,self.now.second)
            self.show_worldclock_number(self.worldclock_time)

    def show_worldclock_number(self,time):
        self.ui.label_worldclock.setText(f"{time.h}:{time.m}:{time.s}")