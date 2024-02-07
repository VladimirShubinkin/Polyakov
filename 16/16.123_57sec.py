from time import perf_counter
from functools import cache


@cache
def f(n):
    if n == 0:
        return 8
    if n % 3 == 0:
        return 5 + f(n // 3)
    return f(n // 3)


t0 = perf_counter()

c = 0
for i in range(1, 100_000_000):
    if f(i) == 18:
        c += 1
print(c)

print(perf_counter() - t0)
