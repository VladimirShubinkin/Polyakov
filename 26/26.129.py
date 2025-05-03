with open('./26data/26-129.txt') as f:
    n = int(f.readline())
    grinding_count = 0
    details = []
    for i in range(1, n + 1):
        grinding, coloring = map(int, f.readline().split())
        if grinding < coloring:
            details.append((grinding, i, 'G'))
            grinding_count += 1
        else:
            details.append((coloring, i, 'C'))

details.sort()
last = details[-1]

print(last[1], grinding_count - (last[-1] == 'G'))
