from string import digits, ascii_uppercase
alphabet = digits + ascii_uppercase


def from_dec(n: int, base: int) -> str:
    result = ''
    while n:
        result = alphabet[n % base] + result
        n //= base
    return result


def from_dec_list(n: int, base: int) -> list[int]:
    result = []
    while n:
        result = [n % base] + result
        n //= base
    return result


def to_dec(digits: list[int], base: int) -> int:
    result = 0
    power = 1
    for d in digits[::-1]:
        result += d * power
        power *= base
    return result


if __name__ == '__main__':
    print()
