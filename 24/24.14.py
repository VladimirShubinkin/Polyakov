'''
14)	В текстовом файле k7-80.txt находится цепочка из символов латинского алфавита A, B, C.
Найдите длину самой длинной подцепочки, состоящей из символов C.
'''

with open('24data/k7-80.txt') as f:
    s = f.read().strip()

# 1
cur_len = 0
max_len = 0
for c in s:
    if c == 'C':
        cur_len += 1
    else:
        cur_len = 0
    max_len = max(max_len, cur_len)
print(max_len)

# 2
s1 = s.replace('A', ' ').replace('B', ' ')
a = s1.split()
print(len(max(a, key=len)))

# 3
ss = 'C'
while ss in s:
    ss += 'C'
print(len(ss) - 1)
