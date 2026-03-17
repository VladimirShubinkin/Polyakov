from functools import total_ordering


@total_ordering
class RomanNumeral:
    rom_digits = 'IVXLCDM'

    def __init__(self, inp: int|str):
        if isinstance(inp, int):
            if not 1 <= inp <= 3999:
                raise ValueError('Некорректное число')
            self.dec_num = inp
        elif isinstance(inp, str) and all(d in self.rom_digits for d in inp):
            self.dec_num = self.to_arabic(inp)
        else:
            raise ValueError('Не число')

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.dec_num + other.dec_num)
        if isinstance(other, int):
            return self.__class__(self.dec_num + other)
        if isinstance(other, str):
            return self + self.__class__(other)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            if self.dec_num + other.dec_num > 3999:
                return ValueError('Слишком большое число')
            self.dec_num += other.dec_num
            return self
        if isinstance(other, int):
            if self.dec_num + other > 3999:
                raise ValueError('Слишком большое число')
            self.dec_num += other
            return self
        if isinstance(other, str):
            if self.dec_num + self.to_arabic(other) > 3999:
                raise ValueError('Слишком большое число')
            self.dec_num += self.to_arabic(other)
            return self
        return NotImplemented

    def __imul__(self, other):
        self.dec_num *= other.dec_num
        return self

    def __mul__(self, other):
        return self.__class__(self.dec_num * other.dec_num)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.to_roman(self.dec_num)}')"

    def __str__(self):
        return self.to_roman(self.dec_num)

    def __eq__(self, other):
        return self.dec_num == other.dec_num

    def __lt__(self, other):
        return self.dec_num < other.dec_num

    def __int__(self):
        return self.dec_num

    def __hash__(self):
        return hash((self.dec_num, self.to_roman(self.dec_num)))

    @staticmethod
    def to_arabic(s: str):
        to_replace = (('CM', 'DCCCC'), ('CD', 'CCCC'), ('XC', 'LXXXX'), ('XL', 'XXXX'), ('IX', 'VIIII'), ('IV', 'IIII'))
        roma_arab = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for with_subtract, without_subtract in to_replace:
            s = s.replace(with_subtract, without_subtract)
        return sum(map(lambda d: roma_arab[d], s))

    @staticmethod
    def to_roman(n: int):
        to_replace = (('CM', 'DCCCC'), ('CD', 'CCCC'), ('XC', 'LXXXX'), ('XL', 'XXXX'), ('IX', 'VIIII'), ('IV', 'IIII'))
        arab_roma = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        result = ''
        for dec, rom in arab_roma.items():
            result += rom * (n // dec)
            n %= dec
        for with_subtract, without_subtract in to_replace:
            result = result.replace(without_subtract, with_subtract)
        return result



def roman_to_arabic(roman_num: str) -> int:
    return RomanNumeral(roman_num).dec_num


def arabic_to_roman(num: int) -> RomanNumeral:
    return RomanNumeral(num)

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

# print(RomanNumber(15) + RomanNumber('IX'))
# print(int(RomanNumber('XXX')))
# print(RomanNumber('IV') >= RomanNumber(5))
a = RomanNumeral(33)
# b = RomanNumeral('III')
# b = 10
b = 'II'
a += b
print(a)
# b *= a
# print(a, b)
