def neg_binar(x, n):
    x = 2**n - abs(x)
    ans = ''
    while x:
        ans = str(x % 2) + ans
        x //= 2
    return ans


def binar(x, n):
    ans = ''
    while x:
        ans = str(x % 2) + ans
        x //= 2
    return f'{ans:0{n}}'


def good_binar(x, n):
    ans = ""
    for i in range(n):
        ans = "01"[x % 2] + ans
        x //= 2
    return ans

a = int(input())
n = int(input())
if a >= 0:
    print(binar(a, n))
else:
    print(neg_binar(a, n))
print(good_binar(a, n))
# print(f'{a:0{n}b}')
# print(bin(a)[2:].zfill(n))

