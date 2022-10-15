# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint

n = int(input('введите число = '))
list_random = []

m = int(input('введите количество множителей = '))
list_random = []

for i in range(n):
    list_random.append(randint(-n, n))
print(list_random, sep='\t')

with open('file.txt', 'w') as file:
    for i in range(m):
        file.write(f'{str(randint(1, n))}\n')

list_index = []
with open('file.txt', 'r') as file:
    for line in file:
        list_index.append(int(line.rstrip('\n')))
print(list_index)
file.close()
prod = 1
for i in range(m):
    prod = prod * list_random[list_index[i]-1]
print(f'произведение позиций = {prod}')
