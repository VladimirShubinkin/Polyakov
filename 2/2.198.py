from itertools import product, permutations


def f(w, x, y, z):
    return (w <= y) and ((x <= z) == (y <= x))


for q, w, e, r in product((0, 1), repeat=4):
    table = ((q, 1, w, 0),
             (0, e, 1, r),
             (0, 1, 0, 1))
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, row))) for row in table):
                print(''.join(p))
