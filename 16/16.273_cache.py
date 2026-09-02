from functools import cache

@cache
def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)


for i in range(1, 3239):
    f(i)

print((f(3238) // 2 + f(3237)) / f(3236))
