with open('24data/24-264.txt') as f:
    s = f.read().strip()
max_len = 0
cur_len = 1
for i in range(len(s) - 1):
    if s[i].isdigit() != s[i + 1].isdigit():
        cur_len += 1
    else:
        cur_len = 1
    max_len = max(max_len, cur_len)
print(max_len)
