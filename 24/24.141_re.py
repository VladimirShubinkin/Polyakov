import re

with open('24data/24-s1.txt') as f:
    s = f.read()

pattern = r'\w*F\wO\w*'
print(len(re.findall(pattern, s)))
