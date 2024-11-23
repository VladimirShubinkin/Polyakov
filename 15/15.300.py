def f(x, y, a):
    return y - x > a or x + 4 * y > 40 or y - 2 * x < -35


def is_good(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not f(x, y, a):
                return False
    return True


a = 1000
while not is_good(a):
    a -= 1
print(a)
