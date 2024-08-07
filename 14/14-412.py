'''
412)	(PRO100 ЕГЭ) Операнды арифметического выражения записаны в системе счисления с основанием 68:
123x5(68) + 1x233(68)
В записи чисел переменной x обозначена неизвестная цифра из алфавита 68-ричной системы счисления.
Определите наибольшее значение x, при котором значение данного арифметического выражения кратно 12.
Для найденного значения x вычислите частное от деления значения арифметического выражения на 12 и
укажите его в ответе в десятичной системе счисления. Основание системы счисления в ответе указывать не нужно.
'''

for x in range(67, -1, -1):
    n1 = 5 + x * 68 + 3 * 68**2 + 2 * 68**3 + 1 * 68**4
    n2 = 3 + 3 * 68 + 2 * 68**2 + x * 68**3 + 1 * 68**4
    s = n1 + n2
    if s % 12 == 0:
        print(s // 12)
        break
