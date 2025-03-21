with open('17-243.txt') as f:
    a = list(map(int, f.readlines()))
sum_digits = 0
for x in a:
    if x % 35 == 0:
        sum_digits += sum(map(int, str(x)))
count = 0
min_sum = 10**10
for i in range(len(a) - 1):
    # if ((a[i] > sum_digits and a[i + 1] <= sum_digits and a[i + 1] % 16**2 == int('EF', 16))
    #         or (a[i + 1] > sum_digits  and a[i] <= sum_digits and a[i] % 16**2 == int('EF', 16))):
    if ((a[i] > sum_digits and a[i + 1] <= sum_digits  and f'{a[i + 1]:X}'[-2:] == 'EF')
            or (a[i + 1] > sum_digits and a[i] <= sum_digits and f'{a[i]:X}'[-2:] == 'EF')):
        count += 1
        min_sum = min(min_sum, a[i] + a[i + 1])
print(count, min_sum)
