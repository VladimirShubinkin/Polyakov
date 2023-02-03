def sum_pow(s):
    n = len(s)
    return sum(map(lambda d: int(d)**n, s))


good = {}
bad = set()
with open('24-234.txt') as f:
    s = f.read().strip()
for i in range(len(s) - 6):
    for j in range(i, i + 6):
        ss = s[i:j + 1]
        if ss in good:
            good[ss] += 1
        elif ss in bad:
            continue
        elif sum_pow(ss) == int(ss):
            good[ss] = 1
        else:
            bad.add(ss)
max_num = max(good, key=int)
print(max_num)
print(good[max_num])
for key, val in sorted(good.items(), key=lambda pair: -int(pair[0])):
    print(key, val)
