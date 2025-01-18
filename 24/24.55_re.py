import re

with open('24data/k8-12.txt') as f:
    s = f.read().strip()

pattern = r'((\w)\2*)'
max_seq = max(map(re.Match.group, re.finditer(pattern, s)), key=len)
print(max_seq[0], len(max_seq))
