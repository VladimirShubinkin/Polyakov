with open('24_18530.txt') as f:
    s = f.read().strip() + 'A'
# s = 'BBDABCADEFBACDFABFFFFF'
s = s.replace('E', 'A')
lengths = [len(line) + 1 for line in s.split('A')]
max_len = 0
cur_len = sum(lengths[:3])
for i in range(3, len(lengths)):
    cur_len += lengths[i]
    max_len = max(max_len, cur_len)
    if lengths[i] - lengths[i - 1] != lengths[i - 1] - lengths[i - 2]:
        cur_len = lengths[i - 2] + lengths[i - 1] + lengths[i]
print(max_len - 1)  # всегда берём лишнее A в конце
