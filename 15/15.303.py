def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((3 * y - x > a) or (2 * x + 3 * y < 30)
                   or (2 * y - x < -31)):
                return False
    return True


a = 1000
while not f(a):
    a -= 1
print(a)
