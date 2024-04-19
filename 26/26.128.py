with open('./26data/26-128.txt') as f:
    n = int(f.readline())
    times = []
    for i in range(n):
        t_start, t_end = map(int, f.readline().split())
        times.append((t_start, t_end))
times.sort(key=lambda p: p[1])

timeline = 0
prev_end = 0
count = 0
for t_start, t_end in times:
    if t_start >= timeline:
        count += 1
        prev_end = timeline
        timeline = t_end
print(count)
for t_start, t_end in times[::-1]:
    if t_start >= prev_end:
        print(t_end)
        break
