'''
(А. Комков) Напишите программу, которая перебирает целые числа, большие 89427150,
в порядке возрастания и ищет среди них те, которые можно представить в виде произведения 8 простых множителей
(не обязательно различных), при этом выполняются оба условия:
- среди простых множителей есть ровно две пары повторяющихся множителей, остальные множители различны.
- минимальный простой множитель не повторяется.
В ответе запишите первые 7 найденных чисел в порядке возрастания,
а через пробел для каждого из них соответствующий наибольший из найденных множителей.
'''

from itertools import combinations
from math import prod


def is_prime(n):
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return n > 1


def get_prime_divisors(n):
    divisors = set()
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            if is_prime(d):
                divisors.add(d)
            if is_prime(n // d):
                divisors.add(n // d)
    return divisors


n = 89_427_150
c = 0
while c < 7:
    n += 1
    prime_divisors = get_prime_divisors(n)
    if len(prime_divisors) == 6:
        sorted_divs = sorted(prime_divisors)
        for p in combinations([1, 2, 3, 4, 5], r=2):
            a = sorted_divs[:p[0]] + [sorted_divs[p[0]]]*2 + sorted_divs[p[0] + 1:p[1]] + [sorted_divs[p[1]]]*2 + sorted_divs[p[1] + 1:]
            if prod(a) == n:
                print(n, sorted_divs[-1])
                c += 1
