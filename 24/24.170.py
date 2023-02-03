with open('24-169.txt') as f:
    s = f.read().strip()

q = 'XYZ'
j = 0
length = 0
max_len = 0
for i in range(len(s)):
    if s[i] == q[j]:
        length += 1
        j = (j + 1) % 3
    elif s[i] in q:
        length = 1
        j = (q.index(s[i]) + 1) % 3
    else:
        length = 0
    max_len = max(max_len, length)
print(max_len)
