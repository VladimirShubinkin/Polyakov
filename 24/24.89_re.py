'''89)	(П.Е. Финкель, г. Тимашевск) Текстовый файл 24-1.txt состоит не более чем из 10^6 символов.
Определите максимальное чётное число, записанное в этом файле.'''
import re

with open('24data/24-1.txt') as f:
    s = f.read().strip()

max_even_num = max(re.findall(r'(?<=[A-Z])[1-9]\d*[02468](?=[A-Z])', s), key=int)
print(max_even_num)
