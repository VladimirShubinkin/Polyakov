'''
Найдите и запишите в ответе целую часть длины кратчайшего пути из вершины с номером 1 в вершину с номером 100,
состоящего не более чем из 6 рёбер.
'''

from functools import cache


@cache
def f(a, b, k):
    if a == b:
        return 0
    if a not in data or k == 0:
        return float('inf')
    min_len = float('inf')
    for v, w in data[a]:
        min_len = min(min_len, w + f(v, b, k - 1))
    return min_len


data= {}
with open('23data/23-1.txt') as fin:
    for line in fin.readlines():
        u, v, w = line.split()
        data[u] = data.get(u, []) + [(v, float(w))]
min_len = f('1', '100', 6)
print(int(min_len))
