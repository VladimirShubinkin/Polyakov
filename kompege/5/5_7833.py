def to_3(n):
    result = ''
    while n:
        result += str(n % 3)
        n //= 3
    return result[::-1]


r_min = 10**9
ans = 0
for n in range(10, 1000):
    n3 = to_3(n)
    if n % 2 == 0:
        n3 += n3[-2] + n3[-1]
    else:
        s = sum(map(int, n3))
        n3 += to_3(s)
    r = int(n3, 3)
    if r < r_min:
        r_min = r
        ans = n
print(ans)
