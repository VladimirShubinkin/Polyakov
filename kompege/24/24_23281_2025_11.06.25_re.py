'''
Текстовый файл состоит из десятичных цифр и заглавных букв латинского алфавита.
Определите в прилагаемом файле максимальное количество идущих подряд символов,
среди которых подстрока 2025 встречается не менее 90 раз и при этом содержится ровно 80 букв Y.
В ответе запишите число - количество символов в найденной последовательности.
'''
from time import perf_counter
t0 = perf_counter()

from re import finditer

with open('24_23281.txt') as f:
    s = f.read().strip()

pattern = r'(?=(([^Y]*Y){80}[^Y]*))'
max_seq = max((m.group(1) for m in finditer(pattern, s) if m.group(1).count('2025') >= 90), key=len)
max_len = len(max_seq)
print(max_len)
print(perf_counter() - t0)  # ~75sec
