from itertools import permutations
from time import perf_counter

t0 = perf_counter()
with open('26_2653.txt') as f:
    n, *a = map(int, f.readlines())
a.sort()
max_weight = sum(a)
weights = [0]*(max_weight + 1)
s = 0
for m in a:
    new_weights = weights[:]
    for w in range(1, s + 1):
        if weights[w]:
            new_weights[w + m] = 1
    new_weights[m] = 1
    weights = new_weights[:]
    s += m
print(weights.count(0) - 1)
for i in range(max_weight - 1, -1, -1):
    if weights[i] == 0:
        print(i)
        break
print(perf_counter() - t0)
