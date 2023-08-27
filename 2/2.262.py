'''¬y ∧ (x → (¬z ≡ w)) ∨ z'''
from itertools import product, permutations


def f(w, x, y, z):
    return not y and (x <= (z != w)) or z


for q, w, e, r in product((0, 1), repeat=4):
    table = ((0, q, 0, 0),
             (w, 0, 1, 0),
             (e, 0, 0, r))
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if not any(f(**dict(zip(p, row))) for row in table):
                print(p)
