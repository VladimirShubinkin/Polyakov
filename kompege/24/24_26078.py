with open('24_26078.txt') as f:
    s = f.read().strip()

min_len = len(s)
count_w = 0
c_2025 = 0
left = 0
for right in range(len(s)):
    if s[right] == 'W':
        count_w += 1
    if s[right-3:right + 1] == '2025':
        c_2025 += 1
    while count_w > 90 or count_w == 90 and c_2025 >= 110 and left < right:
        if count_w == 90 and c_2025 >= 110:
            min_len = min(min_len, right - left + 1)
        if s[left] == 'W':
            count_w -= 1
        if s[left:left+4] == '2025':
            c_2025 -= 1
        left += 1
print(min_len)


# ДЦ Очень медленно
from time import perf_counter

t0 = perf_counter()

min_len = 10_000
for i in range(len(s)):
    for j in range(i + 530, i + min_len):
        ss = s[i:j + 1]
        if ss.count('W') > 90:
            break
        if ss.count('W') == 90 and ss.count('2025') >= 110:
            min_len = min(min_len, len(ss))
print(min_len)

print(perf_counter() - t0)
