from itertools import product, permutations, repeat


def f1(w, x, y, z):
    return (x <= y) or (w != z)


def f2(w, x, y, z):
    return (x <= y) == (w and not z)


for z, x, c, v, b, n, p, q, r in product((0, 1), repeat=9):
    table = ((z, x, c, 0, p, p),
             (v, b, 0, 0, q, q),
             (n, 0, 0, 0, r, r))
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all(f1(**dict(zip(p, row[:-2]))) == row[-2]
                   and f2(**dict(zip(p, row[:-2]))) == row[-1]
                   for row in table):
                print(''.join(p))
