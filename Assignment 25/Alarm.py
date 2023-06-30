from functools import partial
from PySide2.QtWidgets import *
from alarm_data import Database

class Alarm():
    def __init__(self,ui):
        super().__init__()
        self.ui = ui

        self.db = Database()
        self.read_from_data()
        
        self.ui.btn_add_alarm.clicked.connect(self.new_alarm)

    def new_alarm(self):
        new_name = self.ui.le_name_alarm.text()
        new_description = self.ui.te_description__alarm.toPlainText()
        new_time = self.ui.le_time_alarm.text()
        feedback = self.db.add_new_alarm(new_name, new_description, new_time) 

        if feedback == True:
            self.read_from_data()
            self.ui.le_name_alarm.setText("")
            self.ui.te_description__alarm.setText("")
            self.ui.le_time_alarm.setText("")
            self.read_from_data()

        else:
            msg_box = QMessageBox()
            msg_box.setText("مشکلی پیش امده!!")
            msg_box.exec_()

    def remove_alarm(self,name):
        feedback = self.db.remove_alarm(name)

        if feedback == True:
            self.read_from_data()

        else:
            msg_box = QMessageBox()
            msg_box.setText("مشکلی پیش امده!!")
            msg_box.exec_()

    def set_new_alarm(self,name):
        new_name = self.ui.le_name_alarm.text()
        new_description = self.ui.te_description__alarm.toPlainText()
        new_time = self.ui.le_time_alarm.text()

        self.db.Edit_alarm(name,new_name,new_description,new_time)
        self.read_from_data()

    def edit_alarm(self,name):
        feedback = self.db.serch(name)
        
        self.ui.le_name_alarm.setText(feedback[0][0])
        self.ui.te_description__alarm.setText(feedback[0][1])
        self.ui.le_time_alarm.setText(feedback[0][2])

    def read_from_data(self):
        self.alarms = self.db.get_alarms()

        for i in range(len(self.alarms)):
            new_label_n = QLabel()
            new_label_d = QLabel()
            new_label_time = QLabel()
            new_btn_del = QPushButton("❌")
            new_btn_edi = QPushButton("✍️")
            new_btn_set = QPushButton("set")
            new_btn_del.setStyleSheet('background-color: rgb(255, 0, 0);')

            new_label_n.setText(self.alarms[i][0])
            new_label_d.setText(self.alarms[i][1])
            new_label_time.setText(self.alarms[i][2])

            self.ui.gridLayout.addWidget(new_label_n, i, 0)
            self.ui.gridLayout.addWidget(new_label_d, i, 1)
            self.ui.gridLayout.addWidget(new_label_time, i, 2)
            self.ui.gridLayout.addWidget(new_btn_del, i, 3)
            self.ui.gridLayout.addWidget(new_btn_edi, i, 4)
            self.ui.gridLayout.addWidget(new_btn_set, i, 5)

            new_btn_del.clicked.connect(partial(self.remove_alarm, self.alarms[i][0]))
            new_btn_edi.clicked.connect(partial(self.edit_alarm, self.alarms[i][0]))
            new_btn_set.clicked.connect(partial(self.set_new_alarm, self.alarms[i][0]))
