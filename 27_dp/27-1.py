s = 0
min_r = 10**9
with open(r'C:\Users\PC\Documents\ЕГЭ\Поляков\27data\1\27-1b.txt') as f:
    for _ in range(int(f.readline())):
        a, b = map(int, f.readline().split())
        s += min(a, b)
        if abs(a - b) % 3:
            min_r = min(min_r, abs(a - b))
if s % 3 == 0:
    s += min_r
print(s)