import random

words = ["TREE", "BOOK", "BLUE", "TRAIN", "FISH", "WOMAN", "LIVE","SARA","HASAN","OMID","AMIR","AMIN"]
true = []
false = 0
x = 0

y = random.randint(0, len(words) - 1)
word = words[y]

while false <= 6:
    for i in range(len(word)):
        if word[i] in true:
            print(word[i], end = " ")

        else:
            print("-", end= " ")

        if len(true) == len(word):
            print("you win!!!!")
            exit()

    user = input()
    user1 = user.upper()

    if user1 in word:
        true.append(user1)
        print("true")

    for i in range(len(word)):
        if word[i] in true:
            print("")
            break
        else:
            print("false!!!")
            false = false + 1
            print(false)
            break

        if user1 == word:
            print("you win!!!!!")
            exit()
    
print("game over")
print(word)