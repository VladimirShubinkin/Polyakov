from functools import cache


@cache
def f(a, b):
    if a == b:
        return 0
    if a not in dist_to:
        return float('inf')
    min_len = float('inf')
    for v, w in dist_to[a]:
        min_len = min(min_len, w + f(v, b))
    return min_len


dist_to = {}
with open('23data/23-1.txt') as fin:
    for line in fin.readlines():
        u, v, w = line.split()
        dist_to[u] = dist_to.get(u, []) + [(v, float(w))]
print(int(f('1', '4') + f('4', '100')))
