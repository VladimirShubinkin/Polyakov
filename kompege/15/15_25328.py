def f(x, A, B, C):
    return ((x not in B) or (x not in A)) <= (x not in C)


def is_good(y):
    C = get_set(y)
    if not C:
        return False
    for x in range(10_000):
        if not f(x, A, B, C):
            return False
    return True


def get_set(n):
    divisors = set()
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)
    return divisors


A = range(2, 51)
B = get_set(140)
y = 10_000
while not is_good(y):
    y -= 1
print(y)