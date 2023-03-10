for n in range(51, 10**6, 51):
    s = str(n)
    if s[:2] == '12' and '45' in s[2:]:
        print(n, n // 51)
