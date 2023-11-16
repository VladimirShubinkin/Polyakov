from string import ascii_uppercase

with open('24-s1.txt') as f:
    a = f.readlines()

str_with_a = a[0]
for line in a[1:]:
    if line.count('A') < str_with_a.count('A'):
        str_with_a = line
letter = 'A'
letter_count = 0
for let in ascii_uppercase:
    cur_count = str_with_a.count(let)
    if cur_count >= letter_count:
        letter_count = cur_count
        letter = let
print(letter)
print(''.join(a).count(letter))
