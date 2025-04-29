from time import perf_counter

t0 = perf_counter()

with open('26data/26-53.txt') as f:
    n, *a = map(int, f.readlines())

count = 0
max_aver = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] % 2 and a[j] % 2:
            aver = (a[i] + a[j]) // 2
            if aver in a:
                count += 1
                max_aver = max(max_aver, aver)
print(count, max_aver)

print(perf_counter() - t0)  # 234 секунды!
