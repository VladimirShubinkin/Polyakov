'''
Найдите кратчайший путь из вершины с номером 1 в вершину с номером 100, состоящего не более чем из 6 рёбер.
Гарантируется, что такой путь существует и единственный.
Запишите в ответе сумму номеров всех промежуточных вершин (кроме 1 и 100).
'''

from functools import cache


@cache
def f(a, b, k):
    if a == b:
        return 0, 0
    if a not in data or k == 0:
        return float('inf'), float('inf')
    min_len, s = float('inf'), 0
    for v, w in data[a]:
        cur_len, cur_s = f(v, b, k - 1)
        if cur_len + w < min_len:
            min_len = cur_len + w
            s = a + cur_s
    return min_len, s


data = {}
with open('23data/23-1.txt') as fin:
    for line in fin:
        u, v, w = line.split()
        data[int(u)] = data.get(int(u), []) + [(int(v), float(w))]
min_len, s = f(1, 100, 6)
print(s - 1)  # -1, потому что не нужно считать стартовую вершину
# print(min_len)
