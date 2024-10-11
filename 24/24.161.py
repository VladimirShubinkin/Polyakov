from string import ascii_uppercase

with open('24data/24-s1.txt') as f:
    lines = f.read().splitlines()
max_q = 0
line_q = ''
for line in lines:
    cur_count = line.count('Q')
    if cur_count >= max_q:
        max_q = cur_count
        line_q = line
min_count = 10**9
min_letter = ''
for letter in ascii_uppercase:
    cur_count = line_q.count(letter)
    if 0 < cur_count < min_count:
        min_count = cur_count
        min_letter = letter
total_count = ''.join(lines).count(min_letter)
print(min_letter, total_count)
