'''
222)Пусть N(k) = 750 000 + k, где k – натуральное число.
Найдите пять наименьших значений k, при которых N(k) имеет нечётное количество различных чётных делителей.
В ответе запишите найденные значения k в порядке возрастания,
справа от каждого значения запишите число чётных делителей N(k).
'''

def even_divs_count(n):
    result = 0
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            result += d % 2 == 0
            result += n // d % 2 == 0 and n // d != d
    return result


k_count = 0
k = 0
while k_count < 5:
    k += 1
    nk = 750_000 + k
    edc = even_divs_count(nk)
    if edc % 2:
        k_count += 1
        print(k, edc)
