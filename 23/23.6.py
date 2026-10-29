'''
Найдите и запишите в ответе целую часть длины кратчайшего пути из вершины с номером 1 в вершину с номером 100,
состоящего только из рёбер, длина которых не меньше 1000.
'''

from functools import cache


@cache
def f(a, b):
    if a == b:
        return 0
    if a not in data:
        return float('inf')
    min_len = float('inf')
    for v, w in data[a]:
        if w >= 1000:
            min_len = min(min_len, f(v, b) + w)
    return min_len


data = {}
with open('23data/23-1.txt') as fin:
    for line in fin.readlines():
        u, v, w = line.split()
        data[u] = data.get(u, []) + [(v, float(w))]
print(int(f('1', '100')))
