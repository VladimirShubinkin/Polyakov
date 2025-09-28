import re
from collections import Counter

with open('24data/24-s2.txt') as f:
    s = f.read().strip()

pattern = r'(?<=A)[A-Z]'
counter = Counter(re.findall(pattern, s))
max_count = max(counter.values())
letter = min(let for let in counter.keys() if counter[let] == max_count)
print(letter, max_count)
