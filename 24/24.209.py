with open('24data/24-209.txt') as f:
    s = f.read().strip()

count = 0
max_count = 0
pairs = {'AB', 'CB', 'BC', 'BA'}
for i in range(1, len(s)):
    if s[i - 1] + s[i] in pairs:
        count += 1
    else:
        count = 0
    max_count = max(max_count, count)
print(max_count)
