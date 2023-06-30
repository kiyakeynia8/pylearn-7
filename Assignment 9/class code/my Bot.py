import telebot
import random
from telebot import types
import qrcode

bot = telebot.TeleBot("5898456857:AAF6in2_CslOr-oKXHEGx56f9rIPjedHRx0", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def fname(message):
	welcome = ( "سلام "+ message.from_user.first_name+" به ربات من خوش امدی:) ")
	bot.send_message(message.chat.id,welcome)

@bot.message_handler(commands=['game'])
def game(message):
	computer = random.randint(1, 50)
	bot.send_message(message.chat.id,"enter your number: ")
	@bot.message_handler(func=lambda message: True)
	def echo_all(message):
		if computer == int(message.text):
			bot.send_message(message.chat.id, "you win")
		elif computer > int(message.text):
			bot.send_message(message.chat.id, "Go Up")
		elif computer < int(message.text):
			bot.send_message(message.chat.id, "Come down")

@bot.message_handler(commands=['QRcode'])
def QRcode(message):
	bot.send_message(message.chat.id, "enter your text")
	@bot.message_handler(func=lambda message: True)
	def txt(message):
		Q = qrcode.make(message.text)
		Q.save("name.png")
		bot.send_photo(message.chat.id,Q)

@bot.message_handler(commands=['max'])
def max(message):
	markup = types.ReplyKeyboardMarkup(row_width=2)
	itembtn1 = types.KeyboardButton('next number')
	itembtn2 = types.KeyboardButton('finish')
	markup.add(itembtn1, itembtn2,)
	bot.send_message(message.chat.id, "enter one item:", reply_markup = markup)


bot.infinity_polling()