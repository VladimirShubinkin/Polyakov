import re

with open('24_25361.txt') as f:
    s = f.read().strip()
max_len = 0
lines = re.split(r'[02468]', s)
for line in lines:
    if line.count('F') >= 76:
        sub_lines = line.split('F')
        cur_line = 'F'.join(sub_lines[:77])
        max_len = max(max_len, len(cur_line) + 1)
print(max_len)
