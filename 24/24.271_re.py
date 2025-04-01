import re

with open('24data/24-271.txt') as f:
    s = f.read().strip()

all_colors = re.findall(r'(?<=#)[0-9A-F]{6}', s)
count = len([color for color in all_colors if color[2:4] < color[:2] > color[4:]])
print(count)
