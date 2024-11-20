'''В файле электронной таблицы 9-222.xls в каждой строке записаны шесть натуральных чисел.
Определите наименьший номер строки таблицы, для чисел которой выполнены оба условия:
– в строке есть только одно число, которое повторяется дважды, остальные четыре числа различны;
– повторяющееся число строки не меньше, чем среднее арифметическое четырёх её неповторяющихся чисел.
'''
from collections import Counter

with open('9-222.csv') as f:
    for ind, line in enumerate(f.readlines(), start=1):
        a = list(map(int, line.split(';')))
        counter = Counter(a)
        counts = list(counter.values())
        first = counts.count(2) == 1 and counts.count(1) == 4
        if first:
            s = 0
            for num, count in counter.items():
                if count == 2:
                    rep_number = num
                else:
                    s += num
            second = rep_number >= s / 4
            if second:
                print(ind)
                break
