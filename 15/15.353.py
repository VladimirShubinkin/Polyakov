'''353)	(А.М. Кабанов, Тольятти) Укажите наименьшее целое значение A, при котором выражение
(x < 9) → ((5y < x) → (2xy < A))
тождественно истинно при любых целых положительных x и y?
'''
def f(x, y, a):
    return (x < 9) <= ((5 * y < x) <= (2 * x * y < a))


def is_good(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not f(x, y, a):
                return False
    return True


a = 1
while not is_good(a):
    a += 1
print(a)