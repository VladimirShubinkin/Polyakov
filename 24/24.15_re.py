import re

with open('24data/k7-84.txt') as f:
    s = f.read().strip()

max_seq = max(re.findall(r'C+', s))
print(len(max_seq))

