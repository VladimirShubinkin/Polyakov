'''356)	(А.М. Кабанов, Тольятти) Для какого целого положительного значения A выражение
((y ≥ –4x + 12) ∧ (y ≥ 4x – 12)) ≡ (y ≥ A|x – 3|)
тождественно истинно при любых целых положительных x и y?
'''
def f(x, y, a):
    return ((y >= -4 * x + 12) and (y >= 4 * x - 12)) == (y >= a * abs(x - 3))


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