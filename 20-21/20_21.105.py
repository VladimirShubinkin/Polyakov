def f(first, s, moves):
    if first + s >= 259:
        return moves % 2 == 0
    if moves == 0:
        return 0
    calls = [f(first + 1, s, moves - 1),
             f(first * 2, s, moves - 1),
             f(first, s + 1, moves - 1),
             f(first, s * 2, moves - 1)]
    if (moves - 1) % 2 == 0:
        return any(calls)
    return all(calls)


first = 17
print('20:', *(s for s in range(1, 242) if f(first, s, 3) and not f(first, s, 1)))
print('21:', *(s for s in range(1, 242) if f(first, s, 4) and not f(first, s, 2)))
