from itertools import product, permutations


def f(w, x, y, z):
    return not (x <= z) or (y == w) or y


for q, w, e, r, t, y, u in product((0, 1), repeat=7):
    table = [(1, 0, q, w),
             (e, 1, 0, r),
             (0, t, y, u)]
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all(not f(**dict(zip(p, row))) for row in table):
                print(''.join(p))
