'''71)	Набор данных представляет собой последовательность натуральных чисел. Необходимо выбрать такую
подпоследовательность подряд идущих чисел, чтобы их сумма была максимальной и делилась на 69, и определить её длину.
Гарантируется, что такая подпоследовательность существует. Если таких подпоследовательностей несколько, нужно выбрать
подпоследовательность наименьшей длины.'''

with open(r'C:\Users\PC\Documents\ЕГЭ\Поляков\27data\71\27-71a.txt') as f:
    a = [int(x) for x in f.readlines()[1:]]

s = 0
max_s = 0
min_len = 10**9
tail_s = [10**9]*69
tail_s[0] = 0
tail_ind = [10**9]*69
for i in range(len(a)):
    s += a[i]
    r = s % 69
    if s - tail_s[r] > max_s:
        max_s = s - tail_s[r]
        min_len = i - tail_ind[r]
    elif s - tail_s[r] == max_s:
        min_len = min(min_len, i - tail_ind[r])
    if s < tail_s[r]:
        tail_s[r] = s
        tail_ind[r] = i
print(min_len)