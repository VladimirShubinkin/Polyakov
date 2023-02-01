def f(a):
    for x in range(1, 201):
        for y in range(1, 201):
            if not((x + y <= 22) or (y <= x - 6) or (y >= a)):
                return False
    return True


a = 100
while not f(a):
    a -= 1
print(a)
