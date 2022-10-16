# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

N = 11  # int(input('введите сколько элементов в списке: '))
listRandom = []
for i in range(N):
    listRandom.append(random.randint(0, 10))
print(listRandom)
listProd = []
index = int(round(N / 2, 0))
for i in range(index):
    listProd.append(listRandom[i] * listRandom[N - i - 1])
print(listProd)