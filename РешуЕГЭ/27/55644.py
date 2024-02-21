'''
Дана последовательность натуральных чисел. Назовём парой любые два числа из последовательности.
Необходимо определить количество пар, в которых десятичная запись произведения чисел в паре заканчивается ровно на 6 нулей.
Первая строка входного файла содержит целое число N — общее количество чисел в наборе.
Каждая из следующих N строк содержит одно число, не превышающее 10^9.
Гарантируется, что число в ответе не превышает 2*10^9.
'''
def get_factor_count(n, factor):
    for i in range(7, -1, -1):
        if n % factor**i == 0:
            return i


with open('55644_27-B.txt') as f:
    n, *a = map(int, f.readlines())

m_2_5 = [[0]*8 for _ in range(8)]
count = 0
for x in a:
    count_2 = get_factor_count(x, 2)
    count_5 = get_factor_count(x, 5)
    if count_2 == 7 and count_5 == 7:
        continue
    pair_count_2 = max(6 - count_2, 0)
    pair_count_5 = max(6 - count_5, 0)
    end_2 = pair_count_5 + 1 if count_2 == 7 else 8
    end_5 = pair_count_2 + 1 if count_5 == 7 else 8
    count += sum(m_2_5[pair_count_2][pair_count_5:end_2])
    for i in range(pair_count_2 + 1, end_5):
        count += m_2_5[i][pair_count_5]
    m_2_5[count_2][count_5] += 1
print(count)

