import re
import telebot

bot = telebot.TeleBot("5969848738:AAExP_zWgVn2w_TViuc9giRMHaUhKlrCqik")


@bot.message_handler(content_types=['document'])
def GetDoc(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        if message.document.file_name == 'phonebook.html' or message.document.file_name == 'phonebook.txt':
            src = 'D:/учеба/Python/PythonHomeWork/lesson9/справочник/file/' + message.document.file_name;
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message, "Справочник обновлен если уверены что хотите загрузить нажмите экспортировать")
        else:
            bot.reply_to(message, "Выбери другой файл")
    except Exception as e:
        bot.reply_to(message, e)


def ConvertToHTML(phoneBook):
    f = open('phonebook.html', 'w+', encoding="utf-8")
    f.write('<table><tr><th>Фамилия</th><th>Имя</th><th>Отчество</th><th>Телефон</th><th>Должность</th></tr>\n')
    for i in range(0, len(phoneBook)):
        f.write('<tr>')
        for j in range(5):
            f.write('<td> ')
            f.write(phoneBook[i][j])
            f.write('</td>')
        f.write('</tr>\n')
    f.write('</table>')
    f.close()
    print('справочник импортирован в HTML')


def ConvertToTXT(phoneBook):
    f = open('phonebook.txt', 'w+', encoding="utf-8")
    f.write('Фамилия;Имя;Отчество;Телефон;Должность')
    for i in range(0, len(phoneBook)):
        f.write('\n')
        for j in range(5):
            f.write(phoneBook[i][j])
            if j != 4:
                f.write(';')
    f.close()
    print('справочник импортирован в TXT')


def PrintPhoneBook(phoneBook):
    a = ''
    for i in range(0, len(phoneBook)):
        a += '\n№ ' + str(int(i + 1)) + ' '
        for j in range(5):
            a += (phoneBook[i][j]) + ' '
    return a


def SortPhonBook(phoneBook, n):
    phoneBook.sort(key=lambda x: (x[n]))
    PrintPhoneBook(phoneBook)


def ConvertTxtToList(message):
    f = open('file/phonebook.txt', 'r', encoding="utf-8")
    a = f.readlines()
    phone = []
    for i in range(1, len(a)):
        b = (re.split(";", a[i].replace("\n", "")))
        phone.append(b)
    bot.send_message(chat_id=message.chat.id, text=f'данные обновленны')
    return phone


def ConvertHtmlToList(message):
    f = open('file/phonebook.html', 'r', encoding="utf-8")
    a = f.readlines()
    a.pop(0)
    a.pop(-1)
    phone = []
    for i in range(0, len(a)):
        b = re.split("</td><td> ", a[i].replace('<tr><td> ', '').replace('</td></tr>\n', ""))
        phone.append(b)
    bot.send_message(chat_id=message.chat.id, text=f'данные обновленны')
    return phone


def FindEmployee(message, phoneBook, name, n):
    name = message.text
    find = list(list(filter(lambda x: (name.lower() in x[n].lower()), phoneBook)))
    result = f'по данному критерию нашлось записей - {len(find)}\n\n'
    for i in range(len(find)):
        for j in range(5):
            result += find[i][j] + ' '
        result += '\n'
    result += '\nдля возврата в главное меню нажми /start'
    bot.send_message(chat_id=message.chat.id, text=result)


def AddNewEmployeeSurname(message, phoneBook):
    lastName = message.text.split()[0]
    firstName = message.text.split()[1]
    patronymic = message.text.split()[2]
    phoneNumber = message.text.split()[3]
    post = message.text.split()[4]
    phoneBook.append([lastName, firstName, patronymic, phoneNumber, post])
    bot.send_message(chat_id=message.chat.id, text='Запись добавлена')


def DeleteFromPhoneBook(message, phoneBook):
    num = int(message.text) - 1
    phoneBook.pop(num)
    bot.send_message(chat_id=message.chat.id, text='Запись удалена')


def CreatePhoneList():
    phoneBook = [['Коваленко', 'Наталья', 'Николаевна', '1234', 'начальник бюро'],
                 ['Иванов', 'Александр', 'Иванович', '1234', 'программист'],
                 ['Матвейчук', 'Иван', 'Леонидович', '1111', 'зам ген директора'],
                 ['Дубровина', 'Галина', 'Николаевна', '1235', 'глав бух'],
                 ['Матвейчук', 'Инна', 'Артуровна', '1235', 'директор']]
    phoneBook.sort(key=lambda x: (x[0], x[1], x[2]))
    return phoneBook
