with open('24data/24-359.txt') as f:
    s = f.read().strip()

min_cnt = len(s)
left = 0
cnt_e = s[:4].count('E')
cnt_2025 = s[:4] == '2025'
for right in range(4, len(s)):
    cnt_e += s[right] == 'E'
    cnt_2025 += s[right-3:right+1] == '2025'

    while cnt_e > 110 or (cnt_e == 110 and s[left] != 'E'):
        cnt_e -= s[left] == 'E'
        cnt_2025 -= s[left:left+4] == '2025'
        left += 1

    if cnt_e == 110 and cnt_2025 >= 90:
        min_cnt = min(min_cnt, right - left + 1)
print(min_cnt)
