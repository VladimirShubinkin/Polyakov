from functools import total_ordering
from itertools import combinations


@total_ordering
class RomanNumeral:
    def __init__(self, inp: int|str):
        if isinstance(inp, int):
            if not self.is_valid_dec_num(inp):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            self.dec_num = inp
        elif isinstance(inp, str) and self.is_valid_rom_num(inp):
            self.dec_num = self.to_arabic(inp)
        elif isinstance(inp, self.__class__):
            self.dec_num = inp.dec_num
        else:
            raise ValueError('Не число')

    @property
    def rom_num(self):
        return self.to_roman(self.dec_num)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            if not self.is_valid_dec_num(self.dec_num + other.dec_num):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            return self.__class__(self.dec_num + other.dec_num)
        if isinstance(other, int):
            if not self.is_valid_dec_num(self.dec_num + other):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            return self.__class__(self.dec_num + other)
        if isinstance(other, str):
            if not self.is_valid_rom_num(other):
                raise ValueError('Некорректное число.')
            if not self.is_valid_dec_num(self.dec_num + self.to_arabic(other)):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            return self + self.__class__(other)
        return NotImplemented

    __radd__ = __add__

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            if not self.is_valid_dec_num(self.dec_num + other.dec_num):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            self.dec_num += other.dec_num
            return self
        if isinstance(other, int):
            if not self.is_valid_dec_num(self.dec_num + other):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            self.dec_num += other
            return self
        if isinstance(other, str):
            if not self.is_valid_rom_num(other):
                raise ValueError('Некорректное число.')
            if not self.is_valid_dec_num(self.dec_num + self.to_arabic(other)):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            self.dec_num += self.to_arabic(other)
            return self
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            if not self.is_valid_dec_num(self.dec_num - other.dec_num):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            return self.__class__(self.dec_num - other.dec_num)
        if isinstance(other, int):
            if not self.is_valid_dec_num(self.dec_num - other):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            return self.__class__(self.dec_num - other)
        if isinstance(other, str):
            if not self.is_valid_rom_num(other):
                raise ValueError('Некорректное число.')
            if not self.is_valid_dec_num(self.dec_num - self.to_arabic(other)):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            return self - self.__class__(other)
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, self.__class__):
            if not self.is_valid_dec_num(self.dec_num - other.dec_num):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            self.dec_num -= other.dec_num
            return self
        if isinstance(other, int):
            if not self.is_valid_dec_num(self.dec_num - other):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            self.dec_num -= other
            return self
        if isinstance(other, str):
            if not self.is_valid_rom_num(other):
                raise ValueError('Некорректное число.')
            if not self.is_valid_dec_num(self.dec_num - self.to_arabic(other)):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            self.dec_num -= self.to_arabic(other)
            return self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            if not self.is_valid_dec_num(self.dec_num * other.dec_num):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            return self.__class__(self.dec_num * other.dec_num)
        if isinstance(other, int):
            if not self.is_valid_dec_num(self.dec_num * other):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            return self.__class__(self.dec_num * other)
        if isinstance(other, str):
            if not self.is_valid_rom_num(other):
                raise ValueError('Некорректное число.')
            if not self.is_valid_dec_num(self.dec_num * self.to_arabic(other)):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            return self * self.__class__(other)
        return NotImplemented

    __rmul__ = __mul__

    def __imul__(self, other):
        if isinstance(other, self.__class__):
            if not self.is_valid_dec_num(self.dec_num * other.dec_num):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            self.dec_num *= other.dec_num
            return self
        if isinstance(other, int):
            if not self.is_valid_dec_num(self.dec_num * other):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            self.dec_num *= other
            return self
        if isinstance(other, str):
            if not self.is_valid_rom_num(other):
                raise ValueError('Некорректное число.')
            if not self.is_valid_dec_num(self.dec_num * self.to_arabic(other)):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            self.dec_num *= self.to_arabic(other)
            return self
        return NotImplemented

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.rom_num}')"

    def __str__(self):
        return self.rom_num

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.dec_num == other.dec_num
        if isinstance(other, int):
            if not self.is_valid_dec_num(other):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            return self.dec_num == other
        if isinstance(other, str):
            if not self.is_valid_rom_num(other):
                raise ValueError('Некорректное число.')
            return self.rom_num == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.dec_num < other.dec_num
        if isinstance(other, int):
            if not self.is_valid_dec_num(other):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            return self.dec_num < other
        if isinstance(other, str):
            if not self.is_valid_rom_num(other):
                raise ValueError('Некорректное число.')
            other_dec = self.to_arabic(other)
            if not self.is_valid_dec_num(other_dec):
                raise ValueError('Некорректное число. Число должно быть в диапазоне [1, 3999]')
            return self.dec_num < other_dec
        return NotImplemented

    def __int__(self):
        return self.dec_num

    def __hash__(self):
        return hash((self.dec_num, self.rom_num))

    @staticmethod
    def is_valid_dec_num(n: int):
        return 1 <= n <= 3999

    @staticmethod
    def is_valid_rom_num(s: str):
        rom_digits = 'IVXLCDM'
        if not all(d in rom_digits for d in s):
            return False
        if any(d * 4 in s for d in rom_digits):
            return False
        to_replace = (('CM', 'DCCCC'), ('CD', 'CCCC'), ('XC', 'LXXXX'), ('XL', 'XXXX'), ('IX', 'VIIII'), ('IV', 'IIII'))
        for with_subtract, without_subtract in to_replace:
            s = s.replace(with_subtract, without_subtract)
        if any(d * 5 in s for d in rom_digits):
            return False
        for p in combinations(rom_digits, 2):
            if ''.join(p) in s:
                return False
        return True

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
# a = RomanNumeral(33)
# b = RomanNumeral('III')
# b = 10
# b = 'C'
# print(b == a)
# a *= b
#
# print(a)
# print(sorted(['XX', RomanNumeral(20), RomanNumeral('V')]))
# b *= a
# print(a, b)
# number = RomanNumeral('IV') + RomanNumeral('VIII')
#
# print(number)
# print(int(number))

# a = RomanNumeral('X')
# b = RomanNumeral('XII')
#
# print(a == b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# roman = RomanNumeral('L')
# print(roman.__eq__(1))
# print(roman.__ne__(1.1))
# print(roman.__gt__(range(5)))
# print(roman.__lt__([1, 2, 3]))
# print(roman.__ge__({4, 5, 6}))
# print(roman.__le__({1: 'one'}))

a = RomanNumeral('CCC')
b = RomanNumeral(a)
print(b)
