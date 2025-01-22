with open('files/27-123b.txt') as f:
    n, k, v = map(int, f.readline().split())
    a = [0]*k
    for _ in range(n):
        km, vol = map(int, f.readline().split())
        a[km % k] = vol // v + bool(vol % v)
price = 0
s_l = a[0]
s_r = 0
mid = k // 2
mid1 = k // 2 + 1 if k % 2 else k // 2
for i in range(1, k):
    if i <= mid:
        price += a[i] * i
        s_r += a[i]
    else:
        price += a[i] * (k - i)
        if i > mid1:
            s_l += a[i]
min_price = price if a[0] else 10**20
pos = 0
data = [[pos, price, s_l, s_r]]
for i in range(1, k):
    price = price + s_l - s_r
    mid1 = (mid1 + 1) % k
    mid = (mid + 1) % k
    s_l = s_l + a[i] - a[mid1]
    s_r = s_r + a[mid] - a[i]
    data.append([i, price, s_l, s_r])
    if a[i]:
        if price < min_price:
            min_price = price
            pos = i
print(min_price, 'pos =', pos)
with open('prices.txt', 'w') as tf:
    for line in data[10:]:
        tf.write(' '.join(map(str, line)) + '\n')