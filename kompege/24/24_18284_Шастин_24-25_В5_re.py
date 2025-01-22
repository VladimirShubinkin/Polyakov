import re

with open('24_18284.txt') as f:
    s = f.read().strip()

pattern = r'L[A-KM-Z]*?O(?!L.*O)\w*?V(?!L.*O.*V)\w*?E'
max_seq = max(re.findall(pattern, s), key=len)
print(len(max_seq))
