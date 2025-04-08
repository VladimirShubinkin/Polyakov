'''32)	(А.М. Кабанов) В текстовом файле k7b-6.txt находится цепочка
из символов латинского алфавита A, B, C, D, E, F.
Найдите максимальную длину цепочки вида DAFDAFDAF....
(состоящей из фрагментов DAF, последний фрагмент может быть неполным).'''

import re

with open('24data/k7b-6.txt') as f:
    s = f.read().strip()
max_seq = max(re.findall(r'(?:DAF)+(?:DA|D)?', s), key=len)
print(max_seq)
print(len(max_seq))
