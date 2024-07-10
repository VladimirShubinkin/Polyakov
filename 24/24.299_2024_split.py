'''299)	(ЕГЭ-2024) Текстовый файл 24-299.txt состоит не более чем из 10^6 символов и содержит только десятичные цифры,
а также знаки «+» и «*» (сложения и умножения). Определите максимальное количество символов в непрерывной
последовательности, являющейся корректным арифметическим выражением с целыми неотрицательными числами (без знака),
значение которого равно нулю. В этом выражении никакие два знака арифметических операций не стоят рядом,
порядок действий определяется по правилам математики. В записи чисел отсутствуют незначащие (ведущие) нули. В ответе
укажите количество символов в найденном выражении.'''

import re

with open('24data/24-299.txt') as f:
    s = f.read().strip()

a = re.split('\+\+|\*\*|\+\*|\*\+', s)
max_str = ''
for line in a:
    line_strip = line.strip('*+')
    cur_str = ''
    good_numbers = []
    for expression_with_multiplication in line_strip.split('+'):
        if '0' in good_numbers:
            cur_str += '+'
        else:
            cur_str = ''
        good_numbers = []
        for number in expression_with_multiplication.split('*'):
            if number == '0' or number[0] != '0':
                good_numbers.append(number)
                cur_str += f'*{number}' if cur_str and cur_str[-1] != '+' else number
            else:  # ведущий ноль
                good_numbers = []
                cur_str = ''
            if '0' in good_numbers:
                cur_str = cur_str.strip('*+')
                if len(cur_str) > len(max_str):
                    max_str = cur_str
print(len(max_str))
print(max_str)
