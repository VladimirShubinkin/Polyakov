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
    n80 = from_dec(n, 80)
    for _ in range(2):
        s = [0, 0]
        for d in n80:
            s[d not in even_digits] += digits80.index(d)
        n80 += digits80[max(s) % 80]
    return to_dec(n80, 80)    


alphabet = digits + ascii_letters + 'йцукенгшщзхъфывапролджэячсмитьбю'
digits80 = alphabet[:80]
even_digits = digits80[::2]
n = 1
while alg(n) <= 10**6:
    n += 1
print(f'N = {n}, R = {alg(n)}')
print(f'Ответ: {n}')
# Ответ: 156
