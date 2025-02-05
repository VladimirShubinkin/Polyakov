with open('24data/24-263.txt') as f:
    s = f.read().strip()
lines = s.split('Y')
max_len = 0
for i in range(len(lines) - 150):
    cur_len = len('Y'.join(lines[i:i+151]))
    max_len = max(max_len, cur_len)
print(max_len)
