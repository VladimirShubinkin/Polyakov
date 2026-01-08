with open('26_23383.txt') as f:
    n = int(f.readline())
    points = {}
    for _ in range(n):
        s, p = map(int, f.readline().split())
        points[p] = points.get(p, set()) | {s}
max_count = 0
min_point = 10**6
for point, nums in points.items():
    numbers = sorted(nums)
    cur_count = 0
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1] + 1:
            cur_count += 1
            if cur_count > max_count:
                max_count = cur_count
                min_point = point
            elif cur_count == max_count:
                min_point = min(min_point, point)
        else:
            cur_count = 1
print(max_count, min_point)
