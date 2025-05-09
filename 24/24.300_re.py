'''300)	(ЕГЭ-2024) Текстовый файл 24-300.txt состоит не более чем из 10^6 символов
и содержит только десятичные цифры, а также знаки «+» и «*» (сложения и умножения).
Определите максимальное количество символов в непрерывной последовательности,
являющейся корректным арифметическим выражением с целыми неотрицательными числами (без знака),
значение которого равно нулю. В этом выражении никакие два знака арифметических операций не стоят рядом,
порядок действий определяется по правилам математики. В записи чисел отсутствуют незначащие (ведущие) нули.
В ответе укажите количество символов в найденном выражении.'''

import re

with open('24data/24-300.txt') as f:
    s = f.read().strip()

left_m = r'(?:[1-9]\d*\*|0\*)*'
rigth_m = r'(?:\*[1-9]\d*|\*0)*'
term = fr'{left_m}0{rigth_m}'
pattern = fr'(?:{term}\+)*{term}'

max_str = max(re.findall(pattern, s), key=len)
print(max_str)
print(len(max_str))
