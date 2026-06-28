with open('26_31165.txt') as f:
    K, N = map(int, f.readline().split())
    data = []
    for line in f.readlines():
        t0, t1, type_ = line.split()
        data.append((int(t0), int(t1), type_))
data.sort()
priem = [-5]*(K + 1)
count = 0
last = -1
for t0, t1, type_ in data:
    shift = type_ == 'B'
    for i in range(1 + shift, len(priem), 2):
        if t0 >= priem[i] + 5:
            priem[i] = t1
            count += 1
            last = i
            break
print(count, last)
