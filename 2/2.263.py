from itertools import product, permutations


def f(w, x, y, z):
    return (x or y or z) <= (x and (y or w))


for q, w, e, r in product([0, 1], repeat=4):
    table = ((1, 0, q, 0),
             (w, 1, 1, e),
             (1, 1, r, 1))
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if not any([f(**dict(zip(p, row))) for row in table]):
                print(p)
