import dp as dp
import telebot
from aiogram.utils import emoji
from telebot import types
from aiogram.dispatcher.filters import *
import datetime
import schedule, time

full_amount = 0
bot = telebot.TeleBot('1769484585:AAFg4pmZT9y1JJY3y0wVgpsqkfmjrm2nJZA')


def TypeOfTransport():
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    key1 = types.KeyboardButton('Троллейбус ' + emoji.emojize(":trolleybus:"))
    key2 = types.KeyboardButton('Автобус ' + emoji.emojize(":bus:"))
    key3 = types.KeyboardButton('Маршрутка ' + emoji.emojize(":minibus:"))
    key4 = types.KeyboardButton('Статистика ' + emoji.emojize(":bar_chart:"))
    markup.add(key1)
    markup.add(key2)
    markup.add(key3)
    markup.add(key4)
    return markup


def FromStats():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    stat = types.KeyboardButton('Вернуться в главное меню ' + emoji.emojize(":leftwards_arrow_with_hook:"))
    sbros = types.KeyboardButton('Сбросить статистику ' + emoji.emojize(":repeat:"))
    markup.add(stat, sbros)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     'Привет, бот создан для учёта расходов на транспорт.\nНиже выберите вид транспорта ' + emoji.emojize(
                         ":bus:") + emoji.emojize(":trolleybus:") + emoji.emojize(":minibus:"),
                     reply_markup=TypeOfTransport())


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global full_amount
    if call.data == "Troll1":
        full_amount += 26
        bot.send_message(call.message.chat.id, f"Всего потрачено {full_amount} руб.",
                         reply_markup=TypeOfTransport())
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Записан проезд наличными", reply_markup=None)
    elif call.data == "Troll2":
        full_amount += 22
        bot.send_message(call.message.chat.id, f"Всего потрачено {full_amount} руб.",
                         reply_markup=TypeOfTransport())
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Записан проезд по карте", reply_markup=None)

    elif call.data == "Auto1":
        full_amount += 27
        bot.send_message(call.message.chat.id, f"Всего потрачено {full_amount} руб.",
                         reply_markup=TypeOfTransport())
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Записан проезд наличными", reply_markup=None)
    elif call.data == "Auto2":
        full_amount += 23
        bot.send_message(call.message.chat.id, f"Всего потрачено {full_amount} руб.",
                         reply_markup=TypeOfTransport())
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Записан проезд по карте", reply_markup=None)

    elif call.data == "Marsh1":
        full_amount += 27
        bot.send_message(call.message.chat.id, f"Всего потрачено {full_amount} руб.",
                         reply_markup=TypeOfTransport())
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Записан проезд наличными", reply_markup=None)
    elif call.data == "Marsh2":
        full_amount += 23
        bot.send_message(call.message.chat.id, f"Всего потрачено {full_amount} руб.",
                         reply_markup=TypeOfTransport())
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Записан проезд по карте", reply_markup=None)


@bot.message_handler(content_types=['text'])
def cont(message):
    if message.text == 'Троллейбус ' + emoji.emojize(":trolleybus:"):
        InlineTroll = types.InlineKeyboardMarkup(row_width=2)
        Troll1 = types.InlineKeyboardButton("Наличными " + emoji.emojize(":dollar:"), callback_data='Troll1', )
        Troll2 = types.InlineKeyboardButton("По карте " + emoji.emojize(":credit_card:"), callback_data='Troll2')
        InlineTroll.add(Troll1, Troll2)
        bot.send_message(message.chat.id, "Вид оплаты проезда в троллейбусе:", reply_markup=InlineTroll)

    elif message.text == 'Автобус ' + emoji.emojize(":bus:"):
        InlineTroll = types.InlineKeyboardMarkup(row_width=2)
        Auto1 = types.InlineKeyboardButton("Наличными " + emoji.emojize(":dollar:"), callback_data='Auto1', )
        Auto2 = types.InlineKeyboardButton("По карте " + emoji.emojize(":credit_card:"), callback_data='Auto2')
        InlineTroll.add(Auto1, Auto2)
        bot.send_message(message.chat.id, "Вид оплаты проезда в автобусе:", reply_markup=InlineTroll)

    elif message.text == 'Маршрутка ' + emoji.emojize(":minibus:"):
        InlineTroll = types.InlineKeyboardMarkup(row_width=2)
        Marsh1 = types.InlineKeyboardButton("Наличными " + emoji.emojize(":dollar:"), callback_data='Marsh1', )
        Marsh2 = types.InlineKeyboardButton("По карте " + emoji.emojize(":credit_card:"), callback_data='Marsh2')
        InlineTroll.add(Marsh1, Marsh2)
        bot.send_message(message.chat.id, "Вид оплаты проезда в маршрутке:", reply_markup=InlineTroll)

    elif message.text == 'Статистика ' + emoji.emojize(":bar_chart:"):
        global full_amount
        bot.send_message(message.chat.id, f"Всего потрачено {full_amount} руб. с последнего сброса",
                         reply_markup=FromStats())

    elif message.text == "Вернуться в главное меню":
        bot.send_message(message.chat.id, "Выберите нужный вид транспорта:", reply_markup=TypeOfTransport())
    elif message.text == 'Сбросить статистику ' + emoji.emojize(":repeat:"):
        bot.send_message(message.chat.id, "Вы успешно сбросили статистику" + emoji.emojize(":white_check_mark:"),
                         reply_markup=TypeOfTransport())
        full_amount = 0


bot.polling()
