with open('24data/k7b-2.txt') as f:
    s = f.read().strip()

dbac = 'DBAC'
j = 0
cur_len = 0
max_len = 0
for c in s:
    if c == dbac[j]:
        cur_len += 1
        j = (j + 1) % len(dbac)
    elif c == dbac[0]:
        cur_len = 1
        j = 1
    else:
        cur_len = 0
        j = 0
    max_len = max(cur_len, max_len)
print(max_len)
