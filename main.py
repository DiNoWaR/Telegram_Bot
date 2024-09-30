import os

import telebot

bot = telebot.TeleBot(token=os.environ['TELEGRAM_BOT_TOKEN'])


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Hello Denis')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


bot.polling(non_stop=True)