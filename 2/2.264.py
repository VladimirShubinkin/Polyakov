from itertools import product, permutations


def f(w, x, y, z):
    return ((w <= z) == y) <= x


for q, w, e, r, t, y in product([0, 1], repeat=6):
    table = ((q, 1, w, e),
             (1, r, 0, t),
             (1, 0, 1, y))
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if not any([f(**dict(zip(p, row))) for row in table]):
                print(p)
