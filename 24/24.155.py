with open('24data/24-153.txt') as f:
    s = f.read().strip()
if 'AAF' in s:
    print(3)
    exit()
min_len = 10**9
pos_a = 10**9
for i in range(len(s)):
    if s[i] == 'A':
        pos_a = i
    elif s[i] == 'F':
        if 2 < i - pos_a + 1 < min_len:
            min_len = i - pos_a + 1
            start = pos_a
            fin = i
print(min_len)
print(s[start:fin+1])
