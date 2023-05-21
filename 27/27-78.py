'''78)	(А. Богданов) Дана последовательность натуральных чисел. Рассматриваются все её непрерывные
последовательности, такие что сумма элементов каждой из них кратна K = 37, а сумма первого и последнего элемента
последовательности кратна M = 73. Найдите длину такой подпоследовательности с максимальной суммой. Если таких
подпоследовательностей найдено несколько, в ответе укажите количество элементов в самой короткой из них. '''

with open(r'C:\Users\PC\Documents\ЕГЭ\Поляков\27data\78\27-78a.txt') as f:
    a = [int(x) for x in f.readlines()[1:]]

K, M = 37, 73
tail_sum = [[10**9]*K for _ in range(M)]
tail_ind = [[-1]*K for _ in range(M)]
min_len = 10**9
max_s = 0
s = a[0]
tail_sum[0][s % 73] = s
for i in range(1, len(a)):
    r_el = a[i] % M
    if s < tail_sum[r_el][s % K]:
        tail_sum[r_el][s % K] = s
        tail_ind[r_el][s % K] = i - 1
    s += a[i]
    r_s = s % K
    if s - tail_sum[(M - r_el) % M][r_s] > max_s:
        max_s = s - tail_sum[(M - r_el) % M][r_s]
        min_len = i - tail_ind[(M - r_el) % M][r_s]
    elif s - tail_sum[(M - r_el) % M][r_s] == max_s and i - tail_ind[(M - r_el) % M][r_s] < min_len:
        min_len = i - tail_ind[(M - r_el) % M][r_s]
print(min_len, max_s)
