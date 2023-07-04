'''18)	В текстовом файле k7-96.txt находится цепочка из символов латинского алфавита A, B, C.
Найдите длину самой длинной подцепочки, состоящей из символов C.'''

with open('24data/k7-96.txt') as f:
    s = f.read().strip()

# Вариант 1. Конечный автомат
cur_len = 0
max_len = 0
for c in s:
    if c == 'C':
        cur_len += 1
    else:
        cur_len = 0
    max_len = max(max_len, cur_len)
print(max_len)

# Вариант 2. split
s1 = s.replace('B', 'A')
c_sequenses = s1.split('A')
max_len = len(max(c_sequenses))
print(max_len)

# Вариант 2. while
c_sequens = 'C'
while c_sequens in s:
    c_sequens += 'C'
print(len(c_sequens) - 1)
