'''Определите сколько всего существует натуральных чисел R таких, что выражение
(((x & 54  =0) \/ (x & 45  =0)) -> (x & A  =0)) \/ (x & R  =0)
тождественно истинно при любом натуральном A (то есть принимает значение 1 при любом натуральном значении переменной x
и любом натуральном значении A)?
'''
f = lambda x, a, r: (((x & 54 == 0) or (x & 45 == 0)) <= (x & a == 0)) or (x & r == 0)


def is_true(r: int) -> bool:
    for x in range(1, 1000):
        for a in range(1, 1000):
            if not f(x, a, r):
                return False
    return True


count = 0
for r in range(1, 1000):
    count += is_true(r)
print(count)