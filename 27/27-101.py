'''
101)На вход программе подается последовательность целых чисел.
Рассматриваются все непрерывные подпоследовательности исходной последовательности,
такие что произведение элементов каждой из них не кратно M = 858967.
Найдите количество таких подпоследовательностей.
'''
# 858967 = 79*83*131

inds = {79: -1, 83: -1, 131: -1}

with open('files/27-101b.txt') as f:
    n, *a = map(int, f.readlines())

count = 0
for i in range(n):
    for d in inds:
        if a[i] % d == 0:
            inds[d] = i
    count += i - min(inds.values())
print(count)
