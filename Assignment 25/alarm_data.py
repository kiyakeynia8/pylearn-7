import sqlite3

class Database():
    def __init__(self):
        self.con = sqlite3.connect("database_alarm.db")
        self.cursor = self.con.cursor()
        self.alarms = []

    def get_alarms(self):
        query = "SELECT * FROM alarms"
        result = self.cursor.execute(query)
        self.alarms = result.fetchall()
        return self.alarms

    def add_new_alarm(self,new_name,new_description,new_time):
        try:
            query = (f"INSERT INTO alarms(name, description, time)VALUES('{new_name}','{new_description}', '{new_time}')")
            self.cursor.execute(query)
            self.con.commit()
            return True
        
        except:
            return False

    def remove_alarm(self,name):
        try:
            self.cursor.execute(f"DELETE FROM alarms WHERE name = '{name}'")
            self.con.commit()
            return True

        except:
            return False

    def serch(self,name):
        result = self.cursor.execute(f"SELECT * FROM alarms WHERE name = '{name}'")
        alarm = result.fetchall()
        return alarm

    def Edit_alarm(self,name,new_n,new_d,new_t):
        self.cursor.execute(f"UPDATE alarms SET name = '{new_n}' WHERE name = '{name}'")
        self.con.commit()
        self.cursor.execute(f"UPDATE alarms SET description = '{new_d}' WHERE name = '{name}'")
        self.con.commit()
        self.cursor.execute(f"UPDATE alarms SET time = '{new_t}' WHERE name = '{name}'")
        self.con.commit()