with open('24data/24-175.txt') as f:
    a = [len(s) for s in f.read().strip().split('KEGE')]

max_len = 0
for i in range(1, len(a) - 3):
    length = sum(a[i:i + 3]) + 6 + 8
    max_len = max(max_len, length)
max_len = max(max_len, sum(a[:3]) + 3 + 8, sum(a[-3:]) + 3 + 8)
print(max_len)
