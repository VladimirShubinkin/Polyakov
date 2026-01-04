import re


def max_sum_odds(s: str) -> int:
    return sum(int(d) for d in s if d.isdigit() and int(d) % 2)


with open('24_24387.txt') as f:
    s = f.read().strip()
lines = re.split(r'(?<=[13579])(?=[13579])|(?<=[24680])(?=[24680])', s)
max_line = max(lines, key=max_sum_odds)
print(s.index(max_line))
# print(max_line)
