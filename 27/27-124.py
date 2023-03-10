with open('files/27-124b.txt') as f:
    n, k, v, m = map(int, f.readline().split())
    a = [0]*k
    for _ in range(n):
        km, kg = map(int, f.readline().split())
        a[km % k] = kg // v + bool(kg % v)
# считаем ответ для нулевого километра
s = 0
for i in range(-m, m + 1):
    s += a[i]
max_s = s if a[0] else 0
# "переставляем" почтовое отделение
for i in range(1, k):
    s = s - a[i - m] + a[(i + m) % k]
    if a[i]:
        max_s = max(max_s, s)
print(max_s)
