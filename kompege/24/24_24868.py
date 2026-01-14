with open('24_24868.txt') as f:
    s = f.read().strip()
letters = {}
i = 0
while len(letters) < 3:
    letters[s[i]] = i
    i += 1
max_len = max(letters.values())
for k in range(i + 1, len(s)):
    letters[s[k]] = k
    if len(letters) == 4:
        cur = sorted(letters.items(), key=lambda p: p[1])
        max_len = max(max_len, cur[-1][1] - cur[0][1] - 1)
        del letters[cur[0][0]]
max_len = max(max_len, len(s) - min(letters.values()) - 1)
print(max_len)
