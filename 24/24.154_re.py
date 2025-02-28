import re

with open('24data/24-153.txt') as f:
    s = f.read().strip()

min_seq = min(re.findall(r'D[^D]+D', s), key=len)
print(len(min_seq))
print(min_seq)
