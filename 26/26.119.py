with open('26data/26-119.txt') as f:
    n, l, m = map(int, f.readline().split())
    times = []
    for line in f.readlines():
        t0, dt, mark = line.split()
        times.append((int(t0), int(t0) + int(dt), mark))

times.sort()
places_A = [0]*l
places_B = [0]*m
count_B = 0
count_no_place = 0
for t0, t1, mark in times:
    if mark == 'A':
        for i in range(l):
            if t0 >= places_A[i]:
                places_A[i] = t1
                break
        else:
            for i in range(m):
                if t0 >= places_B[i]:
                    places_B[i] = t1
                    break
            else:
                count_no_place += 1
    else:
        for i in range(m):
            if t0 >= places_B[i]:
                places_B[i] = t1
                count_B += 1
                break
        else:
            count_no_place += 1
print(count_B, count_no_place)
