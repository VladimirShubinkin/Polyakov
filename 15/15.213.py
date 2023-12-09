def f(x, a):
    return ((((x & 56 != 0) <= (x & 18 != 0)) or (x & a != 0))
            <= ((x & 18 == 0) and (x & a == 0) and (x & 43 != 0)))

def is_good(a):
    for x in range(1, 1000):
        if f(x, a):
            return False
    return True

a = 50
while not is_good(a):
    a += 1
print(a)
