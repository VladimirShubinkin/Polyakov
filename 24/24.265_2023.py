with open('24data/24-263.txt') as f:
    s = f.read().strip()
positions = [-1]
for i in range(len(s)):
    if s[i] == 'Y':
        positions.append(i)
positions.append(len(s))
max_len = 0
for i in range(151, len(positions)):
    cur_len = positions[i] - positions[i - 151] - 1
    max_len = max(cur_len, max_len)
print(max_len)
