# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k = 2 => 2 * x² + 4 * x + 5 = 0 или x² + 5 = 0 или 10 * x² = 0
import random
import nice


def polynomial_writing(lst):
    with open('Exercise_04.txt', 'a', encoding='utf-8') as f:
        for i in range(0, len(lst)):
            if lst[i] == 0:
                continue
            if i == len(lst) - 2:
                f.write(f'{lst[i]}x ')
            elif i == len(lst) - 1:
                f.write(f'{lst[i]} ')
            else:
                f.write(f'{lst[i]}x{nice.nice(len(lst) - (i + 1))} ')
            if i != len(lst) - 1:
                f.write('+ ')
        else:
            f.write(f'= 0\n')


degree = int(input('Enter degree: ')) + 1
list_0 = []
for _ in range(degree):
    list_0.append(random.randint(0, 100))
polynomial_writing(list_0)
