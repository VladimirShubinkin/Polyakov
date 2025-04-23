from time import perf_counter

t0 = perf_counter()

with open('files/26-53.txt') as f:
    n, *a = map(int, f.readlines())

a.sort()

averages = []
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] % 2 and a[j] % 2:
            averages.append((a[i] + a[j]) // 2)
averages.sort()

count = 0
max_aver = 0
i = 0
for aver in averages:
    while i < n and aver > a[i]:
        i += 1
    if i < n and aver == a[i]:
        count += 1
        max_aver = aver
print(count, max_aver)

print(perf_counter() - t0)
