'''413)	В системе счисления с некоторым основанием p выполняется равенство
y3y + y65 = x2z0
Буквами x, y и z обозначены некоторые цифры из алфавита системы счисления с основанием p.
Запишите в ответе значение числа xyz(p) в десятичной системе счисления.
'''
from string import ascii_uppercase, digits

alphabet = digits + ascii_uppercase

for p in range(7, 37):
    for x in range(1, p):
        for y in range(1, p):
            for z in range(p):
                left = int(f'{alphabet[y]}3{alphabet[y]}', p) + int(f'{alphabet[y]}65', p)
                right = int(f'{alphabet[x]}2{alphabet[z]}0', p)
                if left == right:
                    print(int(f'{alphabet[x]}{alphabet[y]}{alphabet[z]}', p))
                    print(x, y, z, p)
