'''212)	Текстовый файл 24-212.txt содержит строку из символов A, B, C, D и O, всего не более чем из 10^6 символов.
Определите максимальное количество идущих подряд пар символов вида «согласная + гласная».'''

import re

with open('24data/24-212.txt') as f:
    s = f.read().strip()

pattern = r'(?:[BCD][AO])+'
max_seq = max(re.findall(pattern, s), key=len)
print(len(max_seq) // 2)
