from itertools import permutations


def f(w, x, y, z):
    return ((x <= y) or (z == x)) and (w <= z)


table = ((0, 0, 1, 1, 1),
         (0, 0, 1, 0, 0),
         (0, 1, 1, 1, 0))
for p in permutations('wxyz'):
    if all([f(**dict(zip(p, row))) == row[-1] for row in table]):
        print(p)
