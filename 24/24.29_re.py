'''
29)	(А.М. Кабанов) В текстовом файле k7b-3.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F.
Найдите максимальную длину цепочки вида BAFEBAFEBAFE...
(состоящей из фрагментов BAFE, последний фрагмент может быть неполным).
'''

import re

with open('24data/k7b-3.txt') as f:
    s = f.read().strip()
max_seq = max(re.findall(r'(?:BAFE)+(?:BAF|BA|B)?', s), key=len)
print(max_seq)
print(len(max_seq))
