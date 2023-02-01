'''
Укажите наибольшее целое значение А, при котором выражение
(5y + 7x != 129) ∨ (3x > A) ∨ (4y > A)
истинно для любых целых положительных значений x и y.
'''
def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(5 * y + 7 * x != 129 or 3 * x > a or 4 * y > a):
                return False
    return True


a = 10000
while not f(a):
    a -= 1
print(a)