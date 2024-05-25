with open('files/26-134.txt') as f:
    n, t = map(int, f.readline().split())
    a = []
    for line in f.readlines():
        t0, dt, cat = line.split()
        a.append((int(t0), int(dt), cat))
cats = 'GWM'
# a.sort(key=lambda tri: (tri[0], cats.index(tri[-1])))
a.sort()
print(a)
que = {'W': [], 'G': [], 'M': []}
counter = {'W': 0, 'G': 0, 'M': 0}
free = 0
flag = True
for ind, (t_start, dt, cat) in enumerate(a):
    if t_start + dt < t:
        cur_cats = cats[:cats.index(cat) + 1]
        while any(que[i] for i in cur_cats) and flag:
            for c in cur_cats:
                while que[c]:
                    counter[c] += 1
                    if free + que[c][0] < t:
                        free = free + que[c].pop(0)
                    else:
                        cat_end = c
                        flag = False
                        break
                if not flag:
                    break
        if not flag:
            break
        if t_start >= free:
            free = t_start + dt
            counter[cat] += 1
            cat_end = cat
        else:
            que[cat].append(dt)
    else:
        cur_cats = cats[:cats.index(cat) + 1]
        while any(que[i] for i in cur_cats) and flag:
            for c in cur_cats:
                while que[c]:
                    counter[c] += 1
                    if free + que[c][0] < t:
                        free = free + que[c].pop(0)
                    else:
                        cat_end = c
                        flag = False
                        break
                if not flag:
                    break
        if not flag:
            break
        cat_end = cat
        counter[cat] += 1
    print(ind, cur_cats, que, counter, free)
print(sum(counter.values()), counter[cat_end])
print(que)
print(counter)