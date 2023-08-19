'''На числовой прямой даны два отрезка: P = [12; 26] и Q = [30; 53].
Укажите наибольшую возможную длину такого отрезка A, что формула
 (x ∈ A -> x ∈ P) \/ x ∈ Q
тождественно истинна, то есть принимает значение 1 при любом значении переменной х.
'''

def f(x: int, a: list) -> bool:
    return (x in a) <= (12 <= x <= 26) or (30 <= x <= 53)


infinity = 100
a = list(range(1, infinity))
lens = []
for x in range(1, infinity):
    if not f(x, a):
        if a[0] == x:
            del a[0]
        else:
            pos_x = a.index(x)
            lens.append(a[pos_x - 1] - a[0])
            a = a[pos_x + 1:]
print(max(lens))