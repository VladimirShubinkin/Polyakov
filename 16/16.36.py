'''36)(Д.Ф. Муфаззалов) Определите количество различных значений n таких, что n и m – натуральные числа,
находящиеся в диапазоне [100; 1000], а значение F(n, m) равно числу 30.
def F(n,m):
 if m == 0:
   return n
 else:
   return F(m,n%m)
'''


def f(n, m):
    if m == 0:
        return n
    return f(m, n % m)


count = 0
for n in range(100, 1001):
    for m in range(100, 1001):
        if f(n, m) == 30:
            count += 1
            break
print(count)
