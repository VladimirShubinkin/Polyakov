'''218)	(ЕГЭ-2024) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = 1 при n = 1;
F(n) = (n + 1)·F(n – 1), если n > 1.
Чему равно значение (F(2024) + 3·F(2023)) / F(2022)?
'''
# from sys import setrecursionlimit
# setrecursionlimit(3000)

from functools import cache

@cache
def f(n):
    if n == 1:
        return 1
    return (n + 1) * f(n - 1)


for i in range(1, 2024):
    f(i)

print((f(2024) + 3 * f(2023)) / f(2022))