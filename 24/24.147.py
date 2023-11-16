with open('24-s2.txt') as f:
    s = f.read().strip()
counter = {}
for i in range(1, len(s)):
    if s[i - 1] == 'A':
        counter[s[i]] = counter.get(s[i], 0) + 1
max_count = max(counter.values())
ans = min(letter for letter in counter if counter[letter] == max_count)
print(ans, max_count, sep='')
# Подробно:
max_count = 0
ans = ''
for letter, count in sorted(counter.items()):
    if count > max_count:
        max_count = count
        ans = letter
print(ans, max_count, sep='')
