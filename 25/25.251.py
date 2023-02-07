def f(n):
    if n % 2 == 0:
        return 0
    a = []
    for d in range(3, int(n**0.5) + 1):
        if n % d == 0:
            a.append(d)
            if n // d != d:
                a.append(n // d)
    if sum(a) % 2 == 0:
        return 0
    return len(a) + 2


a = 800_001
c = 0
while c < 6:
    m = f(a)
    if m > 10:
        print(a, m)
        c += 1
    a += 1
