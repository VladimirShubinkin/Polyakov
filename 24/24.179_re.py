from collections import Counter
import re

with open('24data/24-179.txt') as f:
    s = f.read().strip()

pattern = r'(?<=CB)[CDE](?=BC)'
lines = re.findall(pattern, s)
counter = Counter(lines)
print(counter.most_common()[0][0], len(lines))
