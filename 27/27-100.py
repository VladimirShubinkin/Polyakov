'''
100)(Д. Муфаззалов) На вход программе подается последовательность целых чисел и натуральное число M.
Рассматриваются все непрерывные подпоследовательности исходной последовательности,
такие что произведение элементов каждой из них не кратно M. Найдите количество таких подпоследовательностей.
'''


def factorize(n: int) -> dict[int, int]:
    result = {}
    d = 2
    while n > 1:
        while n % d == 0:
            result[d] = result.get(d, 0) + 1
            n //= d
        d += 1
    return result


with open('files/27-100b.txt') as f:
    n, m, *a = map(int, f.read().split())

divisors_with_count = factorize(m)
last_inds = {d: [-1]*count for d, count in divisors_with_count.items()}
count = 0
for i, x in enumerate(a):
    for d in last_inds:
        while x % d == 0:
            last_inds[d].append(i)
            del last_inds[d][0]
            x //= d
    count += i - min(min(last_inds.values()))
print(count)
