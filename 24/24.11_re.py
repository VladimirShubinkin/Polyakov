'''11)	В текстовом файле k7-53.txt находится цепочка
из символов латинского алфавита A, B, C.
Найдите длину самой длинной подцепочки, состоящей из символов C.'''

import re

with open('24data/k7-53.txt') as f:
    s = f.read().strip()
max_seq = max(re.findall(r'C+', s), key=len)
print(len(max_seq))
