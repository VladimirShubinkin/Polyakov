def alg(s):
    while '>1' in s or '>2' in s or '>*' in s:
        if '>1' in s:
            s = s.replace('>1', '111>', 1)
        if '>2' in s:
            s = s.replace('>2', '1>', 1)
        if '>*' in s:
            s = s.replace('>*', '2>', 1)
    return s


def sum_digits(s):
    return sum(map(int, s))

n = 99
s = '1'
while sum_digits(alg(s)[:-1]) != 1190:
    n += 1
    for k in range(100, 201):
        for m in range(100, 201):
            s = '>' + '1'*k + '2'*m + '*'*n
print(n)
