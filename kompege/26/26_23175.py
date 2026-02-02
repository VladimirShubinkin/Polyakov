with open('26_2_23175.txt') as f:
    n, m, *a = map(int, f.read().split())
    w = sorted(a[:n], reverse=True)
    boxes = sorted(a[n:], reverse=True)
i = 0
w_list = []
for b in boxes:
    while i < len(w) and w[i] > b:
        i += 1
    if i < len(w):
        w_list.append(w[i])
        i += 1
print(len(w_list))
w2 = n - len(w_list) + 1
print(w_list[0] - w[w2])
