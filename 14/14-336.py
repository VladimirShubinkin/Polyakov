n = 3 * 5**1984 - 7 * 25**777 - 11 * 125**666 - 404
n = abs(n)
count_2 = 0
while n:
    count_2 += n % 5 == 2
    n //= 5
print(count_2)
