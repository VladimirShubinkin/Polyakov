'''73)	В текстовом файле k8-4.txt находится цепочка из символов,
в которую могут входить заглавные буквы латинского алфавита A…Z и десятичные цифры.
Найдите длину самой длинной подцепочки, состоящей из одинаковых символов.
Для каждой цепочки максимальной длины выведите в отдельной строке сначала символ, из которого строится эта цепочка,
а затем через пробел – длину этой цепочки.'''

with open('24data/k8-4.txt') as f:
    s = f.read().strip()

list_sub_strs = []
cur_len = 1
max_len = 0
for i in range(len(s) - 1):
    if s[i + 1] == s[i]:
        cur_len += 1
    else:
        cur_len = 1
    if cur_len > max_len:
        max_len = cur_len
        list_sub_strs = [s[i]]
    elif cur_len == max_len:
        list_sub_strs.append(s[i])
for c in list_sub_strs:
    print(c, max_len)
