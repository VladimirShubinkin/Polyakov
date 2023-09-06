def f(x, y, a):
    return 5 * y + 4 * x > a or 2 * x + 3 * y < 92 or y - 2 * x < -150


def is_good(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not f(x, y, a):
                return False
    return True


a = 1000
while not is_good(a):
    a -= 1
print(a)