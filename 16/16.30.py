'''30)	Определите наименьшее значение n, при котором сумма чисел, которые будут выведены при вызове F(n),
будет больше 3 200 000. Запишите в ответе сначала найденное значение n,
а затем через пробел – соответствующую сумму выведенных чисел
def F( n ):
  print(n*n)
  if n > 1:
    print(2*n+1)
    F(n-2)
    F(n//3)
'''

def f(n):
    global s
    s += n * n
    if n > 1:
        s += 2 * n + 1
        f(n - 2)
        f(n // 3)


n = 1
s = 0
f(n)
while s <= 3_200_000:
    s = 0
    n += 1
    f(n)
print(n, s)