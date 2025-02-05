from string import ascii_uppercase, digits

with open('24data/24-264.txt') as f:
    s = f.read().strip()

for letter in ascii_uppercase[1:]:
    s = s.replace(letter, 'A')
for digit in digits[1:]:
    s = s.replace(digit, '0')
for i in range(2):
    s = s.replace('AA', 'A A')
    s = s.replace('00', '0 0')
max_seq = max(s.split(), key=len)
print(len(max_seq))
