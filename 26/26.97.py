with open('26data/26-97.txt') as f:
    n = int(f.readline())
    pipes = []
    for line in f.readlines():
        d, s = map(int, line.split())
        pipes.append((d, d - 2 * s))
pipes.sort(key=lambda p: p[1], reverse=True)
last = pipes[0][1]
count = 1
for d_out, d_in in pipes:
    if d_out <= last - 3:
        count += 1
        pre_last = last
        last = d_in
print(count)
max_d = 0
for d_out, d_in in pipes:
    if d_out <= pre_last - 3:
        max_d = max(max_d, d_out)
print(max_d)
