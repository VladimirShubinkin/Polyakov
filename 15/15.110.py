def f(x):
    return ((x in a) <= (x in p)) and ((x in q) <= (x not in a))


p = range(2, 21, 2)
q = range(5, 51, 5)
a = set(range(1, 10_000))
for x in range(1, 10_000):
    if not f(x):
        a.remove(x)
print(len(a))
