# Примечание. Авторское условие некорректно


def sum_digits(s):
    return sum(map(int, s))

# 3254?123
for x in range(1, 10):
    n = 3254 * 10**4 + x * 10**3 + 123
    if n % 519 == 0 and sum_digits(str(n // 10000)) == sum_digits(str(n % 10000)):
        print(n, n // 519)

# 32??54?123
for x in range(1, 10):
    for y in range(1, 10):
        for z in range(1, 10):
            n = int(f'32{x}{y}54{z}123')
            if n % 519 == 0 and sum_digits(str(n // 100000)) == sum_digits(str(n % 100000)):
                print(n, n // 519)

# 32????54?123
for x in range(1, 10):
    for y in range(1, 10):
        for a in range(1, 10):
            for b in range(1, 10):
                for z in range(1, 10):
                    n = int(f'32{x}{y}{a}{b}54{z}123')
                    if n % 519 == 0 and sum_digits(str(n // 1000000)) == sum_digits(str(n % 1000000)):
                        print(n, n // 519)
