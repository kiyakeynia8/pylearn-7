import gtts

my_text = "salam"
x = gtts.gTTS(my_text,lang="en",slow = False)

x.save("Assignment 8/class code/my.mp3")