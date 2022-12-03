import telebot
from telebot import types  # для указание типов
import random

user_dict = {}
user_name_dict = {}
listStep = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def new_game():
    user_dict.clear()
    user_name_dict.clear()
    listStep = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return listStep


bot = telebot.TeleBot("5969848738:AAExP_zWgVn2w_TViuc9giRMHaUhKlrCqik")


def count(listField):
    k = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if (listField[i][j] == 'x') or (listField[i][j] == '0'):
                k += 1
    return k


def Check(listField):
    win = False
    if (listField[0][0] == listField[1][1] == listField[2][2] or listField[0][2] == listField[1][1] == listField[2][
        0]) and listField[1][1] != ' ':
        win = True

    for i in range(3):
        if (listField[i][0] == listField[i][1] == listField[i][2] and listField[i][0] != ' ') or (
                listField[0][i] == listField[1][i] == listField[2][i] and listField[2][i] != ' '):
            win = True

    return win


@bot.message_handler(commands=['set'])
def set(message):
    command = types.BotCommand("start", "Старт")
    bot.set_my_commands([command], scope=types.BotCommandScopeAllGroupChats)


@bot.message_handler(commands=['start', 'reg'])
def start_game(message):
    if 1 in user_dict:
        bot.reply_to(message, 'регистрация завершена игра началась')
    else:
        if 0 in user_dict:
            if message.from_user.id != user_dict[0]:
                user_dict[1] = message.from_user.id
                user_name_dict[2] = message.from_user.first_name
                bot.reply_to(message, f'{message.from_user.first_name} присоеденился, игра началась')
                movePlayers = random.randint(0, 1)
                if movePlayers == 0:
                    user_name_dict[1], user_name_dict[2] = user_name_dict[2], user_name_dict[1]
                    user_dict[0], user_dict[1] = user_dict[1], user_dict[0]
                start(message)
            else:
                bot.reply_to(message, f'{message.from_user.first_name} ты уже в игре')
        else:
            user_dict[0] = message.from_user.id
            user_name_dict[1] = message.from_user.first_name
            bot.reply_to(message, f"{message.from_user.first_name} создал игру, нужен еще 1 игрок нажми /start")


def start(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    button1 = types.InlineKeyboardButton(listStep[0][0], callback_data='0')
    button2 = types.InlineKeyboardButton(listStep[0][1], callback_data='1')
    button3 = types.InlineKeyboardButton(listStep[0][2], callback_data='2')
    button4 = types.InlineKeyboardButton(listStep[1][0], callback_data='3')
    button5 = types.InlineKeyboardButton(listStep[1][1], callback_data='4')
    button6 = types.InlineKeyboardButton(listStep[1][2], callback_data='5')
    button7 = types.InlineKeyboardButton(listStep[2][0], callback_data='6')
    button8 = types.InlineKeyboardButton(listStep[2][1], callback_data='7')
    button9 = types.InlineKeyboardButton(listStep[2][2], callback_data='8')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
    k = count(listStep)
    if not Check(listStep):
        if k == 0:
            bot.send_message(message.chat.id, f"ходит игрок {user_name_dict[1]}", reply_markup=markup)
        elif k % 2 == 0:
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                  text=f"ходит игрок {user_name_dict[1]}",
                                  reply_markup=markup)
        else:
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                  text=f"ходит игрок {user_name_dict[2]}",
                                  reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        i = count(listStep)
        if call.data == '0':
            win(i, call)
        elif call.data == '1':
            win(i, call)
        elif call.data == '2':
            win(i, call)
        elif call.data == '3':
            win(i, call)
        elif call.data == '4':
            win(i, call)
        elif call.data == '5':
            win(i, call)
        elif call.data == '6':
            win(i, call)
        elif call.data == '7':
            win(i, call)
        elif call.data == '8':
            win(i, call)


def win(i, call):
    global listStep
    row = int(int(call.data) / 3)
    col = int(int(call.data) % 3)
    if call.from_user.id != user_dict[i % 2]:
        bot.answer_callback_query(callback_query_id=call.id, text="Не ты ходишь")
        return
    if call.from_user.id == user_dict[i % 2]:
        if listStep[row][col] == ' ':
            if i % 2 == 0:
                listStep[row][col] = 'x'
            else:
                listStep[row][col] = '0'
            if Check(listStep):

                if i % 2 == 0:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=f'победил {user_name_dict[1]}')
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=f'победил {user_name_dict[2]}')
                listStep = new_game()
            elif i == 8:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='ничья!')
                listStep = new_game()
    if len(user_dict.keys()) > 0:
        start(call.message)


bot.infinity_polling()
