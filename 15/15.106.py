'''На числовой прямой даны два отрезка: P = [43; 49] и Q = [44; 53].
Укажите наибольшую возможную длину такого отрезка A, что формула
((x in A) -> (x in P)) \/ (x in Q)
тождественно истинна, то есть принимает значение 1 при любом значении переменной х.
'''

def f(x: int, a: list) -> bool:
    return ((x in a) <= (43 <= x <= 49)) or (44 <= x <= 53)


infinity = 100
a = list(range(40, infinity))
lens = []
for x in range(40, infinity):
    if not f(x, a):
        if a[0] == x:
            del a[0]
        else:
            pos_x = a.index(x)
            lens.append(a[pos_x - 1] - a[0])
            a = a[pos_x + 1:]
print(max(lens))

