'''359)	(А.М. Кабанов, Тольятти) Для какого целого положительного значения A выражение
(y ≤ (4 + |x + 8| + |x – 8|)) ≡ ((y ≤ 2x + 4) ∨ (y ≤ A))
тождественно истинно при любых целых неотрицательных x и y?
'''

def f(x, y, a):
    return (y <= (4 + abs(x + 8) + abs(x - 8))) == ((y <= 2 * x + 4) or (y <= a))


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