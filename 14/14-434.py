'''434)	(Е. Джобс) Известно, что значение выражения
27Aх23(16) + 8yE5D2(16)
где х и y – цифры шестнадцатеричной системы счисления, кратно 5.
Укажите максимальное значение суммы x и y, когда это возможно.
В качестве ответа приведите десятичную запись полученной суммы x и y.
'''

from string import digits, ascii_uppercase

hexdigits = digits + ascii_uppercase[:6]
max_s = -1
for x in hexdigits:
    for y in hexdigits:
        n1 = int(f'27A{x}23', 16)
        n2 = int(f'8{y}E5D2', 16)
        if (n1 + n2) % 5 == 0:
            # print(x, y)
            max_s = max(max_s, int(x, 16) + int(y, 16))
print(max_s)
