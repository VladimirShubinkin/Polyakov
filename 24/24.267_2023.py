'''267)	(ЕГЭ-2023) Текстовый файл 24-264.txt состоит не более чем из 10^6 символов
и содержит только заглавные буквы латинского алфавита и цифры. Определите максимальную длину подстроки,
которая может являться записью числа в шестнадцатеричной системе счисления.'''

from string import ascii_uppercase

with open('24data/24-264.txt') as f:
    s = f.read().strip()

# Вариант 1. replace + split
s1 = s
not_hex_digits = ascii_uppercase[6:]
for c in not_hex_digits:
    s1 = s1.replace(c, ' ')
hex_numbers = [num.lstrip('0') for num in s1.split()]
max_len = len(max(hex_numbers, key=len))
print(max_len)

# Вариант 2. Конечный автомат
not_hex_digits = ascii_uppercase[6:]
max_len = 0
cur_len = 0
is_number = False
for c in s:
    if is_number:
        if c in not_hex_digits:
            cur_len = 0
            is_number = False
        else:
            cur_len += 1
    else:
        if c in not_hex_digits or c == '0':
            cur_len = 0
        else:
            cur_len = 1
            is_number = True
    max_len = max(max_len, cur_len)
print(max_len)
