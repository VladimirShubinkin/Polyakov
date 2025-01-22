with open('files/27-13b.txt') as f:
    n, *a = map(int, f.readlines())

k = k7 = k2 = k14 = 0
count = 0
for i in range(7, len(a)):
    if a[i - 7] % 14 == 0:
        k14 += 1
    if a[i - 7] % 7 == 0:
        k7 += 1
    if a[i - 7] % 2 == 0:
        k2 += 1
    k += 1
    if a[i] % 14 == 0:
        count += k
    elif a[i] % 2 == 0:
        count += k7
    elif a[i] % 7 == 0:
        count += k2
    else:
        count += k14
print(count)
