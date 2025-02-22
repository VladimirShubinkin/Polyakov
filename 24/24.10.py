'''10)	В текстовом файле k7-45.txt находится
цепочка из символов латинского алфавита A, B, C.
Найдите длину самой длинной подцепочки,
состоящей из символов C.'''

#1
with open('24data/k7-45.txt') as f:
    s = f.read().strip()
count = 0
max_count = 0
for c in s:
    if c == 'C':
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print(max_count)

#2
from string import ascii_uppercase

with open('24data/k7-45.txt') as f:
    s = f.read().strip()
for letter in ascii_uppercase:
    if letter != 'C':
        s = s.replace(letter, ' ')
a = s.split()
print(len(max(a, key=len)))

#3
with open('24data/k7-45.txt') as f:
    s = f.read().strip()
ss = 'C'
while ss in s:
    ss += 'C'
print(len(ss) - 1)

#4
import re

with open('24data/k7-45.txt') as f:
    s = f.read().strip()

print(len(max(re.findall(r'C+', s), key=len)))
