with open('24_18284.txt') as f:
    s = f.read().strip()
max_L = -10**8
max_LO = -10**8
max_LOV = -10**8
min_len = 10**8
for i in range(len(s)):
    if s[i] == 'L':
        max_L = i
    if s[i] == 'O':
        max_LO = max_L
    if s[i] == 'V':
        max_LOV = max_LO
    if s[i] == 'E':
        min_len = min(min_len, i - max_LOV + 1)
print(min_len)

