with open('24data/24-300.txt') as f:
    s = f.read().strip()
# s = '01234*0+0+000**567*0+0654*0+34*0+0+0*0+0*0*0+0++567*+345+45+*0000+++++++++++6'
for c in '+*':
    while c * 3 in s:
        s = s.replace(c * 3, c * 2)
for d in '0123456789':  # Могут остаться ноли в начале строки. Например, 23+000456+8
    s = s.replace('+0' + d, '+0$' + d)
    s = s.replace('*0' + d, '*0$' + d)
s = s.replace('++', '+$+')
s = s.replace('**', '*$*')
s = s.replace('+*', '+$*')
s = s.replace('*+', '*$+')
lines = s.split('$')
ans_str = ''
for line in lines:
    cur_line = line.lstrip('0')  # Избавились от возможных нолей в начале
    cur_line = cur_line.strip('+*')
    cur_str = ''
    for term in cur_line.split('+'):
        if '0' in term.split('*'):
            cur_str += '+' + term
        else:
            cur_str = ''
        cur_str = cur_str.lstrip('+')
        ans_str = max(ans_str, cur_str, key=len)
print(ans_str)
print(len(ans_str))
