def f(a):
    for x in range(1, 80):
        if not((x % 2 == 0) <= (x % 3 != 0) or (x + a >= 80)):
            return False
    return True


a = 1
while not f(a):
    a += 1
print(a)
