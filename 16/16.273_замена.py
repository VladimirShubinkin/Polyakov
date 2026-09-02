def f(n):
    if n == 3236:
        return 1
    return n * f(n - 1)


print((f(3238) // 2 + f(3237)) / f(3236))
