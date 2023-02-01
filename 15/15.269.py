def f(a):
    for x in range(1000):
        for y in range(1000):
            if (((x < a) and (x * x >= 120))
                   or ((y * y <= 20) and (y > a))):
                return True
    return False


c = 0
for a in range(1, 1000):
    if not f(a):
        c += 1
print(c)
