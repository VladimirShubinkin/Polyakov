def f(a):
    for x in range(1, 10001):
        if not (((x % a == 0) and (x % 16 != 0)) <= (x % 23 == 0)):
            return False
    return True


a = 1
while not f(a):
    a += 1
print(a)
