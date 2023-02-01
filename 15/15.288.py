def f(a):
    for x in range(1000):
        for y in range(1000):
            if not(2 * y + 3 * x < a or x + y > 40):
                return False
    return True


a = 1
while not f(a):
    a += 1
print(a)
