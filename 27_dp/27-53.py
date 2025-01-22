with open('files/27-53b.txt') as f:
    n, *a = map(int, f.readlines())

mins = [[10**9, 10**9, 10**9],
        [10**9, 10**9, 10**9],
        [10**9, 10**9, 10**9]]
for x in a:
    mins[x % 3].append(x)
    mins[x % 3].sort()
    del mins[x % 3][-1]
print(min(sum(mins[0]), sum(mins[1]), sum(mins[2]), mins[0][0] + mins[1][0] + mins[2][0]))
