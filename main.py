import os
import webbrowser

import telebot
from telebot import types

bot = telebot.TeleBot(token=os.environ['TELEGRAM_BOT_TOKEN'])


@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open_new_tab('https://www.google.com')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    google_btn = types.KeyboardButton('Go to site')
    markup.row(google_btn)
    delete_btn = types.KeyboardButton('Delete')
    edit_btn = types.KeyboardButton('Edit')
    markup.row(delete_btn, edit_btn)
    bot.send_message(message.chat.id, 'Hello Denis', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(chat_id=callback.message.chat_id, message_id=callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', message_id=callback.message.message_id)


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


bot.polling(non_stop=True)
