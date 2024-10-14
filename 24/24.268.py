# Автор В.Н. Шубинкин
from string import ascii_uppercase

with open('24-268.txt') as f:
    s = f.read().strip()
for letter in ascii_uppercase[10:]:
    s = s.replace(letter, ' ')
numbers = s.split()
max_even = '0'
for number in numbers:
    if number[0] != '0' and int(number, 20) % 2 == 0:
        #  max_even = max(max_even, number, key=lambda num: int(num, 20))
        if int(number, 20) > int(max_even, 20):
            max_even = number
print(max_even)
