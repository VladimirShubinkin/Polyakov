'''27)	(А.М. Кабанов) В текстовом файле k7b-1.txt находится цепочка из символов латинского алфавита A, B, C, D, E.
Найдите максимальную длину цепочки вида EABEABEABE...
(состоящей из фрагментов EAB, последний фрагмент может быть неполным).'''

with open('24data/k7b-1.txt') as f:
    s = f.read().strip()

eab = 'EAB'
j = 0
cur_len = 0
max_len = 0
for c in s:
    if c == eab[j]:
        cur_len += 1
        j = (j + 1) % len(eab)
    elif c == eab[0]:
        cur_len = 1
        j = 1
    else:
        cur_len = 0
        j = 0
    max_len = max(cur_len, max_len)
print(max_len)
