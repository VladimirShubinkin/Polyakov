with open('24-157.txt') as f:
    s = f.read().strip()

pos = -1
max_len = 0
for i in range(len(s) - 1):
    if s[i] + s[i + 1] in ('PR', 'RP'):
        max_len = max(max_len, i - pos)
        pos = i
max_len = max(max_len, len(s) - 1 - pos)
print(max_len)
