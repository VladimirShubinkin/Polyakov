'''
116)	(С.С. Поляков) Исполнитель Калькулятор преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 5
3. Умножить на 3
Сколько разных чисел может быть получено из числа 1 с помощью программ, состоящих из 4 команд?
'''


def f(a, b, k):
    if a == b and k == 0:
        return 1
    if a > b or k == 0:
        return 0
    return f(a + 1, b, k - 1) + f(a + 5, b, k - 1) + f(3 * a, b, k - 1)


c = 0
for b in range(5, 300):
    c += bool(f(1, b, 4))
print(c)
