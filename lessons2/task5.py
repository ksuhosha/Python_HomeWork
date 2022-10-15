# 5. Реализуйте алгоритм перемешивания списка.
from random import randint

n = int(input('введите число = '))
list = []
list_rand = []
for i in range(n):
    list.append(i)
print(list)
for i in range(n):
    index_rand = randint(0, len(list)-1)
    list_rand.append(list[index_rand])
    list.pop(index_rand)
print(list_rand)
