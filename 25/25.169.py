def is_prime(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def primes_sum(n):
    result = 0
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            if is_prime(d):
                result += d
            if n // d != d and is_prime(n // d):
                result += n // d
    return result


n = 250_001
count = 0
while count < 5:
    s = primes_sum(n)
    if s != 0 and s % 17 == 0:
        print(n, s)
        count += 1
    n += 1
