with open('26data/26-151.txt') as f:
    n, s = map(int, f.readline().split())
    a = []
    for line in f.readlines():
        ID, ex1, ex2, ex3, sob = map(int, line.split())
        a.append([ID, ex1 + ex2 + ex3, sob])
a.sort(key=lambda p: (-p[1], -p[2], p[0]))
pp_ball = a[s - 1][1]
# print(pp_ball)
for i in range(s - 2, -1, -1):
    if a[i][1] > pp_ball:
        p_ball, ans1 = a[i][1], a[i][0]
        break
count = 0
for line in a:
    if line[1] == pp_ball:
        count += 1
print(ans1, count)
