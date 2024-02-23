# 1A2157B4

# 1A21574

for a in range(0, 10, 2):
    n = int(f'1{a}21574')
    if n % 133 == 0:
        print(n, n // 133)

# 1A2157B4

for a in range(0, 10, 2):
    for b in range(1, 10, 2):
        n = int(f'1{a}2157{b}4')
        if n % 133 == 0:
            print(n, n // 133)

# 1A2157BB4

for a in range(0, 10, 2):
    for b in range(11, 100, 2):
        n = int(f'1{a}2157{b}4')
        if b // 10 % 2 == 1 and n % 133 == 0:
            print(n, n // 133)

# 1A2157BBB4

for a in range(0, 10, 2):
    for b in range(111, 1000, 2):
        n = int(f'1{a}2157{b}4')
        if b // 100 % 2 == 1 and b // 10 % 2 == 1 and n % 133 == 0:
            print(n, n // 133)
