'''213)	Текстовый файл 24-213.txt содержит строку из символов N, O и P, всего не более чем из 10^6 символов.
Определите максимальное количество идущих подряд последовательностей символов NРО или РNО в прилагаемом файле.
Искомая подпоследовательность должна состоять только из троек NРО или только из троек РNО
или только из троек NРО и РNО в произвольном порядке их следования. '''

import re

with open('24data/24-213.txt') as f:
    s = f.read().strip()

pattern = r'(?:PNO|NPO)+'
max_seq = max(re.findall(pattern, s), key=len)
print(len(max_seq) // 3)
