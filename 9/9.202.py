'''В файле электронной таблицы 9-202.xls в каждой строке записаны 6 натуральных чисел.
Определите количество строк таблицы, содержащих хотя бы одну ячейку со следующими свойствами:
    – число в данной ячейке не повторяется в ячейках этой строки;
    – число в данной ячейке встречается ровно 11 раз в других ячейках всей таблицы.
'''

def num_count(matrix: list[list[int]], num: int) -> int:
    count = 0
    for row in matrix:
        count += row.count(num)
    return count


with open('9-202.csv') as f:
    matrix = []
    for line in f.readlines():
        row = list(map(int, line.split(';')))
        matrix.append(row)
count = 0
for row in matrix:
    for num in row:
        if row.count(num) == 1 and num_count(matrix, num) == 12:
            count += 1
            break
print(count)
