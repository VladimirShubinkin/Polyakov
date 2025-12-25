def sum_range(first_bound, second_bound):
    if first_bound > second_bound:
        first_bound, second_bound = second_bound, first_bound
    s = 0
    for x in range(first_bound, second_bound + 1):
        s += x
    return s


print(sum_range(0, 5))
print(sum_range(3, -5))
print(sum_range(second_bound=6, first_bound=3))
print(sum_range(-10**6, 10**6))
print(sum_range(0, 10**6))
print(sum_range(-30, -100))
print(sum_range(-3, -3))
