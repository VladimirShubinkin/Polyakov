'''
На числовой прямой даны отрезки A = [80; 90], B = [30; 50] и C = [10; N] и функция
F(x) = (not (x in A) -> (x in B) ) /\ (not (x in C) -> (x in A) )
При каком наименьшем числе N функция F(x) истинна более чем для 25 целых чисел x?
'''

def f(x, n):
    return ((not (80 <= x <= 90)) <= (30 <= x <= 50)) and ((not (10 <= x <= n)) <= (80 <= x <= 90))


def is_good(n):
    count = 0
    for x in range(-1000, 1000):
        count += f(x, n)
        if count > 25:
            return True
    return False


n = -1000
while not is_good(n):
    n += 1
print(n)
