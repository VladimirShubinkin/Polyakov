from string import digits, ascii_uppercase

with open(r'C:\Users\PC\Documents\ЕГЭ\Поляков\17data\17-243.txt') as f:
    a = [int(x) for x in f.readlines()]


def dec_to_n(x, n):
    res = ''
    cifs = digits + ascii_uppercase
    while x:
        res = cifs[x % n] + res
        x = x // n
    return res


mx = max(filter(lambda x: x % 173 == 0, a))
cnt = 0
mn = 20000

for i in range(len(a) - 1):
    if a[i] > mx or a[i + 1] > mx:
        if '22' in dec_to_n(a[i], 3) or '22' in dec_to_n(a[i+1], 3):
            cnt += 1
            mn = min(mn, a[i] + a[i+1])

print(cnt, mn)
