'''
№ 21717 ЕГКР 19.04.25
Текстовый файл состоит из символов F, G, Q, R, S и W.
Определите в этом файле минимальное количество идущих подряд символов,
среди которых подстрока RSQ встречается ровно 130 раз,
при этом искомая последовательность не оканчивается символом Q.
Для выполнения этого задания следует написать программу.
'''

with open('24_21717.txt') as f:
    s = f.read().strip()

min_len = len(s)
left = 0
count_RSQ = 0
for right in range(2, len(s)):
    if s[right - 2:right + 1] == 'RSQ':
        count_RSQ += 1

    while count_RSQ == 130 and s[right] != 'Q':
        min_len = min(min_len, right - left + 1)
        if s[left:left + 3] == 'RSQ':
            count_RSQ -= 1
        left += 1

print(min_len)
