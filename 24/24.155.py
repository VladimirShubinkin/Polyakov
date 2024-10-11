with open('24-153.txt') as f:
    s = f.read().strip()
min_len = 10**9
pos_a = (10**9, 10**9)
for i in range(len(s)):
    if s[i] == 'A':
        pos_a = (i, pos_a[0])
    elif s[i] == 'F':
        if 2 < i - pos_a[0] + 1 < min_len:
            min_len = i - pos_a[0] + 1
        if 2 < i - pos_a[1] + 1 < min_len:
            min_len = i - pos_a[1] + 1
print(min_len)

