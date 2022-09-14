# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
def polynomial_list(file):
    with open(file, 'r', encoding='utf-8') as f:
        lst = f.readline()
    lst = lst.split(' + ')
    lst[-1] = lst[-1].split(' = ')[0]
    return lst


def polynomial_list_of_lists(lst):
    if lst[-1].isdigit():
        dgt = int(lst[-1])
        size = len(lst) - 1
    else:
        size = len(lst) - 2
        dgt = 0
    res = []
    for j in range(size):
        res.append([lst[j].split('x')[1], lst[j].split('x')[0]])
    return res, dgt


lst_1 = polynomial_list('exercise_04.txt')
lst_2 = polynomial_list('Exercise_05_begin.txt')
lst_1, dgt_1 = polynomial_list_of_lists(lst_1)
lst_2, dgt_2 = polynomial_list_of_lists(lst_2)

with open('Exercise_05_end.txt', 'w', encoding='utf-8') as f:
    while True:
        if lst_1[0][0] == lst_2[0][0]:
            tmp = int(lst_1[0][1]) + int(lst_2[0][1])
            f.write(f'{str(tmp)}x{lst_1[0][0]}')
            lst_1.pop(0)
            lst_2.pop(0)
        elif lst_1[0][0] > lst_2[0][0]:
            f.write(f'{lst_1[0][1]}x{lst_1[0][0]}')
            lst_1.pop(0)
        else:
            f.write(f'{lst_2[0][1]}x{lst_2[0][0]}')
            lst_2.pop(0)
        if len(lst_1) != 0 or len(lst_2) != 0:
            f.write(' + ')
        else:
            break
    if len(lst_1) != 0:
        for i in range(len(lst_1)):
            f.write(f'{lst_1[i][0]}x{lst_1[i][1]}')
    if len(lst_2) != 0:
        for i in range(len(lst_2)):
            f.write(f'{lst_2[i][0]}x{lst_2[i][1]}')
    if dgt_1 + dgt_2 != 0:
        f.write(f' + {str(dgt_1 + dgt_2)}')
    f.write(' = 0')
