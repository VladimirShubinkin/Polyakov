'''77)	Текстовый файл k8-1.txt состоит не более чем из 10^6 символов.
Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.'''

with open('24data/k8-1.txt') as f:
    s = f.read().strip()

cur_len = 1
max_len = 0
for i in range(len(s) - 1):
    if s[i + 1] != s[i]:
        cur_len += 1
    else:
        cur_len = 1
    max_len = max(max_len, cur_len)
print(max_len)
