def f(x, y, a):
    return (2 * x + 3 * y != 72) or (a > x and a > y)


def is_good(a):
    for x in range(1000):
        for y in range(1000):
            if not f(x, y, a):
                return False
    return True


a = 1
while not is_good(a):
    a += 1
print(a)
