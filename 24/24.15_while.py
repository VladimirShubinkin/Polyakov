with open('24data/k7-84.txt') as f:
    s = f.read().strip()

length = 1
while 'C' * length in s:
    length += 1
print(length - 1)
