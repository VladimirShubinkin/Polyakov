def f(x, y, a):
    return (3 * y - x > a) or (2 * x + 3 * y < 30) or (2 * y - x < -31)

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
