'''Среди натуральных чисел, не превышающих 10**8, найдите все числа, которые делятся на сумму нечётных цифр числа и
соответствующие маске 124*5*79. В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
а во втором столбце – сумму всех цифр этого числа.'''


def is_odd(n: int):
    return n % 2


def sum_digits(n: int, is_ok=lambda x: 1):
    return sum([int(d) for d in str(n) if is_ok(int(d))])


def check(n: int):
    s = sum_digits(n, is_odd)
    if n % s == 0:
        ans.append(n)


ans = []
# 124579
n = 124579
check(n)

# 124?579
for d in range(10):
    n = int(f'124{d}579')
    check(n)

# 124??579
for d1 in range(10):
    for d2 in range(10):
        n = int(f'124{d1}{d2}579')
        check(n)

# 124?5?79
for d1 in range(10):
    for d2 in range(10):
        n = int(f'124{d1}5{d2}79')
        check(n)

# 1245?79
for d in range(10):
    n = int(f'1245{d}79')
    check(n)

# 1245??79
for d1 in range(10):
    for d2 in range(10):
        n = int(f'1245{d1}{d2}79')
        check(n)

ans.sort()
for n in ans:
    print(n, sum_digits(n))
