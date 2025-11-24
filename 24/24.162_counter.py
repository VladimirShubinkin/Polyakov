from collections import Counter

with open('24data/24-s1.txt') as f:
    lines = f.read().splitlines()

min_count = 10**6
s = ''
for line in lines:
    count = 0
    for i in range(len(line) - 1):
        if ord(line[i + 1]) - ord(line[i]) == 1:
            count += 1
    if 0 < count < min_count:
        min_count = count
        s = line

max_letter = Counter(s).most_common()[0][0]

with open('24data/24-s1.txt') as f:
    count = f.read().count(max_letter)
print(max_letter, count)

