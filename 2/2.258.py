from itertools import product, permutations


def f(w, x, y, z):
    return not ((((not w) <= (not y)) <= (not z)) <= x)


for q, w, e, r, t in product((0, 1), repeat=5):
    table = ((q, w, 1, 0, 1),
             (e, 1, r, 1, 1),
             (0, 1, t, 0, 0))
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, row[:-1]))) == row[-1] for row in table):
                print(''.join(p))
