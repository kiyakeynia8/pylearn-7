import telebot
import random
from telebot import types
import qrcode
import gtts
import datetime
from khayyam import JalaliDate, JalaliDatetime

bot = telebot.TeleBot("5898456857:AAF6in2_CslOr-oKXHEGx56f9rIPjedHRx0", parse_mode=None)

@bot.message_handler(commands=['start'])
def fname(message):
	welcome = ( "سلام "+ message.from_user.first_name+" به ربات من خوش امدی:) ")
	bot.send_message(message.chat.id,welcome)

@bot.message_handler(commands=['help'])
def fname(message):
	bot.send_message(message.chat.id,"/game --> بازی اعداد. یک عدد وارد کن 1,50")
	bot.send_message(message.chat.id,"/QRcode --> متن رو وارد کن تا QRcode ساخته شود")
	bot.send_message(message.chat.id,"/voice --> یک متن وارد کن (EN) تا به صورت ویس برات ارسال بشه")
	bot.send_message(message.chat.id,"/max --> لیستی از اعداد وارد کن تا بزرگترین عدد ان را نمایش دهد")
	bot.send_message(message.chat.id,"/argmax --> لیستی از اعداد وارد کن تا برات خونه بزرگترین عدد رو بفرستم")
	bot.send_message(message.chat.id,"/age --> ناریخ تولدت رو وارد کن تا سن دقیقت رو بگم")


@bot.message_handler(commands=['game','new_game'])
def game(message):
	markup = types.ReplyKeyboardMarkup(row_width=1)
	itembtn1 = types.KeyboardButton('/new_game')
	markup.add(itembtn1)
	bot.send_message(message.chat.id,"...", reply_markup = markup)
	computer = random.randint(1, 50)
	bot.send_message(message.chat.id,"enter your number: ")
	@bot.message_handler(func=lambda message: True)
	def egame(message):
		print(message)
		if computer == int(message.text):
			bot.send_message(message.chat.id, "you win")
		elif computer > int(message.text):
			bot.send_message(message.chat.id, "Go Up")
		elif computer < int(message.text):
			bot.send_message(message.chat.id, "Come down")

@bot.message_handler(commands=['QRcode'])
def QRcode(message):
	sendmessage = bot.send_message(message.chat.id, "enter your text")
	bot.register_next_step_handler(sendmessage, txt)

def txt(message):
	print(message)
	str = message.text
	Q = qrcode.make(str)
	Q.save("name.png")
	Q = open("name.png","rb")
	bot.send_photo(message.chat.id,Q)

@bot.message_handler(commands=['voice'])
def voice(message):
	sendmessage = bot.send_message(message.chat.id, "enter your text")
	bot.register_next_step_handler(sendmessage, evoice)

def evoice(message):
	print(message)
	voice = gtts.gTTS(message.text,lang="en",slow = False)
	voice.save("voice.mp3")
	bot.send_voice(message.chat.id,open("voice.mp3","rb"))

@bot.message_handler(commands=['max'])
def max(message):
	sendmessage = bot.send_message(message.chat.id, "enter your numbers --> 1,3,65,47,21,9...")
	bot.register_next_step_handler(sendmessage, numbers)

def numbers(message):
	print(message)
	number = (str(message.text)).split(",")
	a = 0
	for i in range(len(number)):
		n = number[i]
		n = int(n)
		if n > a:
			a = int(number[i])
	bot.send_message(message.chat.id, a)

@bot.message_handler(commands=['argmax'])
def argmax(message):
	sendmessage = bot.send_message(message.chat.id, "enter your numbers --> 1,3,65,47,21,9...")
	bot.register_next_step_handler(sendmessage, anumbers)

def anumbers(message):
	print(message)
	number = (str(message.text)).split(",")
	a = 0
	l = 0
	for i in range(len(number)):
		n = number[i]
		n = int(n)
		if n > a:
			a = int(number[i])
			l = i
	bot.send_message(message.chat.id, l+1)

@bot.message_handler(commands=['age'])
def age(message):
	sendmessage = bot.send_message(message.chat.id, "enter your berthday --> 1400/5/6")
	bot.register_next_step_handler(sendmessage, uage)
  
def uage(message):
	print(message)
	berthday = (str(message.text)).split("/")
	time = JalaliDatetime.now() - JalaliDatetime(berthday[0],berthday[1],berthday[2])
	year = time.days // 365
	month = (time.days % 365) // 30
	day = ((time.days % 365) % 30) - 7	
	bot.send_message(message.chat.id, "شما" + str(year) + "سال و "+ str(month) + " ماه و "+ str(day) + " روز سن دارید ." )

bot.infinity_polling()