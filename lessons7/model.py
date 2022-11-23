import re
import view


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


def AddToPhoneBook(phoneBook):
    for i in range(len(phoneBook), len(phoneBook) + 1):
        for j in range(5):
            if j == 0:
                lastName = input('Введите фамилию: ')
            elif j == 1:
                firstName = input('Введите имя: ')
            elif j == 2:
                patronymic = input('Введите отчество: ')
            elif j == 3:
                phoneNumber = input('Введите телефон: ')
            elif j == 4:
                post = input('Введите должность: ')
        phoneBook.append([lastName, firstName, patronymic, phoneNumber, post])
        print('запись добавлена')


def DeleteFromPhoneBook(phoneBook):
    num = int(input('Введите номер записи которую требуется удалить: ')) - 1
    phoneBook.pop(num)
    print('запись удалена')


def ConvertTxtToList():
    f = open('phonebook.txt', 'r', encoding="utf-8")
    a = f.readlines()
    phone = []
    for i in range(1, len(a)):
        b = (re.split(";", a[i].replace("\n", "")))
        phone.append(b)
    print('справочник Экспортирован из TXT')
    return phone


def ConvertHtmlToList():
    f = open('phonebook.html', 'r', encoding="utf-8")
    a = f.readlines()
    a.pop(0)
    a.pop(-1)
    phone = []
    for i in range(0, len(a)):
        b = re.split("</td><td> ", a[i].replace('<tr><td> ', '').replace('</td></tr>\n', ""))
        phone.append(b)
    print('справочник Экспортирован из HTML')
    return phone


def FindEmployee(phoneBook):
    i = int(input('что будем искать: ')) - 1
    findText = input("Введите текст:")
    if i == 3:
        i = 4
    find = lambda x: (findText.lower() in x[i].lower())
    result = list(list(filter(find, phoneBook)))
    PrintPhoneBook(result)


def StartProgram(phoneBook):
    view.PrtintMenu()
    ReturnEnterMenu(phoneBook)


def EnterNumMenu():
    step = 0
    while step < 1 or step > 9:
        step = int(input('выберите действие: '))
    return step


def PrintPhoneBook(phoneBook):
    for i in range(0, len(phoneBook)):
        print(f'№ {i + 1} ', end='')
        for j in range(5):
            print(phoneBook[i][j], end=' ')
        print()


def ReturnEnterMenu(phoneBook):
    step = EnterNumMenu()
    while step != 9:
        if step == 1:
            PrintPhoneBook(phoneBook)
            step = EnterNumMenu()
        elif step == 2:
            DeleteFromPhoneBook(phoneBook)
            step = EnterNumMenu()
        elif step == 3:
            AddToPhoneBook(phoneBook)
            step = EnterNumMenu()
        elif step == 4:
            ConvertToHTML(phoneBook)
            step = EnterNumMenu()
        elif step == 5:
            ConvertToTXT(phoneBook)
            step = EnterNumMenu()
        elif step == 6:
            phoneBook = ConvertHtmlToList()
            step = EnterNumMenu()
        elif step == 7:
            phoneBook = ConvertTxtToList()
            step = EnterNumMenu()
        elif step == 8:
            view.PrintPhoneBook(phoneBook)
            view.PrintFindMenu()
            FindEmployee(phoneBook)
            step = EnterNumMenu()
        elif step == 9:
            exit()
