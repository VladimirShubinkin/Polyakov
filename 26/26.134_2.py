with open('files/26-134.txt') as f:
    n, t = map(int, f.readline().split())
    a = []
    for line in f.readlines():
        t0, dt, cat = line.split()
        a.append((int(t0), int(dt), cat))
cats = 'GWM'
a.sort()
que = {'G': [], 'W': [], 'M': []}
counter = {'G': 0, 'W': 0, 'M': 0}
first = a.pop(0)
counter[first[-1]] += 1
free = sum(first[:2])
last = first[-1]
for t_start, dt, cat in a:
    if free > t:
        break
    for c in cats:
        while que[c] and free < t_start:
            free += que[c].pop(0)
            counter[c] += 1
            last = c
    if not any(que.values()):  # когда очередь иссякла, у начальника перерыв
        free = max(t_start, free)
    que[cat].append(dt)

print(sum(counter.values()))
print(counter[last])
