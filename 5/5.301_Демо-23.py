'''Демо-2023. На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. Далее эта запись обрабатывается по следующему правилу:
а) если сумма цифр в двоичной записи числа чётная, то к этой записи справа дописывается 0,
    а затем два левых разряда заменяются на 10;
б) если сумма цифр в двоичной записи числа нечётная, то к этой записи справа дописывается 1,
    а затем два левых разряда заменяются на 11.
Полученная таким образом запись является двоичной записью искомого числа R.
Укажите минимальное число N, после обработки которого с помощью этого алгоритма получается число R, большее 40.
В ответе запишите это число в десятичной системе счисления.
'''


def alg(n):
    n_bi = f'{n:b}'
    if n_bi.count('1') % 2 == 0:
        n_bi = '10' + n_bi[2:] + '0'
    else:
        n_bi = '11' + n_bi[2:] + '1'
    return int(n_bi, 2)


n = 1
while not (alg(n) > 40):
    n += 1
print(n)
