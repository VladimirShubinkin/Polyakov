def to_tri(n):
    result = ''
    while n:
        result = str(n % 3) + result
        n //= 3
    return result


def f(n):
    tri_n = to_tri(n)
    if n % 3 == 0:
        tri_n += tri_n[-2:]
    else:
        tri_n += to_tri(n % 3 * 5)
    return int(tri_n, 3)


min_r = 10 ** 9
for n in range(1, 133):
    r = f(n)
    if 133 < r < min_r:
        min_r = r
print(min_r)
