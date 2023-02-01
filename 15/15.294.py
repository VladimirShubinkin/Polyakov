'''
294) Укажите наименьшее целое значение А, при котором выражение
(y + 4x < A) ∨ (x + 3y > 100) ∨ (5x + 2y > 152)
истинно для любых целых положительных значений x и y.
'''

def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(y + 4 * x < a or x + 3 * y > 100 or 5 * x + 2 * y > 152):
                return False
    return True


a = 1
while not f(a):
    a += 1
print(a)