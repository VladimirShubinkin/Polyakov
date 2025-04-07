from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from string import digits, ascii_uppercase
DIGITS = digits + ascii_uppercase


def int_dec_to_n(n: int, base: int) -> str:
    res = ''
    while n:
        res = DIGITS[n % base] + res
        n //= base
    return res


def int_n_to_dec(s: str, base: int) -> int:
    res = 0
    base_power = 1
    for d in s[::-1]:
        res += int(d, base) * base_power
        base_power *= base
    return res


def frac_n_to_dec(s: str, base: int) -> F:
    res = F(0)
    base_power = base
    for d in s:
        res += F(int(d, base)) * F(1, base_power)
        base_power *= base
    return res


def frac_dec_to_n(s: str, base: int) -> str:
    frac = D('0.' + s)
    res = '.'
    for _ in range(getcontext().prec):
        new = frac * base
        new_as_tuple = new.as_tuple()
        digits_tuple = new_as_tuple.digits
        count_of_digits_after = -new_as_tuple.exponent
        if count_of_digits_after >= len(digits_tuple):
            count_of_digits_before = 0
            zeros_after = '0'*(count_of_digits_after - len(digits_tuple))
            frac = D('0.' + zeros_after + ''.join(map(str, digits_tuple[count_of_digits_before:])))
        else:
            count_of_digits_before = len(digits_tuple) - count_of_digits_after
            frac = D('0.' + ''.join(map(str, digits_tuple[count_of_digits_before:])))
        res += DIGITS[int(''.join(map(str, digits_tuple[:count_of_digits_before])) or '0')]
    return res


def n_to_dec(s: str, base: int) -> str:
    s1, s2 = s.split('.')
    part1 = int_n_to_dec(s1, base)
    part2 = frac_n_to_dec(s2, base)
    return str(part1) + ' ' + str(part2)


def dec_to_n(s: str, base: int) -> str:
    s1, s2 = s.split('.')
    part1 = int_dec_to_n(int(s1), base)
    part2 = frac_dec_to_n(s2, base)
    return str(part1) + str(part2)


# print(n_to_dec('A2B.A9', 12))
# print(frac_dec_to_n('565', 23))
# print(int_dec_to_n(3434, 23))
# print(int_n_to_dec('567', 8))
# print(frac_n_to_dec('101', 2))
print(dec_to_n('3434.565', 23))
# print(n_to_dec(input(), int(input())))
# print(dec_to_n(input(), int(input())))
# 19.004 -> 10

