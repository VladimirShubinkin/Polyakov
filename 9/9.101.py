'''(А. Комков) Откройте файл электронной таблицы 9-101.xls, содержащей в каждой строке три натуральных числа.
Выясните, какое количество троек чисел могут являться сторонами равнобедренного треугольника.'''

with open('9-101.csv') as f:
    count = 0
    for line in f.readlines():
        a = sorted(map(int, line.split(';')))
        if a[-1] < sum(a[:2]) and len(set(a)) < 3:
            count += 1
print(count)