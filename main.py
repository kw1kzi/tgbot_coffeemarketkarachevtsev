import telebot
from telebot import types

bot = telebot.TeleBot("6884576060:AAEHR_Oqb9fYA54UL5wakbyeZxY4tJASjPo")

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    key_cost = types.InlineKeyboardButton(text='Цены на Кофе', callback_data='cost_coffee')
    keyboard.add(key_cost)
    key_menu = types.InlineKeyboardButton(text='Ассортимент', callback_data='menu')
    keyboard.add(key_menu)

    bot.send_message(message.chat.id,'Здравствуйте! Вас приветсвует Телеграм Бот Кофейня It Top, тут вы можете узнать асортимент и цены на кофе', reply_markup=keyboard)

bot.polling(none_stop=True)