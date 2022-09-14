# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности
import random


def list_unique_items(num):
    lst = []
    for item in num:
        if num.count(item) == 1:
            lst.append(item)
    return lst


numbers = [random.randint(0, 9) for _ in range(20)]
print(f'Start: {numbers}')
result = list_unique_items(numbers)
print(f'Final: {result}')
