with open('26data/26-78.txt') as f:
    n, start, end = map(int, f.readline().split())
    times = []
    for line in f.readlines():
        t1, t2 = map(int, line.split())
        if t1 <= end and t2 >= start:
            times.append([t1, t2])
times.sort(key=lambda p: p[1])
border = start
count = ans2 = 0
while border < end:
    best = max(filter(lambda p: p[0] <= border, times), key=lambda p: p[1])
    count += 1
    if count == 1:
        ans2 = best[1] - start
    border = best[1]
print(count, ans2)
