#!/usr/bin/env python -*- coding: utf-8 -*-
import telebot
import time
timer = 0
long = 0
free_time : bool = False
TOKEN = '1542411934:AAF9DGT929qhbPqW_0DXHVBO3k0WVz9onSY'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет!')
    time.sleep(0.5)
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = telebot.types.KeyboardButton(text='🔵Start🔵')
    stop_button = telebot.types.KeyboardButton(text='🔴Stop🔴')
    keyboard.add(start_button,
                 stop_button,)
    bot.send_message(message.chat.id, '🍅Начнем роботу🍅', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def text(message):
    global timer
    global long
    global free_time
    if message.text == 'Start🔵':
        if long != 5:
            if not free_time:
                timer = 15
        else:
            timer =  
        while timer != 0:

    elif message.text == 'Stop🔵':
        pass

bot.polling()

