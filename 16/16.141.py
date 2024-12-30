from functools import cache
from math import factorial


@cache
def f(n):
    if n >= 5000:
        return factorial(n)
    return 2 * f(n + 1) // (n + 1)


for i in range(5000, 3, -1):
    f(i)
print(1000 * f(7) / f(4))
