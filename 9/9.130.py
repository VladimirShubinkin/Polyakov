'''(А. Богданов). Откройте файл электронной таблицы 9-130.xls, содержащей в каждой строке три натуральных числа.
Выясните, какое количество троек могут перестановкой образовать арифметическую прогрессию
с не нулевой разностью прогрессии.'''

with open('9-130.csv') as f:
    count = 0
    for line in f.readlines():
        a = sorted(map(int, line.split(';')))
        if a[2] - a[1] == a[1] - a[0] != 0:
            count += 1
print(count)