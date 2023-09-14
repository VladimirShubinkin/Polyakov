'''367)	(А.М. Кабанов) Для какого наименьшего целого неотрицательного числа А выражение
(x^2 – 3x + 2 > 0)  (y > x^2+7)  (xy < A)
тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y?
'''

def f(x, y, a):
    return (x**2 - 3 * x + 2 > 0) or (y > x**2 + 7) or (x * y < a)


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