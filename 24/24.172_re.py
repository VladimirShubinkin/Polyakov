import re

with open('24data/24-171.txt') as f:
    s = f.read()

pattern = r'(?:YZ|Z)?(?:XYZ)+(?:XY|X)?'
max_seq = max(re.findall(pattern, s), key=len)
print(len(max_seq))
print(max_seq)
