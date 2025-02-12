with open('24data/k7-84.txt') as f:
    s = f.read().strip()

max_len = 0
cur_len = 0
for c in s:
    if c == 'C':
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 0
print(max_len)
