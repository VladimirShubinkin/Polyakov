'''366)	(А.М. Кабанов) Для какого наименьшего целого неотрицательного числа А выражение
(x > 4)  (x + 2 < y)  (x2 + y2 < A)
тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y?
'''

def f(x, y, a):
    return (x > 4) or (x + 2 < y) or (x**2 + y**2 < a)


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