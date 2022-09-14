def nice(num):
    """Переводит число 'num' (int) в верхний индекс 'degree' (str)"""
    degree = ''
    while True:
        degree = utf[num % 10] + degree
        num //= 10
        if num == 0:
            break
    return degree


utf = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}
