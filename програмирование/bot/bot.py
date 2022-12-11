import telebot

bot = telebot.TeleBot("5954980610:AAGiHkHZ3_mBHMTSz5Kd5Z6Sys1-B3-gvBg")
owner_id = 1109954939


@bot.message_handler(commands=['privet'])
def send_welcome(message):
	bot.reply_to(message, "Привет!")
    

        
bot.infinity_polling()