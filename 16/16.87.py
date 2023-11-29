def f(n):
    if n < 2:
        return 1
    if n % 3 == 0:
        return f(n // 3) + 1
    return f(n - 2) + 5


count = 0
for n in range(1, 100_001):
    count += f(n) == 55
print(count)
