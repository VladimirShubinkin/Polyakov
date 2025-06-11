'''
Напишите программу, которая перебирает целые числа, большие 1 324 727, в порядке возрастания
и ищет среди них числа, представленные в виде произведения ровно двух простых множителей, не обязательно различных,
каждый из которых содержит в своей записи ровно одну цифру 5.
В ответе в первом столбце таблицы запишите первые 5 найденных чисел в порядке возрастания,
а во втором столбце - для каждого из чисел наибольший из соответствующих им найденных множителей.
'''


def is_prime(n: int) -> bool:
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return n > 1


def get_divisors(n: int) -> list[int]:
    divisors = []
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            divisors.append(d)
            divisors.append(n // d)
    return divisors


n = 1_324_727 + 1
c = 0
while c < 5:
    divisors = get_divisors(n)
    if len(divisors) == 2 and all(map(is_prime, divisors)) and all(map(lambda d: str(d).count('5') == 1, divisors)):
        print(n, max(divisors))
        c += 1
    n += 1
