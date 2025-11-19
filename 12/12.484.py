def set_seq():
    i = 0
    q = 0
    while i != 'S':
        if seq[i] is None:
            if q == 0:
                seq[i], i, q = None, i + 1, 1
            elif q == 1:
                seq[i], i, q = None, 'S', 1
        elif seq[i] == '0':
            if q == 0:
                pass
            elif q == 1:
                seq[i], i, q = '1', i + 1, 1
        else:  # seq[i] == '1'
            if q == 0:
                pass
            elif q == 1:
                seq[i], i, q = '0', i + 1, 1

for n in range(70_000, 0, -1):
    seq = [None] + list(f'{n:b}') + [None] * 3
    set_seq()
    new_n = int(''.join(d for d in seq if d is not None), 2)
    if new_n == 415:
        print(n)
        break
