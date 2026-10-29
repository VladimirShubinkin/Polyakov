from functools import cache


@cache
def f(a, b):
    if a == b:
        return 0
    if a not in data:
        return float('inf')
    min_dist = float('inf')
    for v, w in data[a]:
        min_dist = min(min_dist, f(v, b) + w)
    return min_dist


data = {}
with open('23_32025.txt') as fin:
    for line in fin.readlines():
        u, v, w = line.split()
        data[u] = data.get(u, []) + [(v, float(w))]
print(int(f('4', '100')))
