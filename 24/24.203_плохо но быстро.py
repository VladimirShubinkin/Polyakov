from time import perf_counter

t0 = perf_counter()

with open('24data/24-203.txt') as f:
    s = f.read().strip()

count = 0
for i in range(len(s) - 1):
    letters = {s[i], s[i + 1]}
    j = i + 2
    while j < len(s):
        letters.add(s[j])
        if len(letters) < 3:
            count += 1
            j += 1
        else:
            break
print(count)

print(perf_counter() - t0)
