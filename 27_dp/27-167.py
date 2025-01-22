with open('files/27-167b.txt') as f:
    n, k, *a = map(int, f.read().split())

min_p = 10**20  # минимальное произведение (искомая величина)
min_prev_2k = a[0]  # минимум на расстоянии не менее 2k
min_p_prev = 10**20  # минимальное произведение двух элементов на расстоянии не менее k от текущего
for i in range(2 * k, n):
    min_prev_2k = min(min_prev_2k, a[i - 2 * k])
    min_p_prev = min(min_p_prev, a[i - k] * min_prev_2k)
    min_p = min(min_p, a[i] * min_p_prev)
print(min_p % (10**6 + 1))

