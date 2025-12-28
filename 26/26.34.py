with open('26data/26-j6.txt') as f:
    n, *a = map(int, f.readlines())
cur_v = sum(a)
v = 0.9 * cur_v
a.sort(reverse=True)
for i in range(len(a)):
    cur_v -= 0.2 * a[i]
    if cur_v <= v:
        print(len(a) - i - 1)
        left, right = i, i + 1
        break

cur_v = cur_v - 0.2 * a[right]
while left > 0 and cur_v + 0.2 * a[left] <= v:
    left -= 1
print(a[left + bool(left)])
