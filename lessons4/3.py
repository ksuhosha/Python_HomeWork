# 3. Задайте последовательность чисел. Напишите программу, которая выведет списокк неповторяющихся элементов исходной последовательности.
import random
numElementsList = 20 #int(input('введите количество елементов в списке'))
listNum = []
for i in range(numElementsList):
    listNum.append(random.randint(1,10))
print(listNum)
print(set(listNum))
uniqueList = []
[uniqueList.append(i) for i in listNum if i not in uniqueList]
print(uniqueList)