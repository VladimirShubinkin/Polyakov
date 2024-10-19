from string import ascii_uppercase

with open('24data/24-164.txt') as f:
    lines = f.read().splitlines()
max_line = ''
max_len = 0
for line in lines:
    cur_len = 1
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
                max_line = line
        else:
            cur_len = 1
min_count = len(max_line)
min_letter = ''
for letter in ascii_uppercase:
    cur_count = max_line.count(letter)
    if 0 < cur_count <= min_count:
        min_count = cur_count
        min_letter = letter
total_count = ''.join(lines).count(min_letter)
print(min_letter, total_count, sep='')
