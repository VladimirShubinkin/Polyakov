from itertools import product, permutations


def f(w, x, y, z):
    return (x <= (z == w)) or not (y <= w)


for q, w, e, r, t, y, u in product([0, 1], repeat=7):
    table = [(q, 1, w, e, 0),
             (0, r, 0, t, 0),
             (y, 0, 0, u, 0)]
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, row[:-1]))) == row[-1] for row in table):
                print(''.join(p))


