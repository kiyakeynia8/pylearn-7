import sqlite3

def show_menu():
    print("1_ show list")
    print("2_ add new")
    print("3_ edit")
    print("4_ remove")
    print("5_ exit")

def load_database():
    global Connection
    global my_cursor

    Connection = sqlite3.connect("Assignment 21/chinook.db")
    my_cursor = Connection.cursor()

def show_list():
    result = my_cursor.execute("SELECT * FROM genres")
    moshtarian = result.fetchall()
    for moshtari in moshtarian:
        print(moshtari)

def add_new():
    new_genre_name = input("enter a name for new genre: ")
    my_cursor.execute(f"INSERT INTO genres(Name) VALUES('{new_genre_name}')")
    Connection.commit()

def edit():
    ...# update

def remove():
    genre_name = input("enter genre name: ")
    my_cursor.execute(f"DELETE FROM genres WHERE Name = '{genre_name}'")
    Connection.commit()

load_database()
while True:
    show_menu()
    choice = int(input())

    if choice == 1:
        show_list()
    elif choice == 2:
        add_new()
    elif choice == 3:
        edit()
    elif choice == 4:
        remove()
    elif choice == 5:
        exit(0)