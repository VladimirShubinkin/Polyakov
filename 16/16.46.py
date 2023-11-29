def f(n):
    if n <= 3:
        return n
    if n % 2 == 0:
        return 2 * n * n + f(n - 1)
    return n * n * n + n + f(n - 1)


n = 1
while f(n) < 10**7:
    n += 1
print(n - 1)
