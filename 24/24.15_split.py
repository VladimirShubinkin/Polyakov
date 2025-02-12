from string import ascii_uppercase

with open('24data/k7-84.txt') as f:
    s = f.read().strip()

for letter in ascii_uppercase:
    if letter != 'C':
        s = s.replace(letter, ' ')
a = s.split()
max_seq = max(a, key=len)
print(len(max_seq))
