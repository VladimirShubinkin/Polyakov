'''413)	В системе счисления с некоторым основанием p выполняется равенство
y3y + y65 = x2z0
Буквами x, y и z обозначены некоторые цифры из алфавита системы счисления с основанием p.
Запишите в ответе значение числа xyz(p) в десятичной системе счисления.
'''
from string import ascii_uppercase, digits

alphabet = digits + ascii_uppercase

for p in range(7, 37):
    for x in alphabet[1:p]:
        for y in alphabet[1:p]:
            for z in alphabet[:p]:
                left = int(f'{y}3{y}', p) + int(f'{y}65', p)
                right = int(f'{x}2{z}0', p)
                if left == right:
                    print(int(f'{x}{y}{z}', p))
                    print('x y z p')
                    print(x, y, z, p)
