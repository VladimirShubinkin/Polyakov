'''
9)	В текстовом файле k7-44.txt находится цепочка из символов латинского алфавита A, B, C.
Найдите длину самой длинной подцепочки, состоящей из символов C.
'''

# 1
with open('24data/k7-44.txt') as f:
    s = f.read().strip()

count = 0
max_count = 0
for c in s:
    if c == 'C':
        count += 1
    else:
        count = 0
    max_count = max(max_count, count)
print(max_count)

# 2
with open('24data/k7-44.txt') as f:
    s = f.read().strip()

s = s.replace('A', ' ').replace('B', ' ')
lines = s.split()
max_seq = max(lines, key=len)
print(len(max_seq))

# 3
import re

with open('24data/k7-44.txt') as f:
    s = f.read().strip()

pattern = r'C+'
lines = re.findall(pattern, s)
max_seq = max(lines, key=len)
print(len(max_seq))

# 4
import re

with open('24data/k7-44.txt') as f:
    s = f.read().strip()

pattern = r'A|B'
lines = re.split(pattern, s)
max_seq = max(lines, key=len)
print(len(max_seq))

# 5
with open('24data/k7-44.txt') as f:
    s = f.read().strip()
ss = 'C'
while ss in s:
    ss += 'C'
print(len(ss) - 1)
