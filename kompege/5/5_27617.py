def f(n):
    n2 = f'{n:b}'
    if n % 3 == 0:
        n2 += n2[-3:]
    else:
        n2 += f'{(n % 3) * 3:b}'
    return int(n2, 2)


n_max = 0
d_min = 100
for n in range(10, 130):
    r = f(n)
    if abs(r - 130) < d_min:
        d_min = abs(r - 130)
        n_max = n
    elif abs(r - 130) == d_min:
        n_max = n
print(n_max)


#  15 -> 127
#  31 -> 127
