def f(a):
    for x in range(1000):
        for y in range(1000):
            if not(((x <= 9) <= (x * x <= a))
                   and ((y * y <= a) <= (y <= 10))):
                return False
    return True


a = 1000
while not f(a):
    a -= 1
print(a)
