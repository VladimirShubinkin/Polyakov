with open('files/27-150b.txt') as f:
    n, k, *a = map(int, f.readlines())
r = [0]*17
ans = 0
for x in a[:k+1]:
    ans += r[(17 - x % 17) % 17]
    r[x % 17] += 1
for i in range(k + 1, len(a)):
    r[a[i - (k + 1)] % 17] -= 1
    ans += r[(17 - a[i] % 17) % 17]
    r[a[i] % 17] += 1
print(ans)
