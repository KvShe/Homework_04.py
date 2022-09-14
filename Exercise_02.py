# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N
def multiplier_list(num):
    lst = []
    for i in range(2, num):
        if num % i == 0:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                lst.append(i)
    return lst


number = int(input('Enter number: '))
multipliers = multiplier_list(number)
print(f"{number}: {', '.join(list(map(str, multipliers)))}")
