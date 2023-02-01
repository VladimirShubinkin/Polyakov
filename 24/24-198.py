with open('24-197.txt') as f:
    s = f.read().strip()

count = 0
max_count = 0
for k in range(3):
    for i in range(k, len(s) - 2, 3):
        if s[i] in 'XZ' and s[i + 2] == 'Y':
            count += 1
        else:
            count = 0
        max_count = max(max_count, count)
print(max_count)
