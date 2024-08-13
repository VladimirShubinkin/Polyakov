'''460)	(ЕГЭ-2024) Определите количество 14-ричных пятизначных чисел, в записи которых ровно одна цифра 9 и не более
трех цифр с числовым значением, превышающим 10.'''
from itertools import product

alphabet = '0123456789ABCD'
count = 0
for p in product(alphabet, repeat=5):
    if p[0] != '0' and p.count('9') == 1:
        if sum(p.count(d) for d in 'BCD') <= 3:
            count += 1
print(count)
