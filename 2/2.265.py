from itertools import product, permutations


def f(w, x, y, z):
    return ((x or y) == (y <= z)) or w


for q, w, e, r, t, y, u, i in product((0, 1), repeat=8):
    table = ((q, 1, w, e),
             (r, t, y, 1),
             (1, u, i, 1))
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all([not f(**dict(zip(p, row))) for row in table]):
                print(p)
    