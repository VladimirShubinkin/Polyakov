'''
17)	В текстовом файле k7-94.txt находится цепочка из символов латинского алфавита A, B, C.
Найдите длину самой длинной подцепочки, состоящей из символов C.
'''

# 1
with open('24data/k7-94.txt') as f:
    s = f.read().strip()
cur_count = 0
max_count = 0
for c in s:
    if c == 'C':
        cur_count += 1
        max_count = max(max_count, cur_count)
    else:
        cur_count = 0
print(max_count)

# 2
with open('24data/k7-94.txt') as f:
    s = f.read().strip()

s = s.replace('A', ' ').replace('B', ' ')
lines = s.split()
max_seq = max(lines, key=len)
print(len(max_seq))

# 3
import re

with open('24data/k7-94.txt') as f:
    s = f.read().strip()
pattern = r'C+'
lines = re.findall(pattern, s)
max_seq = max(lines, key=len)
print(len(max_seq))

# 4
import re

with open('24data/k7-94.txt') as f:
    s = f.read().strip()
pattern = r'A|B'
lines = re.split(pattern, s)
max_seq = max(lines, key=len)
print(len(max_seq))

# 5
with open('24data/k7-94.txt') as f:
    s = f.read().strip()
line = 'C'
while line in s:
    line += 'C'
print(len(line) - 1)
