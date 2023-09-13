'''352)	(А.М. Кабанов, Тольятти) Укажите наибольшее целое значение A, при котором выражение
(5y + 2x = 65) → ((2x ≤ A) → (3y > A))
тождественно истинно при любых целых положительных x и y?
'''
def f(x, y, a):
    return (5 * y + 2 * x == 65) <= ((2 * x <= a) <= (3 * y > a))


def is_good(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not f(x, y, a):
                return False
    return True


a = 1000
while not is_good(a):
    a -= 1
print(a)
