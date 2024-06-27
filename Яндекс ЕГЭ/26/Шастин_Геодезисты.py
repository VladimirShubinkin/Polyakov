# https://education.yandex.ru/ege/task/98cd2984-d281-4a05-be42-ea079f58f4e1
with open('Шастин_Геодезисты.txt') as f:
    n, r = map(int, f.readline().split())
    a = [0]*(r + 1)
    for line in f.readlines():
        start, end = map(int, line.split())
        for i in range(start, end):
            a[i] += 1
count = 0
max_len = 0
cur_len = 0
for i in range(1, r + 1):
    if a[i] >= 2:
        cur_len += 1
        if a[i - 1] <= 1:
            count += 1
    else:
        cur_len = 0
    max_len = max(max_len, cur_len)
print(count, max_len)
