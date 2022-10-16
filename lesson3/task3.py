# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random

N = 11  # int(input('введите сколько элементов в списке: '))
listRandom = []
for i in range(N):
    listRandom.append(round(float(random.randint(0, 10) + random.randint(0, 100) / 100),2))
print(listRandom)
max = listRandom[0] - int(listRandom[0])
min = listRandom[0] - int(listRandom[0])
for i in range(N):
    if float(max) < (listRandom[i] - int(listRandom[i])):
        max = listRandom[i] - int(listRandom[i])
    if min > (listRandom[i] - int(listRandom[i])):
        min = listRandom[i] - int(listRandom[i])
diff = max - min
print(f'min = {round(min,2)}', f'max = {round(max,2)}', f'diff = {round(diff,2)}', sep='\n')
