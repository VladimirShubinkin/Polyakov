'''
Найдите кратчайший путь из вершины с номером 1 в вершину с номером 100
и запишите в ответе сумму номеров всех промежуточных вершин (кроме 1 и 100).
Гарантируется, что такой путь существует и единственный.
'''
from functools import cache

@cache
def f(a, b):
    if a == b:
        return 0, [b]
    if a not in data:
        return float('inf'), []
    min_len, path = float('inf'), []
    for v, w in data[a]:
        cur_len, cur_path = f(v, b)
        if cur_len + w < min_len:
            min_len = cur_len + w
            path = [a] + cur_path
    return min_len, path


data = {}
with open('23data/23-1.txt') as fin:
    for line in fin.readlines():
        u, v, w = line.split()
        data[int(u)] = data.get(int(u), []) + [(int(v), float(w))]
min_len, path = f(1, 100)
print(path)
print(sum(path[1:-1]))
