import gtts

def read_from_file():
    global words_bank

    f = open("C:/Users/home/Desktop/python class/Assignment 8/tamrin/translate/translate.txt","r")

    temp = f.read().split("\n")

    words_bank = []
    for i in range(0,len(temp),2):
        my_dect = {"en": temp[i], "fa": temp[i+1]}
        words_bank.append(my_dect)
    f.close

def english_to_persan():
    user_text = input("enter your english text: ")
    if "." in user_text:
        user_Sentence = user_text.split(".")
        for i in range(len(user_Sentence)): 
            user_words = user_Sentence[i].split(" ")

            output = ""

            for user_word in user_words:
                for word in words_bank:
                    if user_word == word["en"]:
                        output = output + word["fa"] + " "
                        break
                else:
                    output = output + user_word + " "

            print(output)

        text = str(output)
        Voice = gtts.gTTS(text,lang="en",slow = False)
        Voice.save("Assignment 8/tamrin/translate/translate.mp3")
    else:        
        user_words = user_text.split(" ")

        output = ""

        for user_word in user_words:
            for word in words_bank:
                if user_word == word["en"]:
                    output = output + word["fa"] + " "
                    break
            else:
                output = output + user_word + " "

        print(output)
        text = str(output)
        Voice = gtts.gTTS(text,lang="en",slow = False)
        Voice.save("Assignment 8/tamrin/translate/translate.mp3")
        
def persan_to_english():
    user_text = input("enter your persan text: ")
    if "." in user_text:
        user_Sentence = user_text.split(".")
        for i in range(len(user_Sentence)): 
            user_words = user_Sentence[i].split(" ")

            output = ""

            for user_word in user_words:
                for word in words_bank:
                    if user_word == word["fa"]:
                        output = output + word["en"] + " "
                        break
                else:
                    output = output + user_word + " "

            print(output)

        text = str(output)
        Voice = gtts.gTTS(text,lang="en",slow = False)
        Voice.save("Assignment 8/tamrin/translate/translate.mp3")
    else:        
        user_words = user_text.split(" ")

        output = ""

        for user_word in user_words:
            for word in words_bank:
                if user_word == word["fa"]:
                    output = output + word["en"] + " "
                    break
            else:
                output = output + user_word + " "

        print(output)
        text = str(output)
        Voice = gtts.gTTS(text,lang="en",slow = False)
        Voice.save("Assignment 8/tamrin/translate/translate.mp3")

def Add_to_banck():
    en = input("input EN: ")
    per = input("input PER: ")
    new = {"en":en,"fa":per}
    words_bank.append(new)


def show_menu():
    print("welcom to my transslate")

    read_from_file()

    while True:
        print("1 = EN to PER")
        print("2 = PER to EN")
        print("3 = Add to banck")
        print("4 = Exit")
        choice = int(input())
        if choice == 1:
            english_to_persan()
        if choice == 2:
            persan_to_english()
        if choice == 3:
            Add_to_banck()
        if choice == 4:
            f = open("C:/Users/home/Desktop/python class/Assignment 8/tamrin/translate/translate.txt","w")
            for i in range(len(words_bank)):
                n = words_bank[i]
                f.write(n["en"])
                f.write("\n")
                f.write(n["fa"])
                if i == len(words_bank)-1:
                    break
                else:
                    f.write("\n")

            exit(0)


show_menu()


