from itertools import product

count = 0
for p in product(range(7), repeat=5):
    if p[0] != 0 and p[0] % 2 == 0 and p[-1] >= 3 and p.count(4) <= 1:
        count += 1
print(count)

print(2 * 6**3 * 3 + 6**3 * 3 + 3 * 2 * 6**2 * 3 + 2 * 6**3)
