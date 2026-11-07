with open('17_17558.txt') as f:
    a = [int(x) for x in f.readlines()]

c_32 = 0
for x in a:
    if x % 32 == 0:
        c_32 += 1

count = 0
max_s = -200_000
for i in range(len(a) - 1):
    if a[i] < 0 or a[i + 1] < 0:
        s = a[i] + a[i + 1]
        if s < c_32:
            count += 1
            max_s = max(max_s, s)
print(count, max_s)
