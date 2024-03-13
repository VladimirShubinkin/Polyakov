'''113)	(С.С. Поляков) У исполнителя Калькулятор есть три команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 5
3. Умножить на 3
Найдите длину самой короткой программы,
в результате выполнения которой при исходном числе 1 результатом является число 227.
'''
from functools import cache
lens = set()


@cache
def f(a, k):
    if a == 227:
        lens.add(k)
        return
    if a > 227:
        return
    f(a + 1, k + 1)
    f(a + 5, k + 1)
    f(a * 3, k + 1)
    return


f(1, 0)
print(min(lens))


def g(a, b, k):
    if a > b or k < 0:
        return 0
    if a == b and k == 0:
        return 1
    return g(a + 1, b, k - 1) + g(a + 5, b, k - 1) + g(a * 3, b, k - 1)


k = 0
while not g(1, 227, k):
    k += 1
print(k)
