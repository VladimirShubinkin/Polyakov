with open('26_6_23216.txt') as f:
    k, m = map(int, f.readline().split())
    n = int(f.readline())
    times = []
    for line in f.readlines():
        t0, t1 = map(int, line.split())
        times.append((t0, t1))
times.sort()
boxes = [-1] * k
count = 0
for t0, t1 in times:
    for i in range(k):
        if t0 > boxes[i]:
            boxes[i] = t1
            count += 1
            last = i + 1
            break
print(count * m, last)
