for x in range(18, -1, -1):
    n1 = int('98079641', 19) + x * 19**5
    n2 = int('36014', 19) + x * 19**2
    n3 = int('7304', 19) + x * 19
    s = n1 + n2 + n3
    if s % 18 == 0:
        print(s // 18)
        break
