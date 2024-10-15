def f(s):
    while '12' in s or '322' in s or '222' in s:
        s = s.replace('12', '2', 1)
        s = s.replace('322', '21', 1)
        s = s.replace('222', '3', 1)
    return s


def sum_digits(s):
    return sum(map(int, s))


max_sum = 0
for n in range(4, 10_000):
    s = '1' + '2' * n
    max_sum = max(max_sum, sum_digits(f(s)))
print(max_sum)
