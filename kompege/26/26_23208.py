with open('26_23208.txt') as f:
    n = int(f.readline())
    times = []
    for i in range(n):
        g, c = map(int, f.readline().split())
        times.append((g, 'G', i + 1))
        times.append((c, 'C', i + 1))
times.sort()
used = set()
last = 0
g_count = 0
for t, act, ind in times:
    if ind not in used:
        used.add(ind)
        if act == 'G':
            g_count += 1
        last = ind
        last_act = act
print(last, g_count - (last_act == 'G'))
