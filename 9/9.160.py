'''В файле электронной таблицы 9-160.xls в каждой строке содержатся четыре натуральных числа.
Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
– наибольшее из четырёх чисел меньше суммы трёх других;
– четыре числа можно разбить на две пары чисел с равными суммами.
'''

with open('9-160.csv') as f:
    count = 0
    for line in f.readlines():
        a = sorted(map(int, line.split(';')))
        first = a[-1] < sum(a[:3])
        second = a[0] + a[-1] == a[1] + a[2]
        count += first and second
print(count)