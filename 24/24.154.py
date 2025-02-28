with open('24data/24-153.txt') as f:
    s = f.read().strip()

min_seq = ''
min_len = len(s)
prev = -len(s)
for i in range(len(s)):
    if s[i] == 'D':
        if 2 < i - prev + 1 < min_len:
            min_len = i - prev + 1
            min_seq = s[prev:i + 1]
        prev = i
print(min_len)
print(min_seq)
