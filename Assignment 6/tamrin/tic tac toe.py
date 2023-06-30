import pyfiglet
import colorama
from colorama import Fore
import time
import random
a = time.time()

def show():
    for satr in game_board:
        for cell in satr:
            if cell=="X":
                print(cell ,end=" ")
            elif cell == "O":
                print(cell ,end=" ")
            else:
                print(cell, end="  ")
        print()

def chek_game():
    for j in range(3):
        if game_board[j][0] == "X" and game_board[j][1] == "X" and game_board[j][2] == "X" or game_board[0][j] == "X" and game_board[1][j] == "X" and game_board[2][j] == "X" or game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X" or game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
            print("player 1 win!")
            b = time.time()
            print(b - a)
            exit()
        if game_board[j][0] == "O" and game_board[j][1] == "O" and game_board[j][2] == "O" or game_board[0][j] == "O" and game_board[1][j] == "O" and game_board[2][j] == "O" or game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O" or game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
            print("player 2 win!")
            b = time.time()
            print(b - a)
            exit()

def player_player():
    
    k = 0
    while True:
        if k == 9:
            print("DRAW")
            b = time.time()
            print(b - a)
            exit()

        print("player 1")
        while True:
            satr = int(input("satr: "))
            soton = int(input("soton: "))

            if 0 <= satr <= 2 and 0 <= soton <= 2: 
                if game_board[satr][soton] == "-":
                    k = k + 1
                    game_board[satr][soton] = "X"
                    break
                else:
                    print("khone por hast")
                    print("dobare emtehan kon")
            else:
                print("beyn 0 ta 2 entkhab kon :/")
        show()
        chek_game()

        if k == 9:
            print("DRAW")
            b = time.time()
            print(b - a)
            exit()

        print("player 2")
        while True:
            satr = int(input("satr: "))
            soton = int(input("soton: "))

            if 0 <= satr <= 2 and 0 <= soton <= 2:
                if game_board[satr][soton] == "-":
                    k = k + 1
                    game_board[satr][soton] = "O"
                    break
                else:
                    print("khone por hast")
                    print("dobare emtehan kon")
            else:
                print("beyn 0 ta 2 entkhab kon :/")

        show()
        chek_game()

def player_CPU():

    l = 0
    while True:
        if l == 9:
            print("DRAW")
            b = time.time()
            print(b - a)
            exit()

        print("player 1")
        while True:
            satr = int(input("satr: "))
            soton = int(input("soton: "))

            if 0 <= satr <= 2 and 0 <= soton <= 2: 
                if game_board[satr][soton] == "-":
                    l = l + 1
                    game_board[satr][soton] = "X"
                    break
                else:
                    print("khone por hast")
                    print("dobare emtehan kon")
            else:
                print("beyn 0 ta 2 entkhab kon :/")
        show()
        chek_game()

        if l == 9:
            print("DRAW")
            b = time.time()
            print(b - a)
            exit()

        print("player 2")
        while True:
            satr = random.randint(0,2)
            soton = random.randint(0,2)

            if game_board[satr][soton] == "-":
                l = l + 1
                game_board[satr][soton] = "O"
                break
            
            else:
                print("khone por hast")
                print("dobare emtehan kon")
    
        show()
        chek_game()


title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)

game_board = [["-","-","-"],
              ["-","-","-"],
              ["-","-","-"]]

show()

game_mod = input("player_player or player_CPU: ")

if game_mod == "player_player":
    player_player()
if game_mod == "player_CPU":
    player_CPU()