'''296)	(ЕГЭ-2024) Текстовый файл 24-296.txt состоит не более чем из 10^6 символов и содержит только буквы латинского
алфавита A, B, C, D, E и F. Определите максимальное количество идущих подряд символов в прилагаемом файле,
среди которых пара символов СD (в указанном порядке) встречается ровно 160 раз.'''

with open('24data/24-296.txt') as f:
    s = f.read().strip()
N = 160
a = s.split('CD')
first_len = len('CD'.join(a[:N + 1])) + 1
last_len = len('CD'.join(a[-(N + 1):])) + 1
max_len = max(first_len, last_len)
for i in range(1, len(a) - N - 1):
    cur_len = len('CD'.join(a[i: i + N + 1])) + 2
    max_len = max(max_len, cur_len)
print(max_len)
