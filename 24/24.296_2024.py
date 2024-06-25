'''296)	(ЕГЭ-2024) Текстовый файл 24-296.txt состоит не более чем из 10^6 символов и содержит только буквы латинского
алфавита A, B, C, D, E и F. Определите максимальное количество идущих подряд символов в прилагаемом файле,
среди которых пара символов СD (в указанном порядке) встречается ровно 160 раз.'''

with open('24data/24-296.txt') as f:
    s = f.read().strip()
N = 160
indexes = [-1]
for i in range(len(s) - 1):
    if s[i:i+2] == 'CD':
        indexes.append(i)
indexes.append(len(s))
max_len = 0
for i in range(N + 1, len(indexes)):
    max_len = max(max_len, indexes[i] - indexes[i - (N + 1)])
print(max_len)

# Ответ: 1288
