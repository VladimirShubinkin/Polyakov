import re

with open('24data/24-268.txt') as f:
    s = f.read().strip()
pattern = r'(?<=[K-Z])[1-9A-J][0-9A-J]*[02468ACEGI](?=[K-Z])'
max_seq = max(re.findall(pattern, s), key=lambda n: int(n, 20))
print(max_seq)
