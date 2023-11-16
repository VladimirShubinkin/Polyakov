with open('24-2.txt') as f:
    s = f.read().strip()

cur_ss = ''
max_ss = s[0]
for i in range(1, len(s)):
    if s[i] > s[i - 1]:
        cur_ss += s[i]
    else:
        cur_ss = s[i]
    if len(cur_ss) > len(max_ss):
        max_ss = cur_ss
print(max_ss)
