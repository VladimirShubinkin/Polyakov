with open('26data/26-174.txt') as f:
    n = int(f.readline())
    points = {}
    for line in f.readlines():
        s, p = map(int, line.split())
        points[p] = points.get(p, set()) | {s}

min_point = 10**9
max_count = 0
for point, sportsmans in points.items():
    s_numbers = sorted(sportsmans)
    count = 1
    for i in range(1, len(s_numbers)):
        if s_numbers[i] - s_numbers[i - 1] == 1:
            count += 1
            if count > max_count:
                max_count = count
                min_point = point
            elif count == max_count:
                min_point = min(min_point, point)
        else:
            count = 1
print(max_count, min_point)
