with open('24data/24-203.txt') as f:
    s = f.read().strip()

ans = 0
pos = {'A': -1, 'B': -1, 'C': -1}
for i in range(len(s)):
    if s[i] in pos:
        pos[s[i]] = i
    ans += max(0, i - min(pos.values()) - 2)
print(ans)

