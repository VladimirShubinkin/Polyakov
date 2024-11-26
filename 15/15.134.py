def f(x):
    return ((x in a) <= (x in p)) or ((x not in q) <= (x not in a))


p = range(2, 21, 2)
q = range(5, 51, 5)
a = set(range(1000))
for x in range(1000):
    if not f(x):
        a.remove(x)
print(len(a))
print(a)
