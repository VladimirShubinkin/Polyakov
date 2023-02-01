def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((2 * y + 5 * x < a) or (2 * x + 4 * y > 100)
                   or (3 * x - 2 * y > 70)):
                return False
    return True


a = 1
while not f(a):
    a += 1
print(a)
