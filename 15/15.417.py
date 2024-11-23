def f(x, a):
    return (x & 87 == 0) <= ((x & 31 != 0) <= (x & a != 0))


def is_good(a):
    for x in range(1, 1000):
        if not f(x, a):
            return False
    return True


a = 1
while not is_good(a):
    a += 1
print(a)
