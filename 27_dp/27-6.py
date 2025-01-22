with open('files/27-6b.txt') as f:
    n, *a = map(int, f.readlines())

max6_1 = max6_2 = max2 = max3 = max1 = 0
for x in a:
    if x % 6 == 0:
        if x > max6_1:
            max6_2 = max6_1
            max6_1 = x
        elif x > max6_2:
            max6_2 = x
    elif x % 2 == 0:
        max2 = max(max2, x)
    elif x % 3 == 0:
        max3 = max(max3, x)
    else:
        max1 = max(max1, x)
r = max(max6_1 * max6_2, max6_1 * max2, max6_1 * max3, max6_1 * max1, max2 * max3)
print(r)
