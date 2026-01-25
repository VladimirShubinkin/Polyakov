with open('26data/26-90.txt') as f:
    n, *costs = map(int, f.readlines())

costs.sort()
s1 = sum(costs[-n//4:]) * 0.5 + sum(costs[:-n // 4])
s2 = sum(costs[:n // 4]) * 0.5 + sum(costs[n // 4:])
print(s1, s2)
