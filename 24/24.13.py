with open('24data/k7-75.txt') as f:
    s = f.read().strip()

# 1
max_len = 0
cur_len = 0
for i in range(len(s)):
    if s[i] == 'C':
        cur_len += 1
    else:
        cur_len = 0
    max_len = max(max_len, cur_len)
print(max_len)

# 2
from string import ascii_uppercase
s1 = s
for char in ascii_uppercase:
    if char != 'C':
        s1 = s1.replace(char, ' ')
a = s1.split()
print(len(max(a, key=len)))

# 3
ss = 'C'
while ss in s:
    ss += 'C'
print(len(ss) - 1)
