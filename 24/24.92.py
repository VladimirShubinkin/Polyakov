from string import ascii_uppercase as letters

with open('24-1.txt') as f:
    s = f.read().strip()
for letter in letters:
    s = s.replace(letter, ' ')
a = s.split()
max_num = 0
for num in a:
    if not(any(d in num for d in '1357')):
        max_num = max(max_num, int(num))
print(max_num)

