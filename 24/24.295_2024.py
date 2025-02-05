with open('24data/24-295.txt') as f:
    s = f.read().strip()
lines = s.split('DE')
max_len = 0
max_line = ''
for i in range(len(lines) - 240):
    line = 'E' + 'DE'.join(lines[i:i+241]) + 'D'
    if len(line) > max_len:
        max_len = len(line)
        max_line = line
print(max_line)
print(max_len)
