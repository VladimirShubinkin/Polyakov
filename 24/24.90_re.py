'''90)	(П.Е. Финкель, г. Тимашевск) Текстовый файл 24-1.txt состоит не более чем из 10^6 символов.
Определите минимальное чётное число, записанное в этом файле.'''

import re

with open('24data/24-1.txt') as f:
    s = f.read().strip()
min_even_number = min(re.findall(r'(?<=[A-Z])\d*[02468](?=[A-Z])', s), key=int)
print(min_even_number)
