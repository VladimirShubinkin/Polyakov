with open('24-221.txt') as f:
    s = f.read().strip()

for i in '23456789':
    s = s.replace(i, ' ')
s = s.replace('10', '1 0')
a = filter(lambda x: '0' in x and '1' in x, s.split())
max_len = max(map(len, a))
print(max_len)

