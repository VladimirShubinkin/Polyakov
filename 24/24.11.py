'''
11)	В текстовом файле k7-53.txt находится цепочка из символов латинского алфавита A, B, C.
Найдите длину самой длинной подцепочки, состоящей из символов C.
'''

with open('24data/k7-53.txt') as f:
    s = f.read().strip()

# 1 способ
cur_len = 0
max_len = 0
for c in s:
    if c == 'C':
        cur_len += 1
    else:
        cur_len = 0
    max_len = max(cur_len, max_len)
print(max_len)

# 2 способ
new_s = s.replace('B', 'A')
a = new_s.split('A')
max_len = len(max(a, key=len))
print(max_len)

# 3 способ
ss = 'C'
while ss in s:
    ss += 'C'
print(len(ss) - 1)
