def dec(s):
    roma_arab = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    to_replace = (('IV', 'IIII'), ('IX', 'VIIII'),
                  ('XL', 'XXXX'), ('XC', 'LXXXX'),
                  ('CD', 'CCCC'), ('CM', 'DCCCC'))
    for a, b in to_replace:
        s = s.replace(a, b)
    return sum(roma_arab[d] for d in s)


def rom(n):
    arab_roma = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    to_replace = (('CM', 'DCCCC'), ('CD', 'CCCC'),
                  ('XC', 'LXXXX'), ('XL', 'XXXX'),
                  ('IX', 'VIIII'), ('IV', 'IIII'))
                  
    result = ''
    for d, num in arab_roma.items():
        c = n // num
        result += d * c
        n %= num
    for a, b in to_replace:
        result = result.replace(b, a)
    return result


all_rom_nums = [(rom(i), i) for i in range(1, 4000)]
sorted_rom_nums = sorted(all_rom_nums, key=lambda p: (-len(p[0]), p[1]))

with open('24data/24-390.txt') as f:
    s = f.read()
for rom_num, dec_num in sorted_rom_nums:
    if rom_num in s:
        print(dec_num)
        break
