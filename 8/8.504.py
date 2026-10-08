'''
504) Сколько существует чисел, пятнадцатеричная запись которых содержит шесть цифр,
причем среди них по крайней мере одна цифра 0 и ровно две цифры с числовым значением,
превышающим 12, причём стоящие рядом.
'''

from itertools import product

count = 0
for p in product('0123456789ABCDE', repeat=6):
    if p[0] != '0' and p.count('0') >= 1:
        if p.count('D') + p.count('E') == 2:
            s = ''.join(p).replace('D', 'E')
            if 'EE' in s:
                count += 1
print(count)  # 121348
