from itertools import product, permutations


def f(a, b, c):
    return (a == (b or c)) == b


for q, w, e, r in product((0, 1), repeat=4):
    table = ((q, 0, 0),
             (0, w, e),
             (0, r, 0))
    if len(set(table)) == len(table):
        for p in permutations('abc'):
            if all([f(**dict(zip(p, row))) for row in table]):
                print(p)
