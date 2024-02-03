'''
189)Текстовый файл 24-181.txt содержит строку из заглавных латинских букв и точек, всего не более чем из 106 символов.
Определите максимальное количество идущих подряд символов, среди которых нет точек,
а количество гласных (букв A, E, I, O, U, Y) не превышает 7.
'''
with open('24data/24-181.txt') as f:
    s = f.read().strip()
for letter in 'EIOUY':
    s = s.replace(letter, 'A')
a = s.split('.')
# 1
max_len = 0
for line in a:
    seq = line.split('A')
    for i in range(len(seq) - 7):
        ss = 'A'.join(seq[i:i+8])
        max_len = max(max_len, len(ss))
print(max_len)
# 2
max_len = 0
for line in a:
    p = []
    for i in range(len(line)):
        if line[i] == 'A':
            p.append(i)
    for i in range(8, len(p)):
        max_len = max(max_len, p[i] - p[i - 8] - 1)
print(max_len)
