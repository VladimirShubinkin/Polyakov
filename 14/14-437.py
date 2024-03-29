'''
437)	(ЕГЭ-2023) Операнды арифметического выражения записаны в системе счисления с основанием 23:
7x38596(23) + 14х36(23) + 61x7(23)
В записи чисел переменной x обозначена неизвестная цифра из алфавита 23-ричной системы счисления.
Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 22.
Для найденного значения x вычислите частное от деления значения арифметического выражения на 22 и
укажите его в ответе в десятичной системе счисления. Основание системы счисления указывать не нужно.
'''

from string import ascii_uppercase, digits

for x in digits + ascii_uppercase[:13]:
    n1 = int(f'7{x}38596', 23)
    n2 = int(f'14{x}36', 23)
    n3 = int(f'61{x}7', 23)
    s = n1 + n2 + n3
    if s % 22 == 0:
        print(s // 22)
        break
