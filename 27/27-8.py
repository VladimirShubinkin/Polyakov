with open('files/27-8b.txt') as f:
    n, *a = map(int, f.readlines())

min_s = 10**7
cur_min = 10**4
for i in range(5, len(a)):
    cur_min = min(cur_min, a[i - 5])
    min_s = min(min_s, a[i]**2 + cur_min**2)
print(min_s)
