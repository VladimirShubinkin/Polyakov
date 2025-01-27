class Roman_number():
    def __init__(self, inp: int|str):
        self.to_replace = (('CM', 'DCCCC'), ('CD', 'CCCC'), ('XC', 'LXXXX'),
                           ('XL', 'XXXX'), ('IX', 'VIIII'), ('IV', 'IIII'))
        self.roma_arab = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.arab_roma = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        if isinstance(inp, int):
            self.dec_num = inp
            self.rom_num = self.to_roman()
        else:
            self.rom_num = inp
            self.dec_num = self.to_arabic()

    def __add__(self, other):
        return Roman_number(self.dec_num + other.dec_num)

    def __iadd__(self, other):
        return Roman_number(self.dec_num + other.dec_num)

    def __imul__(self, other):
        return Roman_number(self.dec_num * other.dec_num)

    def __mul__(self, other):
        return Roman_number(self.dec_num * other.dec_num)

    def __repr__(self):
        return f"Roman_number('{self.rom_num}')"

    def __str__(self):
        return self.rom_num

    def __eq__(self, other):
        return self.dec_num == other.dec_num

    def __ge__(self, other):
        return self.dec_num >= other.dec_num

    def __gt__(self, other):
        return self.dec_num > other.dec_num

    def __le__(self, other):
        return self.dec_num <= other.dec_num

    def __lt__(self, other):
        return self.dec_num < other.dec_num

    def __int__(self):
        return self.dec_num

    def to_arabic(self):
        s = self.rom_num
        for with_subtract, without_subtract in self.to_replace:
            s = s.replace(with_subtract, without_subtract)
        return sum(map(lambda d: self.roma_arab[d], s))

    def to_roman(self):
        result = ''
        n = self.dec_num
        for dec, rom in self.arab_roma.items():
            result += rom * (n // dec)
            n %= dec
        for with_subtract, without_subtract in self.to_replace:
            result = result.replace(without_subtract, with_subtract)
        return result



def roman_to_arabic(roman_num: str) -> int:
    return Roman_number(roman_num).dec_num


def arabic_to_roman(num: int) -> Roman_number:
    return Roman_number(num)

# print(roman_to_arabic('XXX'))
# print(roman_to_arabic('XIX'))
# print(roman_to_arabic('XVIII'))
# print(roman_to_arabic('LXII'))
# print(roman_to_arabic('I'))
# print(roman_to_arabic('IV'))

# print(arabic_to_roman(15))
# print(arabic_to_roman(72))
# print(arabic_to_roman(149))
# print(arabic_to_roman(1))
# print(arabic_to_roman(9))
# print(arabic_to_roman(30))

print(Roman_number(15) + Roman_number('IX'))
print(int(Roman_number('XXX')))
print(Roman_number('IV') >= Roman_number(5))
a = Roman_number(33)
b = Roman_number('III')
a += b
print(a)
b *= a
print(a, b)
