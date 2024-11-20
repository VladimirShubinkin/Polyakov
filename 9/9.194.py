'''В файле электронной таблицы 9-194.xls в каждой строке записаны 5 натуральных чисел.
Определите количество строк таблицы, для которых выполнены все условия:
– в строке нет повторяющихся чисел;
– чётных чисел больше, чем нечётных;
– сумма чётных чисел меньше, чем сумма нечётных.
'''

def get_evens(a: list[int]) -> list[int]:
    return [x for x in a if x % 2 == 0]


with open('9-194.csv') as f:
    count = 0
    for line in f.readlines():
        a = list(map(int, line.split(';')))
        first = len(set(a)) == len(a)
        evens = get_evens(a)
        second = len(evens) > len(a) - len(evens)
        evens_sum = sum(evens)
        third = evens_sum < sum(a) - evens_sum
        count += first and second and third
print(count)
