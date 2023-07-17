'''87)	(П.Е. Финкель, г. Тимашевск) Текстовый файл 24-1.txt состоит не более чем из 10^6 символов.
Определите максимальное нечётное число, записанное в этом файле.'''

with open('24data/24-1.txt') as f:
    s = f.read().strip() + 'A'
str_num = ''
max_num = 0
for c in s:
    if c.isdigit():
        str_num += c
    else:
        num = int(str_num) if str_num else 0
        max_num = max(max_num, num * (num % 2))
        str_num = ''
print(max_num)
