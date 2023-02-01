def is_ok(s):
    return len(s) == 11 and s[0:2] == '43' and s[4:6] == '78' and s[-2:] == '34'


with open('24-230.txt') as f:
    s = f.read().strip()
a = s.split('K')
numbers = filter(str.isdigit, a)
#print(*numbers, sep='\t')
num = max(filter(is_ok, numbers))
print(num)
p = 1
for c in num:
    if int(c) % 2 == 1:
        p *= int(c)
print(p)
