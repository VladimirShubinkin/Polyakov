from itertools import product, permutations


def f1(w, x, y, z):
    """F1 = (w → y) == (z  → x)"""
    return (w <= y) == (z <= x)


def f2(w, x, y, z):
    """F2 = (w → y) ∧ (¬x  == z)"""
    return (w <= y) and (x != z)


for q, w, e, r, t in product((0, 1), repeat=5):
    table = ((0, q, 0, 0, 0, 1),
             (0, 0, 0, w, 0, e),
             (0, 1, 1, r, t, 0))
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all(f1(**dict(zip(p, row))) == row[-2] and f2(**dict(zip(p, row))) == row[-1] for row in table):
                print(p)
