from string import ascii_uppercase

with open('24data/24-s1.txt') as f:
    lines = f.read().splitlines()

min_count = 10**6
s = ''
for line in lines:
    count = 0
    for i in range(len(line) - 1):
        if ord(line[i + 1]) - ord(line[i]) == 1:
            count += 1
    if 0 < count < min_count:
        min_count = count
        s = line

max_count = 0
max_letter = ''
for letter in ascii_uppercase:
    count = s.count(letter)
    if count >= max_count:
        max_count = count
        max_letter = letter

with open('24data/24-s1.txt') as f:
    count = f.read().count(max_letter)
print(max_letter, count)
