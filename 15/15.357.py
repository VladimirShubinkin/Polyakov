'''357)	(А.М. Кабанов, Тольятти) Для какого целого положительного значения A выражение
((y ≤ 5x – 14) ∧ (y ≤ –5x + A)) ≡ (y – 6 ≤ –5|x – 4|)
тождественно истинно при любых целых положительных x и y?
'''
def f(x, y, a):
    return ((y <= 5 * x - 14) and (y <= -5 * x + a)) == (y - 6 <= -5 * abs(x - 4))


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