# Автор В.Н. Шубинкин
import re

with open('24data/24-268.txt') as f:
    s = f.read().strip()

numbers = re.findall(r'[0-9A-I]+', s)
max_n = 0
max_number = '0'
for number in numbers:
    n = int(number, 19)
    if number[0] != '0' and n % 2 == 0:
        if n > max_n:
            max_n = n
            max_number = number
print(max_number)
