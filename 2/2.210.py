from itertools import product, permutations


def f(w, x, y, z):
    return (x <= w) and (y <= z) or w


good = set()
for q, w, e, r, t, y in product((0, 1), repeat=6):
    table = ((q, w, e, 1),
             (r, t, 1, 1),
             (y, 1, 1, 1))
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all([not f(**dict(zip(p, row))) for row in table]):
                good.add(p)
                # print(p)
print(len(good))
