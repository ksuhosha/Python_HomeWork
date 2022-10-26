# 2. Создайте программу для игры с конфетами человек против человека.
#  Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#  За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
#  чтобы забрать все конфеты у своего конкурента?
#  a) Добавьте игру против бота
#  b) Подумайте как наделить бота "интеллектом"

import random

yellow = "\033[33m {}"
green = "\033[32m {}"
red = "\033[31m {}"
turquoise = "\033[36m {}"
white = "\033[0m {}"


def PrintGoFirst(name):
    print("Первым будет ходить ", turquoise.format(name), white.format("\nВводите количество конфет от 1 до 28"),
          sep='')


def PrintGetCandy(name, color):
    print(color.format(name), white.format(":"), end='')
    numCandyTake = ''
    while type(numCandyTake) != int or numCandyTake < 1 or numCandyTake > 28:
        try:
            numCandyTake = int(input())
            if numCandyTake < 1 or numCandyTake > 28:
                print(red.format(name), "введите количество конфет от 1 до 28:\n", white.format(''), end='')
        except:
            print(red.format(name), "введите количество конфет ЧИСЛОМ!:\n", white.format(''), end='')
    return numCandyTake


def PrintCandy(candy):
    print(white.format(f"на столе осталось {candy} конфет"), white.format(''), end='\n')


def GetCandyBot(candy, color):
    numCandyTake = (candy + 1) % 29 - 1
    if numCandyTake == 0:
        numCandyTake = 28
    print(color.format('Bot'), white.format(f":{abs(numCandyTake)}\n"), end='')
    # print(numCandyTake)
    return abs(numCandyTake)


def PrintWin(candy, movePlayers, typeGame):
    if movePlayers == 1:
        print(turquoise.format(f'На столе осталось {candy} конфет. Поздравляем {player1} Победил!!!'), white.format(''))
    elif typeGame == 0:
        print(green.format(f'На столе осталось {candy} конфет. Поздравляем Bot Победил!!!'), white.format(''))
    else:
        print(green.format(f'На столе осталось {candy} конфет. Поздравляем {player2} Победил!!!'), white.format(''))


candy = 100
movePlayers = random.randint(0, 1)
typeGame = int(input('Для игры в PvE нажмите 0, PvP нажмите 1\nВыберите тип игры: '))

if typeGame:
    print("PvP")  # PVP
    player1 = 'ЛаПа'  # input("Ведите имя игрока: ")
    player2 = 'Контер'  # input("Ведите имя игрока: ")

    name = ''
    if movePlayers == 0:
        player1, player2 = player2, player1
        movePlayers = 1

    PrintGoFirst(player1)
    while candy > 28:
        if movePlayers:
            candy = candy - PrintGetCandy(player1, turquoise)
            movePlayers = 0

        else:
            candy = candy - PrintGetCandy(player2, green)
            movePlayers = 1
            PrintCandy(candy)
    PrintWin(candy, movePlayers, typeGame)
else:
    print("PvE")  # PVP
    player1 = 'Лапа'  # input("Ведите имя игрока: ")

    PrintGoFirst(player1)
    if movePlayers == 0:
        while candy > 28:
            if movePlayers == 0:
                candy = candy - GetCandyBot(candy, turquoise)
                movePlayers = 1

            else:
                candy = candy - PrintGetCandy(player1, green)
                movePlayers = 0
                PrintCandy(candy)
    else:
        while candy > 28:
            if movePlayers:
                candy = candy - PrintGetCandy(player1, turquoise)
                movePlayers = 0

            else:
                candy = candy - GetCandyBot(candy, green)
                movePlayers = 1
                PrintCandy(candy)
    PrintWin(candy, movePlayers, typeGame)
