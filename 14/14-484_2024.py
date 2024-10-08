'''484)	(ЕГЭ-2024) Значение арифметического выражения 6^2030 + 6^100 – х, где х – целое положительное число,
не превышающее 2030, записали в 6-ричной системе счисления. Определите наибольшее количество нулей,
которое может содержать число, являющееся 6-ричной записью значения данного арифметического выражения.'''

def count_zeros(x):
    n = 6**2030 + 6**100 - x
    result = 0
    while n:
        result += n % 6 == 0
        n //= 6
    return result


max_count = 0
for x in range(1, 2031):
    max_count = max(max_count, count_zeros(x))
print(max_count)
