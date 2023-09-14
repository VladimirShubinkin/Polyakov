'''368)	(А.М. Кабанов) Для какого наименьшего целого неотрицательного числа А выражение
(x2 – 10x + 16 > 0) ∨ (y2 – 10y + 21 > 0) ∨ (xy < 2A)
тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y?
'''

def f(x, y, a):
    return (x**2 - 10 * x + 16 > 0) or (y**2 - 10 * y + 21 > 0) or (x * y < 2 * a)


def is_good(a):
    for x in range(0, 100):
        for y in range(0, 100):
            if not f(x, y, a):
                return False
    return True


a = 1
while not is_good(a):
    a += 1
print(a)