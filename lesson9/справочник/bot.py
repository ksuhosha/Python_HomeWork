import telebot
from telebot import types  # для указание типов
import model

n = None
name = ''
phoneBook = model.CreatePhoneList()
bot = telebot.TeleBot("5969848738:AAExP_zWgVn2w_TViuc9giRMHaUhKlrCqik")


@bot.message_handler(commands=['start', 'reg'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton('просмотреть', callback_data='0')
    button2 = types.InlineKeyboardButton('поиск номера телефона', callback_data='1')
    button3 = types.InlineKeyboardButton('добавить запись', callback_data='2')
    button4 = types.InlineKeyboardButton('удалить запись', callback_data='3')
    button5 = types.InlineKeyboardButton('импортировать в txt', callback_data='4')
    button6 = types.InlineKeyboardButton('экспортировать в txt', callback_data='41')
    button7 = types.InlineKeyboardButton('импортировать в HTML', callback_data='5')
    button8 = types.InlineKeyboardButton('экспортировать в HTML', callback_data='51')
    button9 = types.InlineKeyboardButton('сортировка', callback_data='6')
    button10 = types.InlineKeyboardButton('загрузка справочника', callback_data='61')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    bot.send_message(message.chat.id, f"Меню", reply_markup=markup)


def FindMenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('Фамилия', callback_data='7')
    btn2 = types.InlineKeyboardButton("Имя", callback_data='8')
    btn3 = types.InlineKeyboardButton("Отчество", callback_data='9')
    btn4 = types.InlineKeyboardButton("Должность", callback_data='10')
    markup.add(btn1, btn2, btn3, btn4)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                          text=f"выберите по какому полю будем искать", reply_markup=markup)


def SortMenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('Фамилии', callback_data='11')
    btn2 = types.InlineKeyboardButton("Имени", callback_data='12')
    btn3 = types.InlineKeyboardButton("Отчеству", callback_data='13')
    btn4 = types.InlineKeyboardButton("Телефону", callback_data='14')
    btn5 = types.InlineKeyboardButton("Должности", callback_data='15')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                          text=f"выберите по какому полю будем искать", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global n, phoneBook
    if call.message:
        if call.data == '0':
            bot.send_message(chat_id=call.message.chat.id, text=model.PrintPhoneBook(phoneBook))
            # start(call.message)
        elif call.data == '1':
            FindMenu(call.message)
        elif call.data == '2':
            print('добавить запись ')
            msg = bot.send_message(chat_id=call.message.chat.id, text=f'Введи ФИО номер и должность')
            bot.register_next_step_handler(msg, model.AddNewEmployeeSurname, phoneBook)
        elif call.data == '3':
            print('удалить запись')
            msg = bot.send_message(chat_id=call.message.chat.id, text=f'Введи номер позиции которую удалить')
            bot.register_next_step_handler(msg, model.DeleteFromPhoneBook,phoneBook)
        elif call.data == '4':
            print('импортировать в txt')
            data = open('phonebook.txt', encoding='utf-8')
            bot.send_document(call.message.chat.id, data)
            data.close()
        elif call.data == '41':
            print('экспортировать в txt')
            phoneBook = model.ConvertTxtToList(call.message)
        elif call.data == '5':
            print('импортировать в HTML')
            data = open('phonebook.html', encoding='utf-8')
            bot.send_document(call.message.chat.id, data)
            data.close()
        elif call.data == '51':
            print('экспортировать в HTML')
            phoneBook = model.ConvertHtmlToList(call.message)
        elif call.data == '6':
            print('сортировка')
            SortMenu(call.message)
        elif call.data == '61':
            print('загрузка')
            msg = bot.send_message(chat_id=call.message.chat.id,
                                   text=f'загрузите файл phonebook.html или phonebook.txt')
            bot.register_next_step_handler(msg, model.GetDoc)

        # меню поиска телефоного номера
        elif call.data == '7':
            msg = bot.send_message(chat_id=call.message.chat.id, text=f'Введи фамилию')
            n = 0
            bot.register_next_step_handler(msg, model.FindEmployee, phoneBook, name, n)
        elif call.data == '8':
            msg = bot.send_message(chat_id=call.message.chat.id, text=f'Введи имя')
            n = 1
            bot.register_next_step_handler(msg, model.FindEmployee, phoneBook, name, n)
        elif call.data == '9':
            msg = bot.send_message(chat_id=call.message.chat.id, text='Введи отчество')
            n = 2
            bot.register_next_step_handler(msg, model.FindEmployee, phoneBook, name, n)
        elif call.data == '10':
            msg = bot.send_message(chat_id=call.message.chat.id, text='Введи должность')
            n = 4
            bot.register_next_step_handler(msg, model.FindEmployee, phoneBook, name, n)
        # меню сортировки по полю
        elif call.data == '11':
            n = 0
            model.SortPhonBook(phoneBook, n)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f'сортировка по фамилии \n{model.PrintPhoneBook(phoneBook)} \n\nдля возврата в главное меню нажми /start')
        elif call.data == '12':
            n = 1
            model.SortPhonBook(phoneBook, n)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f'сортировка по имени \n{model.PrintPhoneBook(phoneBook)} \n\nдля возврата в главное меню нажми /start')
        elif call.data == '13':
            n = 2
            model.SortPhonBook(phoneBook, n)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f'сортировка по отчеству \n{model.PrintPhoneBook(phoneBook)} \n\nдля возврата в главное меню нажми /start')
        elif call.data == '14':
            n = 3
            model.SortPhonBook(phoneBook, n)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f'сортировка по телефону \n{model.PrintPhoneBook(phoneBook)} \n\nдля возврата в главное меню нажми /start')
        elif call.data == '15':
            n = 4
            model.SortPhonBook(phoneBook, n)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f'сортировка по должности \n{model.PrintPhoneBook(phoneBook)} \n\nдля возврата в главное меню нажми /start')





def PrintPhoneBook(phonebook, call, markup):
    a = ''
    for i in range(0, len(phonebook)):
        a += f'\n№ {i + 1} '
        for j in range(5):
            a += (phonebook[i][j])
    bot.send_message(chat_id=call.message.chat.id, text=f'{a}', reply_markup=markup)


bot.infinity_polling()
