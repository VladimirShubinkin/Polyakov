'''365)	(А.М. Кабанов) Для какого наименьшего целого неотрицательного числа А выражение
 (x > 7) \/ (y > 4) \/ (x^2 + 3y < A)
тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y?
'''
def f(x, y, a):
    return (x > 7) or (y > 4) or (x**2 + 3 * y < a)


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