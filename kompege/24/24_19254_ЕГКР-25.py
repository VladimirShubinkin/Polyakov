'''№ 19254 ЕГКР 21.12.24 (Уровень: Базовый)
Текстовый файл состоит из символов F, G, Q, R, S и W.
Определите в прилагаемом файле максимальное количество идущих подряд символов,
среди которых подстрока FSRQ встречается ровно 80 раз.
Для выполнения этого задания следует написать программу.'''

with open('24_19254.txt') as f:
    s = f.read().strip()
indexes = []
for i in range(len(s) - 3):
    if s[i:i+4] == 'FSRQ':
        indexes.append(i)
max_len = 0
for i in range(81, len(indexes)):
    max_len = max(max_len, indexes[i] - indexes[i - 81] + 2)
print(max_len)
