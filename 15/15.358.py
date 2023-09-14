'''358)	(А.М. Кабанов, Тольятти) Для какого целого положительного значения A выражение
(y ≤ |x^2 – 4x –5|) ≡ ((y ≤ x^2– 4x – 5) ∨ (y ≤ – (x – 2)^2 + A))
тождественно истинно при любых целых неотрицательных x и y?
'''
def f(x, y, a):
    return (y <= abs(x**2 - 4 * x - 5)) == ((y <= x**2 - 4 * x - 5) or (y <= - (x - 2)**2 + a))


def is_good(a):
    for x in range(0, 100):
        for y in range(0, 100):
            if not f(x, y, a):
                return False
    return True


a = 1
while not is_good(a):
    a += 1
print(a)