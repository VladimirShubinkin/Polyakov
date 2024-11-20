'''199)	(Д. Статный) В файле электронной таблицы 9-199.xls в каждой строке записаны 6 неотрицательных целых чисел.
Определите количество строк таблицы, для которых выполнено только одно из условий:
– в строке только одно число повторяется дважды, а остальные не повторяются;
– в строке среднее арифметическое чётных чисел отличается от среднего арифметического нечётных чисел более чем на 50.
Примечание: если в строке нет чётных или нечётных чисел, принять их среднее арифметическое равным нулю.
'''


with open('9-199.txt') as f:
    answer = 0
    for line in f:
        a = [int(x) for x in line.split()]
        # a = list(map(int, line.split()))
        first = sum(a.count(x) for x in a) == 8
        sums = [0, 0]
        counts = [0, 0]
        for x in a:
            sums[x % 2] += x
            counts[x % 2] += 1
        aver_evens = 0
        if counts[0]:
            aver_evens = sums[0] / counts[0]
        aver_odds = 0
        if counts[1]:
            aver_odds = sums[1] / counts[1]
        second = abs(aver_odds - aver_evens) > 50
        answer += first + second == 1
print(answer)
