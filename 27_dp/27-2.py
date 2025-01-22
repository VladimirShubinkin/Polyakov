s = 0
min11 = min12 = min21 = min22 = 10**9
with open(r'C:\Users\PC\Documents\ЕГЭ\Поляков\27data\2\27-2b.txt') as f:
    for _ in range(int(f.readline())):
        a, b = map(int, f.readline().split())
        s += max(a, b)
        r = abs(a - b)
        ost = r % 3
        if ost == 1:
            if r < min11:
                min11, min12 = r, min11
            elif r < min12:
                min12 = r
        elif ost == 2:
            if r < min21:
                min21, min22 = r, min21
            elif r < min22:
                min22 = r
if s % 3 == 1:
    s -= min(min11, min21 + min22)
elif s % 3 == 2:
    s -= min(min21, min11 + min12)
print(s)