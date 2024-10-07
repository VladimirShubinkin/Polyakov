with open('24data/24-157.txt') as f:
    s = f.read().strip()
letters = {}
for i in range(2, len(s)):
    if s[i - 1] == s[i - 2]:
        letters[s[i]] = letters.get(s[i], 0) + 1
print(letters)
max_count = 0
max_letter = ''
for letter, count in letters.items():
    if count > max_count:
        max_count = count
        max_letter = letter
    elif count == max_count:
        max_letter = min(max_letter, letter)
print(f'{max_letter}{max_count}')
