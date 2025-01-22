with open(r'C:\Users\PC\Documents\ЕГЭ\Поляков\27data\52\27-52b.txt') as f:
    a = [int(x) for x in f.readlines()[1:]]
maxs = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in a:
    r = x % 3
    maxs[r].append(x)
    maxs[r].sort()
    del maxs[r][0]
print(max(sum(maxs[0]), sum(maxs[1]), sum(maxs[2]), maxs[0][2] + maxs[1][2] + maxs[2][2]))