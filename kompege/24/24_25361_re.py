import re

with open('24_25361.txt') as f:
    s = f.read().strip()
pattern = r'(?<=[02468])(?:[^F02468]*F){76}[^F02468]*'
max_seq = max(re.findall(pattern, s), key=len)
print(f'{s[s.find(max_seq) - 1]}{max_seq}')
print(len(max_seq) + 1)
