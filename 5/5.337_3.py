def to_base(num, base):
    result = []
    while num:
        result = [num % base] + result
        num //= base
    return result


def to_dec(num, base):
    result = 0
    for d in num:
        result = result * base + d
    return result


def f(n):
    n_80 = to_base(n, 80)
    for i in range(2):
        sums = [0, 0]
        for d in n_80:
            sums[d % 2] += d
        max_s = to_base(max(sums), 80)
        last_digit = max_s[-1]
        n_80.append(last_digit)
    return to_dec(n_80, 80)


n = 1
while f(n) <= 1_000_000:
    n += 1
print(n)

