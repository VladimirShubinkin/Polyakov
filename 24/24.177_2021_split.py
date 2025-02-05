with open('24data/24-157.txt') as f:
    s = f.read().strip()

s = s.replace('PR', 'P R').replace('RP', 'R P')
max_seq = max(s.split(), key=len)
print(len(max_seq))
