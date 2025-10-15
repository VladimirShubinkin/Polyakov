import re

with open('24data/24-221.txt') as f:
    s = f.read().strip()

pattern = r'0+1+'
max_seq = max(re.findall(pattern, s), key=len)
print(len(max_seq))
