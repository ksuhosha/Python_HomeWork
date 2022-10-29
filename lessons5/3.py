# 3. Создайте программу для игры в "Крестики-нолики".
import random

# battelField = [['1[00]', '2[01]', '3[02]'], ['4[10]', '5[11]', '6[12]'], ['7[20]', '8[21]', '9[22]']]
battelField = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
yellow = "\033[33m {}"
green = "\033[32m {}"
red = "\033[31m {}"
turquoise = "\033[36m {}"
white = "\033[0m {}"


def PrintField(battelField):
    print('выберите цифру из доступных')
    for i in range(0, len(battelField)):
        for j in range(0, len(battelField[i])):
            if battelField[i][j] != '0' and battelField[i][j] != 'X':
                print(white.format(battelField[i][j]), sep='\t', end='\t')
            elif battelField[i][j] == player1:
                print(turquoise.format(battelField[i][j]), sep='\t', end='\t')
            else:
                print(green.format(battelField[i][j]), sep='\t', end='\t')
        print()


def Check(battelField, name):
    win = False
    if battelField[0][0] == battelField[1][1] == battelField[2][2] or battelField[0][2] == battelField[1][1] == \
            battelField[2][0]:
        print(yellow.format('победили '), name, white.format("\n"))
        win = True
    for i in range(3):
        if battelField[i][0] == battelField[i][1] == battelField[i][2] or battelField[0][i] == battelField[1][i] == \
                battelField[2][i]:
            print(yellow.format('победили '), name, white.format("\n"))
            win = True
    return win


def PrintGoFirst(name):
    print(turquoise.format("Первым будет ходить "), turquoise.format(name), white.format(""),
          sep='')


def InputCheckNum(battelField, name, color):
    num_digit = False
    while num_digit == False:
        try:
            print(color.format(name), ':', white.format(""), end=' ')
            num_1 = int(input())
            count = 0
            for i in range(0, len(battelField)):
                for j in range(0, len(battelField[i])):
                    if battelField[i][j] == num_1:
                        battelField[i][j] = name
                        num_digit = True
                        count = 1
                        break
                if count == 1:
                    break
        except:
            print(red.format(name), "введите число!:\n", white.format(''), end='')
    return num_1


player1 = 'X'
player2 = '0'
movePlayers = random.randint(0, 1)

if movePlayers == 0:
    player1, player2 = player2, player1
    movePlayers = 1
PrintGoFirst(player1)
win = False
count = 0
PrintField(battelField)
while count != 9:
    if movePlayers:
        num = InputCheckNum(battelField, player1, turquoise)
        movePlayers = 0
        count += 1
        PrintField(battelField)
        if Check(battelField, player1):
            break
    else:
        num = InputCheckNum(battelField, player2, green)
        movePlayers = 1
        count += 1
        PrintField(battelField)
        if Check(battelField, player2):

            break
if count == 9:
    print(yellow.format('НИЧЬЯ!!!!'))
