seq = [None] + [0, 1]*249 + [0, 0] + [1] + [0]*499 + [None]*3
i = 0
q = 0
while i != 'S':
    if seq[i] is None:
        if q == 0:
            seq[i], i, q = None, i + 1, 1
        elif q == 1:
            seq[i], i, q = None, 'S', 1
        else:  # q == 2
            seq[i], i, q = None, 'S', 2
    elif seq[i] == 0:
        if q == 0:
            pass
        elif q == 1:
            seq[i], i, q = 1, i + 1, 2
        else:  # q == 2
            seq[i], i, q = 0, 'S', 2
    else:  # seq[i] == 1
        if q == 0:
            pass
        elif q == 1:
            seq[i], i, q = 0, i + 1, 2
        else:  # q == 2
            seq[i], i, q = 1, i + 1, 1
print(seq)
print(seq.count(0), seq.count(1))
