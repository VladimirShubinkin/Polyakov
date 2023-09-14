'''360)	(А.М. Кабанов, Тольятти) Найдите целые положительные значения A и B, при которых выражение
(y ≤ ((x – 4)^2 + 2 + |(x – 2)^2 – 16| )) ≡ ((y ≤ 2x^2 – 12x + A) ∨ (y ≤ – 4x + B))
тождественно истинно при любых целых неотрицательных x и y. В ответе запишите их сумму.
'''

def f(x, y, a, b):
    return (y <= ((x - 4)**2 + 2 + abs((x - 2)**2 - 16))) == ((y <= 2 * x**2 - 12 * x + a) or (y <= - 4 * x + b))


def is_good(a, b):
    for x in range(0, 100):
        for y in range(0, 100):
            if not f(x, y, a, b):
                return False
    return True


for a in range(1, 100):
    for b in range(1, 100):
        if is_good(a, b):
            print(a + b)
            break
