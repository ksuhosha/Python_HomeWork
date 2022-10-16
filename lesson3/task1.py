# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
#  Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

N = 10  # int(input('введите сколько элементов в списке: '))
listRandom = []
for i in range(N):
    listRandom.append(random.randint(0, 100))
print(listRandom)
sum = 0
for i in range(1, N, 2):
    sum = sum + listRandom[i]
print(f'сумма = {sum}')
