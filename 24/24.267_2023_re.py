'''267)	(ЕГЭ-2023) Текстовый файл 24-264.txt состоит не более чем из 10^6 символов
и содержит только заглавные буквы латинского алфавита и цифры. Определите максимальную длину подстроки,
которая может являться записью числа в шестнадцатеричной системе счисления.'''

import re

with open('24data/24-264.txt') as f:
    s = f.read().strip()

pattern = r'[1-9A-F][0-9A-F]+'
max_seq = max(re.findall(pattern, s), key=len)
print(len(max_seq))
