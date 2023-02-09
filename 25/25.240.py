def sum_divs(n):
    s = 0
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            s += d
            if n // d != d:
                s += n // d
    return s


a = []
c = 0
n = 10**7
while c < 5:
    s = str(n)
    if s[0] == '9' and s[-1] == '7' and '55' in s[2:-1]:
        c += 1
        a.append([n, sum_divs(n) % 21])
    n -= 1
a.sort()
print(*a, sep='\n')
