# Автор В.Н. Шубинкин
from string import digits, ascii_letters


def from_dec(n: int, base: int) -> str:
    result = ''
    while n:
        result = alphabet[n % base] + result
        n //= base
    return result


def to_dec(s: str, base: int) -> int:
    result = 0
    base_power = 1
    for d in s[::-1]:
        result += alphabet.index(d) * base_power
        base_power *= base
    return result


def alg(n: int) -> int:
    n45 = from_dec(n, 45)
    s1 = sum([digits45.index(d) for d in n45[::2]])
    s0 = sum([digits45.index(d) for d in n45[1::2]])
    left = from_dec(min(s1, s0), 45)
    right = from_dec(max(s1, s0), 45)
    n45 = left + n45 + right
    return to_dec(n45, 45)


alphabet = digits + ascii_letters
digits45 = alphabet[:45]
r_min = 10**10
for n in range(1001, 100_000):
    r = alg(n)
    r_min = min(r_min, r)
print(r_min)
