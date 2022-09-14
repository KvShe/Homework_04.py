# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141
import math


def accuracy_calculation(num, d):
    d = d.count('0')
    accuracy = 1
    for i in range(d):
        accuracy *= 10
    num = num * accuracy // 1 / accuracy
    return num


d_1 = input('Enter accuracy: ')
number = math.pi
number = accuracy_calculation(number, d_1)
print(number)
