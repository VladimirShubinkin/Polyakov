'''354)	(А.М. Кабанов, Тольятти) Для скольких целых положительных значений A выражение
(2x + 3y ≠ 13) ∨ (2y + 3x ≠ 12) ∨ ((x^2 + 3x – 1 < A) ∧ (2y^2 – 4y + 20 > A))
тождественно истинно при любых целых положительных x и y?
'''
def f(x, y, a):
    return (2 * x + 3 * y != 13) or (2 * y + 3 * x != 12) or ((x**2 + 3 * x - 1 < a) and (2 * y**2 - 4 * y + 20 > a))


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