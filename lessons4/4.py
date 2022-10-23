# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#  Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def creatPolynomial():
    k = int(input('введите степень многочлена: '))
    listK = []
    [listK.append(random.randint(0, 100)) for i in range(k + 1)]
    print(listK)
    equation = ''
    for i in range(k):
        if listK[k - i - 1] != 0:
            if k - i != 1:
                equation = equation + str(listK[k - i]) + 'x^' + str(k - i) + '+'
            else:
                equation = equation + str(listK[k - i]) + 'x+'
    if listK[0] == 0:
        equation = equation[:-1]
        equation = equation + '= 0'
    else:
        equation = equation + str(listK[0]) + '= 0'
    return equation

equation = creatPolynomial()

data = open('fileEquation.txt', 'w+')
data.write(equation)
data.readlines()
data.close()
