'''298)	(ЕГЭ-2024) Текстовый файл 24-298.txt состоит не более чем из 10^6 символов и содержит только символы,
обозначающие знаки «-», «*», и цифры 0, 7, 8, 9. Определите в прилагаемом файле максимальное количество идущих подряд
символов, которые образуют математически правильную последовательность, в которую входят знаки «-» или «*» и
натуральные числа без незначащих нулей.'''

'''Проблемы:
700000
-0*7
789-
7--8
7*****8
-000007
'''

with open('24data/24-298.txt') as f:
    s = f.read().strip()

s = s.replace('-', '*')
# s = s.replace('*0*', '*1*') понадобилось бы, если бы не гарантия натуральности
a = s.split('**')
max_seq = ''
for sub_str in a:
    ss = sub_str.split('*0')
    max_seq = max(max_seq, *map(lambda line: line.lstrip('*0'), ss), key=len)
print(len(max_seq))
