# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141.  10-1 ≤ d ≤10-10
# π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...

from math import pi

print(pi)
d = int(input('заданная точность: '))
num_pi = 0
i = 1
r = 0
num = (pi // 0.1 ** d / 10 ** d)


while num != (num_pi // 0.1 ** d / 10 ** d):
    num_pi += (4 / i)
    if i < 1:
        i = (abs(i) + 2)
    else:
        i = (i + 2) * -1
    r+=1
print(round(num_pi, d), r, sep='\t')
