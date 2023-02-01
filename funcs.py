def to_base(a, n):
    res = ''
    while a:
        res = str(a % n) + res
        a //= n
    return res


if __name__ == '__main__':
    print(to_base(100_000_000, 3))
