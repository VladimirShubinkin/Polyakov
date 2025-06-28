'''
Укажите наименьшее целое значение А, при котором выражение
(y + 4x < A) ∨ (x + 4y > 120) ∨ (5x – 2y > 50)
истинно для любых целых положительных значений x и y.
'''

def f(x, y, a):
    return y + 4 * x < a or x + 4 * y > 120 or 5 * x - 2 * y > 50


def is_good(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not f(x, y, a):
                return False
    return True

a = 1
while not is_good(a):
    a += 1
print(a)
