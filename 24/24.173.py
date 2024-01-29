'''
173)	(Е. Джобс) Текстовый файл 24-173.txt состоит не более чем из 10^6 букв из набора A, B, C, D, E, F.
Найдите максимальную длину подстроки, в которой ни одна тройка символов не записана два раза подряд.
Например, в искомой подстроке не может быть фрагмента ABCABC.
'''

with open('24data/24-173.txt') as f:
    s = f.read().strip()

count = 5
max_count = 0
for i in range(5, len(s)):
    if s[i-5:i-2] != s[i-2:i+1]:
        count += 1
    else:
        count = 5
    max_count = max(max_count, count)
print(max_count)
