with open('./26data/26-129.txt') as f:
    n = int(f.readline())
    details = []
    for i in range(1, n + 1):
        grinding, coloring = map(int, f.readline().split())
        details.append((i, 'G', grinding))
        details.append((i, 'C', coloring))
details.sort(key=lambda t: t[2])

used = set()
grinding_count = 0
last_ind = -1
last_mark = ''
for i, mark, time in details:
    if i not in used:
        used.add(i)
        grinding_count += mark == 'G'
        last_ind = i
        last_mark = mark
print(last_ind, grinding_count - (last_mark == 'G'))
