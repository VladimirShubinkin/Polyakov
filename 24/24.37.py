'''37)	(А.М. Кабанов) В текстовом файле k7c-5.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F.
Найдите количество цепочек длины 5, в которых соседние символы не совпадают.'''


def nears_are_different(s: str) -> bool:
    '''функция позволяет определить, все ли соседние символы строки s различны'''
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


with open('24data/k7c-5.txt') as f:
    s = f.read().strip()
count = 0
for i in range(len(s) - 4):
    count += nears_are_different(s[i:i+5])
print(count)
