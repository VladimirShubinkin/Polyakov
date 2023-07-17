'''87)	(П.Е. Финкель, г. Тимашевск) Текстовый файл 24-1.txt состоит не более чем из 10^6 символов.
Определите максимальное нечётное число, записанное в этом файле.'''

from string import ascii_uppercase

with open('24data/24-1.txt') as f:
    s = f.read().strip()
for letter in ascii_uppercase:
    s = s.replace(letter, ' ')
odd_numbers = [x for x in map(int, s.split()) if x % 2]
ans = max(odd_numbers)
print(ans)
