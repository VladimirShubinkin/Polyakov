'''
Определите наименьшее натуральное число A, большее 200, такое, что выражение
((x & 56 ≠0) ˅ (x & 43 ≠0)) → (x & A ≠0)
тождественно истинно (то есть принимает значение 1 при любом натуральном значении переменной x)?
'''

def f(x, a):
    return ((x & 56 != 0) or (x & 43 != 0)) <= (x & a != 0)
def is_good(a):
    for x in range(1, 1000):
        if not f(x, a):
            return False
    return True


a = 200
while not is_good(a):
    a += 1
print(a)