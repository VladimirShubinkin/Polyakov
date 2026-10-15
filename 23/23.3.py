from functools import cache


@cache
def f(a, b):
    if a == b:
        return 0
    if a not  in data:
        return float('inf')
    min_len = float('inf')
    for v, w in data[a]:
        min_len = min(min_len, w + f(v, b))
    return min_len


data = {}
with open('23data/23-1.txt') as fin:
    for line in fin.readlines():
        u, v, w = line.split()
        if u != '633':
            data[u] = data.get(u, []) + [(v, float(w))]
print(int(f('1', '100')))
