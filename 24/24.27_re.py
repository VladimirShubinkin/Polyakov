'''27)	(А.М. Кабанов) В текстовом файле k7b-1.txt находится цепочка из символов латинского алфавита A, B, C, D, E.
Найдите максимальную длину цепочки вида EABEABEABE...
(состоящей из фрагментов EAB, последний фрагмент может быть неполным).'''

import re

with open('24data/k7b-1.txt') as f:
    s = f.read().strip()

max_seq = max(re.findall(r'(?:EAB)+(?:EA|E)?', s), key=len)
print(len(max_seq))
