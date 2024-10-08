from string import ascii_uppercase

with open('24data/24-164.txt') as f:
    lines = f.read().splitlines()
max_dist = 0
for line in lines:
    if line.count('G') < 15:
        for letter in ascii_uppercase:
            cur_dist = line.rfind(letter) - line.find(letter)
            max_dist = max(max_dist, cur_dist)
print(max_dist)
