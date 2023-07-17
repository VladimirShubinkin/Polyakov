'''91)	 (П.Е. Финкель, г. Тимашевск) Текстовый файл 24-1.txt состоит не более чем из 10^6 символов.
Определите самое большое число, состоящее только из нечётных цифр.'''

from string import digits, ascii_uppercase


def is_all_digits_odd(s: str) -> bool:
    return all([d in digits[1::2] for d in s])


with open('24data/24-1.txt') as f:
    s = f.read().strip()
for letter in ascii_uppercase:
    s = s.replace(letter, ' ')
ans = max(filter(is_all_digits_odd, s.split()), key=int)
print(ans)
