def f(n1, n2):
    if n1 == n2:
        return 0
    if n1 >= 10_000:
        return n1
    if n1 % 3 == 0:
        return n1 + f(n1 // 3, n2)
    return 2 * n1  + f(n1 + 3, n2)


print(f(999, 46))

print(999 + 333 + 111 + 2*37 + 2*40 + 2*43)
