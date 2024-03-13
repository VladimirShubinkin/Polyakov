def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    if a % 2 == 0:
        return f(a + 1, b) + f(a * 3 // 2, b)
    return f(a + 1, b)


print(f(2, 22))


def g(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    if a % 2 == 0:
        return g(a + 1, b) + g(a * 1.5, b)
    return g(a + 1, b)


print(g(2, 22))
