'''
118)	(С.С. Поляков) Исполнитель Калькулятор преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 2
3. Умножить на 2
Сколько разных чисел на отрезке [34, 59] может быть получено из числа 1 с помощью программ, состоящих из 6 команд?
'''


def f(a, k):
    if k == 0:
        if 34 <= a <= 59:
            ans.add(a)
        return
    f(a + 1, k - 1)
    f(a + 2, k - 1)
    f(2 * a, k - 1)


ans = set()
f(1, 6)
print(len(ans))
