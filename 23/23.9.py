'''
Найдите минимальную длину пути из вершины с номером 1 в вершину с номером 100
среди всех путей с длинами от 16000 до 21000 (включительно).
Гарантируется, что хотя бы один такой маршрут существует.
Запишите в ответе целую часть найденной длины.
'''

from functools import cache


@cache
def f(a, b, cur_len):
    global min_len
    if a == b:
        if 16_000 <= cur_len:
            min_len = min(min_len, cur_len)
        return
    if a not in data or cur_len > 21_000:
        return
    for v, w in data[a]:
        f(v, b, cur_len + w)


data = {}
min_len = float('inf')
with open('23data/23-1.txt') as fin:
    for line in fin.readlines():
        u, v, w = line.split()
        data[u] = data.get(u, []) + [(v, float(w))]
f('1', '100', 0)
print(int(min_len))
