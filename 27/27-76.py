'''76)	(Е. Драчева) Дана последовательность из N натуральных чисел. Рассматриваются всевозможные пары различных
элементов последовательности, между которыми есть хотя бы одно число, при этом сумма пары кратна трём, а сумма чисел
между ними чётна. Найдите количество таких пар. '''

with open(r'C:\Users\PC\Documents\ЕГЭ\Поляков\27data\76\27-76b.txt') as f:
    a = [int(x) for x in f.readlines()[1:]]

count = 0
tail_count = [[0, 0, 0],
              [0, 0, 0]]
s_prev = a[0] % 2
for i in range(2, len(a)):
    r_prev = a[i - 2] % 3
    tail_count[s_prev % 2][r_prev] += 1
    s_prev += a[i - 1] % 2
    parity = s_prev % 2
    r = a[i] % 3
    count += tail_count[parity][(3 - r) % 3]

print(count)