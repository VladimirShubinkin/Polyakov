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
lines = s.split('RSQ')
min_len = len(s)
for i in range(len(lines) - 129):
    cur_seq = 'RSQ' + 'RSQ'.join(lines[i:i+129]) + 'RSQ'
    if not lines[i + 129]:
        cur_seq += 'R'
    elif len(lines[i + 129]) == lines[i + 129].count('Q'):
        cur_seq += lines[i + 129] + 'R'
    else:
        j = 0
        while lines[i + 129][j] == 'Q':
            cur_seq += 'Q'
            j += 1
        cur_seq += lines[i + 129][j]
    min_len = min(min_len, len(cur_seq))
print(min_len)
