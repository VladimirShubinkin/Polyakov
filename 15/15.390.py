def f(x, a):
    return ((110 % a == 0) and
            ((x % 80 == 0 and x % 75 == 0) <= (x % a == 0)))


def is_good(a):
    for x in range(1, 100000):
        if not f(x, a):
            return False
    return True


a = 100000
while not is_good(a):
    a -= 1
print(a)
