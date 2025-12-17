from math import ceil

with open('26data/26-s1.txt') as f:
    n, *costs = map(int, f.readlines())
costs.sort()
cheaps = [cost for cost in costs if cost <= 100]
expensive = [cost for cost in costs if cost > 100]
mid = len(expensive) // 2
s = sum(cheaps) + sum(expensive[mid:]) + sum(expensive[:mid]) * 0.9
print(ceil(s), expensive[mid - 1])
