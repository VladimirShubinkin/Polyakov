def get_prime_divisors(n):
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return [d] + get_prime_divisors(n // d)
    return [n]


n = 8_007_494_154
c = 0
while c < 5:
    n += 1
    prime_divisors = get_prime_divisors(n)
    if len(prime_divisors) > 1:
        m = min(prime_divisors) + max(prime_divisors)
    else:
        m = 0
    if m > 80_000 and len(get_prime_divisors(m)) == 1 and str(m).count('567') == 1:
        c += 1
        print(n, m)
