import re

with open('24data/24-153.txt') as f:
    s = f.read().strip()

pattern = r'(?<=D)[^D]+(?=D)'
min_seq = min(re.findall(pattern, s), key=len)
print(len(min_seq) + 2)
print(min_seq)
