# Автор В.Н. Шубинкин
from math import log


def get_sums(n: int) -> (int, int, int):
    digit_count = 0
    s = [0, 0]
    while n:
        digit_count += 1
        s[digit_count % 2] += n % 45
        n //= 45
    return min(s), max(s), digit_count


def alg(n: int) -> int:
    s_left, s_right, dc = get_sums(n)
    n += s_left * 45**dc
    len_s_rigth = int(log(s_right, 45)) + 1
    n = n * 45**len_s_rigth + s_right
    return n


r_min = 10**10
for n in range(1001, 1050):
    r = alg(n)
    r_min = min(r_min, r)
print('Ответ:', r_min)
