# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

N = 8 #int(input('Введите K: '))

def Fibonacci(N):
    if N <= 0:
        if (N == -1):
            return 1
        elif (N==0):
            return 0
        else:
            return Fibonacci(N + 2) - Fibonacci(N + 1)
    else:
        if (N == 1 or N== 2):
            return 1
        else:
            return Fibonacci(N - 1) + Fibonacci(N - 2)
fib=[]
for i in range(-N, N+1, 1):
    fib.append(Fibonacci(i))
print(fib)