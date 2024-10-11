from string import ascii_uppercase

with open('24data/24-s1.txt') as f:
    lines = f.read().splitlines()
max_count = 0
max_line = ''
for line in lines:
    cur_count = 0
    for i in range(1, len(line)):
        if ord(line[i]) - ord(line[i - 1]) == 1:
            cur_count += 1
    if cur_count >= max_count:
        max_count = cur_count
        max_line = line
min_count = 10**9
min_letter = ''
for letter in ascii_uppercase:
    cur_count = max_line.count(letter)
    if 0 < cur_count < min_count:
        min_count = cur_count
        min_letter = letter
total_count = ''.join(lines).count(min_letter)
print(f'{min_letter}{total_count}')
