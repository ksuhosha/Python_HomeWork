import telebot
from telebot import types
import logger

bot = telebot.TeleBot("5969848738:AAExP_zWgVn2w_TViuc9giRMHaUhKlrCqik")


# print(f"1: умножение, 2: деление' 3: сложение, 4: вычитание")
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton('умножение', callback_data='*')
    button2 = types.InlineKeyboardButton('деление', callback_data='/')
    button3 = types.InlineKeyboardButton('сложение', callback_data='+')
    button4 = types.InlineKeyboardButton('вычитание', callback_data='-')
    markup.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, f"Доступные действия", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        print('фигня')
        if call.data == '*':
            print('умножение')
            sim = 1
            msg = bot.send_message(chat_id=call.message.chat.id, text='введите первое число')
            bot.register_next_step_handler(msg, EnterNum1, sim)
        elif call.data == '/':
            sim = 2
            msg = bot.send_message(chat_id=call.message.chat.id, text='введите первое число')
            bot.register_next_step_handler(msg, EnterNum1, sim)
        elif call.data == '+':
            sim = 3
            msg = bot.send_message(chat_id=call.message.chat.id, text='введите первое число')
            bot.register_next_step_handler(msg, EnterNum1, sim)
        elif call.data == '-':
            sim = 4
            msg = bot.send_message(chat_id=call.message.chat.id, text='введите первое число')
            bot.register_next_step_handler(msg, EnterNum1, sim)


def Calculations(message, a, b, sim):
    a = float(a)
    b = float(b)
    if sim == 1:
        x = a * b
        bot.send_message(message.chat.id, f'{a} * {b} = {x}')
    elif sim == 2:
        x = a / b
        bot.send_message(message.chat.id, f'{a} / {b} = {x}')
    elif sim == 3:
        x = a + b
        bot.send_message(message.chat.id, f'{a} + {b} = {x}')
    elif sim == 4:
        x = a - b
        bot.send_message(message.chat.id, f'{a} - {b} = {x}')
    logger.Logger(a, b, x, sim)

    return x


@bot.message_handler(content_types=['text'])
def EnterNum1(message, sim):
    num1 = message.text
    print(num1)
    if num1.isdigit():
        msg = bot.send_message(chat_id=message.chat.id, text="первое число принято, введите второе")
        bot.register_next_step_handler(msg, EnterNum2, num1, sim)
    else:
        msg = bot.send_message(chat_id=message.chat.id, text="первое число не принято, введите число! ")
        bot.register_next_step_handler(msg, EnterNum1, sim)


def EnterNum2(message, num1, sim):
    num2 = message.text
    print(num2)
    if num2.isdigit():
        bot.send_message(chat_id=message.chat.id, text="второе число принято")
        Calculations(message, num1, num2, sim)
    else:
        msg = bot.send_message(chat_id=message.chat.id, text="второе число не принято, введите второе")
        bot.register_next_step_handler(msg, EnterNum2, num1, sim)


bot.infinity_polling()
