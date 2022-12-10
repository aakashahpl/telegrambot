
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update
from telegram.ext.updater import Updater
import pywhatkit as pwk
import datetime
import sqlite3

#define connection and cursor
connection=sqlite3.connect('caesarisdeadbot.db ',check_same_thread=False)
cursor=connection.cursor()


cursor.execute(
    """ CREATE TABLE IF NOT EXISTS MESSTT
    (WEEKDAY INTEGER PRIMARY KEY,BREAKFAST TEXT , LUNCH TEXT , SNACKS TEXT,DINNER TEXT)""")

# ROWS
cursor.execute("insert into messtt values(1,'pongal vada white peas masala chapati','methi chapati veg topiyaza curry panchratna dal cabbage baigan aloo sabji','Pav bhaji sweet bun','atta paratha channa masala vegetable idly hara moong dal aloo jeera dry fish gravy')")
cursor.execute("insert into messtt values(2,'Poori Potato masala Wheat upma','Chapati Meal maker curry Bahara pulao Variety rice Dal Fry Curd Rice','Bonda/Keerai Vada','Panjabi Paratha White Khorma Steamed rice Dal Makani Sambar Mutton gravy')")
cursor.execute("insert into messtt values(3,'Dosa Sambar Poha Omelete','Poori Aloo Kara curry Veg pulao','Veg puff/Sweet puff','Chapati Dal tadka Butter chicken Paneer Masala')")
cursor.execute("insert into messtt values(6,'Veg Semiya Chapati Aloo Rajma','Mint chapathi White Khorma Onion pulao Dal fry Kadi pokoda Aloo gobi masala','Bajji','Madras Paratha Mattar Paneer Masala, Dal tadka Sambar Dosa Mutton gravy')")
cursor.execute("insert into messtt values(5,'Chapati Chole Dal Aloo Masala','Sweet Chapati Aloo mattar masala Maisoore Dal Veg biryani Curd rice','Cake/Fruit cake','Chapati Veg manchurian Veg Fried rice/Noodles Dal Maharani')")
cursor.execute("insert into messtt values(4,'Chapati Veg Khorma Idiyappam Boiled Egg','Poori White peas curry Aloo Bindi Bahara Pulao/Steamed rice Kootu','Kara Sev','Panjabi Paratha Aloo Capsicum Sabji Rajma curry Masala Dal, Idly ')")
cursor.execute("insert into messtt values(7,'Chole Bhature :)','Chicken/Paneer :)','Samosa/Aloo Bonda','Aloo Paratha Aloo gobi curry Karakozhambu Ice cream')")




from datetime import date
index = date.weekday(date.today())




token = ""

updater = Updater(token,
				  use_context=True)
dpc = updater.dispatcher



	


def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
		
	mess - for today's mess menu
	
	
	""")

def start(update: Update, context: CallbackContext):
	update.message.reply_text("Welcome ")
	update.message.reply_text("/help for more info")
	


def gmail_url(update: Update, context: CallbackContext):
	update.message.reply_text(
			"Your gmail link here (I am not\
		giving mine one for security reasons)")


def youtube_url(update: Update, context: CallbackContext):
	update.message.reply_text("Youtube Link =>\
	https://www.youtube.com/")


def linkedIn_url(update: Update, context: CallbackContext):
	update.message.reply_text(
			"LinkedIn URL =>Your Linkedin URL \
		")



def text(update: Update, context: CallbackContext):
	day=int(date.isoweekday(date.today()))

	cursor.execute("Select * from messtt where weekday = ?",[day])
	result=cursor.fetchone()
	if ((update.message.text).lower() == 'mess'):
		
		update.message.reply_text('BREAKFAST:--')
		update.message.reply_text(result[1])
		update.message.reply_text('LUNCH:--')
		update.message.reply_text(result[2])
		update.message.reply_text('SNACKS:--')
		update.message.reply_text(result[3])
		update.message.reply_text('DINNER:--')
		update.message.reply_text(result[4])
	elif ((update.message.text).lower() == 'breakfast'):
		update.message.reply_text('BREAKFAST:--')
		update.message.reply_text(result[1])
	elif ((update.message.text).lower() == 'lunch'):
		update.message.reply_text('LUNCH:--')
		update.message.reply_text(result[2])
	elif ((update.message.text).lower() == 'snacks'):
		update.message.reply_text('SNACKS:--')
		update.message.reply_text(result[3])
	elif ((update.message.text).lower() == 'dinner'):
		update.message.reply_text('DINNER:--')
		update.message.reply_text(result[4])
	  
	elif (update.message.text).lower() in ('hello', 'hi', 'sup'):
		update.message.reply_text("Hi how it's going?")
	elif (update.message.text).lower() in ('good','great','ok',):
		update.message.reply_text("Great")	
	

def unknown_text(update:Update ,context: CallbackContext):
	update.message.reply_text("Unknown Command")
	

def insta(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Instagram : Your insta URL ")


dpc.add_handler(CommandHandler('start', start))

dpc.add_handler(CommandHandler('youtube', youtube_url))

dpc.add_handler(CommandHandler('help', help))

dpc.add_handler(CommandHandler('linkedin', linkedIn_url))

dpc.add_handler(CommandHandler('gmail', gmail_url))

dpc.add_handler(CommandHandler('instagram', insta))

dpc.add_handler(MessageHandler(Filters.command, unknown_text))        # Filters out unknown commands


dpc.add_handler(MessageHandler(Filters.text, text))                  #To manage messages.

updater.start_polling()

