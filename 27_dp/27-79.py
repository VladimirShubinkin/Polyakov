'''79)	(Л. Шастин) Дана последовательность натуральных чисел. Рассматриваются все её непрерывные
подпоследовательности, в которых начальное число последовательности делится на 21 и является квадратом конечного
числа последовательности. Найдите длину наибольшей такой подпоследовательности.'''

with open(r'C:\Users\PC\Documents\ЕГЭ\Поляков\27data\79\27-79b.txt') as f:
    a = [int(x) for x in f.readlines()[1:]]

maxlen = 0
starts = {}
for i in range(len(a)):
    x2 = a[i]**2
    if x2 in starts:
        maxlen = max(maxlen, i - starts[x2] + 1)
    if a[i] % 21 == 0 and int(a[i]**0.5)**2 == a[i]:
        if a[i] not in starts:
            starts[a[i]] = i
print(maxlen)
