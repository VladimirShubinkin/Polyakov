'''298)	(ЕГЭ-2024) Текстовый файл 24-298.txt состоит не более чем из 10^6 символов и содержит только символы,
обозначающие знаки «-», «*», и цифры 0, 7, 8, 9. Определите в прилагаемом файле максимальное количество идущих подряд
символов, которые образуют математически правильную последовательность, в которую входят знаки «-» или «*» и
натуральные числа без незначащих нулей.'''

'''Проблемы:
700000
-0*7
789-
7--8
'''

with open('24data/24-298.txt') as f:
    s = f.read().strip()

max_len = 0
cur_len = 0
cur_seq = ''
max_seq = ''
is_number = False
for i in range(len(s)):
    if is_number:
        if s[i] in '7890':
            cur_len += 1
            cur_seq += s[i]
            if cur_len > max_len:
                max_len = cur_len
                max_seq = cur_seq
        else:  # s[i] in '-*'
            cur_len += 1
            cur_seq += s[i]
            is_number = False
    else:
        if s[i] in '789':
            cur_len += 1
            cur_seq += s[i]
            if cur_len > max_len:
                max_len = cur_len
                max_seq = cur_seq
            is_number = True
        else:
            cur_len = 0
            cur_seq = ''
print(max_len)
