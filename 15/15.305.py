def f(x):
    return ((x not in b) <= (x not in a)) and ((x not in c) <= (x in b))


a = range(30, 51)
b = range(40, 47)
for n in range(60, -1, -1):
    c = range(n, 62)
    count = 0
    for x in range(1001):
        count += f(x)
    if count > 25:
        print(n)
        break
