for x in range(2030, 0, -1):
    n = 7**91 + 7**160 - x

    count = 0
    while n:
        if n % 7 == 0:
            count += 1
        n //= 7

    if count == 70:
        print(x)
        break
