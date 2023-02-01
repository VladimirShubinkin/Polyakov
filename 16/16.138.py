from sys import setrecursionlimit
setrecursionlimit(5000)

from functools import cache


@cache
def f(n):
    if n < 4:
        return 1
    if n % 2:
        return n
    return f(n - 1) + f(n - 2) + f(n - 3)


print(f(2254) - f(2252))
