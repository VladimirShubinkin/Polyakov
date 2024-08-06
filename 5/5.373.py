def f(n):
    bin_n = f'{n:b}'
    if bin_n.count('1') % 2 == 0:
        bin_r = '10' + bin_n[2:] + '0'
    else:
        bin_r = '11' + bin_n[2:] + '1'
    return int(bin_r, 2)


n = 75
while not f(n) < 75:
    n -= 1
print(n)
