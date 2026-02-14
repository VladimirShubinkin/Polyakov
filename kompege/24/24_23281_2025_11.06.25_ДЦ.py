'''
Текстовый файл состоит из десятичных цифр и заглавных букв латинского алфавита.
Определите в прилагаемом файле максимальное количество идущих подряд символов,
среди которых подстрока 2025 встречается не менее 90 раз и при этом содержится ровно 80 букв Y.
В ответе запишите число - количество символов в найденной последовательности.
'''
from time import perf_counter

t0 = perf_counter()
with open('24_23281.txt') as f:
    s = f.read().strip()

max_len = len('2025') * 90 + 80
for i in range(len(s)):
    for j in range(i + max_len, len(s)):
        ss = s[i:j + 1]
        if ss.count('Y') > 80:
            break
        if ss.count('Y') == 80 and ss.count('2025') >= 90:
            if len(ss) > max_len:
                max_len = len(ss)
                seq = ss
print(seq)
print(max_len)
print(perf_counter() - t0)  # ~15sec
