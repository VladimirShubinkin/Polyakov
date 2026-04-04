with open('24_26078.txt') as f:
    s = f.read().strip()
lines = s.split('W')
min_len = len(s)
for i in range(1, len(lines) - 89):
    line = 'W' + 'W'.join(lines[i:i+89]) + 'W'
    count_2025 = line.count('2025')
    if count_2025 >= 110:
        min_len = min(min_len, len(line))
    else:
        left = lines[i - 1].split('2025')[1:]
        right = lines[i + 89].split('2025')[:-1]
        while count_2025 < 110:
            if not left and not right:
                break
            if left:
                cur_len_left = len(left[-1])
            else:
                cur_len_left = 10**9
            if right:
                cur_len_right = len(right[0])
            else:
                cur_len_right = 10**9
            if cur_len_right < cur_len_left:
                count_2025 += 1
                line += right.pop(0) + '2025'
            else:
                count_2025 += 1
                line = '2025' + left.pop() +  line
        if count_2025 >= 110:
            min_len = min(min_len, len(line))
print(min_len)
