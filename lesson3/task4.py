# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#  Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
bin = ''
N = 456 #int(input('Введите число: '))
while N != 0:
    bin = bin + str(N % 2)
    N = N // 2
print(f'не перевернутый = {bin}')
while (len(bin) % 4) != 0:
    bin = bin + '0'

print('bin =', bin[::-1])