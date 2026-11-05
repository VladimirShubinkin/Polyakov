def factorize(n):
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return [d] + factorize(n // d)
    return [n]


n = 6_651_220
c = 0
while c < 5:
    n += 1
    primes = factorize(n)
    if len(primes) == 2 and str(primes[0]).count('2') == 1 and str(primes[1]).count('2') == 1:
        print(n, max(primes))
        c += 1
