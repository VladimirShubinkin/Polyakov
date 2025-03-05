with open('26data/26-62.txt') as f:
    n, m = map(int, f.readline().split())
    goods = []
    for line in f.readlines():
        cost, mark = line.split()
        goods.append([int(cost), mark])
goods.sort()
i = 0
count_q = 0
while m - goods[i][0] >= 0:
    m -= goods[i][0]
    if goods[i][1] == 'Q':
        count_q += 1
    i += 1
k = i - 1
while m + goods[k][0] - goods[i][0] >= 0:
    if goods[k][1] == 'Q':
        k -= 1
        continue
    if goods[i][1] == 'Z':
        i += 1
        continue
    m = m + goods[k][0] - goods[i][0]
    count_q += 1
    k -= 1
    i += 1
print(count_q, m)
