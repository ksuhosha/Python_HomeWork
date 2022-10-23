# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def FindDiv(num):
    dividers = []
    for i in range(2, num // 2):
        while int(num) % i == 0:
            if num % i == 0:
                dividers.append(i)
                num = int(num/i)
    print(dividers)
num = 12 #int(input('введите число: '))
FindDiv(num)