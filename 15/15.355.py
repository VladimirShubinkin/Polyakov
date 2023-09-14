'''355)	(А.М. Кабанов, Тольятти) Для скольких целых положительных значений A выражение
(–5x + y ≠ –7) ∨ (x^2 – y ≠ 1) ∨ ((x + 3y > A) ∧ (y – x ≤ A))
тождественно истинно при любых целых положительных x и y?
'''
def f(x, y, a):
    return (-5 * x + y != -7) or (x**2 - y != 1) or ((x + 3 * y > a) and (y - x <= a))


def is_good(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not f(x, y, a):
                return False
    return True


count = 0
for a in range(1, 1000):
    count += is_good(a)
print(count)