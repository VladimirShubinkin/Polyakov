with open('24-153.txt') as f:
    s = f.read().strip()

min_len = 10**6
p = -10**6
for i in range(len(s)):
    if s[i] == 'A':
        p = i
    elif s[i] == 'F':
        length = i - p + 1
        if length > 2:
            min_len = min(min_len, length)
print(min_len)
