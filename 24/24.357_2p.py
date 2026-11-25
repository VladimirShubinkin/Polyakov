with open('24data/24-357.txt') as f:
    s = f.read()

min_len = len(s)
count_RSQ = 0
left = 0
for right in range(2, len(s)):
    if s[right - 2:right + 1] == 'RSQ':
        count_RSQ += 1

    while count_RSQ == 130 and s[right] != 'Q':
        min_len = min(min_len, right - left + 1)
        if s[left:left+3] == 'RSQ':
            count_RSQ -= 1
        left += 1

print(min_len)
