from functools import cache


@cache
def f(a, b):
    if a == b:
        return 0
    if a not in data:
        return float('inf')
    return min(f(v, b) + w for v, w in data[a])


data = {}
with open('23data/23-1.txt') as fin:
    for line in fin.readlines():
        u, v, w = line.split()
        if u not in ('173', '633'):
            data[u] = data.get(u, []) + [(v, float(w))]
print(f('1', '100'))
