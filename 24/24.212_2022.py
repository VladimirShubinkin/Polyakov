'''212)	Текстовый файл 24-212.txt содержит строку из символов A, B, C, D и O, всего не более чем из 10^6 символов.
Определите максимальное количество идущих подряд пар символов вида «согласная + гласная».'''

with open('24data/24-212.txt') as f:
    s = f.read().strip()

max_len = 0
cur_len = 0
for start in (0, 1):
    for i in range(start, len(s) - 1, 2):
        if s[i] in 'BCD' and s[i + 1] in 'AO':
            cur_len += 1
            max_len = max(max_len, cur_len)
        else:
            cur_len = 0
print(max_len)
