with open('27-144B.txt') as f:
    n, k, *a = map(int, f.readlines())

r25 = [0]*25
ans = 0
for i in range(k, len(a)):
    r25[a[i - k] % 25] += 1
    r = a[i] % 25
    ans += r25[(25 - r) % 25]
print(ans)
