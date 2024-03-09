with open('27-5b.txt') as f:
    n = int(f.readline())
    s = 0
    min_diffs = [10**9]*5
    for _ in range(n):
        a, b = map(int, f.readline().split())
        s += min(a, b)
        cur_diff = abs(a - b)
        r = cur_diff % 5
        if r > 0:
            temp_min_diffs = min_diffs[:]
            for k in range(1, 5):
                cur_r = (r + k) % 5
                temp_min_diffs[cur_r] = min(temp_min_diffs[cur_r], cur_diff + min_diffs[k])
            temp_min_diffs[r] = min(temp_min_diffs[r], cur_diff)
            min_diffs = temp_min_diffs[:]
r = s % 5
if r != 0:
    s += min_diffs[5 - r]
print(s)
