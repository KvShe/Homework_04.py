# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
def polynomial_list(file):
    with open(file, 'r', encoding='utf-8') as f:
        lst = f.readline()
    lst = lst.split(' + ')
    lst[-1] = lst[-1].split(' = ')[0]
    return lst


def polynomial_dict(lst):
    if lst[-1].isdigit():
        dgt = int(lst[-1])
        size = len(lst) - 1
    else:
        size = len(lst)
        dgt = 0
    res = []
    for j in range(size):
        res.append([lst[j].split('x')[1], lst[j].split('x')[0]])
    return res, dgt


def polynomial_sum(lst_1, dgt_1, lst_2, dgt_2):
    result = ''
    while True:
        if lst_1[0][0] == lst_2[0][0]:
            tmp = int(lst_1[0][1]) + int(lst_2[0][1])
            result += f'{str(tmp)}x{lst_1[0][0]}'
            lst_1.pop(0)
            lst_2.pop(0)
        elif lst_1[0][0] > lst_2[0][0]:
            result += f'{lst_1[0][1]}x{lst_1[0][0]}'
            lst_1.pop(0)
        else:
            result += f'{lst_2[0][1]}x{lst_2[0][0]}'
            lst_2.pop(0)
        if len(lst_1) != 0 and len(lst_2) != 0:
            result += ' + '
        else:
            break
    if len(lst_1) != 0:
        for i in range(len(lst_1)):
            result += f' + {lst_1[i][1]}x{lst_1[i][0]}'
    if len(lst_2) != 0:
        for i in range(len(lst_2)):
            result += f' + {lst_2[i][1]}x{lst_2[i][0]}'
    if dgt_1 + dgt_2 != 0:
        result += f' + {str(dgt_1 + dgt_2)}'
    result += ' = 0\n'
    return result


list_1 = polynomial_list('exercise_04.txt')
list_2 = polynomial_list('Exercise_05_begin.txt')

list_1, digit_1 = polynomial_dict(list_1)
list_2, digit_2 = polynomial_dict(list_2)
res = polynomial_sum(list_1, digit_1, list_2, digit_2)
with open('Exercise_05_end.txt', 'w', encoding='utf-8') as f:
    f.write(res)
