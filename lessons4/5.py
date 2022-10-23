# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
import random

def creatPolynomial():
    k = int(input('введите степень многочлена: '))
    listK = []
    [listK.append(random.randint(0, 100)) for i in range(k+1)]
    print(listK)
    equation = ''
    for i in range(k):
        if listK[k - i - 1] != 0:
            if k-i !=1:
                equation = equation + str(listK[k - i ]) + 'x^' + str(k - i) + '+'
            else:
                equation = equation + str(listK[k - i]) + 'x+'
    if listK[0] == 0:
        equation = equation[:-1]
        equation = equation + '=0'
    else:
        equation = equation + str(listK[0]) + '=0'
    return equation

equation1 = creatPolynomial()
equation2 = creatPolynomial()

data = open('task5_1.txt', 'w+')
data.write(equation1)
data.readlines()
data.close()
data = open('task5_2.txt', 'w+')
data.write(equation2)
data.readlines()
data.close()
import re


def ConvertToList(file1):
    file5_1 = file1.readline()
    print(file5_1)
    list1 = re.split("x|\+|=", file5_1)
    return list1


file1 = open('task5_1.txt', 'r')
file2 = open('task5_2.txt', 'r')
list1 = ConvertToList(file1)
list2 = ConvertToList(file2)

stepen1 = dict()
stepen2 = dict()


def ConvertT0Dict(list1):
    stepen = dict()
    for i in range(1, len(list1), 2):
        if list1[i] != 0:
            if list1[i] != '':
                stepen[int(list1[i].replace("^", "", 1))] = int(list1[i - 1])
            elif list1[i] == '':
                stepen[1] = int(list1[i - 1])
            elif list1 == '0':
                stepen[0] = int(list1[i - 1])
    return stepen


stepen1 = ConvertT0Dict(list1)
stepen2 = ConvertT0Dict(list2)
if max(stepen1.keys()) > max(stepen2.keys()):
    maxStep = max(stepen1.keys())
else:
    maxStep = max(stepen2.keys())
strResult = ''
i = maxStep

while i >= 0:
    sum = 0
    if i in stepen1.keys():
        sum = sum + stepen1[i]
    if i in stepen2.keys():
        sum = sum + stepen2[i]
    if i in stepen1.keys() or i in stepen2.keys():
        if i !=0:
            strResult = strResult + str(sum) + 'x^' + str(i) + '+'
        else:
            strResult = strResult + str(sum) + '=0'
    i -= 1
print(strResult)
data = open('task5res.txt', 'w+')
data.write(strResult)
data.readlines()