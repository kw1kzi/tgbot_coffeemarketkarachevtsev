import telebot
from telebot import types

bot = telebot.TeleBot("6884576060:AAEHR_Oqb9fYA54UL5wakbyeZxY4tJASjPo")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,'Здравствуйте! Вас приветсвует Телеграм Бот Кофейня It Top, тут вы можете узнать асортимент и цены на кофе\n /help \n /cost \n /menu' )

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Вот все команды: \n /help - Все команды которые есть🧐 \n /start - Начало Пути! \n /cost - Вычислитель стоимости🔢 \n /menu - Ассортимент Магазина☕️")

@bot.message_handler(commands=["cost"])
def first_button(message):
        keyboard2 = types.InlineKeyboardMarkup()
        first_mil = types.InlineKeyboardButton(text='0.25', callback_data='0,25_coffee')
        keyboard2.add(first_mil)
        second_mil = types.InlineKeyboardButton(text='0.35', callback_data='0.35_coffee')
        keyboard2.add(second_mil)
        third_mil = types.InlineKeyboardButton(text='0.45', callback_data='0.45_coffee')
        keyboard2.add(third_mil)
        bot.send_message(message.chat.id,'Для того чтобы вычислить цену кофе надо выбрать объем в мл!)', reply_markup=keyboard2)

@bot.callback_query_handler(func=lambda callback: callback.data)
def second_button(callback):
    if callback.data == "0,25_coffee":
        keyboard3 = types.InlineKeyboardMarkup()
        first_coffee25 = types.InlineKeyboardButton(text='ЭКСПРЕССО ДВОЙНОЙ', callback_data='millitrs_1_25_coffee')
        keyboard3.add(first_coffee25)
        second_coffee25 = types.InlineKeyboardButton(text='ФЛЭТ УАЙТ', callback_data='millitrs_2_25_coffee')
        keyboard3.add(second_coffee25)
        third_coffee25 = types.InlineKeyboardButton(text='АМЕРИКАНО', callback_data='millitrs_3_25_coffee')
        keyboard3.add(third_coffee25)
        fourth_coffee25 = types.InlineKeyboardButton(text='КАПУЧИНО', callback_data='millitrs_4_25_coffee')
        keyboard3.add(fourth_coffee25)
        bot.send_message(callback.message.chat.id,'Выберите Напиток☕',reply_markup=keyboard3)
    elif callback.data == "0.35_coffee":
        keyboard4 = types.InlineKeyboardMarkup()
        first_coffee35 = types.InlineKeyboardButton(text='АМЕРИКАНО', callback_data='millitrs_1_25_coffee')
        keyboard4.add(first_coffee35)
        second_coffee35 = types.InlineKeyboardButton(text='КАПУЧИНО', callback_data='millitrs_2_25_coffee')
        keyboard4.add(second_coffee35)
        third_coffee35 = types.InlineKeyboardButton(text='ЛАТТЕ', callback_data='millitrs_3_25_coffee')
        keyboard4.add(third_coffee35)
        fourth_coffee35 = types.InlineKeyboardButton(text='РАФ', callback_data='millitrs_4_25_coffee')
        keyboard4.add(fourth_coffee35)
        five_coffee35 = types.InlineKeyboardButton(text='ЛАТТЕ СОЛЕНАЯ КАРАМЕЛЬ', callback_data='millitrs_5_25_coffee')
        keyboard4.add(five_coffee35)
        six_coffee35 = types.InlineKeyboardButton(text='КАКАО', callback_data='millitrs_6_25_coffee')
        keyboard4.add(six_coffee35)
        seven_coffee35 = types.InlineKeyboardButton(text='ЧАЙ', callback_data='millitrs_7_25_coffee')
        keyboard4.add(seven_coffee35)
        bot.send_message(callback.message.chat.id, 'Выберите Напиток☕', reply_markup=keyboard4)





bot.polling(none_stop=True)


#stop_propagation()