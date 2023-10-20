# Автор В.Н. Шубинкин


def get_sums(n: int) -> [int, int]:
    s = [0, 0]
    while n:
        s[n % 2] += n % 80
        n //= 80
    return s


def alg(n: int) -> int:
    s = get_sums(n)
    add_digit = max(s) % 80
    n = n * 80 + add_digit
    s[add_digit % 2] += add_digit
    add_digit = max(s) % 80
    n = n * 80 + add_digit
    return n


n = 1
while alg(n) <= 10**6:
    n += 1
print(f'N = {n}, R = {alg(n)}')
print(f'Ответ: {n}')
