#!/usr/bin/env python -*- coding: utf-8 -*-
import telebot
from time import sleep
timer = 0
long = 0
free_time: bool = False
is_stop: bool = False
is_pause = False
TOKEN = 'тут токен'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет!')
    sleep(0.5)
    start_keyboard = telebot.types.InlineKeyboardMarkup()
    start_button = telebot.types.InlineKeyboardButton(text='🔵Start🔵', callback_data='start')
    stop_button = telebot.types.InlineKeyboardButton(text='🔴Stop🔴', callback_data='stop')
    start_keyboard.add(start_button,
                       stop_button,)
    bot.send_message(message.chat.id, '🍅Начнем роботу🍅', reply_markup=start_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def start(call):
    global timer
    global long
    global free_time
    global is_stop
    if call.data == 'start':
        while True or not is_stop:
            if is_stop:
                break
            if long != 5:
                if not free_time:
                    timer = 15
                    work_type = 'Перерыв'
                    free_time = True
                else:
                    timer = 5
                    work_type = 'Работа'
                    free_time = False
            elif long == 5 and free_time:
                timer = 25
                free_time = False

            send_message = f'{work_type} через {timer} минут'

            clock(timer, call.message.chat.id, send_message, work_type)
    elif call.data == 'stop':
        is_stop = True
        bot.send_message(call.message.chat.id, 'Таймер остановлен', reply_markup=telebot.types.ReplyKeyboardRemove())


# @bot.message_handler(content_types=['text'], regexp='🔴Stop🔴')
# def stop(message):
#     global is_stop, is_pause


def clock(timer, chat_id, message,work_type):
    global long
    global is_stop
    mes = bot.send_message(chat_id, message)
    timer *= 60
    while timer != 0:
        if is_stop:
            break
        timer -= 1
        sleep(1)
        if timer/60 in [x for x in range(25)]:
            bot.edit_message_text(chat_id=chat_id, message_id=mes.message_id, text=f'{work_type} через {int(timer/60)} минут')
            # bot.send_message(chat_id, timer)
    long += 1



bot.polling()

