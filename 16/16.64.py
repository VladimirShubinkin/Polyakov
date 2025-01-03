def f(n):
    if n <= 18:
        return n + 3
    if n % 3 == 0:
        return n // 3 * f(n // 3) + n - 12
    return f(n - 1) + n * n + 5


count = 0
for n in range(1, 801):
    count += all(int(d) % 2 == 0 for d in str(f(n)))
print(count)
