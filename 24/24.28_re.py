'''
28)	(А.М. Кабанов) В текстовом файле k7b-2.txt находится цепочка из символов латинского алфавита
A, B, C, D, E, F. Найдите максимальную длину цепочки вида DBACDBACDBAC....
(состоящей из фрагментов DBAC, последний фрагмент может быть неполным).
'''

import re

with open('24data/k7b-2.txt') as f:
    s = f.read().strip()

max_seq = max(re.findall(r'(?:DBAC)+(?:DBA|DB|D)', s), key=len)
print(max_seq)
print(len(max_seq))
max_seq = ''
for m in re.finditer(r'(DBAC)+(DBA|DB|D)', s):
    max_seq = max(max_seq, m.group(), key=len)
print(max_seq)
print(len(max_seq))