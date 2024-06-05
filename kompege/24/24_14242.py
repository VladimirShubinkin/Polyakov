'''
В файле содержится строка длиной не более 10^6 из букв A,B,D,E и цифр 0,1,2,3.
Определите в прилагаемом файле максимальную длину подпоследовательности,
в которой количество согласных букв равно количеству гласных и количество четных цифр равно количеству нечетных
'''

with open('24_14242.txt') as f:
    s = f.read().strip().replace('E', 'A').replace('D', 'B').replace('2', '0').replace('3', '1')
pos = {(0, 0): -1}
count_A = 0
count_B = 0
count_0 = 0
count_1 = 0
max_len = 0
for i in range(len(s)):
    if s[i] == 'A':
        count_A += 1
    if s[i] == 'B':
        count_B += 1
    if s[i] == '0':
        count_0 += 1
    if s[i] == '1':
        count_1 += 1
    diffs = (count_A - count_B, count_0 - count_1)
    if diffs in pos:
        max_len = max(max_len, i - pos[diffs])
    else:
        pos[diffs] = i
print(max_len)
