def f(n):
    global s
    s += n - 5
    if n > 1:
        s += n + 8
        f(n - 2)
        f(n - 3)


n = 1
s = 0
while not s > 3_200_000:
    n += 1
    s = 0
    f(n)

print(n, s)
